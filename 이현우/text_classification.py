from transformers import pipeline

class Classification():
    def __init__(self):
        self.pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
    def news_c(self, sentence):
        return self.pipe([sentence])
