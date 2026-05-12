from excepciones import ReservaInvalidaError
from logger import Logger

class Reserva:
    def __init__(self, cliente, servicio, duracion_horas):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion_horas
        self.estado = "pendiente"

    def confirmar(self):
        if self.estado != "pendiente":
            Logger.registrar_error(f"Reserva no pendiente: {self.estado}")
            raise ReservaInvalidaError("Solo se puede confirmar una reserva pendiente")
        self.servicio.validar_disponibilidad()
        self.estado = "confirmada"
        Logger.registrar_evento(f"Reserva confirmada: {self}")

    def cancelar(self):
        if self.estado == "cancelada":
            Logger.registrar_error("Reserva ya cancelada")
            raise ReservaInvalidaError("La reserva ya está cancelada")
        self.estado = "cancelada"
        Logger.registrar_evento(f"Reserva cancelada: {self}")

    def procesar(self, aplicar_descuento=False):
        try:
            costo_base = self.servicio.calcular_costo(self.duracion)
            if aplicar_descuento:
                costo_final = costo_base * 0.9
            else:
                costo_final = costo_base
            return costo_final
        except Exception as e:
            Logger.registrar_error(f"Error al procesar reserva: {str(e)}")
            raise ReservaInvalidaError("No se pudo calcular el costo") from e

    def costo_con_impuestos(self, impuesto=0.19):
        return self.procesar() * (1 + impuesto)

    def __str__(self):
        return f"Reserva [{self.estado}] - {self.cliente.nombre} - {self.servicio.nombre} - {self.duracion}h"