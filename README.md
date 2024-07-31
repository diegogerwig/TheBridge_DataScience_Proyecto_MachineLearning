# TheBridge_DataScience_Proyecto_MachineLearning

## Proyecto Machine Learning
Para el módulo del bootcamp de Data Science tendrás que desarrollar un modelo de machine learning. Este proyecto tiene como objetivo principal practicar y demostrar competencias adquiridas durante el curso para aplicarlos en un proyecto práctico de aprendizaje automático.

* **Miembros**: El proyecto es individual
* **Datos**: datasets de plataformas (Kaggle, INE,..), Apis o Webscrapping un tema que te interese. El volumen de datos no puede ser inferior a **1000 registros x 10 campos**.
* **Entregas**: 
    *  **Semana del 26 de Agosto** Se presentará a la clase el tema de tu proyecto (máx 3 mins) indicando dónde se encuentra el proyecto (Github). Presentación final del proyecto (ppt,...) orientado a negocio (máx 10 mins) con puntos clave a exponer:
        * Naturaleza del proyecto
        * Análisis de datos realizado
        * Aspectos clave del negocio a resolver
        * Modelo(s) empleados y análisis
        * Potencial final del proyecto (aumentar un x% las ventas...)


## Entregable
El objetivo de este proyecto es desarrollar un modelo de machine learning, desde la obtención de datos hasta su despligue.

La entrega será un **repositorio de github** con el desarrollo del proyecto: adquisición de datos, limpieza, EDA, feature engineering, modelado de datos, iteración de modelos, evaluación de modelos, interpretación de modelos, impacto en negocio.
Habrá que aplicar conocimientos aprendidos hasta ahora, tenéis la oportunidad de **demostrar vuestra evolución y el trabajo realizado en durante el espacio de tiempo del que dispones**. No queremos datasets básicos ni trabajos hechos en una tarde.


```
|-- nombre_proyecto_final_ML
    |-- data
    |   |-- raw
    |        |-- dataset.csv
    |        |-- ...
    |   |-- processed
    |   |-- train
    |   |-- test
    |
    |-- notebooks
    |   |-- 01_Fuentes.ipynb
    |   |-- 02_LimpiezaEDA.ipynb
    |   |-- 03_Entrenamiento_Evaluacion.ipynb
    |   |-- ...
    |
    |-- src
    |   |-- data_processing.py
    |   |-- training.py
    |   |-- evaluation.py
    |   |-- ...
    |
    |-- models
    |   |-- trained_model.pkl
    |   |-- model_config.yaml
    |   |-- ...
    |
    |-- app
    |   |-- app.py
    |   |-- requirements.txt
    |   |-- ...
    |
    |-- docs
    |   |-- negocio.ppt
    |   |-- ds.ppt
    |   |-- memoria.md
    |   |-- ...
    |
    |
    |-- README.md    
```


A continuación se detallan las carpetas y los requisitos de cada una:

1. **data**: se almacenarán los datos utilizados en el proyecto. Se deben crear las siguientes subcarpetas:
   - `raw`: Contiene los datos en su formato original, sin procesar.
   - `processed`: Almacena los datos procesados después de realizar las transformaciones necesarias antes de utilizarlos para el modelo.
   - `train`: Contiene los datos de entrenamiento utilizados para entrenar el modelo a partir de los datos procesados
   - `test`: Almacena los datos de prueba utilizados para evaluar el modelo a partir de los datos procesados

2. **notebooks**: se encuentran los archivos Jupyter Notebook que contienen el desarrollo del proyecto. Se deben nombrar y numerar adecuadamente según el orden de ejecución.
   - `01_Fuentes.ipynb`: adquisición de datos y unión de las diferentes fuentes.
   - `02_LimpiezaEDA.ipynb`: transformaciones y limpiezas, incluyendo el feature engineering, así como visualizaciones dentro de un análisis exploratiorio.
   - `03_Entrenamiento_Evaluacion.ipynb`: entrenamiento de modelos (mínimo 5 modelos supervisados diferentes y al menos 1 no supervisado) junto con su hiperparametrización, así como evaluación de los modelos (métricas de evaluación, interpretación de variables,...).
3. **src**: contiene los archivos fuente de Python que implementan las funcionalidades clave del proyecto. Los requisitos de los archivos son los siguientes:
   - `data_processing.py`: código para procesar los datos de la carpeta `data/raw` y guardar los datos procesados en la carpeta `data/processed`.
   - `training.py`: código para entrenar y guardar el modelo entrenado con el input de los datos de la carpeta `data/processed` y guardar los datasets de `data/train` y `data/test` utilizados en el entrenamiento.
   - `evaluation.py`: código para evaluar el modelo utilizando los datos de prueba de la carpeta `data/test` y generar métricas de evaluación.

4. **models**: se almacenarán los archivos relacionados con el modelo entrenado. Los requisitos son los siguientes:
   - `trained_model_n.pkl`: modelos entrenados y guardados en formato pickle, siendo n un identificador para cada modelo.
   - `final_model.pkl`: modelo final guardado en formato pickle.
   - `model_config.yaml`: archivo con la configuración del modelo final (parámetros)

5. **app**: contendrá los archivos necesarios para el despliegue del modelo en Streamlit u otra plataforma similar. Los requisitos son los siguientes:

   - `app.py`: código para la aplicación web que utiliza el modelo entrenado final(Streamlit).
   - `requirements.txt`: especifica las dependencias del proyecto para poder ejecutar la aplicación.

      **NOTA**: Este espacio podrá quedar en blanco a la espera de ver en detalle este material en clase.

5. **docs**: contendrá la documentación adicional relacionada con el proyecto, como las dos presentaciones u otros documentos relevantes como la memoria.

6. **README**: portada de tu proyecto.



## Presentación DS

Para el público técnico (otros equipos de data science):

1. **Contextualización Técnica**: Comienza explicando el contexto del problema y las técnicas de ML utilizadas de manera concisa. Qué problema bamos a resolver, incluir detalles sobre el conjunto de datos, la selección de características y la arquitectura del modelo.

2. **Enfoque en la Metodología**: Destaca el proceso de desarrollo del modelo, desde la limpieza de datos hasta la evaluación del rendimiento. Detalla cualquier técnica, algoritmos o enfoques utilizados durante el proceso.

3. **Resultados y Métricas de Evaluación**: Presenta los resultados obtenidos y cómo se comparan con los objetivos iniciales. Enfatiza las métricas de rendimiento utilizadas y proporciona análisis sobre la robustez y la generalización del modelo, así como las variables más importantes.

4. **Discusión sobre Limitaciones y Mejoras**: Sé transparente sobre las limitaciones del modelo y las áreas donde se pueden realizar mejoras. Esto muestra una comprensión crítica y madura del proceso de modelado y abre oportunidades para la discusión técnica.

5. **Demostraciones Prácticas**: Si es posible, realiza demostraciones prácticas del modelo en acción, mostrando cómo se puede utilizar en situaciones reales.

Prepárate para dar respuesta en la presentación a preguntas técnicas detalladas sobre el modelo, el proceso de desarrollo y las decisiones tomadas durante el proyecto. Algunos ejemplos podrían ser:


