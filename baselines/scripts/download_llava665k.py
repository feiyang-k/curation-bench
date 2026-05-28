#!/usr/bin/env python3
"""Download external artifacts needed by the baseline data generators.

The default path only downloads the LLaVA-665K instruction JSON. Image archives
are large, so they are opt-in via DOWNLOAD_IMAGES=true in .env or
--download-images on the command line.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV = ROOT / ".env"

DEFAULTS = {
    "LLAVA_JSON_REPO_ID": "liuhaotian/LLaVA",
    "LLAVA_JSON_FILENAME": "llava_v1_5_mix665k.json",
    "LLAVA_JSON_PATH": "dataset/llava_v1_5_mix665k.json",
    "LLAVA_ARROW_DIR": "/path/to/llava665k_ds",
    "IMAGE_ROOT": "dataset/images",
    "DOWNLOAD_IMAGES": "false",
    "DOWNLOAD_ARDS": "true",
    "KEEP_ARCHIVES": "false",
    "ARDS_SELECTION_PATH": "dataset/ards_selected.json",
    "ARDS_SELECTION_GDRIVE_ID": "1rgzC3-aO-AgX08452HrlyxHWnldrjm4o",
    "COCO_TRAIN2017_URL": "http://images.cocodataset.org/zips/train2017.zip",
    "GQA_IMAGES_URL": "https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip",
    "TEXTVQA_IMAGES_URL": "https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip",
    "VG_IMAGES_URL": "https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip",
    "VG_IMAGES2_URL": "https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--download-images", action="store_true")
    parser.add_argument("--skip-ards", action="store_true")
    parser.add_argument("--json-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_env(path: Path) -> dict[str, str]:
    env = dict(DEFAULTS)
    if not path.exists():
        return env

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        env[key.strip()] = value
    return env


def as_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def resolve_path(value: str) -> Path:
    path = Path(os.path.expandvars(os.path.expanduser(value)))
    return path if path.is_absolute() else ROOT / path


def download_hf_file(repo_id: str, filename: str, dest: Path, dry_run: bool) -> None:
    if dest.exists():
        print(f"exists: {dest}")
        return

    print(f"download: hf://datasets/{repo_id}/{filename} -> {dest}")
    if dry_run:
        return

    try:
        from huggingface_hub import hf_hub_download
    except ImportError as exc:
        raise SystemExit(
            "huggingface_hub is required. Run from baselines with: "
            "uv run python scripts/download_llava665k.py"
        ) from exc

    dest.parent.mkdir(parents=True, exist_ok=True)
    downloaded = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        repo_type="dataset",
        local_dir=dest.parent,
    )
    downloaded_path = Path(downloaded)
    if downloaded_path.resolve() != dest.resolve() and not dest.exists():
        shutil.copy2(downloaded_path, dest)


def download_file(url: str, dest: Path, dry_run: bool) -> None:
    if dest.exists():
        print(f"exists: {dest}")
        return

    print(f"download: {url} -> {dest}")
    if dry_run:
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=dest.parent, suffix=".part", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        urllib.request.urlretrieve(url, tmp_path)
        tmp_path.replace(dest)
    finally:
        tmp_path.unlink(missing_ok=True)


def download_google_drive_file(file_id: str, dest: Path, dry_run: bool) -> None:
    if dest.exists():
        print(f"exists: {dest}")
        return

    print(f"download: gdrive://{file_id} -> {dest}")
    if dry_run:
        return

    dest.parent.mkdir(parents=True, exist_ok=True)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    base_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = opener.open(base_url)
    confirm = None
    for _, value in response.headers.items():
        match = re.search(r"download_warning[^=]*=([^;]+)", value)
        if match:
            confirm = match.group(1)
            break

    if confirm is None:
        preview = response.read(4096).decode("utf-8", errors="ignore")
        match = re.search(r"confirm=([0-9A-Za-z_]+)", preview)
        if match:
            confirm = match.group(1)

    if confirm is not None:
        response.close()
        response = opener.open(f"{base_url}&confirm={confirm}")

    with tempfile.NamedTemporaryFile(dir=dest.parent, suffix=".part", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        shutil.copyfileobj(response, tmp)

    response.close()
    tmp_path.replace(dest)


def extract_zip(archive: Path, output_dir: Path, sentinel: Path, keep_archive: bool, dry_run: bool) -> None:
    if sentinel.exists():
        print(f"exists: {sentinel}")
        return

    print(f"extract: {archive} -> {output_dir}")
    if dry_run:
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as zf:
        zf.extractall(output_dir)
    if not keep_archive:
        archive.unlink(missing_ok=True)


def maybe_download_images(env: dict[str, str], keep_archive: bool, dry_run: bool) -> None:
    image_root = resolve_path(env["IMAGE_ROOT"])

    coco_dir = image_root / "coco"
    coco_zip = coco_dir / "train2017.zip"
    download_file(env["COCO_TRAIN2017_URL"], coco_zip, dry_run)
    extract_zip(coco_zip, coco_dir, coco_dir / "train2017", keep_archive, dry_run)

    gqa_dir = image_root / "gqa"
    gqa_zip = gqa_dir / "images.zip"
    download_file(env["GQA_IMAGES_URL"], gqa_zip, dry_run)
    extract_zip(gqa_zip, gqa_dir, gqa_dir / "images", keep_archive, dry_run)

    textvqa_dir = image_root / "textvqa"
    textvqa_zip = textvqa_dir / "train_val_images.zip"
    download_file(env["TEXTVQA_IMAGES_URL"], textvqa_zip, dry_run)
    extract_zip(textvqa_zip, textvqa_dir, textvqa_dir / "train_images", keep_archive, dry_run)

    vg_dir = image_root / "vg"
    vg_zip = vg_dir / "images.zip"
    download_file(env["VG_IMAGES_URL"], vg_zip, dry_run)
    extract_zip(vg_zip, vg_dir, vg_dir / "VG_100K", keep_archive, dry_run)

    vg2_zip = vg_dir / "images2.zip"
    download_file(env["VG_IMAGES2_URL"], vg2_zip, dry_run)
    extract_zip(vg2_zip, vg_dir, vg_dir / "VG_100K_2", keep_archive, dry_run)

    print("manual: OCR-VQA images require the OCR-VQA project download script.")


def main() -> None:
    args = parse_args()
    env = load_env(args.env_file)

    llava_json_path = resolve_path(env["LLAVA_JSON_PATH"])
    download_hf_file(
        repo_id=env["LLAVA_JSON_REPO_ID"],
        filename=env["LLAVA_JSON_FILENAME"],
        dest=llava_json_path,
        dry_run=args.dry_run,
    )

    if as_bool(env["DOWNLOAD_ARDS"]) and not args.skip_ards:
        download_google_drive_file(
            file_id=env["ARDS_SELECTION_GDRIVE_ID"],
            dest=resolve_path(env["ARDS_SELECTION_PATH"]),
            dry_run=args.dry_run,
        )

    download_images = as_bool(env["DOWNLOAD_IMAGES"]) or args.download_images
    if args.json_only:
        download_images = False

    if download_images:
        maybe_download_images(env, keep_archive=as_bool(env["KEEP_ARCHIVES"]), dry_run=args.dry_run)
    else:
        print("skip: image archives; set DOWNLOAD_IMAGES=true or pass --download-images")

    print(f"configured Arrow dataset: {resolve_path(env['LLAVA_ARROW_DIR'])}")
    print(f"configured ARDS selection: {resolve_path(env['ARDS_SELECTION_PATH'])}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
