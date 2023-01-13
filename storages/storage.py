from storages.base_storage import BaseStorage


class Storage(BaseStorage):
    def __init__(self):
        self.items = {}
        self.capacity = 5


