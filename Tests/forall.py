import tkinter

from tkinter import *
root=Tk()   #Главное окно


#создаем кнопку, при нажатии которой будет выводиться текст в консоль.

def Hello(event):
    print("Egor-typoi petyshara")

btn= Button(root, #На родительском окне
            text="click",  #надпись на кнопке
            width=30,height=5,# высота и ширина
            bg="white", fg="black") #цвет фона и надписи на кнопке

btn.bind("<Button-1>",Hello)  #При нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()  #расположить кнопку на главном окне
root.mainloop() #mainloop() запускает цикл обработки событий; пока мы не вызовем эту функцию, наше окно не будет реагировать на внешние раздражители.

#Есть 3 вида пака:
#grid() Основные параметры: row/column – строка/столбец в сетке, rowspan/columnspan – сколько строк/столбцов занимает виджет.
#place(). Позволяет размещать виджеты в указанных координатах с указанными размерами. Основные параметры: x, y, width, height.
#pack(). Автоматически размещает виджеты в родительском окне. Имеет параметры side, fill, expand.


