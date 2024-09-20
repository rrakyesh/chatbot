from transformers import pipeline

model = pipeline("text-generation", model="EleutherAI/gpt-j-6B")

def run_llm(document_text, rule):
    prompt = f"Check if this document satisfies the rule: {rule}\nDocument: {document_text}"
    response = model(prompt)
    return response[0]['generated_text']
