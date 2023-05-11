#   default parameters and keyword arguments


def test(name = "Rodrygoes", age = "23"):
    print(f"Hello {name}. You are {age} years old")

test()
test("Israk", 20)
test(age = 20, name = "Vini")