import string

def count_unique_words(text):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return len(set(words))

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def count_word_occurrences(text, target_word):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return words.count(target_word.lower())

def percentage_long_words(text):
    words = text.split()
    avg_length = sum(len(word) for word in words) / len(words)
    long_words = [word for word in words if len(word) > avg_length]
    return (len(long_words) / len(words)) * 100

# Example Usage:
text = """Python is an amazing programming language. It is widely used for data science, 
machine learning, web development, and automation. Python's simplicity makes it popular."""

print("Unique word count:", count_unique_words(text))
print("Longest word:", find_longest_word(text))
print("Occurrences of 'Python':", count_word_occurrences(text, "Python"))
print("Percentage of words longer than average:", percentage_long_words(text), "%")