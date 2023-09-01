from transformers import AutoTokenizer, BertForSequenceClassification

def model_tokenizer_maker(name, num_labels):
    tokenizer = AutoTokenizer.from_pretrained(name)
    model = BertForSequenceClassification.from_pretrained(name, num_labels=num_labels)
    return model, tokenizer