import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("💰 Cost & Savings Analysis")

# -------------------------------
# LOAD DATA
# -------------------------------
if "results" not in st.session_state:
    st.error("⚠️ No process data found. Please run analysis first.")
    st.stop()

res = st.session_state.results

# -------------------------------
# EXTRACT DATA
# -------------------------------
baseline_m = res["baseline_m"]
recommended_m = res["recommended_m"]

mode = res["mode"]
production = res["production"]

# -------------------------------
# STEP 1: HARDNESS ESTIMATION
# -------------------------------
def estimate_hardness(martensite):
    return round(20 + 0.5 * martensite)

baseline_hardness = estimate_hardness(baseline_m)
recommended_hardness = estimate_hardness(recommended_m)

# -------------------------------
# STEP 2: METALLURGICAL LOSS
# -------------------------------

# Microstructure mismatch (core metallurgical loss)
micro_loss_current = abs(recommended_m - baseline_m)
micro_loss_new = 5  # optimized residual mismatch

# Property mismatch (hardness gap)
prop_loss_current = abs(recommended_hardness - baseline_hardness)
prop_loss_new = 1

# Process inefficiency
process_loss_current = 10
process_loss_new = 3

# Weighted loss
current_loss = (0.4 * micro_loss_current +
                0.4 * prop_loss_current +
                0.2 * process_loss_current)

new_loss = (0.4 * micro_loss_new +
            0.4 * prop_loss_new +
            0.2 * process_loss_new)

# -------------------------------
# STEP 3: INDUSTRIAL COST MODEL
# -------------------------------

# 🏭 Production quantity
if "1–50" in production:
    quantity = 50
    part_cost = 300
elif "50–1000" in production:
    quantity = 500
    part_cost = 200
else:
    quantity = 2000
    part_cost = 150

# 🔥 Scrap estimation (based on metallurgy gap)
scrap_rate_current = min(current_loss / 100, 0.3)   # max 30%
scrap_rate_new = min(new_loss / 100, 0.1)           # optimized max 10%

scrap_cost_current = scrap_rate_current * part_cost * quantity
scrap_cost_new = scrap_rate_new * part_cost * quantity

# ⚡ Energy cost
energy_cost_current = 20 * quantity
energy_cost_new = 15 * quantity

# 🔧 Rework cost
rework_cost_current = 10 * quantity
rework_cost_new = 5 * quantity

# -------------------------------
# TOTAL COST
# -------------------------------
current_cost = int(scrap_cost_current + energy_cost_current + rework_cost_current)
new_cost = int(scrap_cost_new + energy_cost_new + rework_cost_new)
savings = current_cost - new_cost

# -------------------------------
# STEP 4: SUMMARY CARDS
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("💰 Current Cost", f"₹ {current_cost:,}")
col2.metric("🟢 Optimized Cost", f"₹ {new_cost:,}")
col3.metric("📉 Savings", f"₹ {savings:,}")

# -------------------------------
# STEP 5: COMPARISON TABLE
# -------------------------------
st.subheader("📊 Performance Comparison")

comparison_df = pd.DataFrame({
    "Parameter": ["Martensite (%)", "Hardness (HRC)", "Scrap Rate (%)", "Total Cost (₹)"],
    "Baseline": [
        baseline_m,
        baseline_hardness,
        round(scrap_rate_current * 100, 2),
        current_cost
    ],
    "Recommended": [
        recommended_m,
        recommended_hardness,
        round(scrap_rate_new * 100, 2),
        new_cost
    ]
})

st.table(comparison_df)

# -------------------------------
# STEP 6: COST BREAKDOWN
# -------------------------------
st.subheader("📉 Cost Breakdown")

cost_df = pd.DataFrame({
    "Type": ["Scrap Loss", "Energy Cost", "Rework Cost"],
    "Current (₹)": [
        int(scrap_cost_current),
        int(energy_cost_current),
        int(rework_cost_current)
    ],
    "Optimized (₹)": [
        int(scrap_cost_new),
        int(energy_cost_new),
        int(rework_cost_new)
    ]
})

st.table(cost_df)

# -------------------------------
# STEP 7: GRAPH
# -------------------------------
st.subheader("📊 Cost Comparison")

fig, ax = plt.subplots()

labels = ["Current", "Optimized"]
values = [current_cost, new_cost]

ax.bar(labels, values)
ax.set_ylabel("Cost (₹)")
ax.set_title("Production Cost Comparison")

st.pyplot(fig)

# -------------------------------
# STEP 8: ENGINEERING INSIGHT
# -------------------------------
st.subheader("🧠 Engineering Insight")

if mode == "Part-Based":
    st.write("""
Baseline process produces lower martensite, leading to higher wear and failure probability.

Optimized process improves phase transformation, reducing scrap and increasing component life.
""")

elif mode == "Property-Based":
    st.write("""
Baseline process fails to meet required hardness, causing rejection and rework.

Optimized process achieves required properties, improving yield and reducing losses.
""")

else:
    st.write("""
Baseline process is not optimized, leading to unnecessary energy consumption.

Optimized process improves cooling and transformation efficiency.
""")

# -------------------------------
# STEP 9: FINAL INSIGHT
# -------------------------------
st.success(f"✅ Estimated Savings: ₹ {savings:,} per production batch")

st.caption("Note: Cost estimation is based on metallurgical inefficiencies, scrap rates, and industrial-scale assumptions.")