* ¿Cuáles fueron los principales desafíos que enfrentaron durante la etapa de preprocesamiento de datos y cómo los abordaron?
* ¿Qué consideraciones tuvieron en cuenta para la selección del algoritmo de aprendizaje automático y por qué creen que fue la elección óptima para este problema en particular?
* ¿Podrían proporcionar más detalles sobre los hiperparámetros seleccionados para el modelo y cómo fueron ajustados?
* ¿Qué enfoque de validación cruzada utilizaron para evaluar el rendimiento del modelo y por qué lo consideraron adecuado para este problema específico?
* ¿Cuáles fueron las métricas de evaluación utilizadas y por qué eligieron esas métricas en particular para evaluar el rendimiento del modelo?
* ¿Cómo abordaron el desequilibrio de clases en el conjunto de datos y qué estrategias de muestreo o técnicas de ajuste utilizaron?
* ¿Podrían explicar cómo interpretan las características más importantes o relevantes para el modelo y cómo influyeron en las decisiones de diseño?
* ¿Qué métodos de regularización consideraron y cómo determinaron cuál era más adecuado para evitar el sobreajuste del modelo?
* ¿Cómo gestionaron los datos faltantes en el conjunto de datos y qué impacto tuvo esta imputación en el rendimiento del modelo?
* ¿Hubo algún problema de multicolinealidad entre las características y cómo lo abordaron?



## Presentación negocio

1. **Contextualización del Problema**: Comienza estableciendo el contexto del problema de manera clara y sencilla, evitando términos técnicos complejos. Utiliza ejemplos y analogías comprensibles para ilustrar la importancia del problema.

2. **Explicación del Valor del Modelo**: Destaca cómo el modelo de ML aborda el problema y el valor que aporta al negocio. Enfatiza cómo puede ayudar a mejorar la eficiencia, reducir costos o aumentar los ingresos.

3. **Beneficios y Aplicaciones Prácticas**: Describe los beneficios tangibles del modelo en términos de casos de uso prácticos. Ejemplifica cómo puede ser implementado en la toma de decisiones diarias o en la optimización de procesos.

4. **Visualización de Resultados**: Utiliza gráficos, tablas u otras visualizaciones intuitivas para comunicar los resultados del modelo de manera efectiva. Evita el uso de jerga técnica y enfócate en destacar las conclusiones clave de manera clara y accesible.

Prepárate para dar respuesta en la presentación a preguntas sobre el impacto del modelo en el negocio, la escalabilidad, la implementación práctica y los costos asociados. Algunos ejemplos podrían ser:

* ¿Cómo se alinea este modelo de ML con los objetivos estratégicos de la empresa?
* ¿Cuáles son los costos asociados con la implementación y mantenimiento de este modelo, y cómo se comparan con los beneficios esperados?
* ¿Qué tan escalable es este modelo y cómo se puede adaptar para abordar futuras necesidades comerciales?
* ¿Cuáles son los posibles riesgos o desafíos en la implementación de este modelo y cómo planean mitigarlos?
* ¿Qué datos adicionales podrían ser útiles para mejorar la precisión o el valor comercial del modelo?
* ¿Cómo planean integrar este modelo en los procesos de toma de decisiones existentes dentro de la empresa?
* ¿Cuál es la expectativa de retorno de la inversión (ROI) asociada con la implementación de este modelo?
* ¿Cómo garantizan la transparencia y la explicabilidad del modelo para los stakeholders y reguladores?
* ¿Qué implicaciones éticas o sociales consideraron al desarrollar este modelo y cómo planean abordarlas?
* ¿Qué métricas de éxito empresarial están utilizando para evaluar el rendimiento y el impacto de este modelo a largo plazo?


## Pasos del proyecto
1. ¿Podemos dar solución a un problema con datos? Elige un tema.
1. Busca y consigue los datos. Vuelta al anterior punto si nos quedamos sin ideas.
1. Define tu problema de Machine Learning: clasificación/regresión, supervisado/ no supervisado, series temporales, imágenes, texto...
1. Exploratorio: obtén todos los estadísticos y gráficos que necesites para entender bien tu dataset.
1. Limpia los datos: duplicados, missings, outliers, columnas inútiles...
1. Feature engineering: transformación y creación de nuevas variables.
1. Prueba varios modelos. Itero tanto en nuevos conjuntos de datos, corrijo overfitting,
1. Analiza los resultados mediante una métrica adecuada a tu problemática.
1. Interpreta los resultados y comprende los outputs del modelo.
1. Siguientes pasos. ¿Se podría seguir enriqueciendo el modelo con otras pruebas o con otros datos?