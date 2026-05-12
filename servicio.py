from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError
from logger import Logger

class Servicio(ABC):
    def __init__(self, nombre, disponible=True):
        self.nombre = nombre
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion_horas):
        pass

    @abstractmethod
    def describir(self):
        pass

    def validar_disponibilidad(self):
        if not self.disponible:
            Logger.registrar_error(f"Servicio no disponible: {self.nombre}")
            raise ServicioNoDisponibleError(f"El servicio {self.nombre} no está disponible")

class ReservaSala(Servicio):
    def __init__(self, nombre, capacidad):
        super().__init__(nombre)
        self.capacidad = capacidad

    def calcular_costo(self, duracion_horas):
        return duracion_horas * 50

    def describir(self):
        return f"Reserva de sala '{self.nombre}' para {self.capacidad} personas."

class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tipo_equipo):
        super().__init__(nombre)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion_horas):
        return duracion_horas * 20

    def describir(self):
        return f"Alquiler de equipo {self.tipo_equipo} - {self.nombre}."

class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.nivel = nivel

    def calcular_costo(self, duracion_horas):
        if self.nivel == "avanzado":
            return duracion_horas * 100
        return duracion_horas * 60

    def describir(self):
        return f"Asesoría {self.nivel} - {self.nombre}."