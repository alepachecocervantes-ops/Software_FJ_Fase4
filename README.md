# Sistema Integral de Gestión de Clientes, Servicios y Reservas — Software FJ

## 1. Descripción del proyecto

Proyecto colaborativo desarrollado para la Fase 4 — Prácticas simuladas del curso Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

El sistema tiene como propósito gestionar clientes, servicios y reservas para la empresa Software FJ, que ofrece servicios de reserva de salas, alquiler de equipos y asesorías especializadas.

La aplicación fue desarrollada en Python, utilizando los principios de la programación orientada a objetos, incluyendo abstracción, encapsulamiento, herencia y polimorfismo. También incorpora validaciones, excepciones personalizadas y registros de eventos para controlar situaciones incorrectas durante su ejecución.

## 2. Objetivo

Desarrollar una aplicación orientada a objetos que permita gestionar clientes, servicios y reservas, mediante clases especializadas, validaciones y mecanismos de manejo de excepciones, garantizando un funcionamiento organizado y controlado del sistema.

## 3. Requisitos principales

- Implementar clases abstractas y clases derivadas.
- Aplicar encapsulación, herencia y polimorfismo.
- Incorporar excepciones personalizadas para gestionar errores específicos del sistema.
- Utilizar estructuras de manejo de excepciones mediante `try`, `except`, `else` y `finally`, según las necesidades de los módulos.
- Implementar mecanismos de registro de eventos y errores mediante `logging`.
- Ejecutar al menos diez operaciones simuladas, incluyendo casos válidos e inválidos.
- Gestionar la información mediante objetos y listas en memoria, sin utilizar bases de datos.
- Organizar el desarrollo mediante ramas, commits, Issues y Pull Requests en GitHub.
- Documentar y verificar el funcionamiento de los módulos.

## 4. Estructura del proyecto

El sistema está organizado en archivos independientes que permiten separar las responsabilidades y facilitar su mantenimiento.

| Archivo | Función |
|---|---|
| `main.py` | Integra los módulos y ejecuta las diez operaciones simuladas del sistema. |
| `entidades.py` | Define la clase abstracta `Entidad`, utilizada como base para otras clases. |
| `clientes.py` | Implementa la gestión de clientes, sus validaciones y operaciones principales. |
| `servicios.py` | Define la clase abstracta `Servicio` y las clases especializadas para los servicios ofrecidos. |
| `reservas.py` | Implementa la clase `Reserva` y las operaciones relacionadas con su gestión. |
| `excepciones.py` | Centraliza las excepciones personalizadas y las funciones de registro de eventos y errores. |
| `prueba_clientes.py` | Contiene pruebas específicas para verificar las funcionalidades del módulo de clientes. |
| `.gitignore` | Excluye del seguimiento de Git los archivos temporales, entornos virtuales y registros generados durante la ejecución. |
| `README.md` | Presenta la descripción, organización, funcionamiento y documentación general del proyecto. |

Durante la ejecución, el sistema genera el archivo `software_fj.log`, en el que se almacenan los eventos y errores registrados. Este archivo está excluido del seguimiento de Git.

## 5. Distribución de responsabilidades

El proyecto fue desarrollado por cuatro integrantes, con responsabilidades organizadas de la siguiente manera.

### Elvis Albeiro Carrascal García — Entidades y gestión de clientes

- Desarrollo de la clase abstracta `Entidad`.
- Implementación de la clase `Cliente`.
- Validación de datos y aplicación del encapsulamiento.
- Implementación de operaciones de registro, consulta, actualización y eliminación de clientes.
- Integración de excepciones para el control de datos incorrectos.

### Robert Tony Chamorro Rivero — Gestión de servicios

- Desarrollo de la clase abstracta `Servicio`.
- Implementación de las clases `ServicioSala`, `AlquilerEquipo` y `AsesoriaEspecializada`.
- Validación de parámetros y cálculo de costos.
- Aplicación de herencia, polimorfismo y parámetros opcionales.
- Integración del manejo de excepciones relacionadas con los servicios.

### Alejandra Paola Pacheco Cervantes — Gestión de reservas e integración del programa principal

- Desarrollo de la clase `Reserva`.
- Implementación de operaciones para crear, consultar, confirmar, cancelar y procesar reservas.
- Relación entre clientes, servicios y reservas.
- Validación de estados y control de operaciones incorrectas.
- Ejecución de pruebas de integración y verificación de registros de errores.

### Andrés Felipe Menco Baldovino — Excepciones y registros

- Desarrollo de la jerarquía de excepciones personalizadas.
- Implementación de excepciones específicas para clientes, servicios, reservas y validaciones.
- Configuración del sistema de registros mediante `logging`.
- Implementación de funciones para registrar eventos informativos, advertencias, errores y depuración.
- Corrección y verificación de las pruebas del módulo de excepciones.

La integración general fue compartida con los integrantes del grupo para recibir observaciones y aprobación antes de su publicación.

## 6. Tecnologías utilizadas

- **Python:** lenguaje utilizado para implementar la lógica del sistema.
- **Visual Studio Code:** entorno de desarrollo y ejecución.
- **Git:** control de versiones y seguimiento de modificaciones.
- **GitHub:** repositorio remoto y plataforma de colaboración.
- **Logging:** módulo estándar de Python utilizado para registrar eventos y errores.

No se requiere una base de datos ni la instalación de bibliotecas externas para las funcionalidades descritas.

## 7. Organización del trabajo colaborativo

El equipo utilizó GitHub para organizar el desarrollo mediante Issues, ramas individuales, commits y Pull Requests.

