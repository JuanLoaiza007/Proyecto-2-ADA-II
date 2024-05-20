# [lector_txt.py]
import os
import tkinter as tk
from tkinter import filedialog
from models.tools.File_selector import File_selector


def leer_archivo_txt():
    """
    Lee un archivo .txt formateado y lo procesa para obtener la finca

    Args:
        Ninguno, se abre en una ruta predefinida y usa un explorador de Tkinter

    Returns:
        datos [(int, int, int), (int, int, int),... (int, int, int)]: La finca
        None si no se seleccionó nada
    """
    ruta_completa = File_selector.select("data/tests")
    if ruta_completa:
        try:
            with open(ruta_completa, "r") as archivo:
                n = int(archivo.readline().strip())

                datos = []
                contenido = str(n) + "\n"
                for _ in range(n):
                    linea = archivo.readline().strip()
                    valores = tuple([int(x) for x in linea.split(",")])
                    contenido += linea + "\n"
                    datos.append(valores)

                nombre_archivo = os.path.basename(ruta_completa)

                return [datos, contenido, nombre_archivo]

        except FileNotFoundError as e:
            print("txt_parser: Error: El archivo no fue encontrado:", e)
            return None

        except ValueError as e:
            print("txt_parser: Error: El formato del archivo NO es correcto.")
            return None
    else:
        return None


def exportar_programacion_txt(programacion):
    """
    Genera un archivo .txt formateado con una programacion dada

    Args:
        programacion [(int, int,... int), int]: La programación  de riego con su costo

    Returns:
        ruta_archivo (str): La ruta al archivo si todo funcionó
        None si la ruta del archivo no es válida
    """
    root = tk.Tk()
    root.withdraw()

    ruta_archivo = filedialog.asksaveasfilename(
        parent=root,
        initialdir="./data/results/",
        title="Guardar archivo como",
        defaultextension=".txt",
        filetypes=(("Archivos de texto", "*.txt"),
                   ("Todos los archivos", "*.*"))
    )

    if not (ruta_archivo):
        return None

    with open(ruta_archivo, 'w') as archivo:
        valor = programacion[1]
        archivo.write(str(valor) + '\n')
        for elemento in programacion[0]:
            archivo.write(str(elemento) + '\n')

    root.destroy()
    return ruta_archivo


if __name__ == '__main__':
    # Ejemplo de uso
    datos_leidos = leer_archivo_txt()
    if datos_leidos:
        print("Datos leídos del archivo:")
        print(datos_leidos)
