from transformers import pipeline
auth_token = "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"

nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english",
               tokenizer="distilbert-base-uncased-finetuned-sst-2-english", use_auth_token=auth_token)


def predict_sentiment(prompt: str):
    return nlp(prompt)[0]
