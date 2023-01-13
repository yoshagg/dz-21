from storages.shop import Shop
from storages.storage import Storage
from storages.store import Store
from request import Request

storages = {"storage": "склад", "store": "магазин", "shop": "магазин_2"}


def main():
    storage = Storage()
    store = Store()
    shop = Shop()
    print("Программа: Добрый день!\n")

    while True:
        print(f"""Программа: В {storages["storage"]} хранится: {storage.get_items()}. """
              f"""Свободного места: {storage.get_free_space()}""")
        print(f"""Программа: В {storages["store"]} хранится: {store.get_items()}. """
              f"""Свободного места: {store.get_free_space()}""")
        print(f"""Программа: В {storages["shop"]} хранится: {shop.get_items()}. """
              f"""Свободного места: {shop.get_free_space()}""")

        user_request = input(f"""Введите запрос в формате: Доставить 3 печенька в ... из ...\n"""
                             """Или введите "stop" или "стоп", чтобы закончить\n / """).lower()

        if user_request == "stop" or user_request == "стоп":
            break

        request = Request(request=user_request, storages=storages)


        if request.designation == storages["storage"]:
            storage.add(request.item, request.amount)

        elif request.designation == storages["shop"]:
            shop.add(request.item, request.amount)

        elif request.designation == storages["store"]:
            store.add(request.item, request.amount)

        if request.departure is not None:
            if request.departure == storages["storage"]:
                storage.remove(request.item, request.amount)

            elif request.departure == storages["shop"]:
                shop.remove(request.item, request.amount)

            elif request.departure == storages["store"]:
                store.remove(request.item, request.amount)


if __name__ == "__main__":
    main()
