import logging

from clientes import Cliente, ErrorCliente, RegistroClientes


def main():
    logging.basicConfig(
        filename="software_fj.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        encoding="utf-8",
    )
    registro = RegistroClientes()
    operaciones = [
        ("Registrar Elvis", lambda: registro.registrar(Cliente(" Elvis ", "C001")).obtener_resumen()),
        ("Registrar Alejandra", lambda: registro.registrar(Cliente("Alejandra", "C002")).obtener_resumen()),
        ("Consultar C001", lambda: registro.consultar("C001").obtener_resumen()),
        ("Actualizar C001", lambda: registro.actualizar("C001", "Elvis Carrascal").obtener_resumen()),
        ("Rechazar nombre vacío", lambda: Cliente("   ", "C003")),
        ("Rechazar identificador vacío", lambda: Cliente("Robert", "")),
        ("Rechazar nombre numérico", lambda: Cliente(123, "C003")),
        ("Rechazar duplicado", lambda: registro.registrar(Cliente("Otro cliente", "C001"))),
        ("Consultar inexistente", lambda: registro.consultar("C999")),
        ("Rechazar actualización vacía", lambda: registro.actualizar("C001", "")),
        ("Comprobar nombre conservado", lambda: registro.consultar("C001").nombre),
        ("Listar clientes", registro.listar),
    ]
    for numero, (descripcion, operacion) in enumerate(operaciones, start=1):
        print(f"\n{numero}. {descripcion}")
        try:
            resultado = operacion()
        except ErrorCliente as error:
            print("Error controlado:", error)
        else:
            print("Resultado:", resultado)
        finally:
            print("Operación finalizada; el programa continúa.")


if __name__ == "__main__":
    main()