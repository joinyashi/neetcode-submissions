from typing import List

def count_unique_words(words: List[str]) -> int:
    a = set(words)
    u_a = list(a)
    c_a = len(u_a)
    return c_a

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
