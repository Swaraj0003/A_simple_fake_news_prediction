import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv("news.csv")  # Should have 'text' and 'label'

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = PassiveAggressiveClassifier(max_iter=50)
model.fit(X_train_tfidf, y_train)

# Save model and vectorizer
with open('ml_model/model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)
