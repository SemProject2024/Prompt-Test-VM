import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, TrainingArguments, Trainer
model = GPT2LMHeadModel.from_pretrained("/content/gpt2_model")
tokenizer = GPT2Tokenizer.from_pretrained("/content/gpt2_model")
dataset = TextDataset(tokenizer=tokenizer, file_path="training_data.txt", block_size=128)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./output",
    overwrite_output_dir=True,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
    evaluation_strategy="steps",
    eval_steps=10_000,
    num_train_epochs=3,
)

# Create Trainer and start training
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)
input_text = input()
input_ids = tokenizer.encode(input_text, return_tensors="pt")  # Convert the input text to token IDs
trainer.model.to(input_ids.device)
# Generate text using the model
generated_code = trainer.model.generate(input_ids, max_length=100, num_return_sequences=1)
decoded_code = tokenizer.decode(generated_code[0], skip_special_tokens=True)
print(generated_code)
print(decoded_code)