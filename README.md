<div align="center">

# 🎲 Estadística y Probabilidades

**Fundamentos de probabilidad e inferencia estadística para la toma de decisiones en Ingeniería Industrial**

Material docente del curso *Estadística y Probabilidades* — Departamento de Ingeniería Industrial, Universidad de Santiago de Chile (USACH).

[![License: CC0 1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)
[![R](https://img.shields.io/badge/An%C3%A1lisis-R-276DC3.svg?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Datos-Python-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Universidad](https://img.shields.io/badge/USACH-Ingenier%C3%ADa%20Industrial-004b8d.svg)](https://www.usach.cl/)
![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen.svg)

</div>

---

## 📌 Descripción

Este repositorio reúne el material del curso **Estadística y Probabilidades** para estudiantes de Ingeniería Industrial. El curso desarrolla pensamiento probabilístico y criterio estadístico para comprender fenómenos aleatorios, modelar variabilidad, interpretar datos y fundamentar decisiones en contextos industriales.

> **Objetivo general.** Desarrollar herramientas fundamentales de probabilidad y estadística para modelar incertidumbre, analizar variabilidad y apoyar decisiones cuantitativas en contextos de Ingeniería Industrial.

El material combina **diapositivas**, **ejercicios de clase**, **11 guías de 50 ejercicios cada una**, **solucionarios** y **conjuntos de datos sintéticos**. Las actividades computacionales pueden desarrollarse en **R o Python**, y cada base incluye un generador en Python con semilla fija.

Los ejemplos abordan logística, manufactura, mantenimiento, control de calidad, atención de clientes y evaluación de mejoras de procesos.

---

## 🗂️ Temario

| Unidad | Contenidos principales | Guía de ejercicios |
|---|---|---|
| 1. **Bienvenida al curso** | Propósito, planificación, evaluación y metodología de trabajo | Presentación en las diapositivas |
| 2. **Conceptos básicos de probabilidad** | Espacio muestral, eventos, reglas de probabilidad, conteo, probabilidad condicional e independencia | [Sesión 1](Ejercicios/Propuestos/Enunciados/Sesion_1.pdf) |
| 3. **Bayes, variables aleatorias y distribuciones** | Teorema de Bayes, pruebas diagnósticas, variables discretas y continuas, funciones de masa, densidad y distribución acumulada | [Sesión 2](Ejercicios/Propuestos/Enunciados/Sesion_2.pdf) |
| 4. **Esperanza, varianza y desviación estándar** | Centro y dispersión, propiedades de la esperanza y la varianza, coeficiente de variación y decisiones bajo riesgo | [Sesión 3](Ejercicios/Propuestos/Enunciados/Sesion_3.pdf) |
| 5. **Modelos probabilísticos discretos** | Bernoulli, binomial, geométrica, Pascal, hipergeométrica y Poisson | [Sesión 4](Ejercicios/Propuestos/Enunciados/Sesion_4.pdf) |
| 6. **Modelos probabilísticos continuos** | Uniforme, exponencial y normal; estandarización, percentiles y cumplimiento de especificaciones | [Sesión 5](Ejercicios/Propuestos/Enunciados/Sesion_5.pdf) |
| 7. **Conceptos básicos de estadística** | Población, muestra, parámetros, estadísticos, medidas muestrales y tipos de estimación | [Sesión 6](Ejercicios/Propuestos/Enunciados/Sesion_6.pdf) |
| 8. **Propiedades de estimadores y Teorema Central del Límite** | Sesgo, varianza, error cuadrático medio, consistencia, eficiencia, suficiencia, distribución muestral y error estándar | [Sesión 7](Ejercicios/Propuestos/Enunciados/Sesion_7.pdf) |
| 9. **Intervalos de confianza e introducción a hipótesis** | Estimación por intervalo, margen de error, hipótesis, errores tipo I y II y valor-p | [Sesión 8](Ejercicios/Propuestos/Enunciados/Sesion_8.pdf) |
| 10. **Pruebas de hipótesis paramétricas** | Pruebas Z y t, inferencia para medias y proporciones y comparación de poblaciones independientes | [Sesión 9](Ejercicios/Propuestos/Enunciados/Sesion_9.pdf) |
| 11. **Pruebas para muestras pareadas** | Diferencias antes-después, prueba t pareada, intervalos de confianza y magnitud del cambio | [Sesión 10](Ejercicios/Propuestos/Enunciados/Sesion_10.pdf) |
| 12. **Bondad de ajuste, independencia y homogeneidad** | Pruebas chi-cuadrado, frecuencias observadas y esperadas, tamaño de efecto y análisis de residuos | [Sesión 11](Ejercicios/Propuestos/Enunciados/Sesion_11.pdf) |

Las diapositivas completas del curso están en [`Slides.pdf`](Slides.pdf).

**Correspondencia de numeración:** las sesiones de ejercicios 1 a 11 corresponden a las unidades 2 a 12; la unidad 1 presenta el curso.

---

## 📁 Estructura del repositorio

| Ruta | Contenido |
|---|---|
| [`Slides.pdf`](Slides.pdf) | Diapositivas completas del curso |
| [`Ejercicios/Clase/`](Ejercicios/Clase/) | Ejercicios trabajados en clase: `Sesion_1.pdf` a `Sesion_11.pdf` |
| [`Ejercicios/Propuestos/Enunciados/`](Ejercicios/Propuestos/Enunciados/) | 11 guías de estudio, con 50 ejercicios por guía |
| [`Ejercicios/Propuestos/Soluciones/`](Ejercicios/Propuestos/Soluciones/) | Solucionarios correspondientes a las 11 guías |
| [`Ejercicios/Datos/`](Ejercicios/Datos/) | Datos organizados en carpetas `Sesion_1/` a `Sesion_11/` |
| `Ejercicios/Datos/Sesion_N/generar_datos.py` | Generador de datos de la sesión correspondiente |
| `Ejercicios/Datos/Sesion_N/diccionario.csv` | Descripción y tipo de cada variable |
| [`LICENSE`](LICENSE) | Texto de CC0 1.0 Universal |

Cada carpeta de datos incluye la base en **CSV y Excel**, su **diccionario de variables** y el **script de generación**. El mismo número de sesión permite relacionar los ejercicios de clase, el enunciado, el solucionario y los datos.

---

## 🧪 Conjuntos de datos

Los datos son **sintéticos** y representan situaciones de Ingeniería Industrial. Se distribuyen en [`Ejercicios/Datos/`](Ejercicios/Datos/):

| Sesión | Contexto del caso | Base de datos CSV |
|---|---|---|
| 1 | Despacho de pedidos: atrasos, daños, rutas e inspección | [`pedidos_piloto.csv`](Ejercicios/Datos/Sesion_1/pedidos_piloto.csv) |
| 2 | Monitoreo de equipos, alarmas y demanda de repuestos | [`monitoreo_piloto.csv`](Ejercicios/Datos/Sesion_2/monitoreo_piloto.csv) |
| 3 | Fallas, tiempos de ciclo y costos de operación | [`operacion_piloto.csv`](Ejercicios/Datos/Sesion_3/operacion_piloto.csv) |
| 4 | Inspección de piezas y llamadas de soporte | [`control_piloto.csv`](Ejercicios/Datos/Sesion_4/control_piloto.csv) |
| 5 | Dimensiones, pesos, tiempos de reparación y llegadas | [`mediciones_piloto.csv`](Ejercicios/Datos/Sesion_5/mediciones_piloto.csv) |
| 6 | Tiempos de atención, gasto y satisfacción de clientes | [`atencion_piloto.csv`](Ejercicios/Datos/Sesion_6/atencion_piloto.csv) |
| 7 | Población de tiempos para estudiar muestreo y error estándar | [`poblacion_tiempos.csv`](Ejercicios/Datos/Sesion_7/poblacion_tiempos.csv) |
| 8 | Tiempos de armado, cumplimiento y errores de documentación | [`armado_piloto.csv`](Ejercicios/Datos/Sesion_8/armado_piloto.csv) |
| 9 | Comparación de proveedores: tiempos de entrega y defectos | [`proveedores_piloto.csv`](Ejercicios/Datos/Sesion_9/proveedores_piloto.csv) |
| 10 | Evaluación de una mejora mediante mediciones antes-después | [`mejora_piloto.csv`](Ejercicios/Datos/Sesion_10/mejora_piloto.csv) |
| 11 | Tipos y gravedad de defectos por turno y proveedor | [`defectos_piloto.csv`](Ejercicios/Datos/Sesion_11/defectos_piloto.csv) |

Cada CSV tiene una copia `.xlsx` con el mismo nombre en su carpeta. Los CSV utilizan **separador coma y punto decimal**; consulte `diccionario.csv` antes de analizar cada base.

> **Rutas de los datos.** Algunas guías utilizan rutas como `datos/S01/`. En este repositorio, esa carpeta corresponde a `Ejercicios/Datos/Sesion_1/`; la misma correspondencia se aplica hasta la sesión 11.

### Reproducibilidad

Cada sesión contiene un script `generar_datos.py` con su propia **semilla fija**, definida mediante `numpy.random.default_rng(...)`. Los scripts generan la base en CSV y Excel, escriben el diccionario de variables y muestran resúmenes o cálculos de referencia.

Para regenerar los datos de una sesión, ejecute desde la raíz del repositorio:

```bash
python3 -m pip install numpy pandas scipy openpyxl
python3 Ejercicios/Datos/Sesion_1/generar_datos.py
```

Cambie `Sesion_1` por la sesión que desee regenerar. Para reproducir un mismo entorno de trabajo, conserve también las versiones de Python y de las bibliotecas utilizadas.

> ⚠️ Los generadores **reescriben los archivos de datos y el diccionario de su sesión**. Guarde sus análisis y resultados en una carpeta separada.

---

## 🚀 Guía de uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/LuisRojo-Gonzalez/Introduction-to-Probabilities-and-Statistics.git
cd Introduction-to-Probabilities-and-Statistics
```

También puede descargar el contenido desde **Code → Download ZIP** en GitHub.

### 2. Requisitos

- **Visor de PDF** para consultar las diapositivas, guías y soluciones.
- **Calculadora** para los ejercicios de trabajo manual.
- **R o Python 3** para los desafíos con datos. R permite cargar los CSV con funciones base; en Python, los ejemplos utilizan `pandas`.
- **NumPy, pandas, SciPy y openpyxl** si desea ejecutar todos los generadores en Python.
- **Excel u otra hoja de cálculo compatible** para consultar las copias `.xlsx`, si lo prefiere.

Las bases ya están disponibles en el repositorio; regenerarlas es opcional.

### 3. Empezar un ejercicio

Consulte el enunciado de la sesión en [`Ejercicios/Propuestos/Enunciados/`](Ejercicios/Propuestos/Enunciados/) y su diccionario en `Ejercicios/Datos/Sesion_N/`.

Por ejemplo, para cargar los datos de la sesión 1 desde la raíz del repositorio:

```r
# R: lectura y exploración inicial
datos <- read.csv("Ejercicios/Datos/Sesion_1/pedidos_piloto.csv")
head(datos)
str(datos)
summary(datos)
```

```python
# Python: lectura y exploración inicial
import pandas as pd

datos = pd.read_csv("Ejercicios/Datos/Sesion_1/pedidos_piloto.csv")
print(datos.head())
datos.info()
print(datos.describe(include="all"))
```

Resuelva y justifique su respuesta antes de contrastarla con el archivo del mismo nombre en [`Ejercicios/Propuestos/Soluciones/`](Ejercicios/Propuestos/Soluciones/).

---

## 🎓 Ejercicios y casos integradores

El repositorio contiene **550 ejercicios propuestos**, organizados en **11 guías de 50 ejercicios**. Cada guía sigue la misma progresión:

| Nivel | Ejercicios | Cantidad por guía | Enfoque |
|---|---|---|---|
| **Introductorio** | 1–10 | 10 | Comprensión de conceptos y aplicación directa |
| **Medio** | 11–30 | 20 | Selección de herramientas e interpretación de resultados |
| **Avanzado** | 31–40 | 10 | Integración de conceptos, supuestos y decisiones |
| **Desafíos con datos** | 41–50 | 10 | Etapas de un caso integrador con análisis computacional |

Los ejercicios **1–40** se trabajan con papel, calculadora y el formulario incluido en cada guía. Los ejercicios **41–50** utilizan datos sintéticos y requieren documentar el procedimiento, los resultados y la decisión operacional mediante R o Python.

El trabajo debe conectar el cálculo con su interpretación: identificar la pregunta industrial, justificar el modelo o procedimiento, revisar sus supuestos y explicar qué decisión respalda la evidencia.

---

## 📈 Evaluación y registro de notas

Las ponderaciones descritas en las [diapositivas del curso](Slides.pdf) son:

| Evaluación | Ponderación |
|---|---|
| Control 1 | 15 % |
| PEP 1 | 35 % |
| Control 2 | 15 % |
| PEP 2 | 35 % |

$$
N_F = 0.15\,C_1 + 0.35\,P_1 + 0.15\,C_2 + 0.35\,P_2
$$

El nivel de exigencia es **60 %**. La **POR** permite recuperar una de las dos PEP mediante el reemplazo de su nota y mantiene las ponderaciones del curso.

Consulte la planificación en las diapositivas y las indicaciones del profesor para las fechas y condiciones de cada evaluación. El registro de calificaciones no forma parte de los archivos de este repositorio; consulte sus notas por el canal indicado en el curso.

---

## 📝 Licencia

El archivo [`LICENSE`](LICENSE) establece **[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)** para este repositorio.

Consulte ese archivo para conocer los términos completos de uso y distribución del material.

---

## 👤 Autor

**Luis Rojo-González, Ph.D.**  
Departamento de Ingeniería Industrial · Universidad de Santiago de Chile

---

<div align="center">
<sub>Material docente · Estadística y Probabilidades · USACH</sub>
</div>
