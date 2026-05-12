# logger.py
import datetime

class Logger:
    @staticmethod
    def registrar_evento(mensaje):
        with open("sistema.log", "a", encoding="utf-8") as log:
            log.write(f"[EVENTO] {datetime.datetime.now()} - {mensaje}\n")

    @staticmethod
    def registrar_error(mensaje):
        with open("sistema.log", "a", encoding="utf-8") as log:
            log.write(f"[ERROR] {datetime.datetime.now()} - {mensaje}\n")