import torch
from transformers import AutoTokenizer, BertForSequenceClassification
from fastapi import FastAPI
from models import MessageCreate
from utils import *

app = FastAPI()

classes = dict({
    "3" : 'Otra', 
    "4" : 'Regulaciones', 
    "0" : 'Alianzas', 
    "2" : 'Macroeconomia', 
    "1" : 'Innovacion',
    "6" : 'Sostenibilidad', 
    "5" : 'Reputacion'
})

@app.post('/message')
async def predict(message: MessageCreate):
    try:
        model, tokenizer = model_tokenizer_maker("Alwaly/spanish-text-classification", 7)
        with torch.no_grad():
            input = tokenizer(message.text, return_tensors='pt')
            output = model(**input)
            pred = torch.max(output.logits, dim=1)
            indice = pred.indices.item()
            print(pred)
        return {
                "status": 200,
                "classes":classes[f"{indice}"],
                "probability": pred.values.item()
            }
    except OSError:
        return {
                "status": 401,
                "Message": "Le model n'existe pas sur le hub de huggingface"
            }

  