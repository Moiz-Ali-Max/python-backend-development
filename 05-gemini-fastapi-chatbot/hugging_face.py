from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "tencent/HY-MT1.5-1.8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

while True:
    text = input("You: ")

    if text.lower() == "exit":
        break

    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=100
    )

    reply = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Bot:", reply)
