import streamlit as st

st.set_page_config(page_title="Heat Treatment DSS", layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.title("🔥 Heat Treatment Decision Support System")
st.markdown("### Optimize Heat Treatment. Reduce Loss. Improve Performance.")

st.markdown("---")

# -------------------------------
# INTRO
# -------------------------------
st.subheader("📌 What is this system?")

st.write("""
This Decision Support System helps engineers and manufacturers select the **optimal heat treatment process** 
based on material, geometry, and production constraints.

It uses **metallurgical principles + process logic** to:
- Predict microstructure transformation
- Recommend heat treatment process
- Estimate industrial cost & savings
""")

# -------------------------------
# HOW IT WORKS
# -------------------------------
st.subheader("⚙️ How it works")

st.markdown("""
1️⃣ **Input Page**  
Enter material, part requirements, geometry, and constraints  

2️⃣ **Process & Recommendation**  
Get target microstructure, cooling strategy, and process parameters  

3️⃣ **Cost & Savings Analysis**  
See production losses, optimized cost, and potential savings  
""")

# -------------------------------
# VALUE PROPOSITION
# -------------------------------
st.subheader("🚀 Why use this system?")

col1, col2, col3 = st.columns(3)

col1.metric("🔬 Accuracy", "Metallurgy-Based")
col2.metric("💰 Cost Impact", "Industrial Scale")
col3.metric("⚡ Decision Time", "Instant")

# -------------------------------
# HIGHLIGHTS
# -------------------------------
st.subheader("✨ Key Features")

st.markdown("""
- Material-based process intelligence  
- Microstructure prediction (Martensite, Bainite, Pearlite)  
- Cooling medium recommendation  
- Feasibility warnings  
- Cost & savings estimation based on production  
""")

# -------------------------------
# INSTRUCTIONS
# -------------------------------
st.markdown("---")

st.info("👉 Use the sidebar to navigate through the system and start with the **Input Page**.")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
---
Built for **Heat Treatment Optimization & Industrial Decision Making**
""")