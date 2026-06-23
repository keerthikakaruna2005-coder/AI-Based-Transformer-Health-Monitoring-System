import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("🔋 AI-Based Transformer Health Monitoring System")

# Load dataset
data = pd.read_excel("transformer_data.xlsx")

# Show columns for debugging
st.write("Detected Columns:", list(data.columns))

# Check required columns
required_columns = ["Temperature", "Voltage", "Current", "OilLevel", "Status"]

if not all(col in data.columns for col in required_columns):
    st.error(
        f"CSV column names are incorrect. Expected: {required_columns}"
    )
    st.stop()

# Features and target
X = data[["Temperature", "Voltage", "Current", "OilLevel"]]
y = data["Status"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

st.subheader("Enter Transformer Parameters")

temp = st.number_input("Temperature (°C)", min_value=0, max_value=150, value=50)
volt = st.number_input("Voltage (V)", min_value=0, max_value=500, value=230)
curr = st.number_input("Current (A)", min_value=0, max_value=100, value=10)
oil = st.number_input("Oil Level (%)", min_value=0, max_value=100, value=90)

if st.button("Check Health"):

    input_data = pd.DataFrame(
        [[temp, volt, curr, oil]],
        columns=["Temperature", "Voltage", "Current", "OilLevel"]
    )

    prediction = model.predict(input_data)[0]

    st.subheader("Result")

    if prediction == "Healthy":
        st.success("✅ Transformer Status: Healthy")

    elif prediction == "Warning":
        st.warning("⚠️ Transformer Status: Warning")

    else:
        st.error("🔴 Transformer Status: Critical")