Cada integrante trabajó en los módulos correspondientes a sus responsabilidades. Los cambios se incorporaron a la rama principal `main` mediante Pull Requests, conservando el historial de contribuciones.

Entre las actividades desarrolladas se encuentran:

- Implementación de entidades y clientes.
- Desarrollo de servicios especializados.
- Implementación de la gestión de reservas.
- Creación y corrección de excepciones personalizadas.
- Configuración de registros de eventos y errores.
- Integración de los módulos en `main.py`.
- Ejecución de diez operaciones simuladas.
- Configuración de `.gitignore` para excluir los archivos de registro.

El Issue #5, denominado **Integración y pruebas**, corresponde a la verificación conjunta del funcionamiento del sistema.

El historial de ramas, commits y Pull Requests permite consultar las contribuciones realizadas por los integrantes.

## 8. Almacenamiento de información

El sistema utiliza objetos y listas en memoria para gestionar la información de clientes, servicios y reservas.

No emplea bases de datos ni almacenamiento persistente para los registros de clientes y reservas.

Los eventos y errores de ejecución se almacenan en el archivo `software_fj.log`, generado mediante el módulo `logging` de Python.

## 9. Ejecución del programa

### Requisitos previos

- Tener Python instalado.
- Disponer de los archivos del proyecto en una misma carpeta.
- Abrir una terminal en el directorio principal del repositorio.

### Instrucciones

**1. Clonar el repositorio:**

```bash
git clone https://github.com/alepachecocervantes-ops/Software_FJ_Fase4.git
```

**2. Ingresar a la carpeta del proyecto:**

```bash
cd Software_FJ_Fase4
```

**3. Ejecutar el programa principal:**

```bash
python main.py
```

En Windows, también puede utilizarse:

```powershell
py main.py
```

El programa ejecuta automáticamente las diez operaciones simuladas y muestra sus resultados en la terminal.

Los eventos y errores generados se registran en `software_fj.log`.

## 10. Simulación de operaciones

El archivo `main.py` integra las funcionalidades de los módulos y ejecuta diez operaciones para verificar el comportamiento del sistema.

### Operaciones válidas

| N.º | Operación | Resultado esperado |
|---|---|---|
| 1 | Registrar un cliente | El cliente se registra correctamente. |
| 2 | Consultar un cliente | Se recupera la información del cliente registrado. |
| 3 | Crear un servicio de sala | El servicio se crea con sus características. |
| 4 | Crear un servicio de alquiler de equipos | El servicio se crea correctamente. |
| 5 | Crear una reserva | La reserva queda en estado pendiente. |
| 6 | Confirmar una reserva | La reserva cambia a estado confirmado. |
| 7 | Procesar una reserva | Se procesa la reserva y se calcula el costo correspondiente. |

### Operaciones inválidas

| N.º | Operación | Resultado esperado |
|---|---|---|
| 8 | Registrar un cliente con nombre vacío | Se controla el error de validación del nombre. |
| 9 | Crear un servicio con precio negativo | Se rechaza el precio inválido mediante una excepción. |
| 10 | Procesar una reserva cancelada | Se controla el error relacionado con el estado de la reserva. |

Estas operaciones permiten comprobar tanto el funcionamiento normal del sistema como su capacidad para identificar y controlar situaciones incorrectas.

## 11. Manejo de excepciones y registros

El sistema utiliza excepciones personalizadas para representar errores relacionados con las diferentes funcionalidades.

El archivo `excepciones.py` centraliza las familias de excepciones correspondientes a clientes, servicios, reservas y validaciones.

Las operaciones implementan mecanismos de manejo de errores para evitar que situaciones incorrectas interrumpan inesperadamente la simulación.

Además, se utiliza el módulo `logging` para almacenar información sobre las operaciones realizadas.

Los registros incluyen diferentes niveles:

- `INFO`: operaciones y eventos ejecutados correctamente.
- `WARNING`: advertencias relevantes durante la ejecución.
- `ERROR`: errores detectados y controlados.
- `DEBUG`: información adicional para tareas de depuración, según la configuración del registro.

El archivo `software_fj.log` se genera localmente y no se incluye en el seguimiento de Git, evitando modificaciones innecesarias en el repositorio cada vez que se ejecutan las pruebas.

## 12. Pruebas de funcionamiento

Se realizaron pruebas locales del programa principal utilizando las versiones actualizadas de los módulos de clientes, servicios, reservas y excepciones.

La ejecución de `py main.py` permitió comprobar:

- Siete operaciones válidas completadas correctamente.
- Tres operaciones inválidas detectadas y controladas.
- Integración funcional entre los módulos utilizados en las simulaciones.
- Cálculo del costo de una reserva procesada.
- Registro de los resultados de las operaciones en `software_fj.log`.

En la prueba de procesamiento de reserva se obtuvo un costo total de **$100.000**, correspondiente al servicio de sala utilizado durante dos horas.

También se verificó que los errores de nombre vacío, precio negativo y procesamiento de una reserva cancelada quedaran registrados con nivel `ERROR`.

Estas pruebas permiten evidenciar el funcionamiento de las diez simulaciones requeridas para la actividad.

## 13. Estado del proyecto

**Estado: módulos desarrollados e integración principal probada localmente.**

El sistema cuenta con los módulos de entidades, clientes, servicios, reservas y excepciones, además del programa principal encargado de ejecutar las diez operaciones.

Las pruebas locales realizadas permitieron comprobar el funcionamiento de las simulaciones y el registro de los errores previstos.

El desarrollo colaborativo y sus actualizaciones pueden consultarse en el historial del repositorio.
