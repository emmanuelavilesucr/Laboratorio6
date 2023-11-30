import time
import random

class EventManager:
    def __init__(self):
        self.subscribers = {}  # Inicializa el diccionario
    
    # Funcion encargada de añadir un suscriptor de un evento específico.
    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
    
    # Funcion encargada de eliminar un suscriptor de un evento específico.
    def unsubscribe(self, event_type, callback):
        if event_type in self.subscribers and callback in self.subscribers[event_type]:
            self.subscribers[event_type].remove(callback)

    # Funcion encargada de notificar a todos los suscriptores registrados cuando ocurre un evento.
    def notify(self, event_type, data=None):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)

class RealTimeDataManager:
    def __init__(self, event_manager):
        # Inicializa los datos y el gestor de eventos
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = event_manager


    # Funcion encargada de simular la actualización periódica de los datos en segundo plano.
    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()


    # Funcion encargada de generar y notificar los datos en tiempo real a través del evento.
    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
        self.event_manager.notify('datos_actualizados', self.data)


# Modulo ejecutable 

if __name__ == "__main__":

    event_manager = EventManager()

    # Esta funcion define el callback que imprime los datos actualizados al stdout
    def callback(data):
        print(f'Datos en tiempo real actualizados: {data}')

    event_manager.subscribe('datos_actualizados', callback)      # Suscribe el callback al evento datos_actualizados
    real_time_data_manager = RealTimeDataManager(event_manager)  # Inicializa el gestor de datos en tiempo real

    # Actualizaciones en tiempo real en segundo plano
    import threading
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    # Captura la interrupción del teclado para terminar el programa
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
