from entidades import Entidad


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")

        self.__nombre = nombre.strip()

    def obtener_resumen(self):
        return {"nombre": self.__nombre}