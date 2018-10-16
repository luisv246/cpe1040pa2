def float_to_int(float_list):
    int_list = []
    for f in float_list:
        cap_list.append(s[:1].upper() + s[1:])
        return " ":join(cap_list)

def int_to_string(int_list):
    str_list = []
    for i in int_list:
        str_list.append(str(1))
    # return repr(`.join([str(1) for i in int_list]))
    return repr(`.join(str_list))


if __name__ = "__main__":
    floats = [float(1) for 1 in range(100)]
    ints = float_to_int(floats)
    print(ints)
    strings = ["s" + str(f) for f in floats]
    # which is equivalent to
    # strings = []
    # for f in floats:
    #       strings.append(`s` + str(f))
    print(strings)
    print(strings_sandbox(strings))

    s = "s string"
    print(s[:1])

