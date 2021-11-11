import matplotlib.pyplot as plt



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x=  [i*2 for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
    x1 = [2, 6.7, 11.2, 16.5, 21.6, 26.1]
    y1 = [1.28, 3.28, 5.28, 7.28, 9.28,  11.28]

    # Квадратичная зависимость
    x2 = [2, 4.1, 6.2, 8.7, 10.2, 16.8, 19.7, 22, 24.3, 26.1, 28]
    y2 = [1.70, 2.70, 3.70, 4.70, 5.70, 6.23, 6.23, 6.23, 6.70, 7.70, 8.70, 9.70, 10.70, 11.70]
    # Построение графика
    plt.title("График зависимости φ от X")  # заголовок
    plt.xlabel("X, м")  # ось абсцисс
    plt.ylabel("φ, В")  # ось ординат
    plt.grid()  # включение отображения сетки
    plt.legend(loc="upper left")
    plt.plot(x1,y1, label="Без кольца")
    plt.plot(x, y2, label="С кольцом")
    plt.legend(loc="upper left")
    plt.show()# построение графика
