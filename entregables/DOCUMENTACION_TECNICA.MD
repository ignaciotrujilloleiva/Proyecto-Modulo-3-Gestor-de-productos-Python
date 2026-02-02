# 📦 Gestor de Productos en Python

## 📌 Descripción general

Este proyecto corresponde al desarrollo de un **Sistema de Gestión de Productos por consola**, implementado en Python, cuyo objetivo es permitir la administración básica de productos mediante un menú interactivo.

El sistema permite **agregar, listar, buscar y eliminar productos**, aplicando estructuras de datos fundamentales de Python y siguiendo una arquitectura modular para mejorar la organización y mantenibilidad del código.

El proyecto fue desarrollado como parte del **Módulo 3 – Python**, cumpliendo con todos los requisitos técnicos y funcionales establecidos en la consigna.

---

## 🎯 Objetivos del sistema

* Aplicar correctamente estructuras de datos como **listas, diccionarios, tuplas y sets**.
* Implementar funciones modulares y reutilizables.
* Validar datos de entrada para evitar errores de ejecución.
* Mantener una salida por consola clara y legible.
* Desarrollar un sistema escalable y fácil de extender.

---

## 🧱 Estructuras de datos utilizadas

### 🔹 Lista (`list`)

Se utiliza una lista para almacenar todos los productos del sistema.

```python
productos = []
```

Permite recorrer, agregar y eliminar productos de forma ordenada.

---

### 🔹 Diccionarios (`dict`)

Cada producto se representa como un diccionario con la siguiente estructura:

```python
{
  "id": int,
  "nombre": str,
  "precio": float,
  "stock": int,
  "categoria": str
}
```

Esto permite acceder a los datos de forma clara mediante claves.

---

### 🔹 Tuplas (`tuple`)

Se utilizan para representar datos inmutables como las categorías disponibles, para este proyecto se dejo de forma general para su posterior adaptación:

```python
categorias = ("cat1","cat2","cat3","cat4")
```
Ejemplo de utilidad

```python
categorias = ("Computación", "Perifericos", "Audio y Video", "Almacenamiento")
```

---

### 🔹 Sets (`set`)

Se emplean para evitar duplicados, especialmente en el control de IDs únicos:

```python
ids_registrados = set()
```

Garantiza que no existan productos con el mismo identificador.

---

## ⚙️ Funcionalidades implementadas

* ➕ **Agregar producto**: Permite ingresar un nuevo producto validando sus datos.
* 📋 **Listar productos**: Muestra todos los productos registrados.
* 🔍 **Buscar producto por ID**: Recupera y muestra la información de un producto específico.
* ✏️ **Actualizar producto**: Modifica los datos de un producto existente.
* 🗑️ **Eliminar producto**: Elimina un producto del sistema por su ID.
* 🚪 **Salir del sistema**: Finaliza la ejecución del programa.

---

## 🧩 Uso de métodos requeridos

Para cumplir con los requisitos del módulo, el proyecto utiliza explícitamente los siguientes métodos:

* `.append()` para agregar productos a la lista.
* `.remove()` para eliminar productos.
* `.get()` para acceder de forma segura a valores de diccionarios.
* `.keys()` y `.values()` para manipular y recorrer información interna de los productos.

Estos métodos se utilizan de forma controlada, evitando redundancias innecesarias en la salida por consola.

---

## 🛡️ Validaciones y control de errores

El sistema incorpora diversas validaciones:

* Verificación de entradas numéricas (ID, precio y stock).
* Prevención de IDs duplicados mediante un set.
* Mensajes informativos cuando no existen productos registrados.
* Control de búsquedas fallidas (producto no encontrado).

Estas validaciones aseguran un uso correcto del sistema y evitan fallos durante la ejecución.

---

## 🗂️ Estructura del proyecto

```text
Proyecto-Modulo-3-Gestor-de-productos-Python/
│
├── main.py                     # Archivo principal del sistema y punto de entrada del programa.
├── README.md                   # Guía técnica y documentación del repositorio.
├── modulos/                    # Directorio de los modulos del sistema.
│   ├── __init__.py             # Inicializador para el sistema de importaciones.
│   ├── menu.py                 # Encargada del menú principal del sistema y gestiona las opciones seleccionadas por el usuario.
│   ├── gestion_datos.py        # Encargada de las gestiones de datos en las funciones Agregar, Listar, Eliminar y Buscar.
│   ├── datos_basicos.py        # Encargada de solicitar al usuario y construir los datos básicos de un producto.
│   ├── validaciones.py         # Contiene funciones reutilizables para validarla entrada de datos del usuario.
│   ├── funciones_utiles.py     # Herramientas de formato y estética visual.
├── entregables/                # Archivos de respaldo y reportes del proyecto.
└── .gitignore                  # Archivos excluidos del control de versiones.
```

La separación en módulos permite un código más limpio, organizado y escalable.

---

## 🧠 Decisiones de diseño

* Se optó por una **arquitectura modular** para separar responsabilidades.
* Se priorizó la **legibilidad del código** sobre soluciones complejas.
* La salida por consola fue diseñada para ser clara y comprensible para el usuario.
* El sistema está preparado para futuras mejoras, como persistencia en archivos o bases de datos.

---

## 📌 Observaciones finales

Este proyecto demuestra la correcta aplicación de los conceptos fundamentales de Python vistos en el módulo, integrando estructuras de datos, validaciones y modularización.

El sistema cumple con todos los requisitos solicitados y puede ser fácilmente extendido o adaptado a nuevos contextos.

---

📅 **Estado del proyecto**: Completo
🐍 **Lenguaje**: Python 3