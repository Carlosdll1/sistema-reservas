#  Sistema de Gestión de Reservas - Software FJ

## 📌 Información del estudiante

| Campo | Información |
|-------|-------------|
| **Nombre del estudiante** | Carlos Daniel Pérez Urzola |
| **Programa** | Ingeniería Electrónica |
| **Curso** | Programación - Código: 213023 |
| **Universidad** | Universidad Nacional Abierta y a Distancia - UNAD |
| **Escuela** | ECBTI |
| **Tutor** | Yahith Yamid Gutierrez Gomez |
| **Fecha** | Mayo 2026 |

## 📌 Descripción del proyecto

Sistema orientado a objetos desarrollado en Python para la gestión de clientes, servicios y reservas de la empresa **Software FJ**.

##  Características implementadas

- ✅ **Programación Orientada a Objetos**: Abstracción, herencia, polimorfismo y encapsulación
- ✅ **Manejo robusto de excepciones**: Excepciones personalizadas y bloques try/except/else/finally
- ✅ **Logging de eventos**: Registro de todas las operaciones y errores en archivo `sistema.log`
- ✅ **Validaciones estrictas**: Datos de clientes, disponibilidad de servicios, estados de reservas
- ✅ **Sin base de datos**: Toda la gestión se realiza con objetos y listas en memoria

## 📁 Estructura del proyecto
sistema-reservas/
├── excepciones.py # Excepciones personalizadas
├── logger.py # Sistema de registro de eventos
├── cliente.py # Clase Cliente con validaciones
├── servicio.py # Clases abstractas y servicios específicos
├── reserva.py # Clase Reserva con estados y procesamiento
├── principal.py # Programa principal con simulación
└── sistema.log # Archivo de logs (se genera automáticamente)

text

##  Cómo ejecutar

```bash
python principal.py
📊 Ejemplo de salida
text
=== SISTEMA DE RESERVAS - SOFTWARE FJ ===

Cliente: Ana Gomez | ana@mail.com | 5551234
Capturado: El nombre no puede estar vacío
Costo sin descuento: 100
Costo con impuestos: 119.0
Error esperado: El servicio Sala A1 no está disponible
Costo con descuento: 270.0
Error esperado: La reserva ya está cancelada

=== FIN DE SIMULACIÓN ===
👨‍💻 Autor
Carlos Daniel Pérez Urzola
Estudiante de Ingeniería Electrónica - UNAD
Curso: Programación (Código: 213023)

👨‍🏫 Tutor
Yahith Yamid Gutierrez Gomez
Universidad Nacional Abierta y a Distancia - UNAD

📚 Referencias bibliográficas (APA)
Van Rossum, G., & Drake Jr, F. L. (2024). El tutorial de Python. Python Software Foundation. https://docs.python.org/es/3.12/tutorial/errors.html

Cuevas Álvarez, A. (2016). Python 3: curso práctico. RA-MA Editorial. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/106404

Fabrizio Romano, Benjamin Baka, & Dusty Phillips. (2019). Getting Started with Python: Understand Key Data Structures and Use Python in Object-oriented Programming. Packt Publishing.

Zambrano, J. P. (2025). Introducción al uso de GitHub. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75876

Silva, F. D. (2025). Basics of using GitHub. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75882

📌 Estado del proyecto
✅ Completado - Funcionalidad 100% implementada y probada
