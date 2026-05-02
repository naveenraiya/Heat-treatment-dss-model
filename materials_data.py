import pandas as pd

materials_data = pd.DataFrame([

    {"Material": "EN3", "C_min": 0.1, "C_max": 0.2, "Mn": 0.4, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 0.25, "Hardenability": "Low", "HRC_min": 10, "HRC_max": 30,
     "Baseline Microstructure": "Ferrite + Pearlite", "Category": "Low Carbon", "Avg_C": 0.15},

    {"Material": "AISI 1018", "C_min": 0.15, "C_max": 0.2, "Mn": 0.6, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 0.3, "Hardenability": "Low", "HRC_min": 15, "HRC_max": 35,
     "Baseline Microstructure": "Ferrite + Pearlite", "Category": "Low Carbon", "Avg_C": 0.175},

    {"Material": "AISI 1020", "C_min": 0.18, "C_max": 0.23, "Mn": 0.5, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 0.32, "Hardenability": "Low", "HRC_min": 15, "HRC_max": 35,
     "Baseline Microstructure": "Ferrite + Pearlite", "Category": "Low Carbon", "Avg_C": 0.205},

    {"Material": "EN8", "C_min": 0.36, "C_max": 0.44, "Mn": 0.8, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 0.5, "Hardenability": "Medium", "HRC_min": 20, "HRC_max": 55,
     "Baseline Microstructure": "Pearlite + Bainite", "Category": "Medium Carbon", "Avg_C": 0.4},

    {"Material": "EN9", "C_min": 0.45, "C_max": 0.55, "Mn": 0.7, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 0.6, "Hardenability": "Medium", "HRC_min": 25, "HRC_max": 58,
     "Baseline Microstructure": "Pearlite + Bainite", "Category": "Medium Carbon", "Avg_C": 0.5},

    {"Material": "AISI 1045", "C_min": 0.43, "C_max": 0.5, "Mn": 0.7, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 0.58, "Hardenability": "Medium", "HRC_min": 25, "HRC_max": 58,
     "Baseline Microstructure": "Pearlite + Bainite", "Category": "Medium Carbon", "Avg_C": 0.465},

    {"Material": "EN31", "C_min": 0.9, "C_max": 1.2, "Mn": 0.5, "Cr": 1.2, "Mo": 0, "Ni": 0,
     "CE": 1.2, "Hardenability": "High", "HRC_min": 55, "HRC_max": 65,
     "Baseline Microstructure": "Martensite", "Category": "High Carbon", "Avg_C": 1.05},

    {"Material": "AISI 1095", "C_min": 0.9, "C_max": 1.03, "Mn": 0.4, "Cr": 0, "Mo": 0, "Ni": 0,
     "CE": 1.05, "Hardenability": "High", "HRC_min": 55, "HRC_max": 65,
     "Baseline Microstructure": "Martensite", "Category": "High Carbon", "Avg_C": 0.965},

    {"Material": "EN19", "C_min": 0.35, "C_max": 0.45, "Mn": 0.7, "Cr": 1, "Mo": 0.3, "Ni": 0,
     "CE": 0.75, "Hardenability": "High", "HRC_min": 30, "HRC_max": 60,
     "Baseline Microstructure": "Bainite + Martensite", "Category": "Low Alloy", "Avg_C": 0.4},

    {"Material": "AISI 4140", "C_min": 0.38, "C_max": 0.43, "Mn": 0.8, "Cr": 1, "Mo": 0.2, "Ni": 0,
     "CE": 0.78, "Hardenability": "High", "HRC_min": 30, "HRC_max": 60,
     "Baseline Microstructure": "Bainite + Martensite", "Category": "Low Alloy", "Avg_C": 0.405},

    {"Material": "EN18", "C_min": 0.15, "C_max": 0.2, "Mn": 0.6, "Cr": 1.2, "Mo": 0.3, "Ni": 0,
     "CE": 0.55, "Hardenability": "Medium", "HRC_min": 20, "HRC_max": 50,
     "Baseline Microstructure": "Bainite", "Category": "Low Alloy", "Avg_C": 0.175},

    {"Material": "EN24", "C_min": 0.36, "C_max": 0.44, "Mn": 0.6, "Cr": 1.2, "Mo": 0.3, "Ni": 1.5,
     "CE": 0.9, "Hardenability": "Very High", "HRC_min": 35, "HRC_max": 65,
     "Baseline Microstructure": "Martensite + Bainite", "Category": "High Alloy", "Avg_C": 0.4},

    {"Material": "AISI 4340", "C_min": 0.38, "C_max": 0.43, "Mn": 0.7, "Cr": 0.8, "Mo": 0.25, "Ni": 1.8,
     "CE": 0.92, "Hardenability": "Very High", "HRC_min": 35, "HRC_max": 65,
     "Baseline Microstructure": "Martensite + Bainite", "Category": "High Alloy", "Avg_C": 0.405},

    {"Material": "D2", "C_min": 1.4, "C_max": 1.6, "Mn": 0.6, "Cr": 12, "Mo": 0.8, "Ni": 0,
     "CE": 1.8, "Hardenability": "Very High", "HRC_min": 55, "HRC_max": 65,
     "Baseline Microstructure": "Martensite + Carbides", "Category": "Tool Steel", "Avg_C": 1.5},

    {"Material": "H13", "C_min": 0.35, "C_max": 0.45, "Mn": 0.5, "Cr": 5, "Mo": 1.3, "Ni": 0,
     "CE": 1.2, "Hardenability": "High", "HRC_min": 40, "HRC_max": 55,
     "Baseline Microstructure": "Tempered Martensite", "Category": "Tool Steel", "Avg_C": 0.4},

    {"Material": "O1", "C_min": 0.9, "C_max": 1.0, "Mn": 1.2, "Cr": 0.5, "Mo": 0.5, "Ni": 0,
     "CE": 1.1, "Hardenability": "High", "HRC_min": 55, "HRC_max": 62,
     "Baseline Microstructure": "Martensite", "Category": "Tool Steel", "Avg_C": 0.95},

    {"Material": "SS304", "C_min": 0.08, "C_max": 0.1, "Mn": 1, "Cr": 18, "Mo": 0, "Ni": 8,
     "CE": 0.6, "Hardenability": "Low", "HRC_min": 15, "HRC_max": 25,
     "Baseline Microstructure": "Austenite", "Category": "Stainless", "Avg_C": 0.09},

    {"Material": "SS316", "C_min": 0.08, "C_max": 0.1, "Mn": 1, "Cr": 17, "Mo": 2.5, "Ni": 10,
     "CE": 0.65, "Hardenability": "Low", "HRC_min": 15, "HRC_max": 25,
     "Baseline Microstructure": "Austenite", "Category": "Stainless", "Avg_C": 0.09},

    {"Material": "SS410", "C_min": 0.1, "C_max": 0.15, "Mn": 1, "Cr": 12, "Mo": 0, "Ni": 0,
     "CE": 0.5, "Hardenability": "Medium", "HRC_min": 25, "HRC_max": 50,
     "Baseline Microstructure": "Martensite", "Category": "Stainless", "Avg_C": 0.125},

])