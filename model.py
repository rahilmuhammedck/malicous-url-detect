import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Reading data from csv file
data = pd.read_csv("data.csv")

# Labels
y = data["label"]

# Features
url_list = data["url"]

# Using TfidfVectorizer
vectorizer = TfidfVectorizer()

# Store vectors into X variable as Our XFeatures
X = vectorizer.fit_transform(url_list)

# Split into training and testing dataset 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building using logistic regression
logit = LogisticRegression()
logit.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(logit, "model_file.pkl")
joblib.dump(vectorizer, "vectorizer_file.pkl")
