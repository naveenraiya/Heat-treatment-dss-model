import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from materials_data import materials_data

st.set_page_config(layout="wide")

st.title("🔬 Process & Recommendation Engine")

# -------------------------------
# LOAD USER INPUT
# -------------------------------
if "user_input" not in st.session_state:
    st.error("⚠️ No input data found. Please go back to Input Page.")
    st.stop()

data = st.session_state.user_input

# -------------------------------
# 1. INPUT SUMMARY
# -------------------------------
st.subheader("📋 Input Summary")

input_df = pd.DataFrame({
    "Parameter": list(data.keys()),
    "Value": list(data.values())
})

st.table(input_df)

# -------------------------------
# 2. MATERIAL ANALYSIS
# -------------------------------
st.subheader("🧪 Material Analysis")

if data["Material"] != "Custom":

    filtered = materials_data[materials_data["Material"] == data["Material"]]

    if filtered.empty:
        st.error(f"❌ Material '{data['Material']}' not found in database.")
        st.stop()

    material_row = filtered.iloc[0]

else:
    comp = data.get("Composition", {})

    C = comp.get("C", 0)
    Mn = comp.get("Mn", 0)
    Cr = comp.get("Cr", 0)
    Mo = comp.get("Mo", 0)
    Ni = comp.get("Ni", 0)

    CE = C + Mn/6 + (Cr + Mo)/5 + Ni/15

    if CE < 0.4:
        hardenability = "Low"
    elif CE < 0.7:
        hardenability = "Medium"
    elif CE < 1.0:
        hardenability = "High"
    else:
        hardenability = "Very High"

    material_row = {
        "Avg_C": C,
        "CE": CE,
        "Hardenability": hardenability,
        "Category": "Custom Alloy",
        "Baseline Microstructure": "Estimated"
    }

material_info = {
    "Carbon Level": "Low" if material_row["Avg_C"] < 0.25 else "Medium" if material_row["Avg_C"] < 0.6 else "High",
    "Carbon Equivalent": round(material_row["CE"], 3),
    "Hardenability": material_row["Hardenability"],
    "Category": material_row["Category"],
    "Baseline Microstructure": material_row["Baseline Microstructure"]
}

st.table(pd.DataFrame(material_info.items(), columns=["Property", "Value"]))

# -------------------------------
# 3. REQUIREMENT
# -------------------------------
st.subheader("🎯 Requirement Understanding")

mode = data["Mode"]

if mode == "Part-Based":
    part = data.get("Part", "General")
    st.write(f"Selected Part: **{part}**")

    if part == "Gear":
        req = ["High hardness", "Wear resistance", "Moderate toughness"]
    elif part == "Shaft":
        req = ["Moderate strength", "High toughness"]
    else:
        req = ["Balanced properties"]

elif mode == "Property-Based":
    req = [
        f"Hardness: {data.get('Hardness')} HRC",
        f"Toughness: {data.get('Toughness')}"
    ]

else:
    req = ["Balanced general-purpose properties"]

for r in req:
    st.write(f"- {r}")

# -------------------------------
# 4. TARGET MICROSTRUCTURE
# -------------------------------
st.subheader("🔬 Target Microstructure")

if mode == "Part-Based":
    martensite = 75
    bainite = 25
    pearlite = 0

elif mode == "Property-Based":
    martensite = 70
    bainite = 30
    pearlite = 0

else:
    martensite = 20
    bainite = 30
    pearlite = 50

if material_row["Hardenability"] == "Low":
    martensite -= 15
    bainite += 10
    pearlite += 5

# Normalize safety
total = martensite + bainite + pearlite
martensite = round((martensite/total)*100)
bainite = round((bainite/total)*100)
pearlite = 100 - martensite - bainite

micro_df = pd.DataFrame({
    "Phase": ["Martensite", "Bainite", "Pearlite"],
    "Recommended (%)": [martensite, bainite, pearlite]
})

st.table(micro_df)

# -------------------------------
# 📊 PIE CHART
# -------------------------------
st.subheader("📊 Microstructure Distribution")

fig1, ax1 = plt.subplots()
ax1.pie(
    micro_df["Recommended (%)"],
    labels=micro_df["Phase"],
    autopct='%1.1f%%'
)
st.pyplot(fig1)

# -------------------------------
# 🟥 BASELINE COMPARISON
# -------------------------------
st.subheader("🟥 Baseline vs 🟢 Recommended")

