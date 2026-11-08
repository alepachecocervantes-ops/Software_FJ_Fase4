from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase base para las entidades del sistema."""

    @abstractmethod
    def obtener_resumen(self):
        """Cada clase hija deberá implementar su resumen."""
        pass