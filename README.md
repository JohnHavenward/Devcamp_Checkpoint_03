# PREGUNTAS TEÓRICAS


### ¿Cuáles son los tipos de Datos en Python?

Los siguientes son los principales tipos de datos usados en python
Booleans: solo pueden tener el valor de True o False
Numbers: incluyen todo tipo de números como enteros, decimales, fracciones…
Strings: son cadenas de caracteres alfanuméricos y pueden ser cortas como frases o tan largas como textos
Bytes: un tipo de dato que suele usarse para representar imágenes
None: representa un valor nulo y sirve para especificar cuando un valor no ha sido asignado aún a la variable

Las siguientes son colecciones o estructuras de datos
Lists: una lista de elementos que pueden modificarse y quitar o añadir nuevos
Tuples: una agrupación de elementos que no puede modificarse
Sets: parecidos a las listas pero los elementos deben ser únicos y no pueden estar repetidos
Dictionaries: los diccionarios organizan los datos en pares de clave y valor
</br></br>


### ¿Qué tipo de convención de nomenclatura deberíamos utilizar para las variables en Python?

Debemos usar el formato llamado “snake_case” en el cual los espacios son sustituidos por guiones bajos y todas las letras deben estar en minúsculas incluidas las iniciales. El nombre solo puede contener caracteres alfanuméricos y guiones bajos. Además no debe empezar por un número y se tiene que tener cuidado con el uso de caracteres como la i mayúscula y la ele minúscula o la letra O y el cero que pueden resultar ambiguos.

A continuacón se muestran algunos ejemplos:

```python
mi_variable
suma_total
item_35
columna_4_fila_8
```
</br></br>

### ¿Qué es un Heredoc en Python?

Un Heredoc es una cadena de caracteres que ocupa múltiples líneas. Este bloque de texto debe abrir y cerrarse con tres comillas dobles tal y como se muestra a continuación:

```python
mi_heredoc = """
Esta es la primera línea.
Esta otra la segunda.
Y esta la tercera.
""".strip()
```

En el ejemplo mostrado tanto la primera como la última posición representan líneas vacías por lo que esta forma de declaración suele combinarse con la función strip() que elimina ambas líneas.

Como alternativa a un Heredoc podemos usar el carácter especial  \n  dentro de una cadena para añadir los saltos de línea y obtener una representación equivalente. Sin embargo resulta mucho menos intuitivo y práctico para bloques de textos muy largos por estar reducidos a una sola línea.

Por último cabe resaltar que debe evitarse el uso de tres comillas simples ya que estas se usan para definir comentarios de múltiples líneas.
</br></br>


### ¿Qué es una interpolación de cadenas?

Son necesarias dos partes para poder realizar una  interpolación de cadenas.
- Por un lado se define una cadena de caracteres con una serie de posiciones vacías con un número que las identifica.
- Por el otro tenemos una lista de variables que deben ocupar esas posiciones.

La interpolación es la combinación de ambas partes para generar una única cadena que muestre el valor de cada variable en la posición asignada dentro de la cadena inicial.

Podemos ver un ejemplo del empleo de la interpolación de cadenas a continuación:

```python
cadena_interpolada = “Nombre: {0} Color: {1} Talla: {2}”.format(product_name, product_color, product_size)
```

Esta forma de interpolar cadenas no resulta tan intuitiva ya que debemos enumerar cada posición y tener en cuenta el orden en el que escribimos las variables para poder controlar dónde se muestra cada una. Por ello hay un nueva forma en la versión más reciente de python que permite intercalar las variables directamente dentro de la cadena y resulta mucho más intuitiva.

A continuación se muestra un ejemplo:

```python
otra_cadena_interpolada = f"Nombre: {product_name} Color: {product_color} Talla: {product_size}"
```
</br></br>


### ¿Cuándo deberíamos usar comentarios en Python?

Los comentarios sirven para explicar el código a futuros desarrolladores que tengan que trabajar en él.
Sin embargo el uso de comentarios debe tratar de evitarse lo máximo posible empleando para ello nombres mas descriptivos que faciliten el entendimiento del código. Esto se debe a que los comentarios tienden a no ser actualizados cuando el código del programa es cambiado en futuras versiones haciendo que en vez de resultar de ayuda hagan más confuso el entender cómo funciona el programa.

Un caso adecuado para el uso de comentarios es para la organización del código. Al igual que el nombre del archivo describe su principal función, si cada parte dentro de este se acompaña de un comentario que describa la función principal de ese bloque de código nos facilita la navegación a través del programa y entender cómo está estructurado.

Otro uso muy útil es la definición de tareas pendientes durante el desarrollo del software, las cuales se suelen marcar por convenio con la palabra clave TODO ya que la mayoría de software de escritura de código tienen la capacidad de resaltarlas y llevar un seguimiento de estas.

También existen herramientas que generan comentarios de forma automática y se aseguran de que estos se mantengan actualizados en todo momento.
</br></br>


### ¿Cuáles son las diferencias entre aplicaciones monolíticas y de microservicios?

Las aplicaciones monolíticas son aquellas que se desarrollan como una gran aplicación que incluye todas las funciones en un solo módulo y usan un único sistema de archivos. Son más fáciles de desarrollar porque no necesitan una planificación previa y normalmente empiezan con una función básica a la que se van añadiendo todas las demás. Una de sus ventajas es la rapidez de funcionamiento al tratarse de un solo bloque; pero debido a ello tienen un peor mantenimiento ya que en caso de hacer cambios en una parte de la aplicación se pueden crear errores que pueden propagarse a través de todo el código sobre todo cuando se trabaja en equipo. Un fallo en una parte de la aplicación puede provocar que deje de funcionar y resulte en una mala experiencia de usuario.

Por otro lado, las aplicaciones de microservicios deben ser planificadas para su desarrollo debido a que la aplicación se estructura en varios módulos más pequeños que cumplen funciones más específicas y se comunican entre sí mediante APIs. Esta forma de desarrollo facilita el trabajo en equipo pudiendo asignar diferentes desarrolladores a cada módulo. Además se pueden incorporar nuevas funciones a la aplicación creando nuevos módulos o escalar los ya existentes de una forma controlada y evitando crear fallos en el funcionamiento de esta. En caso de fallo de un módulo el resto de la aplicación puede seguir funcionando y comunicar al usuario acerca problema.