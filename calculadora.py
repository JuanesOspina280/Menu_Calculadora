#importo las librerias que utilizaré
from tkinter import Tk, Label, Button, Entry, Menu, messagebox

#Creamos las funciones
def fnSuma():
    try:
        resultado = float(entrada1.get()) + float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnResta():
    try:
        resultado = float(entrada1.get()) - float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnMultiplicacion():
    try:
        resultado = float(entrada1.get()) * float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnDivision():
    try:
        divisor = float(entrada2.get())
        if divisor != 0:
            resultado = float(entrada1.get()) / divisor
            etiqueta_resultado.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Error", "División por cero no permitida.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnValorAbsoluto():
    try:
        resultado = abs(float(entrada1.get()))
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def fnMCM():
    try:
        from math import gcd
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado = abs(a * b) // gcd(a, b)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")

def fnMCD():
    try:
        from math import gcd
        resultado = gcd(int(entrada1.get()), int(entrada2.get()))
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")

#Creación del menú, barra superior
def crear_menu(vent):

    #creación del objeto menú, para la barra superior
    barra_menu = Menu(vent)
    vent.config(menu=barra_menu)
    
    #Agregamos el menú al primer item de la barra superior
    menu_inicio = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Salir", command=vent.destroy)

    #Agregamos el menú al segundo item de la barra superior
    menu_operacion = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Operación", menu=menu_operacion)
    menu_operacion.add_command(label="Sumar", command=fnSuma)
    menu_operacion.add_command(label="Restar", command=fnResta)
    menu_operacion.add_command(label="Multiplicación", command=fnMultiplicacion)
    menu_operacion.add_command(label="División", command=fnDivision)
    menu_operacion.add_command(label="Valor Absoluto", command=fnValorAbsoluto)
    menu_operacion.add_command(label="Mínimo Común Múltiplo", command=fnMCM)
    menu_operacion.add_command(label="Máximo Común Divisor", command=fnMCD)

#creamos y agregamos los estilos a la ventana CALCULADORA
def crear_ventana():
    vent = Tk()
    vent.title("Calculadora Dev-Juanes")
    vent.geometry("300x250")
    vent.config(bg="#f0f0f0")
    
    crear_menu(vent)
    
    #definimos que tipo de datos se ingresarán 
    global entrada1, entrada2, etiqueta_resultado
    
    Label(vent, text="Número 1:", bg="#f0f0f0").pack(pady=5)
    entrada1 = Entry(vent)
    entrada1.pack(pady=5)
    
    Label(vent, text="Número 2:", bg="#f0f0f0").pack(pady=5)
    entrada2 = Entry(vent)
    entrada2.pack(pady=5)
    
    etiqueta_resultado = Label(vent, text="Resultado:", bg="#f0f0f0", font=("Arial", 12, "bold"))
    etiqueta_resultado.pack(pady=20)
    
    Button(vent, text="Sumar", command=fnSuma, bg="#4CAF50", fg="white").pack(side="left", padx=10, pady=10)
    Button(vent, text="Restar", command=fnResta, bg="#f44336", fg="white").pack(side="left", padx=10, pady=10)

    return vent

vent = crear_ventana()
vent.mainloop()
