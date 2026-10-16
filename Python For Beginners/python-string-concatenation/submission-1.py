def concatenate(s1: str, s2: str) -> str:
    l = s1 + s2
    leng = len(l)
    if leng > 10:
        return "Too long"
    else:
        return l



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
