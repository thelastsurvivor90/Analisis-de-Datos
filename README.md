# Analisis-de-Datos
Deyvi Samuel Barrera
# 📊 Análisis de Probabilidad - Bank Marketing Dataset

> Proyecto de análisis estadístico aplicando conceptos de probabilidad y el Teorema de Bayes a datos reales de campañas de marketing bancario.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-Document-green.svg)](https://www.latex-project.org/)
[![Dataset](https://img.shields.io/badge/Dataset-UCI%20ML-orange.svg)](https://archive.ics.uci.edu/dataset/222/bank+marketing)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📑 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Metodología](#-metodología)
- [Resultados](#-resultados)
- [Video Explicativo](#-video-explicativo)
- [Documentación](#-documentación)
- [Contribuir](#-contribuir)
- [Créditos](#-créditos)
- [Licencia](#-licencia)

---

## 🎯 Descripción

Este proyecto realiza un análisis exhaustivo del **Bank Marketing Dataset** del repositorio UCI Machine Learning, aplicando conceptos fundamentales de probabilidad para responder preguntas de negocio relacionadas con campañas de marketing telefónico bancario.

### Objetivos del Proyecto

1. ✅ Analizar un dataset abierto aplicando probabilidad
2. ✅ Calcular probabilidades marginales, condicionales y conjuntas
3. ✅ Aplicar el Teorema de Bayes para inferencia estadística
4. ✅ Generar un informe académico en LaTeX
5. ✅ Crear un video explicativo del análisis (6-10 minutos)

### Dataset

- **Fuente:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing)
- **Tema:** Campañas de marketing telefónico de un banco portugués
- **Registros:** 4,521 clientes contactados
- **Objetivo:** Predecir si el cliente suscribirá un depósito a plazo fijo
- **Variables:** Edad, trabajo, estado civil, educación, saldo, contacto previo, resultado

---

## ✨ Características

### Análisis Probabilístico Completo

- 📈 **Probabilidad Marginal:** Tasa base de suscripción
- 🎲 **Probabilidad Condicional:** Tasas por grupo demográfico
- 🔄 **Teorema de Bayes:** Inferencia inversa de probabilidades
- 🔗 **Independencia Estadística:** Test Chi-cuadrado
- 🎯 **Probabilidad Conjunta:** Eventos simultáneos

### Visualizaciones Profesionales

- Gráficos de barras y circulares
- Tablas de contingencia
- Comparaciones visuales
- Esquemas de fórmulas matemáticas

### Informe Académico

- Documento LaTeX completo y profesional
- Marco teórico de probabilidad
- Metodología detallada
- Resultados con interpretación
- Referencias bibliográficas

### Material Educativo

- Código Python bien documentado
- Guión para video explicativo
- Presentación de diapositivas
- Ejemplos paso a paso

---

## 🔧 Requisitos

### Software Necesario

- **Python 3.8 o superior**
- **LaTeX** (para compilar el informe)
  - [MiKTeX](https://miktex.org/) (Windows)
  - [MacTeX](https://tug.org/mactex/) (macOS)
  - TeX Live (Linux)
- **Editor de código** (VS Code, PyCharm, Jupyter)
- **Software de video** (OBS Studio, Camtasia) - opcional

### Librerías Python

```txt
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
```

---

## 📥 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/bank-marketing-probability.git
cd bank-marketing-probability
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Descargar el Dataset

**Opción A - Manual:**
1. Visitar: https://archive.ics.uci.edu/dataset/222/bank+marketing
2. Descargar `bank-additional-full.csv`
3. Colocar en la carpeta `data/`

**Opción B - Script automático:**
```bash
python download_dataset.py
```

---

## 🚀 Uso

### Ejecutar Análisis Completo

```bash
python analisis_probabilidad.py
```

**Salida generada:**
- `analisis_probabilidad_completo.png` - Visualizaciones
- `resultados_probabilidad.csv` - Tabla de resultados
- Estadísticas en consola

### Compilar Informe LaTeX

**Opción 1 - Overleaf (Recomendado para principiantes):**
1. Ir a [Overleaf.com](https://www.overleaf.com)
2. Crear nuevo proyecto
3. Copiar contenido de `informe.tex`
4. Compilar y descargar PDF

**Opción 2 - Local:**
```bash
cd latex/
pdflatex informe.tex
pdflatex informe.tex  # Segunda vez para referencias
```

**Salida:** `informe.pdf`

### Visualización Interactiva

```bash
python app_interactive.py
```

Abre `http://localhost:8050` en tu navegador

---

## 📁 Estructura del Proyecto

```
bank-marketing-probability/
│
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias Python
├── LICENSE                            # Licencia del proyecto
│
├── data/                              # Datos
│   ├── bank-additional-full.csv      # Dataset principal
│   └── data_description.txt          # Descripción de variables
│
├── src/                               # Código fuente
│   ├── analisis_probabilidad.py      # Análisis principal
│   ├── download_dataset.py           # Descarga automática
│   ├── visualizaciones.py            # Funciones de gráficos
│   └── utils.py                      # Utilidades
│
├── latex/                             # Documentos LaTeX
│   ├── informe.tex                   # Informe principal
│   └── referencias.bib               # Bibliografía
│
├── output/                            # Resultados generados
│   ├── analisis_probabilidad_completo.png
│   ├── resultados_probabilidad.csv
│   └── informe.pdf
│
├── video/                             # Material para video
│   ├── guion_video.md                # Script completo
│   ├── presentacion.pptx             # Diapositivas
│   └── notas_produccion.txt          # Notas técnicas
│
└── docs/                              # Documentación adicional
    ├── guia_completa.md              # Guía detallada
    ├── tutorial_latex.md             # Tutorial LaTeX
    └── conceptos_probabilidad.md     # Teoría de probabilidad
```

---

## 🔬 Metodología

### 1. Preparación de Datos

- Carga del dataset desde UCI ML Repository
- Limpieza y validación de datos
- Creación de grupos de edad (jóvenes, edad media, mayores)
- Análisis exploratorio inicial

### 2. Cálculos de Probabilidad

#### Probabilidad Marginal
```
P(Suscripción) = Suscripciones / Total Clientes
```

#### Probabilidad Condicional
```
P(Suscripción | Edad) = P(S ∩ E) / P(E)
```

#### Teorema de Bayes
```
P(Edad | Suscripción) = [P(S | E) × P(E)] / P(S)
```

#### Test de Independencia
```
H₀: P(S|E) = P(S) para toda E
Test: Chi-cuadrado (χ²)
```

### 3. Análisis e Interpretación

- Comparación de tasas de conversión por segmento
- Identificación de patrones y tendencias
- Aplicación del Teorema de Bayes para actualizar creencias
- Recomendaciones de negocio basadas en datos

---

## 📊 Resultados

### Hallazgos Principales

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| **Tasa de Conversión General** | 11.52% | Aprox. 1 de cada 9 clientes suscribe |
| **Mejor Segmento** | Jóvenes (18-35) | 15.00% - 30% sobre promedio |
| **Mayor Volumen** | Edad Media (36-55) | 53.75% de todas las suscripciones |
| **Menor Conversión** | Mayores (56+) | 7.43% - 35% bajo promedio |
| **Independencia** | NO independientes | χ² test: p < 0.001 |

### Preguntas Respondidas

1. ✅ **¿Cuál es la probabilidad marginal de suscripción?**
   - Respuesta: 11.52%

2. ✅ **¿Qué grupo de edad tiene mayor tasa de conversión?**
   - Respuesta: Jóvenes (15.00%)

3. ✅ **¿Cuál es la composición por edad de los suscriptores? (Bayes)**
   - Jóvenes: 34.54%
   - Edad Media: 53.75%
   - Mayores: 11.71%

4. ✅ **¿Son independientes la edad y la suscripción?**
   - Respuesta: NO (p < 0.001)

5. ✅ **¿Cuál es la probabilidad conjunta de ser joven Y suscribir?**
   - Respuesta: 3.98%

### Visualizaciones Generadas

![Análisis de Probabilidad](output/analisis_probabilidad_completo.png)

*Gráficos de distribución, probabilidades condicionales y aplicación del Teorema de Bayes*

---

## 🎥 Video Explicativo

### Información del Video

- **Duración:** 8-10 minutos
- **Contenido:**
  - Introducción al dataset (1 min)
  - Conceptos de probabilidad (2 min)
  - Análisis y cálculos (4 min)
  - Teorema de Bayes (2 min)
  - Conclusiones (1 min)

### Estructura del Video

1. **Introducción** - Presentación del problema y dataset
2. **Análisis Exploratorio** - Distribución de datos
3. **Probabilidades Básicas** - Marginal y condicional
4. **Teorema de Bayes** - Aplicación paso a paso
5. **Conclusiones** - Insights y recomendaciones

### Recursos

- 📄 Guión completo: `video/guion_video.md`
- 📊 Presentación: `video/presentacion.pptx`
- 🎬 Notas de producción: `video/notas_produccion.txt`

**Ver video:** [Enlace al video en YouTube](#) *(próximamente)*

---

## 📚 Documentación

### Informe LaTeX

El informe completo incluye:

- **Resumen ejecutivo**
- **Introducción y objetivos**
- **Marco teórico de probabilidad**
- **Metodología detallada**
- **Resultados con tablas y gráficos**
- **Interpretación y discusión**
- **Conclusiones y recomendaciones**
- **Referencias bibliográficas**

📄 **Descargar:** [informe.pdf](output/informe.pdf)

### Conceptos de Probabilidad Cubiertos

- ✅ Espacio muestral y eventos
- ✅ Probabilidad marginal
- ✅ Probabilidad condicional
- ✅ Teorema de la probabilidad total
- ✅ Teorema de Bayes
- ✅ Independencia estadística
- ✅ Probabilidad conjunta
- ✅ Regla de la multiplicación

### Tutoriales Adicionales

- [Guía completa del proyecto](docs/guia_completa.md)
- [Tutorial de LaTeX](docs/tutorial_latex.md)
- [Conceptos de probabilidad](docs/conceptos_probabilidad.md)

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Ideas para Contribuciones

- 🔍 Análisis de variables adicionales (ocupación, educación)
- 📊 Visualizaciones más avanzadas
- 🤖 Modelos predictivos de machine learning
- 🌐 Aplicación web interactiva
- 📱 Dashboard con Streamlit o Dash
- 📖 Traducciones a otros idiomas

---

## 👥 Créditos

### Dataset

- **Autores:** S. Moro, P. Cortez, P. Rita
- **Publicación:** "A Data-Driven Approach to Predict the Success of Bank Telemarketing" (2014)
- **Fuente:** UCI Machine Learning Repository
- **Licencia:** Creative Commons Attribution 4.0

### Referencias

1. Moro, S., Cortez, P., & Rita, P. (2014). A data-driven approach to predict the success of bank telemarketing. *Decision Support Systems*, 62, 22-31.

2. Ross, S. (2014). *A First Course in Probability* (9th ed.). Pearson Education.

3. Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer.

4. UCI Machine Learning Repository: https://archive.ics.uci.edu/

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

```
MIT License

Copyright (c) 2024 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contacto

**Autor:** [Tu Nombre]
- 📧 Email: tu.email@ejemplo.com
- 🐙 GitHub: [@tu-usuario](https://github.com/tu-usuario)
- 💼 LinkedIn: [Tu Perfil](https://linkedin.com/in/tu-perfil)

---

## 🙏 Agradecimientos

- UCI Machine Learning Repository por proporcionar el dataset
- Comunidad de Python y LaTeX por las herramientas
- Profesores y compañeros por su apoyo

---

## 🎓 Uso Académico

Este proyecto fue desarrollado como parte de un curso de Probabilidad y Estadística. Está diseñado para propósitos educativos y puede ser utilizado como:

- ✅ Material de estudio para conceptos de probabilidad
- ✅ Ejemplo de análisis de datos reales
- ✅ Plantilla para proyectos similares
- ✅ Referencia para aplicar el Teorema de Bayes

**Nota:** Si utilizas este proyecto como referencia, por favor cita apropiadamente.

---

## ⭐ Si este proyecto te fue útil...

- Dale ⭐ al repositorio
- Compártelo con tus compañeros
- Déjanos tu feedback
- Contribuye con mejoras

---

## 🔄 Actualizaciones

### Versión 1.0.0 (Diciembre 2024)
- ✅ Análisis probabilístico completo
- ✅ Informe LaTeX profesional
- ✅ Guión de video detallado
- ✅ Código Python documentado
- ✅ Visualizaciones de alta calidad

### Próximas Funcionalidades
- [ ] Dashboard interactivo con Streamlit
- [ ] Análisis de más variables
- [ ] Modelos predictivos avanzados
- [ ] API REST para consultas
- [ ] Versión en inglés

---

## 📈 Estadísticas del Proyecto

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/bank-marketing-probability?style=social)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/bank-marketing-probability?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/tu-usuario/bank-marketing-probability?style=social)

---

<div align="center">

**¡Gracias por usar este proyecto!** 🎉

Si tienes preguntas o sugerencias, no dudes en abrir un [Issue](https://github.com/tu-usuario/bank-marketing-probability/issues) o [Pull Request](https://github.com/tu-usuario/bank-marketing-probability/pulls).

---

Hecho con ❤️ y ☕ por [Deyvi Samuel]

[⬆️ Volver arriba](#-análisis-de-probabilidad---bank-marketing-dataset)

</div>
