def getSimple(state=[]):
    if len(state) < 4:
        state.append(" ")
        return " "


testIt2 = iter(getSimple, None)
print(x for x in testIt2)
