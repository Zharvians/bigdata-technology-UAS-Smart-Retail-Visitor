import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from datetime import datetime
import plotly.graph_objects as go
import os

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Smart Retail Visitor Prediction",
    page_icon="🛍️",
    layout="wide"
)

st.container()

st.markdown("""
<div style="
background:rgba(0,31,63,.7);
backdrop-filter:blur(15px);
padding:40px;
border-radius:30px;
border:1px solid rgba(0,255,255,.2);
text-align:center;
margin-bottom:30px;
">

<h1 style="color:white;">
🌊 SMART RETAIL COMMAND CENTER
</h1>

<p style="color:#bdefff;">
Muhammad Ade Ramadhani - 230104040213 | Zharvian
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* ==============================
BACKGROUND OCEAN
============================== */

            .stApp::before{

content:"";

position:fixed;

top:0;
left:0;

width:100%;
height:100%;

background:

radial-gradient(
circle at 20% 30%,
rgba(0,255,255,.15),
transparent 30%
),

radial-gradient(
circle at 80% 20%,
rgba(0,100,255,.2),
transparent 35%
),

radial-gradient(
circle at 50% 80%,
rgba(0,255,180,.12),
transparent 40%
);

pointer-events:none;

animation:aurora 12s linear infinite;
}

@keyframes aurora{

0%{
transform:translateX(0);
}

50%{
transform:translateX(40px);
}

100%{
transform:translateX(0);
}

}

.stApp{
    background:
    linear-gradient(
        180deg,
        #001f3f 0%,
        #003366 30%,
        #004d80 60%,
        #001f3f 100%
    );
}

/* ==============================
JUDUL
============================== */

h1{
    text-align:center;
    color:white !important;
    font-size:42px !important;
    font-weight:700 !important;
}

/* ==============================
SUBTITLE
============================== */

h2,h3{
    color:#d9f7ff !important;
}

/* ==============================
KPI CARD
============================== */

[data-testid="metric-container"]{

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);

    border:1px solid rgba(255,255,255,0.2);

    border-radius:20px;

    padding:20px;

    box-shadow:
    0 8px 30px rgba(0,0,0,.3);

    transition:.3s;
}

[data-testid="metric-container"]:hover{

    transform:translateY(-5px);

    box-shadow:
    0 15px 40px rgba(0,150,255,.5);
}

/* ==============================
SIDEBAR
============================== */

section[data-testid="stSidebar"]{

    background:
    linear-gradient(
        180deg,
        #001b33,
        #003d66
    );
}

/* ==============================
TEXT
============================== */

label,
span,
p,
div{
    color:white !important;
}

/* ==============================
DATAFRAME
============================== */

[data-testid="stDataFrame"]{
    border-radius:20px;
    overflow:hidden;
}

/* ==============================
PLOTLY
============================== */

.js-plotly-plot{
    border-radius:20px;
}

/* ==============================
BUBBLE
============================== */

.bubble{

    position:fixed;

    bottom:-100px;

    border-radius:50%;

    background:rgba(255,255,255,0.15);

    backdrop-filter:blur(10px);

    box-shadow:
    0 0 15px rgba(255,255,255,.3),
    0 0 30px rgba(0,255,255,.2);

    animation:rise linear infinite;

    z-index:0;
}

@keyframes rise{

    from{
        transform:translateY(0);
    }

    to{
        transform:translateY(-120vh);
    }
}

.b1{
    width:25px;
    height:25px;
    left:10%;
    animation-duration:12s;
}

.b2{
    width:40px;
    height:40px;
    left:25%;
    animation-duration:16s;
}

.b3{
    width:18px;
    height:18px;
    left:45%;
    animation-duration:11s;
}

.b4{
    width:30px;
    height:30px;
    left:65%;
    animation-duration:18s;
}

.b5{
    width:50px;
    height:50px;
    left:85%;
    animation-duration:20s;
}

</style>

<div class="bubble b1"></div>
<div class="bubble b2"></div>
<div class="bubble b3"></div>
<div class="bubble b4"></div>
<div class="bubble b5"></div>

""", unsafe_allow_html=True)

# ==================================================
# ABSOLUTE PATH
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
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

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "visitor_prediction.pkl"
)

# ==================================================
# LOAD DATA
# ==================================================

df_total = pd.read_parquet(VISITOR_TOTAL_PATH)

df_time = pd.read_parquet(VISITOR_TIME_PATH)

df_ml = pd.read_parquet(
    os.path.join(
        PROJECT_ROOT,
        "output",
        "ml_visitor"
    )
)

DETAIL_PATH = os.path.join(
    PROJECT_ROOT,
    "output",
    "visitor_detail"
)

df_raw = pd.read_parquet(
    DETAIL_PATH
)

df_raw["timestamp"] = pd.to_datetime(
    df_raw["timestamp"]
)

model = joblib.load(MODEL_PATH)

if not os.path.exists(VISITOR_TOTAL_PATH):

    os.system(
        f"python {os.path.join(PROJECT_ROOT,'scripts','spark_processing.py')}"
    )

if not os.path.exists(MODEL_PATH):

    os.system(
        f"python {os.path.join(PROJECT_ROOT,'scripts','train_model.py')}"
    )

