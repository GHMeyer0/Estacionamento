from tkinter import *
import vagas

estacionamento = vagas.Vaga(20)


root = Tk()
root.title("Named colour chart")
row = 0
col = 0
for vaga in estacionamento.vagas:
        e = Label(root, text=vaga['numero'], background='blue')
        e.grid(row=row, column=col, sticky=E+W)
        row += 1
        if (row > 9):
            row = 0
            col += 1
root.mainloop()
