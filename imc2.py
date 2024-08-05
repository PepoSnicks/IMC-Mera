import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os

def calcular_bmi():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        sexo = entry_sexo.get()
        peso = float(entry_peso.get())  # Cambiado a float para permitir decimales
        altura = float(entry_altura.get())  # Cambiado a float para permitir decimales
        
        # Convertir altura a metros si está en centímetros
        if altura > 3:  # Si la altura es mayor a 3, se asume que está en centímetros
            altura /= 100  # Convertir centímetros a metros
        
        bmi = peso / (altura ** 2)
        
        # Mostrar el resultado del BMI
        label_resultado.config(text=f"BMI: {bmi:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def guardar_datos():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        sexo = entry_sexo.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        # Convertir altura a metros si está en centímetros
        if altura > 3:
            altura /= 100
        
        bmi = peso / (altura ** 2)
        
        # Crear un nombre de archivo CSV basado en el nombre del usuario
        nombre_archivo = f"{nombre}.csv"
        
        # Verificar si el archivo ya existe
        archivo_nuevo = not os.path.isfile(nombre_archivo)
        
        # Guardar los datos en el archivo CSV
        with open(nombre_archivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Escribir la cabecera si es un archivo nuevo
            if archivo_nuevo:
                writer.writerow(["Nombre", "Edad", "Sexo", "Peso", "Altura", "BMI"])
            
            # Escribir los datos del usuario
            writer.writerow([nombre, edad, sexo, peso, altura, bmi])
        
        messagebox.showinfo("Guardado", f"Datos guardados en {nombre_archivo}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora de BMI")

# Redimensionar la imagen de fondo
image = Image.open("C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/merita/fondo.jpg")
fondo = ImageTk.PhotoImage(image.resize((750, 750)))

# Crear un Canvas con un tamaño más grande y colocar la imagen de fondo redimensionada
canvas = tk.Canvas(root, width=750, height=750)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

# Dimensiones del Canvas
canvas_width = fondo.width()
canvas_height = fondo.height()

# Coordenadas para centrar los widgets verticalmente
y_center = canvas_height // 2
y_start = y_center - 4 * 80  # Ajustar según la cantidad de widgets
y_step = 100  # Separación vertical entre widgets

# Coordenadas para centrar los widgets horizontalmente
x_center = canvas_width // 2.3

# Estilo de fuente reducido
font_style = ("Helvetica", 10, "bold italic")
font_color = "#666666"

# Crear y colocar los widgets centrados verticalmente en el Canvas
label_nombre = tk.Label(root, text="Nombre:", bg="white", font=font_style, fg=font_color)
canvas.create_window(x_center - 100, y_start, anchor="e", window=label_nombre)

entry_nombre = tk.Entry(root)
canvas.create_window(x_center, y_start, anchor="w", window=entry_nombre)

label_edad = tk.Label(root, text="Edad:", bg="white", font=font_style, fg=font_color)
canvas.create_window(x_center - 100, y_start + y_step, anchor="e", window=label_edad)

entry_edad = tk.Entry(root)
canvas.create_window(x_center, y_start + y_step, anchor="w", window=entry_edad)

label_sexo = tk.Label(root, text="Sexo:", bg="white", font=font_style, fg=font_color)
canvas.create_window(x_center - 100, y_start + 2 * y_step, anchor="e", window=label_sexo)

entry_sexo = tk.Entry(root)
canvas.create_window(x_center, y_start + 2 * y_step, anchor="w", window=entry_sexo)

label_peso = tk.Label(root, text="Peso (kg):", bg="white", font=font_style, fg=font_color)
canvas.create_window(x_center - 100, y_start + 3 * y_step, anchor="e", window=label_peso)

entry_peso = tk.Entry(root)
canvas.create_window(x_center, y_start + 3 * y_step, anchor="w", window=entry_peso)

label_altura = tk.Label(root, text="Altura (m):", bg="white", font=font_style, fg=font_color)
canvas.create_window(x_center - 100, y_start + 4 * y_step, anchor="e", window=label_altura)

entry_altura = tk.Entry(root)
canvas.create_window(x_center, y_start + 4 * y_step, anchor="w", window=entry_altura)

# Cargar las imágenes originales y redimensionarlas
img_calcular = Image.open("C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/merita/calcular.jpg").resize((200, 70), Image.LANCZOS)
img_guardar = Image.open("C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/merita/guardar.jpg").resize((200, 70), Image.LANCZOS)

# Convertir las imágenes redimensionadas a PhotoImage
photo_calcular = ImageTk.PhotoImage(img_calcular)
photo_guardar = ImageTk.PhotoImage(img_guardar)

# Crear los botones con las imágenes
button_calcular = tk.Button(root, image=photo_calcular, command=calcular_bmi, cursor="hand2", borderwidth=0)
canvas.create_window(x_center - 50, y_start + 5 * y_step, anchor="e", window=button_calcular)

button_guardar = tk.Button(root, image=photo_guardar, command=guardar_datos, cursor="hand2", borderwidth=0)
canvas.create_window(x_center + 50, y_start + 5 * y_step, anchor="w", window=button_guardar)

label_resultado = tk.Label(root, text="BMI:", bg="white", font=font_style, fg=font_color)
canvas.create_window(x_center, y_start + 6 * y_step, anchor="center", window=label_resultado)

# Iniciar el bucle principal de la aplicación
root.mainloop()