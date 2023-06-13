import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        myList = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            if i == "price":
                myList.append(f"{i} : ${ordered[i]}")
            else:
                myList.append(f"{i} : {ordered[i]}")
            myList.append("\n")
        return ''.join(myList)

    def copy(self):
        object = self
        return object


class Prototype:

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier, obj):
        del self.objects[identifier]

    def deepClone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(
                f"Object not found or Incorrect identifier: {identifier}")

        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(
                f"Object not found or Incorrect identifier: {identifier}")

        obj = found.copy()
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book(name="C Programing Language",
              authors=("Forrest", "Snow"),
              price=118,
              publisher="A",
              length=228,
              publiocation_date="1983-04-15",
              tags=("C", "data", "algo", "BigO"))
    prototype = Prototype()

    cid = "book1"
    prototype.register(cid, b1)

    b2 = prototype.deepClone(cid,
                             price=48.99,
                             publisher="A",
                             length=228,
                             publiocation_date="1983-04-15",
                             version=2)

    for i in (b1, b2):
        print(i)

    print(f"{id(b1) != id(b2)}")
    b3 = prototype.clone(cid,
                         price=8.99,
                         publisher="山寨版",
                         length=2280,
                         publiocation_date="1983-04-15",
                         version=20)
    for i in (b1, b2, b3):
        print(i)

    print(f"{(id(b1) == id(b3)) and (id(b3) != id(b2))}")


if __name__ == "__main__":
    main()