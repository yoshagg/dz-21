from abc import ABC, abstractmethod


class Storage(ABC):
    @property
    @abstractmethod
    def add(self):
        pass

    @property
    @abstractmethod
    def remove(self):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


class BaseStorage(Storage):
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, name, count):
        try:
            if self.capacity > 0 and count <= self.capacity:
                self.capacity -= count
                if name not in self.items.keys():
                    self.items[name] = count
                elif name in self.items.keys():
                    self.items[name] += count
            else:
                return "Недостаточно места"
        except Exception as e:
            return e

    def remove(self, name, count):
        try:
            if count <= self.items[name]:
                self.items[name] -= count
                self.capacity += count
                if self.items[name] <= 0:
                    del self.items[name]
            else:
                return print("На точке нет такого товара или вы указали большое количество")
        except Exception as e:
            print(e)

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        items_list = []
        for k in self.get_items().keys():
            items_list.append(k)
        return len(set(items_list))


# items = {"печенька": 3}
# def test(items):
#     return items

# print(test(items))
