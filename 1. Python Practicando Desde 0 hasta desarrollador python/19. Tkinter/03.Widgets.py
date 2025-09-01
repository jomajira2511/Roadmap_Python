import tkinter as tk
import webbrowser 

ventana = tk.Tk()
ventana.title("Widgets")
ventana.geometry("700x700")

# Etiqueta o label en tkinter
etiqueta = tk.Label(
    ventana, text="Este es mi primer label", 
    bg="red",
    fg="white", 
    font="30",
    width="30",
    height="5"
    )
etiqueta.pack()

# Botón en tkinter para abrir Google
boton = tk.Button(
    ventana, 
    text="Presiona este botón para abrir Google",  # Permite colocarle texto al boton
    command=lambda: webbrowser.open("https://www.google.com")  #Command, permite darle una accion una vez se presione el texto 
)
boton.pack()

#Pendiente agregar correciones
boton.tk_setPalette()


ventana.mainloop()
