from storages.shop import Shop
from storages.storage import Storage
from storages.store import Store
from request import Request

storages = ["склад", "магазин", "магазин_2"]


def main():
    storage_exemp = Storage()
    store_exemp = Store()
    shop_exemp = Shop()
    print("Программа: Добрый день!\n")

    while True:
        print(f"""Программа: В {storages[0]} хранится: {storage_exemp.get_items()}""")
        print(f"""Программа: В {storages[1]} хранится: {store_exemp.get_items()}""")
        print(f"""Программа: В {storages[2]} хранится: {shop_exemp.get_items()}""")

        user_request = input(f"""Введите запрос в формате: Доставить 3 печенька из склад в магазин/магазин_2\n"""
                             """Или введите "stop" или "стоп", чтобы закончить\n / """).lower()

        if user_request == "stop" or user_request == "стоп":
            break

        request = Request(request=user_request, storages=storages)

        if request.designation == storages[0]:
            Storage.add(request.item, request.amount)

        elif request.designation == storages[1]:
            Shop.add(request.item, request.amount)

        elif request.designation == storages[2]:
            Store.add(request.item, request.amount)

        if request.departure is not None:
            if request.departure == storages[0]:
                Storage.remove(request.item, request.amount)

            elif request.departure == storages[1]:
                Shop.remove(request.item, request.amount)

            elif request.departure == storages[2]:
                Store.remove(request.item, request.amount)


if __name__ == "__main__":
    main()
