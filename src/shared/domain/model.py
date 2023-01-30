class IModel:
    pass

def need_attribute(attribute_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            attr_value = getattr(self, attribute_name)
            if attr_value is None:
                raise AttributeError(f"{attribute_name} is required to perform this action")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
