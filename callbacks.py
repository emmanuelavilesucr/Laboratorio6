import time
import random

class EventManager:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        if event_type in self.subscribers and callback in self.subscribers[event_type]:
            self.subscribers[event_type].remove(callback)

    def notify(self, event_type, data=None):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)


class RealTimeDataManager:
    def __init__(self, event_manager):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = event_manager

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
        self.event_manager.notify('datos_actualizados', self.data)        

# Actualizaciones en tiempo real en segundo plano
import threading
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")

