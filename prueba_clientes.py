from clientes import Cliente

cliente = Cliente("Elvis")

try:
    cliente.actualizar_nombre("   ")
except ValueError as error:
    print("Error controlado:", error)

print("Nombre conservado:", cliente.nombre)
print("El programa continúa.")