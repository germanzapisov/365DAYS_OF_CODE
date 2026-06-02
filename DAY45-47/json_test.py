import json


# data_json = json.dumps(data)
#
# new_data = json.loads(data_json)
#
# print(new_data)
#

def logg(func):
    def wrapper(*args):
        print("Start")
        result = func(*args)
        print("Finish!")
        return result
    return wrapper

class JsonSchema:
    def __init__(self, data):
        self.__data = data

    @logg
    def writer(self):
        with open ('data.json', "w") as f:
            json.dump(self.__data, f,
                          ensure_ascii=False,
                          indent = 1)


    @logg
    def reader(self):
        with open('data.json') as f:
            try:
                create_data = json.load(f)
                for el in create_data:
                    print(el)
                return create_data
            except json.JSONDecodeError:
                print("invalid data")

def menu():
    while True:
        choice = int(input("Select an action from the list below\n"
                           "1 >> Write to Json File\n"
                           "2 >> Output information from Json File"))
        if choice == 1:
            json_schema.writer()
        elif choice == 2:
            json_schema.reader()

if __name__ == "__main__":
    data = [
        {"Gerkaaa": 'skittles'},
        {"Andrew": 'M&Ms'}
            ]
    json_schema = JsonSchema(data)
    menu()