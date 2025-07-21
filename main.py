from stats import get_word_count, get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    num_words = get_word_count(content)
    print(f"{num_words} words found in the document")
    char_dict = get_character_count(content)
    print(char_dict)
    
main()