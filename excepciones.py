# ======================================================
# PROYECTO: SOFTWARE FJ - GESTIÓN DE RESERVAS(FASE...4)
# Módulo: excepciones.py
# Responsable: Andrés Felipe Menco Baldovino
# Grupo:
# Objetivo: Definir excepciones personalizadas y sistema de registro


# llamamos los modulos que permiten el registros de mensajes, fechas y horas.
import logging
from datetime import datetime

# PARTE 1: CONFIGURACIÓN DEL SISTEMA DE REGISTRO (LOGS)
# ======================================================

def configurar_logging():
    """
    Configura el sistema de registro para guardar eventos y errores
    en el archivo 'software_fj.log'
    """
    # Configurar el sistema de registro
    logging.basicConfig(
        level=logging.DEBUG,  # Registrar desde mensajes de depuración en adelante
        format='%(asctime)s | %(levelname)s | %(message)s',  # Formato: Fecha | Nivel | Mensaje
        datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
        filename='software_fj.log',  # Nombre del archivo donde se guardará todo
        filemode='a'  # 'a' = agregar al final del archivo, no sobrescribir
    )

    # Mensaje de confirmación en el registro
    logging.info("=" * 50)
    logging.info("Sistema de registro iniciado correctamente")


# Llamar a la función para inicializar el registro al importar este módulo
configurar_logging()


# Funciones auxiliares para facilitar el registro desde otros módulos
def registrar_info(mensaje):
    """Registra un mensaje informativo en el archivo de log"""
    logging.info(mensaje)

def registrar_advertencia(mensaje):
    """Registra una advertencia en el archivo de log"""
    logging.warning(mensaje)

def registrar_error(error, operacion):
    """Registra un error y la operación relacionada en el archivo de log"""
    logging.error("Operación: %s | Error: %s", operacion, error)

def registrar_depuracion(mensaje):
    """Registra un mensaje de depuración en el archivo de log"""
    logging.debug(mensaje)


# ======================================================
# PARTE 2: EXCEPCIONES PERSONALIZADAS


