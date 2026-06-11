from datetime import datetime, timedelta
import pandas as pd
import random
import os

# =====================================================
# ABSOLUTE PATH PROJECT
# =====================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

os.makedirs(DATA_FOLDER, exist_ok=True)

OUTPUT_FILE = os.path.join(DATA_FOLDER, "visitor_data.csv")

# =====================================================
# PARAMETER
# =====================================================

zones = [
    "FoodCourt",
    "FashionArea",
    "Cinema"
]

start_time = datetime(2025, 1, 1, 8, 0, 0)

records = []

# =====================================================
# GENERATE 180 MENIT DATA
# =====================================================

for minute in range(180):

    current_time = start_time + timedelta(minutes=minute)

    hour = current_time.hour

    for zone in zones:

        # pola pengunjung berdasarkan jam

        if hour < 10:
            visitor = random.randint(10, 120)

        elif hour < 12:
            visitor = random.randint(100, 250)

        elif hour < 14:
            visitor = random.randint(250, 500)

        else:
            visitor = random.randint(150, 350)

        records.append([
            current_time,
            zone,
            visitor
        ])

# =====================================================
# DATAFRAME
# =====================================================

df = pd.DataFrame(
    records,
    columns=[
        "timestamp",
        "zone",
        "visitor_count"
    ]
)

# =====================================================
# SAVE CSV
# =====================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("DATA BERHASIL DIBUAT")
print("Lokasi :", OUTPUT_FILE)
print("Jumlah Data :", len(df))
print("=" * 50)