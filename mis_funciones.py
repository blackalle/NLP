from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords

wpt = WordPunctTokenizer()
stop_words = set(stopwords.words('spanish'))

def normalize_document(doc):
    doc = doc.replace("!", "").replace("¡", "").replace(",", "").replace(".", "")
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc
