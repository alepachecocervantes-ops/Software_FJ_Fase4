from abc import ABC, abstractmethod


class Entidad(ABC):
    

    @abstractmethod
    def obtener_resumen(self):
        
        pass