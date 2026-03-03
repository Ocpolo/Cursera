# Curso Python - Proyecto de Predicción de Lluvia

Este repositorio contiene ejercicios y un proyecto de análisis/predicción usando Python.

## Contenido

- `cursera.py`: script principal de ciencia de datos y machine learning.
- `FinalProject_AUSWeather.ipynb`: notebook del proyecto final.
- `hola-mundo.py`: script de ejemplo básico.

## Objetivo del proyecto

El script `cursera.py` trabaja con el dataset **weatherAUS** para predecir si lloverá (`RainToday`) a partir de variables meteorológicas.

Incluye:
- limpieza de datos (`dropna`),
- transformación de fecha a estación (`Season`),
- preprocesamiento con `ColumnTransformer`,
- entrenamiento y ajuste con `GridSearchCV`,
- comparación de modelos (`RandomForestClassifier` y `LogisticRegression`),
- evaluación con reporte de clasificación y matriz de confusión.

## Requisitos

Instala Python 3.10+ y las librerías necesarias:

```bash
pip install pandas matplotlib scikit-learn seaborn
```

## Ejecución

### 1) Script principal

```bash
python cursera.py
```

### 2) Script de prueba

```bash
python hola-mundo.py
```

### 3) Notebook

Abre `FinalProject_AUSWeather.ipynb` en VS Code o Jupyter y ejecuta las celdas.

## Importante: ruta del dataset

El script ahora busca el dataset primero en una ruta relativa del proyecto:

- `data/weatherAUS.csv`

Si no lo encuentra, usa como respaldo tu ruta local anterior.

Para que cualquier colaborador lo ejecute sin cambios, recomienda guardar el archivo en:

1. Crear carpeta `data` en la raíz del repositorio.
2. Copiar `weatherAUS.csv` dentro de `data`.

## Flujo básico con Git

Para guardar nuevos cambios:

```bash
git add .
git commit -m "Describe tus cambios"
git push
```

## Autor

- GitHub: [Ocpolo](https://github.com/Ocpolo)
- Correo: orcastrop@unadvirtual.edu.co
