# ETL - Pipeline de Booking con Apache Spark
# **Curso:** Master de Big Data & Business Intelligence
# **Asignatura:** Procesamiento de Datos Masivos
# **Alumno:** Raul Alvaro Proleon

## 1. Importing Libraries

import os
import findspark
from pyspark.sql import SparkSession   # crear la session de spark
from pyspark.sql import SQLContext     # utilizar las funciones de spark
from pyspark.sql.window import Window  # manipulacion de ventana
from pyspark.sql import functions as F # operaciones para un dataframe
from pyspark.sql.types import IntegerType # convertir datos
from pyspark.sql.types import DateType    # convertir datos
from pyspark.sql.functions import to_date # convertir datos
import matplotlib.pyplot as plt           # Mostrar graficos


# Iniciamos el entorno de Apache Spark
def init_spark():

    findspark.init()

    spark = SparkSession.builder.master("local[*]").getOrCreate()
    
    spark = SparkSession.builder.appName("Test_spark").master("local[*]").getOrCreate()
    sqlCtx = SQLContext(sparkContext=spark.sparkContext, sparkSession=spark)
    spark
    return spark