if mode == "Part-Based":
    baseline_m = martensite - 20
    baseline_b = bainite + 10
    baseline_p = pearlite + 10

elif mode == "Property-Based":
    baseline_m = martensite - 15
    baseline_b = bainite + 10
    baseline_p = pearlite + 5

else:
    baseline_m = martensite - 5
    baseline_b = bainite + 5
    baseline_p = pearlite

# normalize
baseline_m = max(0, baseline_m)
baseline_b = max(0, baseline_b)
baseline_p = max(0, baseline_p)

total = baseline_m + baseline_b + baseline_p
baseline_m = round((baseline_m/total)*100)
baseline_b = round((baseline_b/total)*100)
baseline_p = 100 - baseline_m - baseline_b

comparison_df = pd.DataFrame({
    "Phase": ["Martensite", "Bainite", "Pearlite"],
    "Baseline (%)": [baseline_m, baseline_b, baseline_p],
    "Recommended (%)": [martensite, bainite, pearlite]
})

st.table(comparison_df)

# -------------------------------
# 📊 BAR GRAPH
# -------------------------------
st.subheader("📊 Comparison Graph")

fig2, ax2 = plt.subplots()

x = range(3)
ax2.bar(x, comparison_df["Baseline (%)"], width=0.4, label="Baseline")
ax2.bar([i + 0.4 for i in x], comparison_df["Recommended (%)"], width=0.4, label="Recommended")

ax2.set_xticks([i + 0.2 for i in x])
ax2.set_xticklabels(["Martensite", "Bainite", "Pearlite"])
ax2.set_ylabel("Percentage")
ax2.legend()

st.pyplot(fig2)

# -------------------------------
# 🧠 IMPROVEMENT EXPLANATION
# -------------------------------
st.subheader("🧠 Why Recommended is Better")

if martensite > baseline_m:
    st.write("✔ Higher martensite → increased hardness and wear resistance")

if bainite < baseline_b:
    st.write("✔ Controlled bainite → balanced toughness")

if pearlite < baseline_p:
    st.write("✔ Reduced pearlite → improved strength")

# -------------------------------
# 5. PROCESS RECOMMENDATION
# -------------------------------
st.subheader("⚙️ Process Recommendation")

if martensite > 60:
    cooling_rate = "High"
elif bainite > 40:
    cooling_rate = "Medium"
else:
    cooling_rate = "Low"

available_media = data.get("Cooling Medium", [])

if cooling_rate == "High":
    recommended_medium = "Water" if "Water" in available_media else "Oil"
elif cooling_rate == "Medium":
    recommended_medium = "Oil" if "Oil" in available_media else "Air"
else:
    recommended_medium = "Air"

avg_c = material_row["Avg_C"]

if avg_c < 0.25:
    austenite_temp = "750–850°C"
elif avg_c < 0.6:
    austenite_temp = "800–900°C"
else:
    austenite_temp = "850–950°C"

tempering_temp = "200–350°C" if martensite > 50 else "400–600°C"

process_df = pd.DataFrame({
    "Parameter": ["Cooling Rate", "Cooling Medium", "Austenitizing", "Tempering"],
    "Value": [cooling_rate, recommended_medium, austenite_temp, tempering_temp]
})

st.table(process_df)

# -------------------------------
# FINAL STEPS
# -------------------------------
st.subheader("🛠️ Heat Treatment Steps")

st.markdown(f"""
1. Heat to **{austenite_temp}**  
2. Hold for uniform heating  
3. Quench using **{recommended_medium}**  
4. Temper at **{tempering_temp}**  
""")

# -------------------------------
# WARNINGS
# -------------------------------
st.subheader("⚠️ Feasibility")

if data["Thickness"] > 100:
    st.warning("Large thickness may reduce hardening effectiveness")

if material_row["Hardenability"] == "Low" and martensite > 60:
    st.warning("Material may not achieve full martensite")

# SAVE IMPORTANT DATA FOR PAGE 3
st.session_state.results = {
    "baseline_m": baseline_m,
    "baseline_b": baseline_b,
    "baseline_p": baseline_p,
    "recommended_m": martensite,
    "recommended_b": bainite,
    "recommended_p": pearlite,
    "material": data["Material"],
    "mode": data["Mode"],
    "thickness": data["Thickness"],
    "production": data.get("Production", "Medium"),
}

if st.button("➡️ Go to Cost & Savings"):
    st.switch_page("pages/3_Cost_and_Savings.py")