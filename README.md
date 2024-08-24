![](./img/traffic_crash.png)

# TRAFFIC ACCIDENTS ANALISYS

## ENUNCIADO

[TheBridge ENUNCIADO del proyecto](./enunciado.md)

### Naturaleza del proyecto

Este proyecto se centra en el análisis de los datos de accidentes de tráfico. La principal finalidad es analizar las diferentes varibles de cada accidente y realizar un model que prediga la lesividad. El proyecto involucra la recolección, limpieza, y análisis de datos para proporcionar el pronóstico de heridos, de cara a poder tomar acciones que reduzcan la gravedad de las lesiones.

### Análisis de datos realizado

En esta sección, se detallan los pasos y técnicas utilizadas para el análisis de datos:

* Recolección de Datos: La fuente de datos ha sido [KAGGLE](https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents/data).
* Limpieza y Preprocesamiento: Se ha procedido a la limpieza del dataset mediante la eliminación de valoress nulos, eliminación de duplicados y normalización.
* Análisis Exploratorio: Se ha realzaido el análisis exploratorio, incluyendo la visualización de datos, la identificación de patrones iniciales, y la generación de estadísticas descriptivas.
* Análisis Avanzado: Se ha aplicado técnicas de análisis avanzadas, como análisis de correlación.

### Aspectos clave del negocio a resolver

Los resultados del análisis ayudarán a optimizar las medidas disuasorias y de control de trafico, realzaicón de inversiones en la mejora del paruqe de vehículos o de la infraestructura, realzaición de medidas de conciación dirigidas a los diferentes colectivos (edad, nivel cultural, etc)

### Modelo(s) empleados y análisis

Se han empleado los siguinetes modelos para el análisis:

* LogisticRegression
* DecisionTreeClassifier
* KNeighborsClassifier
* RandomForestClassifier

### Potencial final del proyecto

El potencial final del proyecto es la utilidad de lso resultados para la toma de decsiones por parte de las Autoridades de trafico para la mejora de la seguridad vial.

![](./img/vision_zero.jpg)


## REQUIREMENTS

python 3.10.11

* numpy>=1.23.2
* pandas==2.2.2
* ydata-profiling==4.8.3
* scikit-learn==1.5.1
* imbalanced-learn==0.12.3
* matplotlib==3.8.4
* seaborn==0.13.2
* ipywidgets==8.1.3

## AUTHOR

[Diego Gerwig](https://github.com/diegogerwig)

## LICENSE 

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
