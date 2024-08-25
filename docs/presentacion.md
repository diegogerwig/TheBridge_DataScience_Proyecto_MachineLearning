<!-- Markdown con HTML para un encabezado fijo -->
<html>

  <head>
    <style>
      body {
        margin-top: 100px;
      }
      .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #333;
        color: white;
        padding: 10px 3px;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: column; 
      }
      .logos {
        display: flex;
        justify-content: space-between;
        width: 100%;
        max-width: 1000px; 
        padding: 0 30px; 
        box-sizing: border-box; 
      }
      .logo-left {
        height: 60px; 
      }
      .logo-right {
        height: 40px; 
      }
      .header-content {
        text-align: center;
        margin-top: 5px; 
      }
    </style>
  </head>

  <body>
    <div class="fixed-header">
      <div class="logos">
        <img src="../img/traffic_crash.png" alt="Imagen Izquierda" class="logo-left">
        <img src="../img/logo_theBridge.svg" alt="Imagen Derecha" class="logo-right">
      </div>
      <div class="header-content">
        <h1>TRAFFIC ACCIDENTS ANALYSIS</h1>
        <h4 style="white-space: pre;">Diego Gerwig      2024-SEP      Bilbao</h4>
      </div>
    </div>
  </body>

</html>

#
#
#
#
# 🎯 NATURALEZA DEL PROYECTO

Este proyecto se centra en el análisis de los datos de accidentes de tráfico. La principal finalidad es analizar las diferentes varibles de cada accidente y obtener un modelo que prediga la lesividad. El proyecto involucra la recolección, limpieza, y análisis de datos para proporcionar el pronóstico de heridos, de cara a poder tomar acciones que reduzcan la gravedad de las lesiones.

# 📊 ANALISIS DE DATOS

## Fuente de datos

La fuente de datos ha sido [KAGGLE](https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents/data).

Tamaño del dataset:
* Registros: 12316
* Columnas: 32 

Columnas con valores NULOS: 26

Máximo de valores nulos: 4427

Registros DUPLICADOS: 0

[Notebook -> 01_Fuentes](../notebooks/01_Fuentes.ipynb)

## Limpieza y procesamiento

Se ha procedido a la limpieza del dataset mediante la gestión/eliminación de valores nulos, label encoder de datos, obtención de dummies.




[Notebook -> 02_LimpiezaEDA](../notebooks/02_LimpiezaEDA.ipynb)

## Análisis exploratorio

Se ha realzaido el análisis exploratorio, incluyendo la visualización de datos, la identificación de patrones iniciales, y la generación de estadísticas descriptivas.

## Análisis Avanzado

Se ha aplicado técnicas de análisis avanzadas, como análisis de correlación.

# 🏆 ASPECTOS CLAVE

Los resultados del análisis ayudarán a optimizar las medidas disuasorias y de control de trafico, realzaicón de inversiones en la mejora del paruqe de vehículos o de la infraestructura, realzaición de medidas de conciación dirigidas a los diferentes colectivos (edad, nivel cultural, etc)

# 💫 MODELOS

Se han empleado los siguinetes modelos para el análisis:

* LogisticRegression
* DecisionTreeClassifier
* KNeighborsClassifier
* RandomForestClassifier

[Notebook -> 03_Entrenamiento_Evaluacion](../notebooks/03_Entrenamiento_Evaluacion.ipynb)

# 💥 POTENCIAL

El potencial final del proyecto es la utilidad de lso resultados para la toma de decsiones por parte de las Autoridades de trafico para la mejora de la seguridad vial.

![](../img/vision_zero.jpg)

# 🏁 CONCLUSIONES

* 
* 
