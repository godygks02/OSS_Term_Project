!pip install transformers

from transformers import pipeline

# Hugging Face의 감정 분석 파이프라인 로드
sentiment_analyzer = pipeline("sentiment-analysis")

# 분석할 텍스트 데이터
texts = [
    "I love this movie! It's fantastic!",
    "This is the worst experience I've ever had.",
    "The product is okay, not great but not bad.",
    "I'm so happy with the results!",
    "I'm really disappointed with the service."
]

# 감정 분석 실행
results = sentiment_analyzer(texts)

# 결과 출력
for i, text in enumerate(texts):
    print(f"Text: {text}")
    print(f"Sentiment: {results[i]['label']}, Score: {results[i]['score']:.2f}")
    print("-" * 50)

while True:
    user_text = input("Enter a sentence to analyze sentiment (type 'exit' to quit): ")
    if user_text.lower() == "exit":
        break
    result = sentiment_analyzer(user_text)
    print(f"Sentiment: {result[0]['label']}, Score: {result[0]['score']:.2f}")
