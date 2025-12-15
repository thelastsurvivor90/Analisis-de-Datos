# 🚀 Guía Rápida de Inicio

> Comienza en 5 minutos con el análisis de probabilidad

---

## ⚡ Inicio Rápido (5 minutos)

### 1️⃣ Instalar Python (si no lo tienes)

**Windows:**
```bash
# Descargar desde: https://www.python.org/downloads/
# Asegúrate de marcar "Add Python to PATH"
```

**macOS:**
```bash
brew install python3
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### 2️⃣ Descargar el Proyecto

```bash
# Opción A: Con Git
git clone https://github.com/tu-usuario/bank-marketing-probability.git
cd bank-marketing-probability

# Opción B: Descarga directa
# Descarga el ZIP desde GitHub y descomprime
cd bank-marketing-probability-main
```

### 3️⃣ Instalar Dependencias

```bash
# Instalar librerías necesarias
pip install pandas numpy matplotlib seaborn scipy

# O usar el archivo de requisitos
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el Análisis

```bash
python analisis_probabilidad.py
```

**¡Listo!** El análisis se ejecutará y generará:
- ✅ Gráficos en `analisis_probabilidad_completo.png`
- ✅ Resultados en `resultados_probabilidad.csv`
- ✅ Estadísticas en la consola

---

## 📊 Ejemplo de Salida

```
======================================================================
ANÁLISIS DE PROBABILIDAD - BANK MARKETING DATASET
======================================================================

[1] CARGANDO Y PREPARANDO DATOS...
Dataset cargado: 4521 registros
Variables: ['age_group', 'y', 'age']

[2] ANÁLISIS DESCRIPTIVO
Edad - Media: 40.9 años
Edad - Mediana: 38.0 años

[3] CÁLCULOS DE PROBABILIDAD

[3.1] PROBABILIDAD MARGINAL
P(Suscripción = Sí) = 521/4521
                    = 0.115208
                    = 11.52%

[3.2] PROBABILIDADES CONDICIONALES: P(Suscripción | Edad)
Jóvenes (18-35):
  P(Sí | young) = 180/1200 = 0.150000 (15.00%)

[3.4] TEOREMA DE BAYES: P(Edad | Suscripción)
P(Jóvenes | Suscripción) = 34.54%
P(Edad Media | Suscripción) = 53.75%
P(Mayores | Suscripción) = 11.71%

...
```

---

## 📄 Compilar el Informe LaTeX

### Opción 1: Overleaf (Más Fácil) ⭐

1. Ir a https://www.overleaf.com
2. Crear cuenta gratuita
3. Nuevo proyecto → Blank Project
4. Copiar contenido de `informe.tex`
5. Click en "Recompile"
6. Descargar PDF

**Tiempo:** 3 minutos

### Opción 2: Local

```bash
# Instalar LaTeX primero
# Windows: https://miktex.org/download
# Mac: brew install --cask mactex
# Linux: sudo apt-get install texlive-full

# Compilar
cd latex/
pdflatex informe.tex
pdflatex informe.tex
```

**Tiempo:** 10 minutos (incluyendo instalación)

---

## 🎥 Crear el Video

### Método Simple (Recomendado)

1. **Preparar diapositivas** (PowerPoint/Google Slides)
   - Usar el guión en `video/guion_video.md`
   - 15-17 diapositivas
   - Incluir gráficos generados

2. **Grabar con Zoom** (gratis)
   - Iniciar reunión solo contigo
   - Compartir pantalla con las diapositivas
   - Click en "Grabar"
   - Narrar siguiendo el guión
   - Detener y guardar

3. **Editar (opcional)**
   - Cortar errores
   - Añadir intro/outro
   - Usar software gratuito: DaVinci Resolve

**Tiempo:** 1-2 horas

---

## ✅ Checklist de Entrega

Antes de entregar, verifica que tienes:

### Archivos Obligatorios
- [ ] `analisis_probabilidad.py` - Código Python
- [ ] `informe.pdf` - Documento LaTeX compilado
- [ ] `video_analisis.mp4` - Video de 6-10 minutos
- [ ] `README.md` - Este archivo

### Archivos Generados
- [ ] `analisis_probabilidad_completo.png` - Gráficos
- [ ] `resultados_probabilidad.csv` - Tabla de resultados

### Contenido Verificado
- [ ] Probabilidad marginal calculada ✓
- [ ] Probabilidades condicionales calculadas ✓
- [ ] Teorema de Bayes aplicado ✓
- [ ] Test de independencia realizado ✓
- [ ] 5+ preguntas respondidas ✓
- [ ] Video dura 6-10 minutos ✓
- [ ] Informe tiene más de 10 páginas ✓

