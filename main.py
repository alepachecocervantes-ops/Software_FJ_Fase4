import logging

from clientes import Cliente, RegistroClientes
from servicios import ServicioSala, AlquilerEquipo
from reservas import Reserva
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorEstadoReserva,
    ErrorClienteDuplicado,
    ErrorDuracion,
    ErrorCapacidad,
    ErrorServicioNoDisponible
)

def main():
    """Punto de entrada del sistema Software FJ."""
    registro = None
    cliente = None
    servicio = None
    equipo = None
    reserva = None
    print("=" * 50)
    print("       SISTEMA DE GESTIÓN SOFTWARE FJ")
    print("=" * 50)
    print("Iniciando simulación de operaciones...")

    # Aquí integraremos las operaciones de clientes, servicios y reservas.

    # OPERACIÓN 1: Registrar un cliente
    print("\nOPERACIÓN 1: Registrar un cliente")

    try:
        registro = RegistroClientes()
        cliente = Cliente("Ana Martínez", "12345")
        registro.registrar(cliente)

    except Exception as error:
        print(f"Error al registrar el cliente: {error}")
        logging.error("Error al registrar cliente: %s", error)

    else:
        print("Cliente registrado correctamente.")
        logging.info("Operación 1: Cliente registrado correctamente.")

    finally:
        print("Operación 1 finalizada.")


    # OPERACIÓN 2: Consultar un cliente
    print("\nOPERACIÓN 2: Consultar un cliente")

    try:
        if registro is None or cliente is None:
            raise ErrorCliente(
            "No se puede consultar el cliente porque el registro inicial falló."
        )
        cliente_encontrado = registro.consultar("12345")

    except Exception as error:
        print(f"Error al consultar el cliente: {error}")
        logging.error("Error al consultar cliente: %s", error)

    else:
        print(f"Cliente encontrado: {cliente_encontrado.obtener_resumen()}")
        logging.info("Operación 2: Cliente consultado correctamente.")

    finally:
        print("Operación 2 finalizada.")


    # OPERACIÓN 3: Crear un servicio de sala
    print("\nOPERACIÓN 3: Crear un servicio de sala")

    try:
        servicio = ServicioSala(
            "Sala A",
            "Sala de reuniones",
            50000,
            10
        )

    except Exception as error:
        print(f"Error al crear el servicio: {error}")
        logging.error("Error al crear servicio: %s", error)

    else:
        print("Servicio creado correctamente.")
        print(f"Servicio: {servicio.describir()}")
        logging.info("Operación 3: Servicio creado correctamente.")

    finally:
        print("Operación 3 finalizada.")


    # OPERACIÓN 4: Crear un servicio de alquiler de equipos
    print("\nOPERACIÓN 4: Crear un servicio de alquiler de equipos")

    try:
        equipo = AlquilerEquipo(
            "Proyector",
            "Alquiler de proyector multimedia",
            30000,
            5
        )

    except Exception as error:
        print(f"Error al crear el equipo: {error}")
        logging.error("Error al crear equipo: %s", error)

    else:
        print("Servicio de alquiler creado correctamente.")
        print(f"Servicio: {equipo.describir()}")
        logging.info("Operación 4: Servicio de alquiler creado correctamente.")

    finally:
        print("Operación 4 finalizada.")


    # OPERACIÓN 5: Crear una reserva
    print("\nOPERACIÓN 5: Crear una reserva")

    try:
        if cliente is None or servicio is None:
            raise ErrorReserva(
                "No se puede crear la reserva porque falta el cliente o el servicio."
            )
            
        reserva = Reserva(cliente, servicio, 2)

    except Exception as error:
        print(f"Error al crear la reserva: {error}")
        logging.error("Error al crear reserva: %s", error)

    else:
        print("Reserva creada correctamente.")
        print(f"Reserva: {reserva}")
        logging.info("Operación 5: Reserva creada correctamente.")

    finally:
        print("Operación 5 finalizada.")


    # OPERACIÓN 6: Confirmar una reserva
    print("\nOPERACIÓN 6: Confirmar una reserva")

    try:
        if reserva is None:
            raise ErrorReserva(
            "No se puede confirmar la reserva porque no fue creada."
        )

        reserva.confirmar()

    except Exception as error:
        print(f"Error al confirmar la reserva: {error}")
        logging.error("Error al confirmar reserva: %s", error)

    else:
        print("Reserva confirmada correctamente.")
        print(f"Reserva: {reserva}")
        logging.info("Operación 6: Reserva confirmada correctamente.")

    finally:
        print("Operación 6 finalizada.")


    # OPERACIÓN 7: Procesar una reserva
    print("\nOPERACIÓN 7: Procesar una reserva")

    try:
        if reserva is None:
            raise ErrorReserva(
            "No se puede procesar la reserva porque no fue creada."
        )

        total = reserva.procesar()

    except Exception as error:
        print(f"Error al procesar la reserva: {error}")
        logging.error("Error al procesar reserva: %s", error)

    else:
        print("Reserva procesada correctamente.")
        print(f"Total a pagar: ${total:,.2f}")
        print(f"Reserva: {reserva}")
        logging.info("Operación 7: Reserva procesada correctamente.")

    finally:
        print("Operación 7 finalizada.")


    # OPERACIÓN 8: Intentar registrar un cliente inválido
    print("\nOPERACIÓN 8: Registrar cliente con nombre vacío")

    try:
        cliente_invalido = Cliente("", "67890")
        registro.registrar(cliente_invalido)

    except ErrorCliente as error:
        print(f"Error controlado: {error}")
        logging.error("Operación 8: %s", error)

    except ValueError as error:
        print(f"Error de validación controlado: {error}")
        logging.error("Operación 8: %s", error)

    else:
        print("ADVERTENCIA: Se aceptó un cliente inválido.")
        logging.warning("Operación 8: Se aceptó un cliente inválido.")

    finally:
        print("Operación 8 finalizada.")


    # OPERACIÓN 9: Intentar crear un servicio con precio negativo
    print("\nOPERACIÓN 9: Crear servicio con precio negativo")

    try:
        servicio_invalido = ServicioSala(
            "Sala B",
            "Sala de reuniones",
            -50000,
            10
        )

    except (ErrorServicio, ValueError) as error:
        print(f"Error controlado: {error}")
        logging.error("Operación 9: %s", error)

    else:
        print("ADVERTENCIA: Se aceptó un servicio con precio negativo.")
        logging.warning("Operación 9: Se aceptó un precio inválido.")

    finally:
        print("Operación 9 finalizada.")


    # OPERACIÓN 10: Intentar procesar una reserva cancelada
    print("\nOPERACIÓN 10: Procesar una reserva cancelada")

    try:
        if cliente is None or servicio is None:
            raise ErrorReserva(
            "No se puede crear la reserva de prueba porque falta el cliente o el servicio."
        )

        reserva_cancelada = Reserva(cliente, servicio, 2)
        reserva_cancelada.cancelar()
        reserva_cancelada.procesar()

    except ErrorEstadoReserva as error:
        print(f"Error de reserva controlado: {error}")
        logging.error("Operación 10: %s", error)
    
    except ErrorReserva as error:
        print(f"Error inesperado de reserva: {error}")
        logging.error("Operación 10: Error inesperado: %s", error)

    else:
        print("ADVERTENCIA: Se procesó una reserva cancelada.")
        logging.warning("Operación 10: Se procesó una reserva cancelada.")
        
    finally:
        print("Operación 10 finalizada.")

    # OPERACIÓN 11: Intentar registrar un cliente duplicado
    print("\nOPERACIÓN 11: Registrar cliente duplicado")

    try:
        if registro is None:
            raise ErrorCliente("No existe un registro de clientes para la prueba.")

        registro.registrar(Cliente("Ana Martínez", "12345"))

    except ErrorClienteDuplicado as error:
        print(f"Error controlado (ErrorClienteDuplicado): {error}")
        logging.error("Operación 11: %s", error)

    else:
        print("ADVERTENCIA: Se permitió registrar un cliente duplicado.")
        logging.warning("Operación 11: Se aceptó un cliente duplicado.")

    finally:
        print("Operación 11 finalizada.")

    # OPERACIÓN 12: Intentar calcular el costo con duración negativa
    print("\nOPERACIÓN 12: Calcular costo con duración negativa")

    try:
        if servicio is None:
            raise ErrorServicio("No existe una sala para la prueba.")

        servicio.calcular_costo(-2)

    except ErrorDuracion as error:
        print(f"Error controlado (ErrorDuracion): {error}")
        logging.error("Operación 12: %s", error)

    else:
        print("ADVERTENCIA: Se aceptó una duración negativa.")
        logging.warning("Operación 12: Se aceptó una duración negativa.")

    finally:
        print("Operación 12 finalizada.")

    # OPERACIÓN 13: Intentar crear una sala con capacidad inválida
    print("\nOPERACIÓN 13: Crear sala con capacidad cero")

    try:
        ServicioSala("Sala C", "Sala de reuniones", 40000, 0)

    except ErrorCapacidad as error:
        print(f"Error controlado (ErrorCapacidad): {error}")
        logging.error("Operación 13: %s", error)

    else:
        print("ADVERTENCIA: Se aceptó una capacidad inválida.")
        logging.warning("Operación 13: Se aceptó una capacidad inválida.")

    finally:
        print("Operación 13 finalizada.")

    # OPERACIÓN 14: Intentar alquilar un equipo sin unidades disponibles
    print("\nOPERACIÓN 14: Alquilar equipo no disponible")

    try:
        equipo_agotado = AlquilerEquipo(
            "Proyector agotado",
            "Equipo sin existencias",
            30000,
            0
        )

        equipo_agotado.calcular_costo(1)

    except ErrorServicioNoDisponible as error:
        print(f"Error controlado (ErrorServicioNoDisponible): {error}")
        logging.error("Operación 14: %s", error)

    else:
        print("ADVERTENCIA: Se permitió alquilar un equipo no disponible.")
        logging.warning("Operación 14: Se aceptó un servicio no disponible.")

    finally:
        print("Operación 14 finalizada.")

if __name__ == "__main__":
    main()
