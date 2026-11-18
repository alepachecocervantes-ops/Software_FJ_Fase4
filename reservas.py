import logging
import math

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio
from excepciones import ErrorDatosReserva, ErrorEstadoReserva, ErrorProcesamientoReserva

logger = logging.getLogger(__name__)


class Reserva(Entidad):
    """Representa la reserva de un cliente para un servicio de Software FJ."""

    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    PROCESADA = "Procesada"

    __contador = 1

    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise ErrorDatosReserva("El cliente debe ser de tipo Cliente.")

        if not isinstance(servicio, Servicio):
            raise ErrorDatosReserva("El servicio debe ser de tipo Servicio.")

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ErrorDatosReserva("La duración debe ser un número finito mayor que cero.")

        self.__id = Reserva.__contador
        Reserva.__contador += 1
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = self.PENDIENTE

        logger.info("Reserva %s creada correctamente.", self.__id)

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        """Confirma únicamente una reserva pendiente."""
        if self.__estado != self.PENDIENTE:
            raise ErrorEstadoReserva(self.__estado)

        self.__estado = self.CONFIRMADA
        logger.info("Reserva %s confirmada.", self.__id)
        return True

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""
        if self.__estado not in (self.PENDIENTE, self.CONFIRMADA):
            raise ErrorEstadoReserva(self.__estado)

        self.__estado = self.CANCELADA
        logger.info("Reserva %s cancelada.", self.__id)
        return True

    def procesar(self, impuesto=0, descuento=0):
        """Procesa una reserva confirmada y devuelve el costo calculado."""
        if self.__estado != self.CONFIRMADA:
            raise ErrorEstadoReserva(self.__estado)

        try:
            costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto=impuesto,
                descuento=descuento,
            )

            if (
                isinstance(costo, bool)
                or not isinstance(costo, (int, float))
                or not math.isfinite(costo)
                or costo < 0
            ):
                raise ValueError("El servicio devolvió un costo inválido.")

        except Exception as error:
            raise ErrorProcesamientoReserva(
                f"No fue posible procesar la reserva {self.__id}: {error}"
            ) from error
        else:
            self.__estado = self.PROCESADA
            logger.info("Reserva %s procesada. Costo: %s.", self.__id, costo)
            return costo

    def obtener_resumen(self):
        """Implementa el método abstracto exigido por Entidad."""
        return {
            "id": self.__id,
            "cliente": self.__cliente,
            "servicio": self.__servicio,
            "duracion": self.__duracion,
            "estado": self.__estado,
        }

    def __str__(self):
        return (
            f"Reserva N.º {self.__id} | "
            f"Duración: {self.__duracion} | "
            f"Estado: {self.__estado}"
        )
