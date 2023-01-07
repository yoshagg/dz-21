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

    @property
    def add(self, name, count):
        try:
            if self.capacity > 0 and count <= self.capacity:
                self.items[name] = count
                self.capacity -= count
            else:
                return "Недостаточно места"
        except Exception as e:
            return e

    @property
    def remove(self, name, count):
        try:
            if count <= self.capacity:
                self.items[name] -= count
                if self.items[name] <= 0:
                    del self.items[name]
            else:
                return "Вы не можете сделать вместимость меньше нуля"
        except Exception as e:
            print(e)

    @property
    def get_free_space(self):
        return self.capacity

    @property
    def get_items(self):
        return self.items

    @property
    def get_unique_items_count(self):
        items_list = []
        for k in self.get_items().keys():
            items_list.append(k)
        return len(set(items_list))
