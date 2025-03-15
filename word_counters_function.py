# ESPINO, NICHAELA
# ITELECT2
# Laboratory #23 - Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python 

def get_sentence_input() -> str:
    return input("Enter a sentence: ")
def count_words(sentence: str) -> int:
    words = sentence.split()
    return len(words)
def main():
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")
if __name__ == "__main__":
    main()