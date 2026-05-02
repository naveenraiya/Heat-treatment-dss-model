import streamlit as st

st.set_page_config(layout="wide")

st.title("🔧 Heat Treatment DSS - Input")

# =============================
# 1. MATERIAL SELECTION
# =============================
st.header("1️⃣ Material Selection")

materials = [
    "EN3",
    "AISI 1018",
    "AISI 1020",
    "EN8",
    "EN9",
    "AISI 1045",
    "EN31",
    "AISI 1095",
    "EN19",
    "AISI 4140",
    "EN18",
    "EN24",
    "AISI 4340",
    "D2",
    "H13",
    "O1",
    "SS304",
    "SS316",
    "SS410",
    "Custom"
]

material = st.selectbox("Select Material", materials)

# Custom composition
custom_data = {}
if material == "Custom":
    st.subheader("Enter Composition (%)")
    col1, col2, col3 = st.columns(3)
    with col1:
        custom_data["C"] = st.number_input("Carbon (C %)", 0.0, 2.0, 0.3)
        custom_data["Mn"] = st.number_input("Manganese (Mn %)", 0.0, 3.0, 0.5)
    with col2:
        custom_data["Cr"] = st.number_input("Chromium (Cr %)", 0.0, 5.0, 0.5)
        custom_data["Mo"] = st.number_input("Molybdenum (Mo %)", 0.0, 5.0, 0.2)
    with col3:
        custom_data["Ni"] = st.number_input("Nickel (Ni %)", 0.0, 5.0, 0.2)

# =============================
# 2. REQUIREMENT
# =============================
st.header("2️⃣ Requirement")

mode = st.radio(
    "Select Requirement Type",
    ["Part-Based", "Property-Based", "Baseline (Not Sure)"]
)

part = None
hardness = None
toughness = None

if mode == "Part-Based":
    part = st.selectbox(
        "Select Part Type",
        ["Gear", "Shaft", "Spring", "Bearing", "Structural", "Tool", "General"]
    )

elif mode == "Property-Based":
    col1, col2 = st.columns(2)
    with col1:
        hardness = st.number_input("Hardness (HRC)", 10, 70, 40)
    with col2:
        toughness = st.selectbox("Toughness Level", ["Low", "Medium", "High"])

# =============================
# 3. GEOMETRY
# =============================
st.header("3️⃣ Geometry")

col1, col2 = st.columns(2)

with col1:
    thickness = st.number_input("Thickness (mm)", 1, 1000, 20)

with col2:
    shape = st.selectbox("Shape Type", ["Thin", "Thick", "Complex"])

# =============================
# 4. CONSTRAINTS
# =============================
st.header("4️⃣ Constraints")

cooling_medium = st.multiselect(
    "Available Cooling Medium",
    ["Air", "Oil", "Water", "Polymer"]
)

production_size = st.radio(
    "Production Size",
    ["1–50 (Small Batch)", "50–1000 (Medium Batch)", "1000+ (Large Batch)"]
)

priority = st.radio(
    "Priority",
    ["Performance", "Balanced", "Cost Saving"]
)

# =============================
# ANALYZE BUTTON
# =============================
st.markdown("---")

if st.button("🔍 Analyze Data"):

    user_input = {
        "Material": material,
        "Mode": mode,
        "Thickness": thickness,
        "Shape": shape,
        "Cooling Medium": cooling_medium,
        "Production": production_size,
        "Priority": priority
    }

    # Mode-specific inputs (FIXED)
    if mode == "Part-Based":
        user_input["Part"] = part

    elif mode == "Property-Based":
        user_input["Hardness"] = hardness
        user_input["Toughness"] = toughness

    # Custom composition (if any)
    if material == "Custom":
        user_input["Composition"] = custom_data

    # Save to session state
    st.session_state.user_input = user_input

    # Success message
    st.success("✅ Data saved successfully!")

    # OPTIONAL (recommended UX)
    st.switch_page("pages/2_Process_and_Recommendation.py")