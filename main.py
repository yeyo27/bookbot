def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_letters(text: str) -> dict[str, int]:
    chars = {}
    for c in text.casefold():
        # dict.get: if c doesn't exist in chars, value is 0. Then add 1
        chars[c] = chars.get(c, 0) + 1
    return chars


def print_report(text: str) -> None:
    print(f"--- Beginning report of {BOOK_PATH} ---")
    words_number = count_words(text)
    print(f"Number of words: {words_number}")
    chars = count_letters(file_contents)
    for c in sorted(list(chars)):
        if c.isalpha():
            print(f"The letter '{c}' appears {chars[c]} times")
    print(f"--- End report ---")


if __name__ == "__main__":
    BOOK_PATH = "books/frankenstein.txt"
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        print_report(file_contents)
