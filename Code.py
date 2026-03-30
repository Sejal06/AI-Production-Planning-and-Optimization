import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Production Optimizer", layout="wide")

st.title("🏭 AI Production Planning & Bottleneck Optimizer")

st.markdown("---")

# -----------------------------
# INPUT
# -----------------------------
st.sidebar.header("⚙️ Line Configuration")

stations = ["Cutting", "Welding", "Assembly", "Painting", "Inspection"]

capacity = {}

for s in stations:
    capacity[s] = st.sidebar.slider(f"{s} Capacity (units/hr)", 10, 200, 100)

# -----------------------------
# BOTTLENECK LOGIC
# -----------------------------
values = list(capacity.values())
bottleneck_value = min(values)

bottleneck_station = stations[values.index(bottleneck_value)]

# -----------------------------
# OUTPUT
# -----------------------------
st.subheader("📊 Production Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Max Throughput (units/hr)", bottleneck_value)

with col2:
    st.metric("Bottleneck Station", bottleneck_station)

# -----------------------------
# VISUALIZATION
# -----------------------------
st.subheader("📈 Station Capacity")

fig, ax = plt.subplots()
ax.bar(stations, values)
ax.set_ylabel("Capacity")

st.pyplot(fig)

# -----------------------------
# OPTIMIZATION SUGGESTION
# -----------------------------
st.subheader("🧠 AI Recommendation")

for s in stations:
    if capacity[s] == bottleneck_value:
        st.error(f"{s} is limiting production. Increase capacity here.")

    elif capacity[s] < bottleneck_value * 1.2:
        st.warning(f"{s} is near bottleneck. Monitor closely.")

    else:
        st.success(f"{s} is performing well.")