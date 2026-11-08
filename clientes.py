import logging

from entidades import Entidad


logger = logging.getLogger(__name__)


class ErrorCliente(ValueError):
    pass
    


def _validar_texto(valor, campo):
    
    if not isinstance(valor, str) or not valor.strip():
        logger.error("Dato inválido en el campo %s.", campo)
        raise ErrorCliente(f"{campo} debe ser un texto no vacío.")
    return valor.strip()


class Cliente(Entidad):
    

    def __init__(self, nombre, identificador):
        self.__identificador = _validar_texto(identificador, "El identificador")
        self.__nombre = _validar_texto(nombre, "El nombre")

    @property
    def identificador(self):
        return self.__identificador

    @property
    def nombre(self):
        return self.__nombre

    def actualizar_nombre(self, nuevo_nombre):
        self.__nombre = _validar_texto(nuevo_nombre, "El nombre")
        logger.info("Nombre de cliente actualizado.")

    def obtener_resumen(self):
        return {"identificador": self.__identificador, "nombre": self.__nombre}


class RegistroClientes:
   
    def __init__(self):
        self.__clientes = []

    def registrar(self, cliente):
        if not isinstance(cliente, Cliente):
            logger.error("Intento de registrar un objeto que no es Cliente.")
            raise ErrorCliente("Solo se pueden registrar objetos Cliente.")
        for existente in self.__clientes:
            if existente.identificador == cliente.identificador:
                logger.error("Intento de registrar un identificador duplicado.")
                raise ErrorCliente("Ya existe un cliente con ese identificador.")
        self.__clientes.append(cliente)
        logger.info("Cliente registrado correctamente.")
        return cliente

    def consultar(self, identificador):
        identificador = _validar_texto(identificador, "El identificador")
        for cliente in self.__clientes:
            if cliente.identificador == identificador:
                return cliente
        logger.error("Consulta de un cliente inexistente.")
        raise ErrorCliente("No existe un cliente con ese identificador.")

    def actualizar(self, identificador, nuevo_nombre):
        cliente = self.consultar(identificador)
        cliente.actualizar_nombre(nuevo_nombre)
        return cliente

    def listar(self):
        return [cliente.obtener_resumen() for cliente in self.__clientes]
    