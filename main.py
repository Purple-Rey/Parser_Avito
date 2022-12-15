from functools import partial
import time
import tkinter
import math

from parser_avito import Parser
from book import Excel

g_name = 0
g_count = 0


def _get_entry_(city, count) -> None:
    global g_name, g_count
    g_name = city.get()
    g_count = count.get()


def _start_() -> None:
    excel = Excel()  # создание объекта (создание таблицы)
    parser = Parser()  # создание объекта класса Parser,
    parser.__start__("https://www.avito.ru/?ysclid=lbez1dbmun669282747")
    time.sleep(5)
    parser.__city__(f"{g_name}")
    time.sleep(5)

    if int(g_count) > 51:  # проверяет количество объявлений, поскольку на 1 странице 51 объявлений
        count_page = math.ceil(int(g_count)/51)
        count_advertisement = 51
    else:
        count_page = 1
        count_advertisement = int(g_count)

    counter = 0
    for count_p in range(0, count_page):  # цикл парсинга
        count_advertisement = int(g_count) - counter
        time.sleep(5)
        parser.__scroll__(1000)  # пролистывает страницу на 1000 пикселей вниз
        for i in range(1, count_advertisement):
            counter += 1
            try:  # обработчик
                parser.__perebor__(i)
                time.sleep(5)
                parser.__win_too__()
                time.sleep(1)
                parser.__scroll__(500)
                time.sleep(5)
                name = parser.__name__()
                url = parser.__url__()
                price = parser.__price_full__()
                sell = parser.__price_sell__()
                adres = parser.__adres__()
                discription = parser.__product__()

                trigger = 0
                array = []

                for line in discription:  # цикл занесение
                    array.insert(trigger, line.text)
                    trigger += 1

                excel.__name_line__()
                excel.__with_book__(i, name.text, url,
                                    price.text, sell.text, adres.text, array)
                print(name.text)
                print(url)
                print(price.text)
                print(sell.text)
                print(adres.text)

                for line in discription:
                    print(line.text)

                parser.__closes__()

                time.sleep(5)
            finally:
                continue
        parser.__next__()

    parser.__end__()


def main() -> None:
    try:

        soft = tkinter.Tk()  # создание окна
        soft.title("Parser Avito by Myagkov Andrey")
        soft.geometry("810x600+200+100")
        soft.config(bg="#242424")
        soft.resizable(False, False)

        lable_table = tkinter.Label(
            soft, text="Добро пожаловать\nВы используете парсер Avito\nПриятного использования",
            bg="#878787",
            fg="black",
            font=("Arial", 14, "bold"),
            width="66",
            height="20",
            relief=tkinter.RAISED,
            bd=3)
        lable_table.grid(row=0, column=0, columnspan="4", sticky="we")

        tkinter.Label(
            soft,
            text="(Парсер использует Avito для сохрание в Excel основные данные с размещённых страниц о недвижимости)",
            bg="#878787",
            fg="black",
            font=("Arial", 8, "bold")).grid(row=1, column=0, columnspan="4", sticky="we")

        tkinter.Label(
            soft, text="Введите город и число объявлений: ",
            bg="#878787",
            fg="black",
            font=("Arial", 10, "bold"),
            anchor='w',
            padx=4,
            pady=4,
            relief=tkinter.RAISED,
            bd=3).grid(row=2, column=0, sticky="we")

        city = tkinter.Entry(  # строка ввода
            soft,
            bg="#b0b0b0",
            fg="black",
            font=("Arial", 14, "bold"),
            relief=tkinter.RAISED,
            bd=3)
        city.grid(row=2, column=1, sticky="we")

        count = tkinter.Entry(  # строка ввода, количество
            soft,
            bg="#b0b0b0",
            fg="black",
            font=("Arial", 14, "bold"),
            relief=tkinter.RAISED,
            bd=3)
        count.grid(row=2, column=2, sticky="we")

        button_confirm = tkinter.Button(  # кнопка подтверждения
            soft, text="Подтвердить", bg="#a5a5a5",
            fg="#184c12",
            font=("Arial", 10, "bold"),
            relief=tkinter.RAISED,
            bd=3,
            activebackground="#7f3eea",
            command=partial(_get_entry_, city, count))
        button_confirm.grid(row=2, column=3, sticky="we")

        button_parsing = tkinter.Button(  # кнопка начала парсинга
            soft, text="Парсинг", bg="#a5a5a5",
            fg="#184c12",
            font=("Arial", 10, "bold"),
            relief=tkinter.RAISED,
            bd=3,
            activebackground="#7f3eea",
            command=_start_)
        button_parsing.grid(row=3, column=0, sticky="we")

        button_quite = tkinter.Button(  # выход из приложения
            soft, text="Выход", bg="#a5a5a5",
            fg="red",
            font=("Arial", 10, "bold"),
            relief=tkinter.RAISED,
            bd=3,
            activebackground="#7f3eea",
            command=soft.quit)
        button_quite.grid(row=4, column=0, sticky="we")

        soft.mainloop()

    except Exception as ex:
        print(f"ОШИБКА!!! -->> {ex}")  # вывод ошибки
    finally:
        pass


if __name__ == "__main__":
    main()
