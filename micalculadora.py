from tkinter import *
from tkinter import messagebox

class App:
	def __init__(self, root):
		self.master = root
		self.master.title("Calculadora")

		# --------------
		# --- Visual ---
		#---------------

		body = Frame(self.master)
		body.pack()

		# Display
		display = Entry(body, font = ("Helvetica", 36, "normal"), width=12)
		display.config(bg = "white", fg = "black", justify = "left")
		display.grid(row = 0, columnspan = 4)

		#First line
		button_c = Button(body, text = "CE", width = 4, height = 1, font = "Helvetica")
		button_c.grid (row = 1, column = 0)

		button_cuadrado = Button(body, text = "x²", width = 4, height = 1, font = "Helvetica")
		button_cuadrado.grid (row = 1, column = 1)

		button_raiz = Button(body, text = "√", width = 4, height = 1, font = "Helvetica")
		button_raiz.grid (row = 1, column = 2)

		button_c = Button(body, text = "÷", width = 4, height = 1, font = "Helvetica")
		button_c.grid (row = 1, column = 3)


		#Second line
		button_7 = Button(body, text = "7", width = 4, height = 1, font = "Helvetica")
		button_7.grid (row = 2, column = 0)

		button_8 = Button(body, text = "8", width = 4, height = 1, font = "Helvetica")
		button_8.grid (row = 2, column = 1)

		button_9 = Button(body, text = "9", width = 4, height = 1, font = "Helvetica")
		button_9.grid (row = 2, column = 2)

		button_x = Button(body, text = "x", width = 4, height = 1, font = "Helvetica")
		button_x.grid (row = 2, column = 3)

		#Thirth line
		button_4 = Button(body, text = "4", width = 4, height = 1, font = "Helvetica")
		button_4.grid (row = 3, column = 0)

		button_5 = Button(body, text = "5", width = 4, height = 1, font = "Helvetica")
		button_5.grid (row = 3, column = 1)

		button_6 = Button(body, text = "6", width = 4, height = 1, font = "Helvetica")
		button_6.grid (row = 3, column = 2)

		button_resta = Button(body, text = "-", width = 4, height = 1, font = "Helvetica")
		button_resta.grid (row = 3, column = 3)

		#Fourth line
		button_1 = Button(body, text = "1", width = 4, height = 1, font = "Helvetica")
		button_1.grid (row = 4, column = 0)

		button_2 = Button(body, text = "2", width = 4, height = 1, font = "Helvetica")
		button_2.grid (row = 4, column = 1)

		button_3 = Button(body, text = "3", width = 4, height = 1, font = "Helvetica")
		button_3.grid (row = 4, column = 2)

		button_suma = Button(body, text = "+", width = 4, height = 1, font = "Helvetica")
		button_suma.grid (row = 4, column = 3)

		#Fifth line
		button_punto = Button(body, text = "·", width = 4, height = 1, font = "Helvetica")
		button_punto.grid (row = 5, column = 0)

		button_0 = Button(body, text = "0", width = 4, height = 1, font = "Helvetica")
		button_0.grid (row = 5, column = 1)

		button_resultado = Button(body, text = "=", width = 12, height = 1, font = "Helvetica")
		button_resultado.grid (row = 5, column = 2, columnspan = 2)










def main():
    root = Tk()
    Applicacion = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()