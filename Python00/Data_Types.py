class DataTypes:
    def __init__(self):
        self.integer_value = 10
        self.float_value = 10.5
        self.string_value = "Hello, World!"
        self.boolean_value = True
        self.list_value = [1, 2, 3, 4, 5]
        self.tuple_value = (1, 2, 3)
        self.set_value = {1, 2, 3}
        self.dict_value = {"key1": "value1", "key2": "value2"}

    def display_data_types(self):
        print(f"Integer: {self.integer_value}")
        print(f"Float: {self.float_value}")
        print(f"String: {self.string_value}")
        print(f"Boolean: {self.boolean_value}")
        print(f"List: {self.list_value}")
        print(f"Tuple: {self.tuple_value}")
        print(f"Set: {self.set_value}")
        print(f"Dictionary: {self.dict_value}")

if __name__ == "__main__":
    data_types = DataTypes()
    data_types.display_data_types()
    