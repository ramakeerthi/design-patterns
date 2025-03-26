from abc import ABC, abstractmethod

# Interface Equivalent in Python

# We need 3 interfaces, one for the Subject, one for the Observer and other for the common Display

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update():
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

# Now we need to implement the Classes

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
    
    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def measurements_changed(self):
        self.notify_observers()
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update()
    
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.measurements_changed()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
    
    def update(self):
        self.temperature = weather_data.temperature
        self.humidity = weather_data.humidity
        self.display()
    
    def display(self):
        print(f"Current conditions: {self.temperature} celsius, {self.humidity} humidity")


weather_data = WeatherData()
current_dispaly = CurrentConditionsDisplay(weather_data)
weather_data.set_measurements(25,85,1012)
