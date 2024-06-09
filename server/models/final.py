# to ensure that an attribute can not longer be set after it 
# is set initially

class Final:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if getattr(instance, self.private_name, False):
            raise AttributeError('Attribute can no longer be mutated')
        setattr(instance, self.private_name, value)

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'
