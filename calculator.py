# function overloading example
def add(datatype, *args):
    result = ""
    if datatype == "int":
        result = 0
    if datatype == "str":
        result = ""

    for value in args:
        result += value
    return result


addition = add("str", "ade", "wer")
print(addition)
