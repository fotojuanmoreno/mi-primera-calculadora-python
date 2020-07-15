from tkinter import *
from tkinter import messagebox

#PRUEBA UN BUCLE WHILE PARA MIENTRAS SEA MENOS QUE TRES AÑADA Y SINO SUME O LO QUE DIGA LA OPERACION

class App:
	def __init__(self, root):
		self.master = root
		self.master.title("Calculadora")

		elementos =[] 
		self.operacion = ""
		self.resultado = 0
		self.reset_pantalla = False
		self.contador = 0
		self.contador_resta = 0
		self.contador_suma = 0
		self.num1 = 0

		# -------------------
		# --- Enter dates ---
		#--------------------

		def insert_value(num):
			if self.reset_pantalla != False or displayValue.get() == "0":
				displayValue.set(num)
				print(num)
				self.reset_pantalla = False
			else:
				displayValue.set(displayValue.get() + num)
				print(num)

		def clean():
			displayValue.set("0")
			self.resultado = 0
			self.contador_resta = 0
			self.reset_pantalla = True
			elementos[:] = []
			print("clean")
			print(elementos)

		def preparacuentas():
			num1 = float(displayValue.get())
			elementos.append(float(num1))
			elementos.append(self.operacion)
			if num1 != 0 and len(elementos) <= 2:
				print (elementos)
			elif len(elementos) > 2:
				calcularesultado()
			self.reset_pantalla = True
			displayValue.set(self.resultado)

		def lascuentas():
			cifra1 = float(elementos[0])
			cifra2 = float(elementos[2])
			if elementos[1] == "suma":
				self.resultado = cifra1+cifra2
			elif elementos[1] == "resta":
				self.resultado = cifra1-cifra2
			elif elementos[1] == "multiplica":
				self.resultado = cifra1*cifra2
			elif elementos[1] == "divide":
				self.resultado = cifra1/cifra2
			elif elementos[1] == "cuadrado":
				self.resultado = cifra1**cifra2

		def calcularesultado():
			print(elementos)
			
			if len(elementos) < 4:
				lascuentas()
				elementos[:] = []
				elementos.append(self.resultado)

			else:
				cuenta = elementos[3]
				lascuentas()
				elementos[:] = []
				elementos.append(self.resultado)
				elementos.append(str(cuenta))

		def suma(num):
			print("suma")
			self.operacion = "suma"
			preparacuentas()

		def resta(num):
			print("resta")
			self.operacion = "resta"
			preparacuentas()

		def multiplica(num):
			print("multiplicacion")
			self.operacion = "multiplica"
			preparacuentas()

		def divide(num):
			print("division")
			self.operacion = "divide"
			preparacuentas()

		def cuadrado(num):
			print("cuadrado")
			self.operacion = "cuadrado"
			preparacuentas()

		


		def resultado():
			elementos.append(float(displayValue.get()))
			calcularesultado()
			print(elementos)
			displayValue.set(self.resultado)
			elementos[:] = []
			




		# --------------
		# --- Visual ---
		#---------------

		body = Frame(self.master)
		body.pack()

		# Display
		displayValue = StringVar()
		displayValue.set("0")
		display = Entry(body, font = ("Helvetica", 36, "normal"), width=12, textvariable = displayValue)
		display.config(bg = "white", fg = "black", justify = "right")
		display.grid(row = 0, columnspan = 4)

		#First line
		button_c = Button(body, text = "CE", width = 4, height = 1, font = "Helvetica", command = lambda:clean())
		button_c.grid (row = 1, column = 0)

		button_cuadrado = Button(body, text = "xˣ", width = 4, height = 1, font = "Helvetica", command = lambda:cuadrado(displayValue.get()))
		button_cuadrado.grid (row = 1, column = 1)

		button_raiz = Button(body, text = "√", width = 4, height = 1, font = "Helvetica")
		button_raiz.grid (row = 1, column = 2)

		button_c = Button(body, text = "÷", width = 4, height = 1, font = "Helvetica", command = lambda:divide(displayValue.get()))
		button_c.grid (row = 1, column = 3)


		#Second line
		button_7 = Button(body, text = "7", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("7"))
		button_7.grid (row = 2, column = 0)

		button_8 = Button(body, text = "8", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("8"))
		button_8.grid (row = 2, column = 1)

		button_9 = Button(body, text = "9", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("9"))
		button_9.grid (row = 2, column = 2)

		button_x = Button(body, text = "x", width = 4, height = 1, font = "Helvetica", command = lambda:multiplica(displayValue.get()))
		button_x.grid (row = 2, column = 3)

		#Thirth line
		button_4 = Button(body, text = "4", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("4"))
		button_4.grid (row = 3, column = 0)

		button_5 = Button(body, text = "5", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("5"))
		button_5.grid (row = 3, column = 1)

		button_6 = Button(body, text = "6", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("6"))
		button_6.grid (row = 3, column = 2)

		button_resta = Button(body, text = "-", width = 4, height = 1, font = "Helvetica", command = lambda:resta(displayValue.get()))
		button_resta.grid (row = 3, column = 3)

		#Fourth line
		button_1 = Button(body, text = "1", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("1"))
		button_1.grid (row = 4, column = 0)

		button_2 = Button(body, text = "2", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("2"))
		button_2.grid (row = 4, column = 1)

		button_3 = Button(body, text = "3", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("3"))
		button_3.grid (row = 4, column = 2)

		button_suma = Button(body, text = "+", width = 4, height = 1, font = "Helvetica", command = lambda:suma(displayValue.get()))
		button_suma.grid (row = 4, column = 3)

		#Fifth line
		button_punto = Button(body, text = "·", width = 4, height = 1, font = "Helvetica")
		button_punto.grid (row = 5, column = 0)

		button_0 = Button(body, text = "0", width = 4, height = 1, font = "Helvetica", command = lambda:insert_value("0"))
		button_0.grid (row = 5, column = 1)

		button_resultado = Button(body, text = "=", width = 12, height = 1, font = "Helvetica", command = lambda:resultado())
		button_resultado.grid (row = 5, column = 2, columnspan = 2)












def main():
    root = Tk()
    Applicacion = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()