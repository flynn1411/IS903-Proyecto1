# Proyecto de Compiladores

## Objetivo
- Elaborar un traductor básico que pueda recibir una entrada de cadenas y elaborar un análisis léxico y sintáctico para entregar una salida de acorde a una gramática elaborada.

## Indicaciones
- Recibir una entrada, ya sea a través de un txt o dentro del programa tener las cadenas, la última cadena debe reconocer el $ que ha llegado a su fin.
- Mostrar una salida que contenga un cuadro con el detalle del analizador léxico y sintáctico.

### Analizador Léxico:
  - Línea del token encontrado.
  - Tipo de token.
  - Valor o elemento de operación.
  - Otros que considere importante de mostrar.
  - Analizador Sintáctico:
  - Genera la salida de la operación.
  - Construir el árbol (esto es opcional y solo si logra mostrarlo de forma clara).

### Elaborar un informe final con los siguientes elementos:
  - Detalle de los tokens, patrones y lexemas elaborados para el
  proyecto.
 - Detalle de las reglas de producción y la gramática elaborada para el
  proyecto.
  - Detalle del nombre de las funciones (reglas semánticas) utilizadas
  para el proyecto.
  - Capturas del programa en ejecución.
  - Hoja de desempeño de los integrantes de grupo con él % de trabajo.
  - Bibliografía base utilizada.
  
- Fecha de presentación será el próximo sábado 13/08/2022.
- Se habilitará un link de subida del informe para ese sábado, no del código, porque será lo que va a explicar y mostrar en día de la presentación.
- El código debe estar disponible en un repositorio en línea. El enlace a este repositorio debe formar parte de su informe y el repositorio debe poder ser accedido de forma pública, o incluyendo al correo francisco.nunez.unah@gmail.com con permisos de lectura.
- La presentación será según el horario asignado y tendrá 25 minutos para explicarlo, en este día solo será entre el grupo y el docente la demostración.
- La(s) persona(s) que exponga(n) podrá(n) ser elegida(s) por el grupo, pero todos deben dar su punto de vista sobre el proyecto

# Proyecto Calculadora de Operaciones.
- Recibir cadenas que contengan operaciones numéricas y que la salida logre identificar el uso de números enteros, decimales, operadores (+,-,*,/), paréntesis (“()” y/o “[]”), además del resultado de la operación y de forma opción la construcción del árbol.
## Ejemplo:
  - Cadena: 5+3*(2+1)
  - Tokens: Numero entero: 5, Operador: +, Paréntesis: Si
  - Funciones: OperacionSuma: 2+1, OperacionMultiplicacion: 3*(E)
  - Resultado: 14
  - Recuerde que esto es un ejemplo de una línea del txt, el grupo tiene la libertar de trabajar con diferentes nombres y formas de identificar los elementos.
