from FletcherRivse import FlatcherRivse_print
from NewtonRafson import NewtonRafson_print
from GaussaZeydel import GaussaZeydel_print


def main():
    while True:
        metod = int(input("Выберите метод:\n"
                          "1: Метод Метод Гаусса-Зейделя\n"
                          "2: Метод Флетчера-Ривса\n"
                          "3: Метод Ньютона-Рафсона\n"
                          ))
        while metod < 1 or metod > 3:
            print('Неверный номер метода')
        if metod == 1:
            GaussaZeydel_print()
        elif metod == 2:
            FlatcherRivse_print()
        elif metod == 3:
            NewtonRafson_print()
        print("\n")


if __name__ == "__main__":
    main()
