from storages.base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self):
        self.shop = BaseStorage(items={}, capacity=20)

    def add(self, name, count):
        self.shop.add()

    def remove(self, name, count):
        self.shop.remove()

    def get_items(self):
        self.shop.get_items()

    def get_free_space(self):
        self.shop.get_free_space()

    def get_unique_items_count(self):
        self.shop.get_unique_items_count()
