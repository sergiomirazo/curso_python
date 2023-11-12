import tkinter as tk
import sympy as sp

root = tk.Tk()
BG_ = '#1ee3c9'
FG_ = '#212423'
ACCENT = '#ab0790'
x = sp.symbols('x')

window = tk.Canvas(root, width=500, height=500, relief='raised', bg=BG_)
window.pack()

#TITULO
label1 = tk.Label(root, text='Calculadora de derivadas e integrales', bg=BG_, fg=ACCENT)
label1.config(font=('arial', 16, 'bold'))
window.create_window(250, 125, window=label1)

#INGRESAR FUNCION
label2 = tk.Label(root, text='Ingresa la función')
label2.config(font=('helvetica', 10), bg=BG_, fg=FG_)
window.create_window(250, 200, window=label2)

#FUNCION INGRESADA
label3 = tk.Label(root, text='')
label3.config(font=('helvetica', 10), bg=BG_, fg=FG_)
window.create_window(250, 350, window=label3)

#RESULTADO
label4 = tk.Label(root, text='')
label4.config(font=('helvetica', 10), bg=BG_, fg=FG_)
window.create_window(250, 380, window=label4)

#ENTRADA
entry1 = tk.Entry(root)
window.create_window(250, 240, window=entry1)

def derivate():
    global label3
    global label4
    label3.destroy()
    label4.destroy()
    fun = entry1.get()
    print(fun)
    label3 = tk.Label(root, text=f"La derivada de {fun} es: ")
    label3.config(font=('helvetica', 10, 'bold'), bg=BG_, fg=FG_)
    window.create_window(250, 350, window=label3)
    derivada = sp.diff(fun, x)
    label4 = tk.Label(root, text=derivada)
    label4.config(font=('helvetica', 10, 'bold'), bg=BG_, fg='#ebe83f')
    window.create_window(250, 380, window=label4)

def integrate():
    global label3
    global label4
    label3.destroy()
    label4.destroy()
    fun = entry1.get()
    print(fun)
    label3 = tk.Label(root, text=f"La integral de {fun} es: ")
    label3.config(font=('helvetica', 10, 'bold'), bg=BG_, fg=FG_)
    window.create_window(250, 350, window=label3)
    integral = str(sp.integrate(fun, x))+'+ C'
    label4 = tk.Label(root, text=integral)
    label4.config(font=('helvetica', 10, 'bold'), bg=BG_, fg='#9e37de')
    window.create_window(250, 380, window=label4)

button1 = tk.Button(text='Derivar', command=derivate, bg='#ebe83f', fg=FG_, font=('courier', 10, 'bold'))
window.create_window(350, 300, window=button1)
    
button2 = tk.Button(text='Integrar', command=integrate, bg='#9e37de', fg=FG_, font=('courier', 10, 'bold'))
window.create_window(150, 300, window=button2)

root.mainloop()
