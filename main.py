def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowered_string = text.lower()
    chars = {}
    for char in lowered_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