# ==================================================
# TITLE
# ==================================================

st.markdown("""
<h1>
🌊 Smart Retail Visitor Prediction System
</h1>
""", unsafe_allow_html=True)

st.caption(
    "Big Data Analytics • PySpark • Machine Learning • Streamlit"
)

st.markdown("---")

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("Filter Zona")

st.sidebar.markdown(
f"""
### 🕒 Command Center Time

{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
"""
)

selected_zone = st.sidebar.selectbox(
    "Pilih Zona",
    df_raw["zone"].unique()
)

# ==================================================
# FILTER DATA
# ==================================================

zone_data = df_raw[
    df_raw["zone"] == selected_zone
]

st.subheader("📊 Real-Time Visitor Analytics")

# ==================================================
# KPI
# ==================================================

total_zone = zone_data["visitor_count"].sum()

avg_visitors = int(
    zone_data["visitor_count"].mean()
)

peak_visitors = int(
    zone_data["visitor_count"].max()
)

col1,col2,col3=st.columns(3)

with col1:
    st.markdown(f"""
    <div style="
    background:rgba(0,255,255,.08);
    border:1px solid rgba(0,255,255,.3);
    border-radius:25px;
    padding:25px;
    text-align:center;
    box-shadow:0 0 25px rgba(0,255,255,.4);
    ">
    <h3>👥 Total Visitors</h3>
    <h1>{total_zone:,}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
    background:rgba(0,255,255,.08);
    border:1px solid rgba(0,255,255,.3);
    border-radius:25px;
    padding:25px;
    text-align:center;
    box-shadow:0 0 25px rgba(0,255,255,.4);
    ">
    <h3>📈 Rata-rata Visitor</h3>
    <h1>{avg_visitors}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
    background:rgba(0,255,255,.08);
    border:1px solid rgba(0,255,255,.3);
    border-radius:25px;
    padding:25px;
    text-align:center;
    box-shadow:0 0 25px rgba(0,255,255,.4);
    ">
    <h3>🔥 Peak Visitor</h3>
    <h1>{peak_visitors}</h1>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# DASHBOARD LAYOUT MODERN
# ==================================================

left,right = st.columns([2,1])

with left:

    st.subheader(
        f"📈 Visitor Trend - {selected_zone}"
    )

    trend = zone_data.groupby(
        "timestamp"
    )["visitor_count"].sum().reset_index()

    fig = px.line(
        trend,
        x="timestamp",
        y="visitor_count",
        title="Visitor Trend Analysis"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📊 Visitor Distribution")

    hist = px.histogram(
        zone_data,
        x="visitor_count",
        nbins=20
    )

    hist.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        hist,
        use_container_width=True
    )

    st.subheader("🔥 Peak Hour Analysis")

    zone_data["hour"] = pd.to_datetime(
        zone_data["timestamp"]
    ).dt.hour

    heat = zone_data.groupby(
        "hour"
    )["visitor_count"].mean().reset_index()

    heat_fig = px.bar(
        heat,
        x="hour",
        y="visitor_count",
        title="Average Visitors Per Hour"
    )

    heat_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        heat_fig,
        use_container_width=True
    )

with right:

    st.subheader("🤖 AI Prediction")

    hour_input = st.slider(
        "Pilih Jam",
        0,
        23,
        12
    )

    prediction = float(
        model.predict([[hour_input]])[0]
    )

    prediction = max(
        0,
        min(
            prediction,
            zone_data["visitor_count"].max()
        )
    )

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=int(prediction),
            title={
                "text": "Predicted Visitors"
            },
            gauge={
                "axis": {
                    "range": [0, 500]
                }
            }
        )
    )

    gauge.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        height=350
    )   

    if prediction > 350:
        status = "🔥 HIGH TRAFFIC"
        border_color = "#ff4444"

    elif prediction > 200:
        status = "⚡ MODERATE TRAFFIC"
        border_color = "#ffaa00"

    else:
        status = "🌊 LOW TRAFFIC"
        border_color = "#00ffff"

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    st.success(
        f"Prediksi Visitor Jam {hour_input}:00 = {int(prediction)} Pengunjung"
    )

    st.markdown(
    f"""
    <div style="
    background:linear-gradient(135deg,#003d66,#005b99);
    padding:25px;
    border-radius:20px;
    border-left:6px solid {border_color};
    box-shadow:0 0 20px rgba(0,255,255,.2);
    margin-top:15px;
    ">

    <h2 style="color:white;margin-bottom:10px;">
    {status}
    </h2>

    <h4 style="color:#d9f7ff;">
    Predicted visitor volume at {hour_input}:00
    </h4>

    <h1 style="color:#00ffff;">
    {int(prediction)}
    </h1>

    </div>
    """,
    unsafe_allow_html=True
)

    
# ==================================================
# RAW DATA
# ==================================================

with st.expander("Lihat Data Mentah"):

    st.dataframe(
        zone_data.head(20),
        use_container_width=True
    )

    st.markdown("---")

st.markdown(
"""
<center>

🌊 Smart Retail Visitor Prediction System

Built with PySpark • Parquet • Streamlit • Plotly • Linear Regression

</center>
""",
unsafe_allow_html=True
)