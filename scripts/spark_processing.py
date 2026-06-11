from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    sum,
    hour,
    window,
    col
)
import os

# ==================================================
# ABSOLUTE PATH
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

INPUT_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "visitor_data.csv"
)

VISITOR_TOTAL_PATH = os.path.join(
    PROJECT_ROOT,
    "output",
    "visitor_total"
)

VISITOR_TIME_PATH = os.path.join(
    PROJECT_ROOT,
    "output",
    "visitor_time"
)

ML_VISITOR_PATH = os.path.join(
    PROJECT_ROOT,
    "output",
    "ml_visitor"
)

print("PROJECT_ROOT :", PROJECT_ROOT)
print("INPUT_FILE   :", INPUT_FILE)

# ==================================================
# SPARK SESSION
# ==================================================

spark = SparkSession.builder \
    .appName("SmartRetailVisitorPrediction") \
    .getOrCreate()

# ==================================================
# LOAD DATA
# ==================================================

df = spark.read.csv(
    INPUT_FILE,
    header=True,
    inferSchema=True
)

print("\nDATA AWAL")
df.show(5)

# ==================================================
# 1. TOTAL PENGUNJUNG TIAP ZONA
# ==================================================

visitor_total = df.groupBy("zone").agg(
    sum("visitor_count").alias("total_visitors")
)

print("\nTOTAL PENGUNJUNG")
visitor_total.show()

# ==================================================
# 2. TREN TIAP 15 MENIT
# ==================================================

visitor_time = df.groupBy(
    window("timestamp", "15 minutes")
).agg(
    sum("visitor_count").alias("total_visitors")
)

print("\nTREN 15 MENIT")
visitor_time.show()

# ==================================================
# 3. DATASET AI BERDASARKAN HOUR
# ==================================================

ml_dataset = df.withColumn(
    "hour",
    hour("timestamp")
)

ml_dataset = ml_dataset.select(
    "hour",
    "visitor_count"
)

print("\nDATASET ML")
ml_dataset.show()

# ==================================================
# SIMPAN PARQUET
# ==================================================

visitor_total.write \
    .mode("overwrite") \
    .parquet(VISITOR_TOTAL_PATH)

visitor_time.write \
    .mode("overwrite") \
    .parquet(VISITOR_TIME_PATH)

ml_dataset.write \
    .mode("overwrite") \
    .parquet(ML_VISITOR_PATH)

print("\nPARQUET BERHASIL DISIMPAN")

VISITOR_DETAIL_PATH = os.path.join(
    PROJECT_ROOT,
    "output",
    "visitor_detail"
)

df.write \
    .mode("overwrite") \
    .parquet(VISITOR_DETAIL_PATH)

spark.stop()