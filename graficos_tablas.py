import random
import time
import matplotlib.pyplot as plt
import pandas as pd

def binary_search(arr, clave):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == clave:
            return medio
        elif arr[medio] < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

if __name__ == "__main__":
    tamaños = [1000, 5000, 10000, 20000, 50000, 75000, 100000]
    tiempos_ms = []

    print("Iniciando pruebas de búsqueda binaria...\n")

    for tam in tamaños:
        arreglo = [random.randint(1, 100000) for _ in range(tam)]
        arreglo.sort()
        clave = random.randint(1, 100000)

        inicio = time.perf_counter()
        indice = binary_search(arreglo, clave)
        fin = time.perf_counter()

        tiempo_ms = (fin - inicio) * 1000
        tiempos_ms.append(tiempo_ms)

        encontrado = "Sí" if indice != -1 else "No"
        print(f"Tamaño: {tam:6} - Clave encontrada: {encontrado} - Tiempo: {tiempo_ms:.3f} ms")

  
    df = pd.DataFrame({
        "Tamaño del arreglo": tamaños,
        "Tiempo de búsqueda (ms)": tiempos_ms
    })

    print("\nTabla de resultados:")
    print(df.to_string(index=False))

  
    plt.figure(figsize=(8,5))
    plt.plot(tamaños, tiempos_ms, marker='o', color='b')
    plt.title("Tiempo de búsqueda binaria según tamaño del arreglo")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
