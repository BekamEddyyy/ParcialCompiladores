# Compiladores - Analizador Sintáctico

## Descripción del Proyecto
Este repositorio contiene todos los archivos de código fuente necesarios para implementar un analizador sintáctico para un lenguaje de programación diseñado como parte del curso de Compiladores en la Universidad La Salle. El objetivo principal es desarrollar un analizador que pueda construir un árbol sintáctico y generar visualizaciones del mismo utilizando Graphviz o Three.js.

## Motivación
El lenguaje fue diseñado para demostrar comprensión en la construcción de compiladores, especialmente en la parte del análisis sintáctico. Este analizador utiliza el método LL1 para el análisis, asegurando que la gramática del lenguaje esté bien definida, no sea ambigua y esté correctamente factorizada por la izquierda.

## Especificaciones
- **Entrada:** Archivo de texto con código fuente en el lenguaje diseñado.
- **Salida:** Árbol sintáctico representado en memoria y como un archivo de texto visualizable.

## Componentes del Repositorio
- `parser.py`: Implementa el analizador sintáctico.
- `lexer.py`: Contiene el analizador léxico que genera tokens a partir del código fuente.
- `gramatica.txt`: Define la gramática del lenguaje.
- `README.md`: Este archivo, que proporciona una visión general del proyecto.

## Cómo Usar
Para ejecutar el analizador sintáctico:
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. Ejecuta `python parser.py` en la terminal, asegurándote de que el archivo de código fuente esté en el directorio correcto.

## Visualización
Para visualizar el árbol sintáctico generado:
- Utiliza Graphviz para abrir el archivo de salida generado por `parser.py`.
- O visualiza el árbol utilizando Three.js si prefieres una representación en 3D.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el analizador o sugerir cambios en la gramática, por favor haz un fork del repositorio y envía un pull request con tus modificaciones.

## Licencia
Este proyecto está bajo una licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autores
- Bekam Eddy Marc Huaracha Cabrera

