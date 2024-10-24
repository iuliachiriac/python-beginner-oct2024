vowels = "aeiouAEIOU"


def remove_vowels(input_str):
    output_str = ""
    for char in input_str:
        if char in vowels:
            continue
        output_str += char
    return output_str


if __name__ == "__main__":
    text = """In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now."""
    text_without_vowels = remove_vowels(text)
    print(text_without_vowels)
