from transformers import pipeline

class Summarization():
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    def news_s(self, sentence):
        return self.summarizer(sentence, max_length=130, min_length=30, do_sample=False)
