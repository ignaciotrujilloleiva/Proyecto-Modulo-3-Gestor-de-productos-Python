# Gestor de Productos por Consola (Python) 🐍

## 📌 Descripción del sistema

Este proyecto corresponde a un **Sistema de Gestión de Productos por consola**, desarrollado en Python como parte del Módulo 3 del bootcamp. El sistema permite administrar productos utilizando estructuras de datos nativas de Python y una arquitectura modular.

El sistema fue desarrollado bajo los requerimientos técnicos de una empresa de tecnología. No obstante, el diseño se centró en la creación de un gestor de productos versátil y genérico. Gracias a esta arquitectura modular, el programa posee una alta capacidad de adaptación a diversos rubros comerciales con mínimos ajustes en su configuración.

El programa se ejecuta desde la terminal y ofrece un menú interactivo que permite al usuario agregar, listar, buscar y eliminar productos.

La arquitectura del proyecto se construyó de manera progresiva, utilizando la rúbrica del proyecto como hoja de ruta. Este proceso permitió validar cada módulo de código en sintonía con las solicitudes de las lecciones, garantizando una cobertura total de los requerimientos funcionales y una estructura lógica coherente.

---

## 🧠 Estructuras de datos utilizadas

### 📋 Listas

* Se utiliza una lista de diccionarios **productos = []** para almacenar los productos del sistema.
* Cada elemento de la lista representa un producto con sus atributos.

### 📦 Diccionarios

* Cada producto se representa como un diccionario con las siguientes claves:

  * `id`
  * `nombre`
  * `precio`
  * `stock`
  * `categoria`

* Se utilizan métodos como:

  * `.get()` para acceder de forma segura a los datos
  * `.keys()` y `.values()` para acceder y utilizar los datos de los diccionarios

### 🧾 Sets

* Se utiliza un set **ids_registrados = set()** para almacenar los IDs registrados y evitar duplicados al agregar productos.

### 🔒 Tuplas

* Se utiliza una tupla **categorias = ()** para definir las categorías disponibles del sistema.

---

## ⚙️ Funcionalidades implementadas

* ➕ Agregar productos
* 📄 Listar productos
* 🔍 Buscar productos por ID
* ❌ Eliminar productos
* 📑 Menú interactivo por consola
* ✅ Validaciones de entrada de datos

---

## 🗂️ Estructura del proyecto

```
Proyecto-Modulo-3-Gestor-de-productos-Python/
│
├── main.py
├── README.md
├── modulos/
│   ├── __init__.py
│   ├── menu.py
│   ├── gestion_datos.py
│   ├── datos_basicos.py
│   ├── validaciones.py
│   └── funciones_utiles.py
├── entregables/
│   ├── documentacion_tecnica.md
│   ├── informe_validacion.md
│   │    └── Incluye video demostrativo
│   └── imagenes/
│        └── imagenes utilizadas en el informe
└── .gitignore

```

---

## ▶️ Ejecución del proyecto

python main.py

El proyecto debe ejecutarse desde main.py, cuenta con una verificación que asegura que **main( )** solo se ejecute si ese archivo es el punto de entrada

## 🛠️ Tecnologías utilizadas

* Python 3
* Programación estructurada
* Control de flujo
* Estructuras de datos nativas
* Git y GitHub

---

## 🧪 Validaciones y control de errores

El sistema incorpora validaciones para asegurar la correcta ejecución del programa y evitar errores comunes:
* Validación de entradas numéricas mediante funciones dedicadas.
* Verificación de IDs duplicados utilizando un set.
* Mensajes claros cuando un producto no existe o la lista está vacía.
Estas validaciones mejoran la experiencia del usuario y la estabilidad del sistema.

---

## 🧩 Decisiones de diseño

* Se utilizó una lista de diccionarios para facilitar el recorrido y manipulación de los productos.
* Se empleó un set para garantizar la unicidad de los identificadores de productos.
* La separación en módulos permite mantener el código ordenado, reutilizable y fácil de mantener.
* Los métodos .get(), .keys() y .values() se utilizaron para acceder a la información de forma segura. .get() evita errores si una clave no existe, mientras que .keys() y .values() permiten procesar los datos de forma dinámica, facilitando que el sistema sea adaptable a cualquier rubro. 
* La generación de IDs utiliza un contador independiente del estado de la lista, evitando reutilización de identificadores eliminados y garantizando consistencia.

## 📌 Observaciones

El proyecto fue desarrollado siguiendo buenas prácticas de programación en Python, priorizando la legibilidad del código, la modularidad y el cumplimiento de los requisitos establecidos en la consigna del módulo.

Este sistema puede ampliarse fácilmente incorporando persistencia de datos, más validaciones o nuevas funcionalidades.
