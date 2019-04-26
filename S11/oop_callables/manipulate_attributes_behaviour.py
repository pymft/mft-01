class WeirdTuple(tuple):
    def __getattribute__(self, item):
        if item.startswith('_') and item[1:].isdigit():
        # if item[0] == '__' and item[1:].isdigit():
            indx = int(item[1:])
            return self[indx]

        return super().__getattribute__(item)


w = WeirdTuple([1, 2, 3, 4,])
w._1
