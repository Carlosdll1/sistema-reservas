from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import *
from logger import Logger

def main():
    print("=== SISTEMA DE RESERVAS - SOFTWARE FJ ===\n")

    # Clientes válidos e inválidos
    try:
        c1 = Cliente("Ana Gomez", "ana@mail.com", "5551234")
        print(c1)
    except Exception as e:
        print(f"Error: {e}")

    try:
        c2 = Cliente("", "sinemail", "123")
    except Exception as e:
        print(f"Capturado: {e}")

    c3 = Cliente("Luis Paz", "luis@correo.com", "5556789")

    # Servicios
    sala = ReservaSala("Sala A1", 20)
    equipo = AlquilerEquipo("Proyector", "Video")
    asesoria = AsesoriaEspecializada("Python avanzado", "avanzado")

    # Reservas
    reserva1 = Reserva(c1, sala, 2)
    try:
        reserva1.confirmar()
        costo = reserva1.procesar()
        print(f"Costo sin descuento: {costo}")
        print(f"Costo con impuestos: {reserva1.costo_con_impuestos()}")
    except Exception as e:
        print(f"Error: {e}")

    # Servicio no disponible
    sala.disponible = False
    reserva2 = Reserva(c3, sala, 1)
    try:
        reserva2.confirmar()
    except Exception as e:
        print(f"Error esperado: {e}")

    # Con descuento
    sala.disponible = True
    reserva3 = Reserva(c3, asesoria, 3)
    reserva3.confirmar()
    costo_dto = reserva3.procesar(aplicar_descuento=True)
    print(f"Costo con descuento: {costo_dto}")

    # Cancelar reserva
    reserva3.cancelar()
    try:
        reserva3.cancelar()
    except Exception as e:
        print(f"Error esperado: {e}")

    print("\n=== FIN DE SIMULACIÓN ===")
    print("Revisa el archivo sistema.log")

if __name__ == "__main__":
    main()