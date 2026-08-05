class CallByValueAndReference:
    def __init__(self):
        self.value = 0
        self.nested_tuple = ((1, 2), (3, 4))
        self.list_obj = [0, 1, 2]

    def call_by_value(self, x, nested_tuple):
        x += 10
        print(f"Inside call_by_value: x = {x}")
        print(f"object id of x inside call_by_value: {id(x)}")
        #nested tuples
        # nested_tuple[0] = (5, 6)
        print(f"Inside call_by_value: nested_tuple = {nested_tuple}")
        print(f"object id of nested_tuple inside call_by_value: {id(nested_tuple)}")

    def call_by_reference(self, obj, list_obj):
        obj.value += 10
        print(f"Inside call_by_reference: obj.value = {obj.value}")
        print(f"object id of obj inside call_by_reference: {id(obj)}")
        list_obj = [1, 2, 3]
        list_obj.append(4)
        print(f"Inside call_by_reference: list_obj = {list_obj}")
    def call_by_value_with_nested(self, x, nested_tuple):
        x += 10
        print(f"Inside call_by_value_with_nested: x = {x}")
        print(f"object id of x inside call_by_value_with_nested: {id(x)}")
        # #nested tuples
        # nested_tuple[0] = (5, 6)
        print(f"Inside call_by_value_with_nested: nested_tuple = {nested_tuple}")
        print(f"object id of nested_tuple inside call_by_value_with_nested: {id(nested_tuple)}")

if __name__ == "__main__":
    obj = CallByValueAndReference()
    print(f"Before call_by_value: obj.value = {obj.value}")
    print(f"object id of obj before call_by_value: {id(obj)}")
    obj.call_by_value(obj.value, obj.nested_tuple)
    print(f"After call_by_value: obj.value = {obj.value}")
    print(f"object id of obj after call_by_value: {id(obj)}")

    print("\n---\n")

    print(f"Before call_by_reference: obj.value = {obj.value}")
    print(f"object id of obj before call_by_reference: {id(obj)}")
    obj.call_by_reference(obj, obj.list_obj)
    print(f"After call_by_reference: obj.value = {obj.value}")
    print(f"object id of obj after call_by_reference: {id(obj)}")
    print(f"Before call_by_value: obj.nested_tuple = {obj.nested_tuple}")
    print(f"object id of obj.nested_tuple before call_by_value: {id(obj.nested_tuple)}")
    obj.call_by_reference(obj, obj.list_obj)
    print(f"Before call_by_reference: obj.list_obj = {obj.list_obj}")
    print(f"After call_by_reference: obj.list_obj = {obj.list_obj}")
    print(f"object id of obj.list_obj after call_by_reference: {id(obj.list_obj)}")
    print("\n---\n")
    obj.call_by_value_with_nested(obj.value, obj.nested_tuple)