import re  # regular expressions

input_list = ['9999999999', '9999999999999', '8999999999', '7999999999', '999999-999', 'some text', '99999x9999']
input_list_int = list()

input_list = list(filter(lambda x: len(x) == 10, input_list))
result = list(filter(lambda x: x[0] == "9" or x[0] == "8", input_list))


for item in result:
    try:
        input_list_int.append(int(item))
    except ValueError:
        pass

print(input_list_int)


