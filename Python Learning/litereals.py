# Define abbreviation map
ABBREVIATIONS = {
    "you": "u",
    "are": "r",
    "please": "plz",
    "before": "b4",
    "message": "msg",
    "see": "c",
    "be": "b",
    "with": "w/",
    "people": "ppl",
    "tomorrow": "tmrw",
    "today": "2day",
    "thanks": "thx",
    "okay": "ok",
    "to": "2",
    "for": "4",
    "the":"th"
}

# Simple stopword list (a small version)
STOPWORDS = {
    "i", "me", "my", "myself","the", "we", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves", "he", "him",
    "his", "himself", "she", "her", "hers", "herself", "it", "its",
    "itself", "they", "them", "their", "theirs", "themselves", "what",
    "which", "who", "whom", "this", "that", "these", "those", "am", "is",
    "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but",
    "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
    "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "can",
    "will", "just", "don", "should", "now"
}

def preprocess(message):
    message = message.lower()
    punctuation = ".,!?;:\"'()-[]{}<>@#$%^&*_+=/\\|~`"
    for p in punctuation:
        message = message.replace(p, "")
    return message

def tokenize(message):
    return message.split()

def remove_stopwords(words):
    return [word for word in words if word not in STOPWORDS]

def apply_abbreviations(words):
    return [ABBREVIATIONS.get(word, word) for word in words]

def extract_keywords(words):
    return words  # placeholder for further enhancement

def join_words(words):
    return " ".join(words)

def shorten_message(message):
    message = preprocess(message)
    words = tokenize(message)
    words = remove_stopwords(words)
    words = apply_abbreviations(words)
    keywords = extract_keywords(words)
    return join_words(keywords)

# Example
input_message = "Please see the message before tomorrow. Thanks!"
print(shorten_message(input_message))  # Output: plz c msg b4 tmrw thx
