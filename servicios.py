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

class ServicioSala(Servicio):
    """Servicio de reserva y alquiler de salas."""

    def __init__(self, nombre, descripcion, precio_base, capacidad):
        super().__init__(nombre, descripcion, precio_base)

        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise ValueError("La capacidad debe ser un entero positivo.")

        self.__capacidad = capacidad

    @property
    def capacidad(self):
        return self.__capacidad

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        duracion = self._validar_numero(
            duracion, "La duración", permitir_cero=False
        )
        subtotal = self.precio_base * duracion
        return self._calcular_total(subtotal, impuesto, descuento)

    def describir(self):
        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Precio por hora: ${self.precio_base:.2f}"
        )

class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def __init__(
        self, nombre, descripcion, precio_base,
        cantidad_disponible, costo_adicional=0
    ):
        super().__init__(nombre, descripcion, precio_base)

        if (
            isinstance(cantidad_disponible, bool)
            or not isinstance(cantidad_disponible, int)
            or cantidad_disponible < 0
        ):
            raise ValueError(
                "La cantidad disponible debe ser un entero no negativo."
            )

        self.__cantidad_disponible = cantidad_disponible
        self.__costo_adicional = self._validar_numero(
            costo_adicional, "El costo adicional"
        )

    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible

    @property
    def costo_adicional(self):
        return self.__costo_adicional
# Implementación compatible con el módulo de reservas.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        duracion = self._validar_numero(
            duracion, "La duración", permitir_cero=False
        )

        if self.__cantidad_disponible < 1:
        raise ValueError("No hay equipos disponibles.")

        subtotal = (
            self.precio_base * duracion
        ) + self.costo_adicional

        return self._calcular_total(subtotal, impuesto, descuento)

    def describir(self):
        return (
            f"Equipo: {self.nombre} | "
            f"Disponibles: {self.cantidad_disponible} | "
            f"Precio por hora: ${self.precio_base:.2f}"
        )