---

## 🆘 Solución Rápida de Problemas

### Problema: "ModuleNotFoundError: No module named 'pandas'"

**Solución:**
```bash
pip install pandas numpy matplotlib seaborn scipy
```

---

### Problema: LaTeX no compila

**Solución 1:** Usar Overleaf (online, más fácil)

**Solución 2:** Verificar errores comunes:
- Paréntesis/llaves sin cerrar
- Caracteres especiales: usar `\%`, `\$`, `\&`
- Verificar que todas las etiquetas `\begin{}` tengan su `\end{}`

---

### Problema: Video muy largo (>10 min)

**Solución:**
- Hablar más rápido (sin perder claridad)
- Eliminar ejemplos redundantes
- Ir directo a los cálculos importantes
- Reducir intro y cierre a 30 segundos cada uno

---

### Problema: No tengo dataset

**Solución:**
El código Python ya incluye datos simulados realistas. Puedes ejecutarlo sin descargar nada.

Para dataset real:
```bash
python download_dataset.py
```

O descarga manual: https://archive.ics.uci.edu/dataset/222/bank+marketing

---

## 💡 Tips para Destacar

### En el Código
```python
# ✅ BUENO: Código comentado y claro
prob_subscribe = subscribed / total_clients  # P(S) = n(S) / n(Ω)
print(f"P(Suscripción) = {prob_subscribe:.4f}")

# ❌ MALO: Sin explicación
p = s / t
print(p)
```

### En el Informe
- ✅ Usar fórmulas matemáticas en LaTeX
- ✅ Incluir gráficos de alta calidad
- ✅ Interpretar cada resultado
- ❌ Solo poner números sin explicación

### En el Video
- ✅ Hablar claro y pausado
- ✅ Mostrar ejemplos paso a paso
- ✅ Usar puntero/resaltador en pantalla
- ❌ Ir muy rápido o sin pausas

---

## 📚 Recursos de Apoyo

### Si necesitas ayuda con...

**Python:**
- Tutorial oficial: https://docs.python.org/3/tutorial/
- Real Python: https://realpython.com/

**Probabilidad:**
- Khan Academy (español): https://es.khanacademy.org/math/statistics-probability
- 3Blue1Brown: https://www.youtube.com/c/3blue1brown

**LaTeX:**
- Overleaf Tutorial: https://www.overleaf.com/learn
- LaTeX Wikibook: https://en.wikibooks.org/wiki/LaTeX

**Video:**
- OBS Studio Tutorial: https://obsproject.com/wiki/
- DaVinci Resolve: https://www.blackmagicdesign.com/products/davinciresolve/training

---

## ⏱️ Tiempo Estimado por Tarea

| Tarea | Tiempo Estimado |
|-------|----------------|
| Instalar software | 15-30 min |
| Ejecutar análisis Python | 5 min |
| Entender resultados | 30 min |
| Compilar LaTeX | 10 min |
| Crear diapositivas | 1-2 horas |
| Grabar video | 1 hora |
| Editar video | 30 min - 1 hora |
| **TOTAL** | **4-6 horas** |

---

## 🎯 Plan de Trabajo Sugerido

### Día 1 (2 horas)
- Instalar software y dependencias
- Ejecutar análisis Python
- Revisar resultados
- Entender conceptos de probabilidad

### Día 2 (2 horas)
- Compilar informe LaTeX
- Hacer ajustes al código si es necesario
- Crear diapositivas para video

### Día 3 (2 horas)
- Practicar guión del video
- Grabar video
- Editar video
- Verificar todo antes de entregar

---

## 📞 Ayuda Adicional

¿Tienes dudas? Opciones:

1. **Revisa la documentación completa:** `docs/guia_completa.md`
2. **Lee el README:** `README.md`
3. **Consulta ejemplos:** Código en `src/`
4. **Busca en el guión:** `video/guion_video.md`

---

## ✨ ¡Listo para Empezar!

```bash
# Ejecuta estos comandos en orden:

# 1. Instalar dependencias
pip install pandas numpy matplotlib seaborn scipy

# 2. Ejecutar análisis
python analisis_probabilidad.py

# 3. Ver resultados
# - Abre: analisis_probabilidad_completo.png
# - Abre: resultados_probabilidad.csv
```

**¡Éxito con tu proyecto!** 🎉

---

<div align="center">

**[⬅️ Volver al README](README.md)**

</div>
