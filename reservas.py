import logging
import math


# Registro de eventos del módulo de reservas.
logger = logging.getLogger(__name__)


class Reserva:
    """
    Representa una reserva de un cliente para un servicio.

    Estados posibles:
    - Pendiente
    - Confirmada
    - Cancelada
    - Procesada
    """

    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    PROCESADA = "Procesada"

    # Contador para asignar identificadores únicos en memoria.
    __contador = 1

    def __init__(self, cliente, servicio, duracion):
        """
        Inicializa una reserva validando sus datos.
        """

        if cliente is None:
            raise ValueError("La reserva debe tener un cliente.")

        if servicio is None:
            raise ValueError("La reserva debe tener un servicio.")

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ValueError(
                "La duración debe ser un número mayor que cero."
            )

        self.__id = Reserva.__contador
        Reserva.__contador += 1

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = self.PENDIENTE

        logger.info(
            "Reserva %s creada correctamente.",
            self.__id
        )

    # Propiedades para consultar los atributos privados.

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
        """
        Confirma una reserva que se encuentre pendiente.
        """

        if self.__estado != self.PENDIENTE:
            raise RuntimeError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = self.CONFIRMADA

        logger.info(
            "Reserva %s confirmada.",
            self.__id
        )

        return True

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.
        """

        if self.__estado not in (
            self.PENDIENTE,
            self.CONFIRMADA
        ):
            raise RuntimeError(
                "No se puede cancelar una reserva "
                "que ya está cancelada o procesada."
            )

        self.__estado = self.CANCELADA

        logger.info(
            "Reserva %s cancelada.",
            self.__id
        )

        return True

    def procesar(self, impuesto=0, descuento=0):
        """
        Procesa una reserva confirmada y calcula su costo.

        El servicio debe implementar el método:
        calcular_costo(duracion, impuesto=0, descuento=0).
        """

        if self.__estado != self.CONFIRMADA:
            raise RuntimeError(
                "Solo se pueden procesar reservas confirmadas."
            )

        try:
            metodo_calculo = getattr(
                self.__servicio,
                "calcular_costo",
                None
            )

            if not callable(metodo_calculo):
                raise AttributeError(
                    "El servicio no tiene el método calcular_costo()."
                )

            costo = metodo_calculo(
                self.__duracion,
                impuesto=impuesto,
                descuento=descuento
            )

            if (
                isinstance(costo, bool)
                or not isinstance(costo, (int, float))
                or not math.isfinite(costo)
                or costo < 0
            ):
                raise ValueError(
                    "El servicio devolvió un costo inválido."
                )

            self.__estado = self.PROCESADA

            logger.info(
                "Reserva %s procesada. Costo: %s.",
                self.__id,
                costo
            )

            return costo

        except Exception as error:
            logger.exception(
                "Error al procesar la reserva %s.",
                self.__id
            )

            raise RuntimeError(
                f"No fue posible procesar la reserva {self.__id}."
            ) from error

    def obtener_resumen(self):
        """
        Devuelve los datos principales de la reserva.
        """

        return {
            "id": self.__id,
            "cliente": self.__cliente,
            "servicio": self.__servicio,
            "duracion": self.__duracion,
            "estado": self.__estado
        }

    def __str__(self):
        return (
            f"Reserva N.º {self.__id} | "
            f"Duración: {self.__duracion} | "
            f"Estado: {self.__estado}"
        )
