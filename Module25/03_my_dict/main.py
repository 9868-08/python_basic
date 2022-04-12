class MyDict:
    def __init__(self, incoming_dict):
        self.def_dict = dict()
        for key in incoming_dict:
            self.def_dict[key] = incoming_dict[key]
        return


    def get(self, key_def):
        if key_def in self.def_dict.keys():
#            print("key=", key_def, "self.def_dict.keys()=", self.def_dict.keys())
            return self.def_dict[key_def]
        else:
            return 0


my_dict = {0: "zero", 1: "one"}
my_new_dict = MyDict(my_dict)

print("my_dict=", my_dict.get(0))
print("my_dict=", my_dict.get(2))
print("my_new_dict=", my_new_dict.get(0))
print("my_new_dict=", my_new_dict.get(2))
