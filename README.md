# ETL Pipeline con Apache Spark en Google Colab

## 📌 Descripción del Proyecto
Este proyecto implementa un **ETL (Extract, Transform, Load) Pipeline** utilizando **Apache Spark** en **Google Colab**. Su objetivo es procesar datos de reservas hoteleras y generar insights clave mediante transformaciones y análisis exploratorio de datos (EDA).

## 🚀 Tecnologías Utilizadas
- **Apache Spark** (PySpark)
- **Google Colab**
- **Python** (pandas, matplotlib)
- **Google Drive** (para almacenamiento de archivos)

## ⚙️ Requerimientos Técnicos
### 📌 Hardware Necesario
- Procesador: Mínimo **Intel Core i5** o equivalente
- Memoria RAM: **8GB** (recomendado 16GB o más)
- Espacio en Disco: **Al menos 10GB** libres

### 📌 Instalaciones Preliminares
- **Google Colab** (se ejecuta en la nube, no requiere instalación local)
- **Google Drive** (para almacenamiento de archivos de entrada/salida)
- **Apache Spark** (instalación dentro de Colab, se incluye en el código)

### 📌 Dependencias
Las siguientes librerías deben instalarse en el entorno de ejecución:
```bash
!apt-get update
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz
!tar xf spark-3.5.4-bin-hadoop3.tgz
!pip install -q findspark
```

## 📂 Estructura del Proyecto
```
Proyecto_Booking_Raul_AlvaroProleon/
├── input/                         # Archivos de entrada
│   ├── hotel_bookings.csv         # Dataset de reservas hoteleras
├── output/                        # Archivos de salida
│   ├── tabla_bkg_reservas.csv     # Reservas y cancelaciones por mes y año
│   ├── tabla_bkg_dias_espera.csv  # Promedio de días de espera y huéspedes
│   ├── tabla_bkg_tarifa.csv       # Tarifas diarias promedio por habitación
├── etl_pipeline.py                # Código principal del ETL
├── README.md                      # Documentación del proyecto
```

## 📥 Extracción de Datos
La extracción se realiza desde un archivo CSV almacenado en **Google Drive**. Se usa PySpark para cargar los datos:
```python
def f_extraccion(path):
    df_hotel = spark.read.csv(path, header=True, inferSchema=True)
    print(f'Columnas: {len(df_hotel.columns)}, Registros: {df_hotel.count()}')
    return df_hotel
```

## 🔍 Análisis Exploratorio de Datos (EDA)
Se incluyen:
- Medidas de tendencia central (`df.describe()`)
- Estructura del DataFrame (`df.printSchema()`)
- Análisis de valores nulos y duplicados
- Detección de outliers con diagramas de caja (Boxplot)

## 🔄 Transformación de Datos
Las principales transformaciones incluyen:
- Conversión de tipos de datos (`IntegerType`, `DateType`)
- Tratamiento de valores nulos
- Creación de nuevas variables (`total_huespedes`, `arrival_date_month_esp`)
- Conversión de nombres de meses a español

Ejemplo de conversión de tipos de datos:
```python
def f_casting_df(df, num_cols, fecha_cols):
    for column in num_cols:
        df = df.withColumn(column, F.col(column).cast(IntegerType()))
    for column in fecha_cols:
        df = df.withColumn(column, to_date(df[column], 'dd-MM-yy'))
    return df
```

## 📤 Carga de Datos
Los datos transformados se guardan en archivos CSV dentro del directorio **output/**.
```python
def f_carga(df, output_path):
    df.write.mode("overwrite").option('header', 'true').csv(output_path)
```

## 🔄 Diagrama del Proceso ETL
A continuación, se presenta un esquema visual del proceso ETL implementado:

```
    +------------+       +----------------+       +---------------+
    | Extracción | ----> | Transformación | ----> | Carga (CSV)   |
    +------------+       +----------------+       +---------------+
          |                     |                        |
    Fuente de Datos       Limpieza de Datos       Almacenamiento en CSV
   (hotel_bookings.csv)   Creación de Features
```

## 🏁 Ejecución del Pipeline ETL
Para ejecutar el pipeline, sigue estos pasos en Google Colab:
1. **Montar Google Drive**:
```python
from google.colab import drive
drive.mount('/content/drive')
```
2. **Instalar dependencias** (si aún no están instaladas):
```python
!apt-get update
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz
!tar xf spark-3.5.4-bin-hadoop3.tgz
!pip install -q findspark
```
3. **Ejecutar el script principal**:
```python
main()
```

## 📌 Autor
**Raúl Alvaro Proleon**  
Master en Big Data & Business Intelligence  

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.

## 📢 Conclusión
Este proyecto demuestra la efectividad de **Apache Spark** en el procesamiento de grandes volúmenes de datos mediante un pipeline **ETL** optimizado. Se logró extraer, transformar y cargar datos de reservas hoteleras, proporcionando información valiosa para la toma de decisiones. Gracias a la capacidad de procesamiento distribuido de Spark, el flujo de trabajo es escalable y eficiente. Este enfoque puede adaptarse para distintos dominios de análisis de datos en **Big Data**.

