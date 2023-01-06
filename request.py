class Request:
    def __init__(self, request, storages):
        split_request = request.strip().lower().split(" ")
        if 7 < len(split_request) > 7:
            raise "Запрос составлен неверно"

        self.amount = int(split_request[1])
        self.operation = split_request[0]
        self.item = split_request[2]
        self.departure = split_request[4]
        self.designation = split_request[6]
