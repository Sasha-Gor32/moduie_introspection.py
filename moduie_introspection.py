
{'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
def introspection_info(obj):
    obj_type = type(obj).__name__
    attrgetter = dir(obj)
    methods = [method for method in attrgetter if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attrgetter': attrgetter, 'methods': methods, 'module': module},
    return info
number_info = introspection_info(42)
print(number_info)
string_info = introspection_info('Hello')
print(string_info)
list_info = introspection_info([1, 20, 4.0, 'word'])
print(list_info)