import tkinter as tk
import webbrowser 

ventana = tk.Tk()
ventana.title("Widgets")
ventana.geometry("700x700")

#Espacio para definir funciones 

def AbrirGoogle():  #Permite al momento de presionar un boton, nos lleve automaticamente a google 
    webbrowser.open("https://www.google.com")

# Etiqueta o label en tkinter
etiqueta = tk.Label(
    ventana, text="Este es mi primer label", 
    bg="red",
    fg="white", 
    font= ("Helvetica",30,"italic"),
    width="30",
    height="5"
    )
etiqueta.pack(pady = 30)

# Botón en tkinter para abrir Google
boton = tk.Button(
    ventana, 
    text="Presiona este botón para abrir Google",  # Permite colocarle texto al boton
    command= AbrirGoogle, #Command, permite darle una accion una vez se presione el texto 
    bg="lightgreen", # Colocar un fondo de color al botn
    font=("Courier", 20,"bold"), # Cambiar el dise;o 
    border=10, # Asignar el borde
    activebackground="lightpink",
    activeforeground="gold"

)
boton.pack()

ventana.mainloop()
