from entidades import Entidad


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, nombre):
        self.actualizar_nombre(nombre)

    def obtener_resumen(self):
        return {"nombre": self.__nombre}
    @property
    def nombre(self):
        """Permite consultar el nombre."""
        return self.__nombre

    def actualizar_nombre(self, nuevo_nombre):
        """Valida el nuevo nombre antes de cambiarlo."""
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")

        self.__nombre = nuevo_nombre.strip()
    