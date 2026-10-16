def remove_fourth_character(word: str) -> str:
    bf = word[:3]
    af = word[4:]
    return bf + af


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
