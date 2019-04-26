class ListKhafan(list):
    def __getitem__(self, item):
        return super().__getitem__(item-1)


class RotationList(list):
    def __getitem__(self, item):
        return super().__getitem__(item % len(self))

    def __setitem__(self, key, value):
        return super().__setitem__(key % len(self), value)

something = ListKhafan([1, 2, 3, 4, 5])
print(something[1])
something.__getitem__(1)

rot = RotationList([1, 2, 3, 4, 5])
print(rot[1001])
rot[1001] = 1000

print(rot)