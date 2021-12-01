def read_as_ints(filename):
    f = open(filename, "r")
    string_list = f.read().split("\n")
    return [int(i) for i in string_list]
