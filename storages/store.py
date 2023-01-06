class Store:
    items = {}
    capacity = 100

    @staticmethod
    def add(name, count):
        try:
            if Store.capacity > 0 and count <= Store.capacity:
                Store.items[name] = count
                Store.capacity -= count
            else:
                return "Недостаточно места"
        except Exception as e:
            return e

    @staticmethod
    def remove(name, count):
        try:
            if count <= Store.capacity:
                Store.items[name] -= count
                if Store.items[name] <= 0:
                    del Store.items[name]
            else:
                return "Вы не можете сделать вместимость меньше нуля"
        except Exception as e:
            return e

    @staticmethod
    def get_free_space():
        return Store.capacity

    @staticmethod
    def get_items():
        return Store.items

    @staticmethod
    def get_unique_items_count():
        items_list = []
        for k in Store.get_items().keys():
            items_list.append(k)
        return len(set(items_list))
