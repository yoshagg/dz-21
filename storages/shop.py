from storages.base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self):
        self.items = {}
        self.capacity = 100
