def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didn't enter any names"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name(input("enter your name"), input("enter your name")))
