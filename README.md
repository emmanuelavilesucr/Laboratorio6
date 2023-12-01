# Laboratorio 6

# Ejercicio: Callbacks en Python

## events.py

### Descripción de events.py:

- **events.py:** Simula una gestión de eventos simple. Permite a los suscriptores registrarse para recibir notificaciones cuando ocurren eventos específicos y cancelar su suscripción. La función `notify` se utiliza para notificar a los suscriptores cuando ocurre un evento.

### Cambios realizados en el archivo:

1. **RealTimeDataManager:**
   - Se agregó el método `notify_data_change` que utiliza el `EventManager` para notificar a los suscriptores cuando los datos han cambiado.

2. **EventManager:**
   - Se añadió el método `subscribe` para que los suscriptores se registren y reciban notificaciones.
   - Se implementó el método `unsubscribe` para que los suscriptores puedan cancelar su suscripción.

## datamanager.py

### Descripción de  datamanager.py:

- **datamanager.py:** Utiliza un temporizador para simular la actualización de datos en tiempo real. Utiliza la clase `RealTimeDataManager` como base.

### Cambios realizados en el archivo:

1. **Instanciación y suscripción:**
   - Se creó una instancia de `RealTimeDataManager`.
   - Se suscribió un callback al `EventManager` para imprimir los datos actualizados al stdout.
   - Se utilizó la función `subscribe` del `EventManager` para registrar el callback.

2. **Resultado esperado:**
   - La salida del programa deberá verse similar a lo siguiente:

     ```
     Datos en tiempo real actualizados: {'temperatura': 24.768027210482213, 'humedad': 60.49139977588436}
     Datos en tiempo real actualizados: {'temperatura': 25.063307518136966, 'humedad': 61.90356994047687}
     Datos en tiempo real actualizados: {'temperatura': 24.25791118771628, 'humedad': 63.09901270516206}
     Datos en tiempo real actualizados: {'temperatura': 23.60913577897327, 'humedad': 62.16625078834271}
     ```

**Conclusiones:**
- Se ha implementado la notificación de eventos de cambio de datos mediante callbacks y la utilización de la clase `RealTimeDataManager`.
- La suscripción y cancelación de suscripción se gestionan a través del `EventManager`.
- La salida muestra la actualización periódica de datos en tiempo real, proporcionando una experiencia simulada de datos dinámicos.

---

## Ejercicio: Funciones Lambda en Python

### Cambios realizados en calculadora.py:

1. **Menú y ejecución de operaciones:**
   - Se ha extendido el menú para utilizar funciones lambda en lugar de callbacks directos.
   - Cada operación ahora se asocia a una función lambda que realiza la operación matemática correspondiente.

### Ejemplo de código:

```python
# Uso de funciones lambda en el menú
operations = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x - y,
    '3': lambda x, y: x * y,
    '4': lambda x, y: x / y if y != 0 else "Error: No es posible dividir por cero."
}

# Ejecución de la operación seleccionada
if opcion in operations:
    result = operations[opcion](num1, num2)
else:
    result = "Operacion invalida"

print("Resultado:", result)


**Conclusiones:**
- Se han utilizado funciones lambda para asociar cada operación con su función matemática correspondiente.
- La ejecución de operaciones ahora se realiza mediante funciones lambda, proporcionando una mayor concisión y claridad en el código
- Se ha logrado implementar correctamente la gestión de eventos mediante callbacks y la utilización de funciones lambda para operaciones matemáticas.
- Los cambios realizados permiten una mayor flexibilidad y mantenibilidad del código, facilitando la extensión y comprensión de las funcionalidades implementadas.
