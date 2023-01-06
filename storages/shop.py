class Shop:
    items = {}
    capacity = 20

    @staticmethod
    def add(name, count):
        try:
            if Shop.capacity > 0 and count <= Shop.capacity:
                Shop.items[name] = count
                Shop.capacity -= count
            else:
                return "Недостаточно места"
        except Exception as e:
            return e

    @staticmethod
    def remove(name, count):
        try:
            if count <= Shop.capacity:
                Shop.items[name] -= count
                if Shop.items[name] <= 0:
                    del Shop.items[name]
            else:
                return "Вы не можете сделать вместимость меньше нуля"
        except Exception as e:
            print(e)

    @staticmethod
    def get_free_space():
        return Shop.capacity

    @staticmethod
    def get_items():
        return Shop.items

    @staticmethod
    def get_unique_items_count():
        items_list = []
        for k in Shop.get_items().keys():
            items_list.append(k)
        return len(set(items_list))
