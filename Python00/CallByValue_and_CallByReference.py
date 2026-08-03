class CallByValueAndReference:
    def __init__(self):
        self.value = 0

    def call_by_value(self, x):
        x += 10
        print(f"Inside call_by_value: x = {x}")
        print(f"object id of x inside call_by_value: {id(x)}")

    def call_by_reference(self, obj):
        obj.value += 10
        print(f"Inside call_by_reference: obj.value = {obj.value}")
        print(f"object id of obj inside call_by_reference: {id(obj)}")
    
if __name__ == "__main__":
    obj = CallByValueAndReference()
    print(f"Before call_by_value: obj.value = {obj.value}")
    print(f"object id of obj before call_by_value: {id(obj)}")
    obj.call_by_value(obj.value)
    print(f"After call_by_value: obj.value = {obj.value}")
    print(f"object id of obj after call_by_value: {id(obj)}")

    print("\n---\n")

    print(f"Before call_by_reference: obj.value = {obj.value}")
    print(f"object id of obj before call_by_reference: {id(obj)}")
    obj.call_by_reference(obj)
    print(f"After call_by_reference: obj.value = {obj.value}")
    print(f"object id of obj after call_by_reference: {id(obj)}")

    