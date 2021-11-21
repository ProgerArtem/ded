#-*- codding:utf-8 -*-
from tkinter import *
from logic import Search_engine

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.db_search = Search_engine()
        Label(self ,text="Введіть пошуковий запит:").grid(
           row = 0, column=0, columnspan=2, rowspan=3 
        )
        self.search_text = StringVar()
        self.entry_search = Entry(self, width=60, 
                                  textvariable=self.search_text)
        self.search_but = Button(self, text="Пошук",
                                 command=self.search)
        self.entry_search.grid(row=3, column=0,
                               columnspan=2)
        self.search_but.grid(row=3, column=2)
def on_change(event):
    widget = event.widget  # виджет, с которым произошло событие (в данном случае listbox)
    selection = widget.curselection()  # получаем список индексов выделенных элементов
    if selection:  # если что-то выделено
        text = widget.get(selection[0])  # Текст в выбранной строке
        # выводим текст выделенного элемента в консоль
        print(text)
        # то же самое, но вывод в диалоговое окно
        messagebox.showinfo('Title', text)

lbox.bind('<<ListboxSelect>>', on_change)
        self.list_track = Listbox(self, width=60, height=15)
        self.list_track.grid(row=4, column=0, columnspan=2,
                             rowspan=3,
                             sticky=W)
        self.mode_var = StringVar()
        self.mode_var.set("tracks")
        dict_modes = { "Search in tracks": "tracks",
                       "Search in authors": "authors",
                       "Search in genres": "genres"
        

        }
        for i, (text, val) in enumerate(dict_modes.items()):
            r1 = Radiobutton(self, text=text,
                              variable=self.mode_var,
                              value=val)
            r1.grid(row=i, column=2, sticky=W)                         
    def search(self):
        print("Text from entry:",self.search_text.get())
        text = self.search_text.get()
        result = self.db_search.search_track(text)
        print (result)
        self.list_track.delete(0, END)
        for row in result:
            self.list_track.insert(END, row[0])
    def new_window(self):
        Window().mainloop()
if __name__=="__main__":
    root = Window()
    root.geometry("600x400")
    root.mainloop()