from storages.base_storage import BaseStorage


class Store(BaseStorage):
    def __init__(self):
        self.items = {}
        self.capacity = 20
