from excepciones import ClienteInvalidoError, DatosFaltantesError
from logger import Logger

class Cliente:
    def __init__(self, nombre, email, telefono):
        self._nombre = None
        self._email = None
        self._telefono = None
        
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        Logger.registrar_evento(f"Cliente creado: {self.nombre}")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) == 0:
            Logger.registrar_error("Nombre de cliente vacío")
            raise DatosFaltantesError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            Logger.registrar_error(f"Email inválido: {valor}")
            raise ClienteInvalidoError("Email debe contener @ y .")
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit() or len(valor) < 7:
            Logger.registrar_error(f"Teléfono inválido: {valor}")
            raise ClienteInvalidoError("Teléfono debe tener solo dígitos (mínimo 7)")
        self._telefono = valor

    def __str__(self):
        return f"Cliente: {self.nombre} | {self.email} | {self.telefono}"