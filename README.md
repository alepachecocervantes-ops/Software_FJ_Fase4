Sistema Integral de Gestión de Clientes, Servicios y Reservas — Software FJ

1. Descripción del proyecto

Proyecto colaborativo desarrollado para la Fase 4 — Prácticas simuladas del curso Programación de la Universidad Nacional Abierta y a Distancia (UNAD).
El sistema tiene como propósito gestionar clientes, servicios y reservas para la empresa Software FJ, que ofrece reservas de salas, alquiler de equipos y asesorías especializadas.

2. Objetivo

Desarrollar una aplicación orientada a objetos que permita gestionar clientes, servicios y reservas, incorporando validaciones y un manejo robusto de excepciones para controlar los errores y mantener la estabilidad del programa.

3. Requisitos principales

- Implementar clases abstractas y clases derivadas.
- Aplicar encapsulación, herencia y polimorfismo.
- Incorporar excepciones personalizadas y diferentes estructuras de manejo de errores.
- Implementar el manejo de excepciones mediante try, except, else y finally, incluyendo el encadenaiento de excepciones.
- Registrar eventos y errores relevantes en un archivo de logs.
- Simular al menos diez operaciones, incluyendo casos válidos e inválidos.
- Gestionar la información mediante objetos y listas, sin utilizar bases de datos.
- Documentar el código y verificar su funcionamiento.

4. Estructura del proyecto

El proyecto estará organizado en los siguientes archivos:

main.py -- Ejecución e integración general del sistema.

entidades.py -- Definición de la clase abstracta Entidad.

clientes.py -- Gestión de clientes mediante la clase Cliente.

servicios.py -- Clase abstracta Servicio y sus clases especializadas.

reservas.py -- Gestión de reservas mediante la clase Reserva.

excepciones.py -- Excepciones personalizadas y configuración de registros.

5. Distribución de responsabilidades

El desarrollo del proyecto se organizará entre los cuatro integrantes de la siguiente manera:

Elvis Albeiro Carrascal García – Entidades y gestión de clientes
- Desarrollo de la clase abstracta Entidad.
- Implementación de la clase Cliente.
- Validación de datos, encapsulamiento y operaciones de registro, consulta y actualización de clientes.

Robert Tony Chamorro Rivero – Gestión de servicios
- Desarrollo de la clase abstracta Servicio.
- Implementación de ServicioSala, AlquilerEquipo y AsesoriaEspecializada.
- Cálculo de costos, descripción de servicios y validación de parámetros.
- Aplicación de herencia, polimorfismo y sobrecarga simulada mediante parámetros opcionales.

Alejandra Paola Pacheco Cervantes – Gestión de reservas
- Desarrollo de la clase Reserva.
- Relación entre clientes, servicios y reservas.
- Implementación de operaciones para crear, consultar, confirmar, cancelar y procesar reservas.
- Validación de las operaciones y control de situaciones incorrectas.

Andres Felipe Menco Baldovino – Excepciones y registros
- Creación de excepciones personalizadas.
- Configuración del módulo logging.
- Registro de eventos y errores en el archivo software_fj.log.
- Coordinación del manejo de excepciones con los demás módulos.

La integración de main.py, las pruebas de funcionamiento y la documentación final se realizarán de manera colaborativa.

6. Tecnologías utilizadas
- Python.
- Git.
- GitHub.
- Visual Studio Code.

7. Organización del trabajo colaborativo

El equipo utilizará GitHub para organizar y dar seguimiento al desarrollo del proyecto mediante Issues.

Cada integrante trabajará en una rama independiente, realizará commits descriptivos y enviará Pull Requests hacia la rama main para revisar e integrar sus contribuciones.

8. Almacenamiento de información

El sistema no utilizará bases de datos. La información se gestionará mediante objetos y listas en memoria. Los archivos se utilizarán para almacenar los registros de eventos y errores.

9. Ejecución

Las instrucciones de ejecución se completarán cuando el programa esté integrado y se haya verificado su funcionamiento.

10. Estado del proyecto

Estructura inicial y distribución de responsabilidades definidas. El sistema se desarrollará, integrará y probará progresivamente durante la Fase 4.

Estructura inicial en preparación. El sistema se desarrollará y probará progresivamente durante la Fase 4.

