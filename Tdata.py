from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

# Load your dataset from the text file
dataset = load_dataset('text', data_files='C:/Users/harpi/Documents/memory-tic-tac-toe/questions.txt')

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
tokenizer.pad_token = tokenizer.eos_token  # Set padding token to eos_token

# Tokenize the dataset
def tokenize_function(examples):
    encodings = tokenizer(examples['text'], padding="max_length", truncation=True)
    encodings['labels'] = encodings['input_ids'].copy()  # Set labels for loss calculation
    return encodings

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",          # Output directory
    evaluation_strategy="epoch",     # Evaluation strategy
    learning_rate=2e-5,              # Learning rate
    per_device_train_batch_size=4,   # Batch size for training
    per_device_eval_batch_size=4,    # Batch size for evaluation
    num_train_epochs=3,              # Number of training epochs
    weight_decay=0.01,               # Strength of weight decay
    save_total_limit=2,              # Limit the total amount of checkpoints
    logging_dir='./logs',            # Directory for storing logs
)

# Load the model
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['train']  # Use the same for simplicity; you can use a different split
)

# Train the model
trainer.train()

