from storages.base_storage import BaseStorage


class Store(BaseStorage):
    def __init__(self):
        self.store = BaseStorage(items={}, capacity=100)

    def add(self, name, count):
        self.store.add()

    def remove(self, name, count):
        self.store.remove()

    def get_items(self):
        self.store.get_items()

    def get_free_space(self):
        self.store.get_free_space()

    def get_unique_items_count(self):
        self.store.get_unique_items_count()
