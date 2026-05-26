"""Fixed training configuration for multimodal finetune methods.

All hyperparameters are constants by default. The caller may provide a
small set of safe overrides in the run config (for smoke tests).
"""

DEFAULT_QWEN_MODEL = "Qwen/Qwen2.5-VL-7B-Instruct"
DEFAULT_LLAVA_MODEL = "llava-hf/llava-1.5-7b-hf"
DEFAULT_SMOLVLM_MODEL = "HuggingFaceTB/SmolVLM-Base"
DEFAULT_SMOLVLM_256M_MODEL = "HuggingFaceTB/SmolVLM-256M-Base"
DEFAULT_SMOLVLM_500M_MODEL = "HuggingFaceTB/SmolVLM-500M-Base"

QWEN_FIXED_TRAINING_ARGS = dict(
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=1e-5,
    weight_decay=0.1,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    bf16=True,
    optim="adamw_torch_fused",
    gradient_checkpointing=True,
    dataloader_num_workers=4,
    save_strategy="no",
    report_to="none",
    remove_unused_columns=False,
)

LLAVA_FULL_FT_TRAINING_ARGS = dict(
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    learning_rate=2e-5,
    weight_decay=0.0,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    bf16=True,
    optim="adamw_torch_fused",
    gradient_checkpointing=True,
    dataloader_num_workers=2,
    save_strategy="no",
    report_to="none",
    remove_unused_columns=False,
    logging_steps=1,
)

# SmolVLM-Base is a ~2B-param model so we can afford a larger effective batch
# than LLaVA-1.5-7B at the same memory budget. Image preprocessing is heavier
# (tile splitting), hence dataloader_num_workers=2.
SMOLVLM_FULL_FT_TRAINING_ARGS = dict(
    num_train_epochs=1,
    per_device_train_batch_size=16,
    gradient_accumulation_steps=1,
    learning_rate=1e-5,
    weight_decay=0.0,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    bf16=True,
    optim="adamw_torch_fused",
    gradient_checkpointing=True,
    dataloader_num_workers=2,
    save_strategy="no",
    report_to="none",
    remove_unused_columns=False,
    logging_steps=1,
)

DEFAULT_QWEN2VL_2B_MODEL = "Qwen/Qwen2-VL-2B"

QWEN2VL_2B_FIXED_TRAINING_ARGS = dict(
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=1e-5,
    weight_decay=0.1,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    bf16=True,
    tf32=True,
    optim="adamw_torch_fused",
    adam_beta2=0.95,
    gradient_checkpointing=True,
    dataloader_num_workers=4,
    save_strategy="no",
    report_to="none",
    remove_unused_columns=False,
    ddp_find_unused_parameters=True,
)
