def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


inc = '192.168.0.255'
list = list(inc.split("."))
print(list)
for i in list:
    if RepresentsInt(i) and int(i) < 254:
        q = 1
    else:
        print(i, 'превышает 254 или это не число')
