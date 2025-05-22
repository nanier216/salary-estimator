from sklearn.feature_extraction.text import TfidfVectorizer

def extract_skills_tfidf(texts, top_k=10):
    tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
    X = tfidf.fit_transform(texts)
    features = tfidf.get_feature_names_out()
    scores = X.sum(axis=0).A1
    keywords = sorted(zip(features, scores), key=lambda x: -x[1])[:top_k]
    return [kw[0] for kw in keywords]
