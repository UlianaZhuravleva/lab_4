class Unique(object):
    def __init__(self, items, **kwargs):
        self.items=items
        self.arr = []
        try:
            self.ignore_case=kwargs.get('ignore_case')
        except:
            self.ignore_case = False
        if type(self.items) == list: iter(self.items)

    def __next__(self):
        for i in self.items:
            if (self.ignore_case == True) and (type(i) != int):
                if i.upper() in self.arr: continue
                else:
                    self.arr.append(i.upper())
                    return i
            else:
                if i in self.arr: continue
                else:
                    self.arr.append(i)
                    return i
        raise StopIteration

    def __iter__(self):
        return self


