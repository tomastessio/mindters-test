import time

def tiempo_ejecucion(func):
    def demora(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f'Tiempo de ejecución de {func.__name__}: {tiempo_total:.4f} segundos')
        return resultado
    return demora

@tiempo_ejecucion
def funcion_ejemplo():
    print('Ejecutando la función de ejemplo...')
    time.sleep(2)
    print('Función de ejemplo completada')

funcion_ejemplo()