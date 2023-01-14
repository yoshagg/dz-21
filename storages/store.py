from storages.base_storage import BaseStorage


class Store(BaseStorage):
    def __init__(self):
        self.items = {}
        self.capacity = 20

    def add(self, name, count):
        try:
            if self.capacity > 0 and count <= self.capacity:
                if self.get_unique_items_count() < 5:
                    self.capacity -= count
                    if name not in self.items.keys():
                        self.items[name] = count
                    elif name in self.items.keys():
                        self.items[name] += count
                else:
                    return print("В магазине может быть не больше 5 уникальных товаров")
            else:
                return print("Недостаточно места")
        except Exception as e:
            return e