# ----------------------
# Excepción base del sistema
# ----------------------
class SoftwareFJError(Exception):
    """Excepción base para todos los errores del sistema Software FJ"""
    def __init__(self, mensaje="Error en el sistema Software FJ"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        # Registrar automáticamente el error al crearlo
        registrar_error(
            self.mensaje,
            f"Creación de {type(self).__name__}"
        )


class ErrorCliente(SoftwareFJError):
    """Clase base para errores relacionados con clientes"""


class ErrorServicio(SoftwareFJError):
    """Clase base para errores relacionados con servicios"""


class ErrorReserva(SoftwareFJError):
    """Error general relacionado con una reserva"""
    def __init__(self, mensaje="Error en la reserva"):
        super().__init__(mensaje)


class ErrorValidacion(SoftwareFJError):
    """Clase base para errores de entrada y validación"""

#Errores organizados por jerarquia
# ----------------------
# Errores relacionados con Clientes

class ErrorClienteDuplicado(ErrorCliente):
    """Se lanza cuando se intenta registrar un cliente que ya existe"""
    def __init__(self, nombre_cliente):
        self.mensaje = f"El cliente '{nombre_cliente}' ya se encuentra registrado en el sistema"
        super().__init__(self.mensaje)


class ErrorDatosClienteInvalidos(ErrorCliente):
    """Se lanza cuando los datos del cliente no cumplen con los requisitos"""
    def __init__(self, motivo):
        self.mensaje = f"Datos del cliente inválidos: {motivo}"
        super().__init__(self.mensaje)


class ErrorClienteNoEncontrado(ErrorCliente):
    """Se lanza cuando no se encuentra un cliente en las búsquedas"""
    def __init__(self, identificador):
        self.mensaje = f"No se encontró el cliente con el identificador: {identificador}"
        super().__init__(self.mensaje)


# ----------------------
# Errores relacionados con Servicios

class ErrorServicioNoDisponible(ErrorServicio):
    """Se lanza cuando se intenta acceder a un servicio que no existe"""
    def __init__(self, nombre_servicio):
        self.mensaje = f"El servicio '{nombre_servicio}' no se encuentra disponible"
        super().__init__(self.mensaje)


class ErrorDisponibilidad(ErrorServicio):
    """Se lanza cuando la disponibilidad de un servicio no es válida"""
    def __init__(self, disponibilidad):
        self.mensaje = f"La disponibilidad '{disponibilidad}' del servicio no es válida"
        super().__init__(self.mensaje)


class ErrorModalidad(ErrorServicio):
    """Se lanza cuando la modalidad de un servicio no es válida"""
    def __init__(self, modalidad):
        self.mensaje = f"La modalidad '{modalidad}' del servicio no es válida"
        super().__init__(self.mensaje)


class ErrorCalculoCosto(ErrorServicio):
    """Se lanza cuando ocurre un problema al calcular el costo de un servicio"""
    def __init__(self, detalle):
        self.mensaje = f"Error al calcular el costo del servicio: {detalle}"
        super().__init__(self.mensaje)


class ErrorDuracion(ErrorServicio):
    """Se lanza cuando la duración de un servicio no es válida"""
    def __init__(self, duracion):
        self.mensaje = f"La duración '{duracion}' del servicio no es válida"
        super().__init__(self.mensaje)


class ErrorCapacidad(ErrorServicio):
    """Se lanza cuando la capacidad de un servicio no es válida"""
    def __init__(self, capacidad):
        self.mensaje = f"La capacidad '{capacidad}' del servicio no es válida"
        super().__init__(self.mensaje)


class ErrorDatosServicio(ErrorServicio):
    """Se lanza cuando los datos de un servicio no cumplen con los requisitos"""
    def __init__(self, motivo):
        self.mensaje = f"Datos del servicio inválidos: {motivo}"
        super().__init__(self.mensaje)


# ----------------------
# Errores relacionados con Reservas

class ErrorDatosReserva(ErrorReserva):
    """Se lanza cuando los datos de una reserva no son válidos"""
    def __init__(self, motivo):
        self.mensaje = f"Datos de la reserva inválidos: {motivo}"
        super().__init__(self.mensaje)


class ErrorEstadoReserva(ErrorReserva):
    """Se lanza cuando el estado de una reserva no es válido"""
    def __init__(self, estado):
        self.mensaje = f"El estado '{estado}' de la reserva no es válido"
        super().__init__(self.mensaje)


class ErrorProcesamientoReserva(ErrorReserva):
    """Se lanza cuando ocurre un error al procesar una reserva"""
    def __init__(self, detalle):
        self.mensaje = f"Error al procesar la reserva: {detalle}"
        super().__init__(self.mensaje)


# ----------------------
# Errores de entrada y validación general

class ErrorEntradaInvalida(ErrorValidacion):
    """Se lanza cuando el usuario ingresa un dato con formato incorrecto"""
    def __init__(self, campo, tipo_esperado):
        self.mensaje = f"Valor inválido para '{campo}'. Se esperaba: {tipo_esperado}"
        super().__init__(self.mensaje)


class ErrorOpcionInvalida(ErrorValidacion):
    """Se lanza cuando se selecciona una opción que no está en el menú"""
    def __init__(self, opcion, rango_valido):
        self.mensaje = f"La opción {opcion} no es válida. Por favor elige un valor entre {rango_valido}"
        super().__init__(self.mensaje)

#===========================================================
#Bloques de pruebas(verificar que el programa si se ejecuta)

if __name__ == "__main__":
    try:
        registrar_info("Iniciando prueba del sistema")

        # Simular un error
        raise ErrorDatosReserva("Rodolfo Hernandes")

    except ErrorDatosReserva as e:
        print(f"Mensaje del error: {e}")
        registrar_advertencia(f"Se manejó la excepción: {e}")
        registrar_error(e, "Prueba de ErrorDatosReserva")
    

    finally:
        registrar_info("Prueba finalizada")
        print("Revisa el archivo 'software_fj.log' para ver el registro de las pruebas")

#-------------------------
#Prueba de valueError

    print("\nProbando que la excepción también se reconoce como ValueError...")
    try:
        raise ErrorDatosReserva("Rodolfo Hernandes")
    except ValueError as e:
        print(f"{type(e).__name__} se capturo como ValueError: {e}")
        registrar_error(e, "Prueba de reconocimiento como ValueError")

    print("\nProbando la excepción ErrorCalculoCosto...")
    try:
        raise ErrorCalculoCosto("No se pudo calcular el costo del servicio")
    except ErrorCalculoCosto as e:
        print(f"Mensaje del error: {e}")
        registrar_error(e, "Prueba de ErrorCalculoCosto")
