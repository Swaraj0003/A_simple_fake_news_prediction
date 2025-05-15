import pickle

with open('ml_model/model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

def predict_news(news_text):
    vec = vectorizer.transform([news_text])
    prediction = model.predict(vec)
    return prediction[0]
