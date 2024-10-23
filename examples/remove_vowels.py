vowels = "aeiouAEIOU"


def remove_vowels(text):
    output = ""
    for char in text:
        if char not in vowels:
            output += char
    return output


poem = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested."""
print(remove_vowels(poem), end="\n\n")
print(remove_vowels("hello world"), end="\n\n")
print(remove_vowels("test"))
