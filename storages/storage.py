class Storage:
    items = {"печенька": 3}
    capacity = 5

    @staticmethod
    def add(name, count):
        try:
            if Storage.capacity > 0 and count <= Storage.capacity:
                Storage.items[name] = count
                Storage.capacity -= count
            else:
                return "Недостаточно места"
        except Exception as e:
            return e

    @staticmethod
    def remove(name, count):
        try:
            if count <= Storage.capacity:
                Storage.items[name] -= count
                if Storage.items[name] <= 0:
                    del Storage.items[name]
            else:
                return "Вы не можете сделать вместимость меньше нуля"
        except Exception as e:
            print(e)

    @staticmethod
    def get_free_space():
        return Storage.capacity

    @staticmethod
    def get_items():
        return Storage.items

    @staticmethod
    def get_unique_items_count():
        items_list = []
        for k in Storage.get_items().keys():
            items_list.append(k)
        return len(set(items_list))
