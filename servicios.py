# Importamos las herramientas necesarias para trabajar
# con clases abstractas y operaciones matemáticas.
from abc import ABC, abstractmethod
import math

class Servicio(ABC):
    """
    Clase abstracta que representa un servicio
    ofrecido por Software FJ.
    """
    def __init__(self, nombre, descripcion, precio_base):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción es obligatoria.")

        self.__nombre = nombre.strip()
        self.__descripcion = descripcion.strip()
        self.__precio_base = self._validar_numero(
            precio_base, "El precio base", permitir_cero=False
        )

    @staticmethod
    def _validar_numero(valor, mensaje, permitir_cero=True):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or valor < 0
            or (not permitir_cero and valor == 0)
        ):
            raise ValueError(
                f"{mensaje} debe ser un número válido "
                "mayor que cero."
                if not permitir_cero
                else f"{mensaje} debe ser un número igual o mayor que cero."
            )
        return float(valor)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio_base(self):
        return self.__precio_base

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo total del servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve una descripción del servicio."""
        pass

    def _calcular_total(self, subtotal, impuesto=0, descuento=0):
        impuesto = self._validar_numero(
            impuesto, "El impuesto"
        )
        descuento = self._validar_numero(
            descuento, "El descuento"
        )

        if impuesto > 100 or descuento > 100:
            raise ValueError(
                "El impuesto y el descuento no pueden superar el 100 %."
            )

        total = subtotal * (1 + impuesto / 100)
        total -= subtotal * (descuento / 100)

        return round(total, 2)

    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"

