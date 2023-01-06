class Request:
    def __init__(self, request, storages):
        split_request = request.strip().lower().split(" ")
        if 5 > len(split_request) > 7:
            raise "Запрос составлен неверно"

        if len(split_request) == 7:
            self.amount = int(split_request[1])
            self.operation = split_request[0]
            self.item = split_request[2]
            self.designation = split_request[4]
            self.departure = split_request[6]

        elif len(split_request) == 5:
            self.amount = int(split_request[1])
            self.operation = split_request[0]
            self.item = split_request[2]
            self.designation = split_request[4]
            self.departure = None
