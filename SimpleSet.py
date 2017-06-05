class SimpleSet:

    def __init__(self,values=None):
        s1 = SimpleSet()
        s2 = SimpleSet([1,2,3,4])
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

# This is the String representation of a Set Object,
# if you type it at the python prompt or pass it to str()
    def __repr__(self):
        return "SimpleSet: " + str(self.dict.keys())

    def add(self,value):
        self.dict[value] = True

    def contains(self,value):
        return value in self.dict

    def remove(self,value):
        del self.dict[value]