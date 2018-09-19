from tkinter import Tk, Canvas, Frame, Button, Entry, Label
from tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT, NE, E, Y, HORIZONTAL, VERTICAL, BOTTOM, RIGHT
import numpy as np

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pausa = True
        self.tam = 200
        self.tam_cuadro = 2
        self.ceros = "white"
        self.unos = "black"
        self.regla = [2, 3, 3, 3]
        self.e1 = None
        self.contador = 0
        self.a = np.zeros(shape=(self.tam, self.tam), dtype=int)
        self.celulas = np.random.randint(2, size=(self.tam, self.tam))
        self.historia_x = list()
        self.historia_y = list()
        self.archivo = open("grafica.txt", "w")
        for i in range(self.tam):
            for j in range(self.tam):
                if self.celulas[i, j] == 1:
                    self.contador += 1

        self.canvas = None
        self.tiempo = 0
        self.initUI()
        self.update()
        self.animacion()


    def initUI(self):
        self.parent.title("Layout Test")
        self.config(bg = '#F0F0F0')
        self.pack(fill = BOTH, expand = 1)
        #create canvas
        self.canvas1 = Canvas(self, relief = 'raised', width = self.tam, height = self.tam)

        self.canvas1.pack(side = LEFT)
        for i in range(self.tam):
            for j in range(self.tam):
                if self.celulas[i][j] == 0:
                    self.a[i][j] = self.canvas1.create_rectangle(0 + (i * self.tam_cuadro), 0 + (j * self.tam_cuadro),
                                                       self.tam_cuadro + (i * self.tam_cuadro), self.tam_cuadro + (j * self.tam_cuadro),
                                                 fill=self.ceros, width=0)
                else:
                    self.a[i][j] = self.canvas1.create_rectangle(0 + (i * self.tam_cuadro), 0 + (j * self.tam_cuadro),
                                                       self.tam_cuadro + (i * self.tam_cuadro), self.tam_cuadro + (j * self.tam_cuadro),
                                                 fill=self.unos, width=0)
                    self.contador += 1
        Label(self, text="Regla:").pack(side=TOP)
        self.e1 = Entry(self, fg="black")
        self.e1.insert(10, "2,3,3,3")
        self.e1.pack(side=TOP)
        #add quit button
        button1 = Button(self, text="Pausa/Reanudar", command=self.empezar_dentener, )
        button1.configure(width=10, activebackground="#33B5E5")
        #button1_window = canvas1.create_window(610, 10, anchor=NE, window=button1)
        button1.pack(side = TOP)

    def empezar_dentener(self):
        print("empezar_detener")
        texto = self.e1.get().split(",")
        self.regla[0] = int(texto[0])
        self.regla[1] = int(texto[1])
        self.regla[2] = int(texto[2])
        self.regla[3] = int(texto[3])

        print(texto)
        self.pausa = not self.pausa

    def animacion(self):
        print("ANIMACION")
        if not self.pausa:
            self.historia_y.append(self.contador)
            self.historia_x.append(self.tiempo)
            self.archivo.write("")
            nueva_poblacion = self.celulas.copy()
            for i in range(self.tam):
                print(i)
                for j in range(self.tam):
                    vecinos = (self.celulas[i - 1, j - 1] + self.celulas[i - 1, j] + self.celulas[i - 1, (j + 1) % self.tam]
                               + self.celulas[i, (j + 1) % self.tam] + self.celulas[(i + 1) % self.tam, (j + 1) % self.tam]
                               + self.celulas[(i + 1) % self.tam, j] + self.celulas[(i + 1) % self.tam, j - 1] + self.celulas[i, j - 1])
                    if self.celulas[i, j] == 1:
                        if vecinos < self.regla[0] or vecinos > self.regla[1]:
                            nueva_poblacion[i, j] = 0
                            self.canvas1.itemconfig(self.a[i][j], fill=self.ceros)
                            self.contador -= 1
                    else:
                        if vecinos >= self.regla[2] and vecinos <= self.regla[3]:
                            nueva_poblacion[i, j] = 1
                            self.canvas1.itemconfig(self.a[i][j], fill=self.unos)
                            self.contador += 1

            self.celulas[:] = nueva_poblacion[:]
            self.update_idletasks()
            print("Termino")
            self.tiempo += 1
        self.after(1000, self.animacion)

def main():
    root = Tk()
    root.geometry('1000x600+0+0')
    app = Example(root)
    app.mainloop()

main()