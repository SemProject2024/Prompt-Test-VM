import pandas as pd
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, TrainingArguments, Trainer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

df = pd.read_csv('/content/Shuffled-Resource-Groups.csv')

df['text'] = df['prompt'] + ',"' + df['code'] + '"'

df['text'].to_csv('training_data.txt', index=False, header=False)

import accelerate
import transformers

model_path = "/content/gpt2_model"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

dataset = TextDataset(tokenizer=tokenizer, file_path="training_data.txt", block_size=128)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

training_args = TrainingArguments(
    output_dir="./output",
    overwrite_output_dir=True,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
    evaluation_strategy="steps",
    eval_steps=10_000,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=100,
    report_to="wandb",
    logging_first_step=True,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    gradient_accumulation_steps=1,
    learning_rate=5e-5,
    weight_decay=0.0,
    adam_beta1=0.9,
    adam_beta2=0.999,
    adam_epsilon=1e-8,
    max_grad_norm=1.0,
    num_train_epochs=3,
    max_steps=-1,
    lr_scheduler_type="linear",
    warmup_ratio=0.0,
    warmup_steps=0,
    seed=42,
    dataloader_pin_memory=True,
    skip_memory_metrics=True,
    fp16=False,
    label_smoothing_factor=0.0,
    adafactor=False,
    report_to=["tensorboard"],
    run_name="run_name",
    disable_tqdm=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)
trainer.train()


model_path = "/content/gpt2_model"
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

def generate_code(input_text, max_length=100, num_return_sequences=1, device="cpu"):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    model.to(device)

    generated_code = model.generate(input_ids.to(device), max_length=max_length, num_return_sequences=num_return_sequences)

    decoded_code = tokenizer.decode(generated_code[0], skip_special_tokens=True)

    return decoded_code

if __name__ == "__main__":
    input_text = input("Enter input text: ")

    device = "cuda" if torch.cuda.is_available() else "cpu"

    generated_code = generate_code(input_text, device=device)

    print("Generated code:")
    print(generated_code)
    

model = GPT2LMHeadModel.from_pretrained("/content/gpt2_model")
tokenizer = GPT2Tokenizer.from_pretrained("/content/gpt2_model")

input_text = input()
input_ids = tokenizer.encode(input_text, return_tensors="pt")  
trainer.model.to(input_ids.device)
generated_code = trainer.model.generate(input_ids, max_length=100, num_return_sequences=1)
decoded_code = tokenizer.decode(generated_code[0], skip_special_tokens=True)
print(generated_code)
print(decoded_code)





