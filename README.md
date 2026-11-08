# Sistema Integral de Gestión de Clientes, Servicios y Reservas — Software FJ

## 1. Descripción del proyecto

Proyecto colaborativo desarrollado para la Fase 4 — Prácticas simuladas del curso Programación de la Universidad Nacional Abierta y a Distancia (UNAD). El sistema tiene como propósito gestionar clientes, servicios y reservas para la empresa Software FJ, que ofrece reservas de salas, alquiler de equipos y asesorías especializadas.

## 2. Objetivo

Desarrollar una aplicación orientada a objetos que permita gestionar clientes, servicios y reservas, incorporando validaciones y un manejo robusto de excepciones para controlar los errores y mantener la estabilidad del programa.

## 3. Requisitos principales

- Implementar clases abstractas y clases derivadas.
- Aplicar encapsulación, herencia y polimorfismo.
- Incorporar excepciones personalizadas y diferentes estructuras de manejo de errores.
- Implementar el manejo de excepciones mediante `try`, `except`, `else` y `finally`, incluyendo el encadenamiento de excepciones.
- Registrar eventos y errores relevantes en un archivo de logs.
- Simular al menos diez operaciones, incluyendo casos válidos e inválidos.
- Gestionar la información mediante objetos y listas, sin utilizar bases de datos.
- Documentar el código y verificar su funcionamiento.

## 4. Estructura del proyecto

El proyecto estará organizado en los siguientes archivos:

- `main.py` -- Ejecución e integración general del sistema.
- `entidades.py` -- Definición de la clase abstracta Entidad.
- `clientes.py` -- Gestión de clientes mediante la clase Cliente.
- `servicios.py` -- Clase abstracta Servicio y sus clases especializadas.
- `reservas.py` -- Gestión de reservas mediante la clase Reserva.
- `excepciones.py` -- Excepciones personalizadas y configuración de registros.
- `prueba_clientes.py` -- Pruebas de las operaciones y validaciones del módulo de clientes.

## 5. Distribución de responsabilidades

El desarrollo del proyecto se organizará entre los cuatro integrantes de la siguiente manera:

**Elvis Albeiro Carrascal García – Entidades y gestión de clientes**

- Desarrollo de la clase abstracta Entidad.
- Implementación de la clase Cliente.
- Validación de datos, encapsulamiento y operaciones de registro, consulta y actualización de clientes.

**Robert Tony Chamorro Rivero – Gestión de servicios**

- Desarrollo de la clase abstracta Servicio.
- Implementación de ServicioSala, AlquilerEquipo y AsesoriaEspecializada.
- Cálculo de costos, descripción de servicios y validación de parámetros.
- Aplicación de herencia, polimorfismo y sobrecarga simulada mediante parámetros opcionales.

**Alejandra Paola Pacheco Cervantes – Gestión de reservas**

- Desarrollo de la clase Reserva.
- Relación entre clientes, servicios y reservas.
- Implementación de operaciones para crear, consultar, confirmar, cancelar y procesar reservas.
- Validación de las operaciones y control de situaciones incorrectas.

**Andres Felipe Menco Baldovino – Excepciones y registros**

- Creación de excepciones personalizadas.
- Configuración del módulo logging.
- Registro de eventos y errores en el archivo `software_fj.log`.
- Coordinación del manejo de excepciones con los demás módulos.

La integración de `main.py`, las pruebas de funcionamiento y la documentación final se realizarán de manera colaborativa.

## 6. Tecnologías utilizadas

- Python.
- Git.
- GitHub.
- Visual Studio Code.

## 7. Organización del trabajo colaborativo

El equipo utilizará GitHub para organizar y dar seguimiento al desarrollo del proyecto mediante Issues.

Cada integrante trabajará en una rama independiente, realizará commits descriptivos y enviará Pull Requests hacia la rama `main` para revisar e integrar sus contribuciones.

Actualmente, los módulos desarrollados cuentan con los siguientes Pull Requests abiertos:

- **Pull Request #9:** Entidades y gestión de clientes, desarrollado por Elvis.
- **Pull Request #10:** Gestión de servicios, desarrollado por Robert.
- **Pull Request #11:** Actualización del módulo de reservas, con mejoras de herencia, validaciones y manejo de errores, desarrollado por Alejandra.

Los Pull Requests permanecerán abiertos mientras se espera la retroalimentación del tutor. Posteriormente, se realizarán las correcciones necesarias antes de integrar los cambios a la rama principal.

## 8. Almacenamiento de información

El sistema no utilizará bases de datos. La información se gestionará mediante objetos y listas en memoria. Los archivos se utilizarán para almacenar los registros de eventos y errores.

## 9. Ejecución

Las instrucciones de ejecución se completarán cuando el programa esté integrado y se haya verificado su funcionamiento.

Por el momento, los módulos se encuentran en desarrollo y revisión individual. Las pruebas de integración se realizarán una vez que los archivos necesarios estén disponibles y sean compatibles entre sí.

## 10. Estado del proyecto

**Estado actual: desarrollo de módulos y revisión de Pull Requests.**

La estructura inicial del proyecto y la distribución de responsabilidades ya se encuentran definidas.

Avances realizados:

- **Entidades y clientes:** módulo desarrollado por Elvis y enviado a revisión mediante el Pull Request #9.
- **Servicios:** módulo desarrollado por Robert y enviado a revisión mediante el Pull Request #10.
- **Reservas:** módulo desarrollado y actualizado con mejoras de herencia, validaciones y manejo de errores. Los cambios se encuentran en revisión mediante el Pull Request #11.
- **Excepciones:** módulo pendiente de desarrollo e integración.
- **Programa principal (`main.py`):** pendiente de integración colaborativa.

Actualmente, el equipo se encuentra a la espera de la retroalimentación del tutor sobre los módulos desarrollados.

Una vez revisados, se realizarán los ajustes necesarios, la integración de los archivos, las pruebas de funcionamiento y la documentación final del sistema.
