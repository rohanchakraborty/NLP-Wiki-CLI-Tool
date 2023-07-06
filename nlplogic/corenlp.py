from textblob import TextBlob
import wikipedia


def search_wiki(name):
    print(f"Search for name {name}")
    return wikipedia.search(name)


def summarize_wiki(name):
    """Logic"""
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Returns Text Blob"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """find wikipedia name and return phrases"""
    text = summarize_wiki(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
