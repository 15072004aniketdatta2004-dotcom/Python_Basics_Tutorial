class DataTypes:
    def __init__(self):
        self.integer_value = 10
        self.float_value = 10.5
        self.string_value = "Hello, World!"
        self.boolean_value = True
        self.list_value = [[1, 2], [3, 4, 5]]
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

    def shallow_copy(self):
        shallow_copied_list = self.list_value.copy()
        self.list_value.append([6, 7])
        print("original List after shallow copy: ", self.list_value)
        print("Object id of the original list: ", id(self.list_value))
        print(f"Original List after shallow copy: {self.list_value}")
        print(f"Shallow Copied List: {shallow_copied_list}")
        print(f"Object id of the shallow copied list: {id(shallow_copied_list)}")
        print(f"Object id of the shared internal lists: {id(self.list_value[0])} for original list and {id(shallow_copied_list[0])} for shallow copy")
        shallow_copied_list.remove([1, 2])
        print("original List after removing an element from shallow copy: ", self.list_value)
    def deep_copy(self):
        import copy
        deep_copied_list = copy.deepcopy(self.list_value)
        self.list_value.append([8, 9])
        print("original List after deep copy: ", self.list_value)
        print("Object id of the original list: ", id(self.list_value))
        print(f"Original List after deep copy: {self.list_value}")
        print(f"Deep Copied List: {deep_copied_list}")
        print(f"Object id of the deep copied list: {id(deep_copied_list)}")
        print(f"Object id of the shared internal lists: {id(self.list_value[0])} for original list and {id(deep_copied_list[0])} for deep copy")
        deep_copied_list.remove([3, 4, 5])
        print("Deep Copied List after removing an element: ", deep_copied_list)
        print("original List after removing an element from deep copy: ", self.list_value)
       
if __name__ == "__main__":
    data_types = DataTypes()
    data_types.display_data_types()
    data_types.shallow_copy()
    data_types.deep_copy()
