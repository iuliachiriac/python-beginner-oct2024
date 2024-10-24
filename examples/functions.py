X = 4


def welcome(name: str, age: int, is_student: bool = False, hobbies: list = None):
    if not isinstance(name, str):
        print("Error! name is not a string!!")
    print(f"{name} is {age} years old.")
    if is_student:
        print(f"{name} is a student.")
    if hobbies:
        print(f"{name} has the following hobbies:")
        for hobby in hobbies:
            print(f" - {hobby}")


def welcome_2(name, age, is_student=False, hobbies=None):
    print(f"{name} is {age} years old.")
    if is_student:
        print(f"{name} is a student.")
    if hobbies:
        print(f"{name} has the following hobbies:")
        for hobby in hobbies:
            print(f" - {hobby}")


if __name__ == "__main__":
    welcome(10, 20)
    welcome("Ana", 21, hobbies=[])

    lst = [200, 7, 56456, 45, 1, 2, 3]
    list_length = len(lst)
    print(len(lst))
    print(list_length)
    print(7)
