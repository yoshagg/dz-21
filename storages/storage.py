from storages.base_storage import BaseStorage


class Storage(BaseStorage):
    def __init__(self):
        self.storage = BaseStorage(items={}, capacity=5)

    def add(self, name, count):
        self.storage.add()

    def remove(self, name, count):
        self.storage.remove()

    def get_items(self):
        self.storage.get_items()

    def get_free_space(self):
        self.storage.get_free_space()

    def get_unique_items_count(self):
        self.storage.get_unique_items_count()
