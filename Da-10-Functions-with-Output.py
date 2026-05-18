def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name("mostafa", "ghasemi"))

### second one
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

out_put = function_2(function_1("hello"))
print(out_put)