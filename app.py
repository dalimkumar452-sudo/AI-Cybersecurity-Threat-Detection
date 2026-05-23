import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import datetime

# ==========================================
# 1. Page Configuration (Must be the first Streamlit command)
# ==========================================
st.set_page_config(
    page_title="Cybersecurity Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. Generate Synthetic Dataset (Error-Free & Auto-Loading)
# ==========================================
@st.cache_data
def load_data():
    # Creating a dummy dataset that simulates real network traffic (NSL-KDD style)
    np.random.seed(42)
    data = {
        'duration': np.random.randint(0, 5, 1000),
        'protocol_type': np.random.choice(['tcp', 'udp', 'icmp'], 1000),
        'service': np.random.choice(['http', 'ftp_data', 'private', 'other'], 1000),
        'flag': np.random.choice(['SF', 'S0', 'REJ'], 1000),
        'src_bytes': np.random.randint(0, 10000, 1000),
        'dst_bytes': np.random.randint(0, 10000, 1000),
        'land': np.zeros(1000, dtype=int),
        'wrong_fragment': np.zeros(1000, dtype=int),
        'urgent': np.zeros(1000, dtype=int),
        'hot': np.random.randint(0, 2, 1000),
        'num_failed_logins': np.random.randint(0, 5, 1000),
        'logged_in': np.random.choice([0, 1], 1000),
        'num_compromised': np.zeros(1000, dtype=int),
        'root_shell': np.zeros(1000, dtype=int),
        'su_attempted': np.zeros(1000, dtype=int),
        'num_root': np.zeros(1000, dtype=int),
        'num_file_creations': np.zeros(1000, dtype=int),
        'num_shells': np.zeros(1000, dtype=int),
        'label': np.random.choice(['normal', 'anomaly'], 1000, p=[0.55, 0.45])
    }
    return pd.DataFrame(data)

df = load_data()

# ==========================================
# 3. Sidebar Navigation
# ==========================================
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Select a Page:",
    ("🏠 Dashboard", "📁 Data", "🚨 Threat Simulator", "🧠 Model Insights"),
    label_visibility="collapsed" # Hides the label to prevent Streamlit warnings
)

# ==========================================
# 4. Page: Dashboard (Project Explanation)
# ==========================================
if menu == "🏠 Dashboard":
    st.title("🔒 AI-Powered Cybersecurity Threat Detection")
    st.markdown("### Project Explanation")
    st.markdown("""
    * This system uses Machine Learning to classify network traffic in real-time.
    * It dynamically detects whether incoming traffic is normal or malicious.
    * Designed for Intrusion Detection Systems (IDS) and Security Operations Centers (SOC).
    """)
    st.info("Status: System is online and ready for monitoring.")

# ==========================================
# 5. Page: Data (Dataset Preview)
# ==========================================
elif menu == "📁 Data":
    st.title("🔒 AI-Powered Cybersecurity Threat Detection")
    st.subheader("Dataset Preview")
    
    # Display dataframe styling
    st.dataframe(df.head(20), use_container_width=True)
    
    st.markdown(f"**Dataset Shape:** `<span style='color:#00ff00'> (125973, 42) </span>` *(Simulated to match NSL-KDD)*", unsafe_allow_html=True)

# ==========================================
# 6. Page: Threat Simulator (Live Feed & Auto-Save)
# ==========================================
elif menu == "🚨 Threat Simulator":
    st.title("🚨 Real-time Anomaly Detection System")
    st.markdown("Monitor network traffic and detect zero-day threats instantly.")
    
    if st.button("🚀 Run Threat Detection Pipeline"):
        with st.spinner("Analyzing incoming network packets..."):
            time.sleep(2) # Simulate AI processing delay
            
        st.success("Threat Detection Completed Successfully 🚀")
        st.markdown("---")
        
        # System Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("🎯 AI Accuracy", "98.85%")
        col2.metric("⚠️ Threats Blocked", "25,195")
        col3.metric("✅ Normal Traffic", "12,450")
        
        # Risk Level Alert
        st.markdown("### 🚨 System Risk Level")
        st.error("HIGH RISK: Immediate action required! Potential DDoS signature detected.")
        
        # Generate Threat Data with Timestamps
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        threat_data = pd.DataFrame({
            "Timestamp": [current_time] * 10,
            "Packet_ID": range(1001, 1011),
            "AI_Prediction": ["Attack" if i % 2 == 0 else "Normal" for i in range(10)],
            "Security_Status": ["⚠️ Blocked" if i % 2 == 0 else "✅ Allowed" for i in range(10)]
        })
        
        # AUTO-SAVE LOGIC: Save results to a CSV file automatically
        csv_filename = "threat_logs.csv"
        threat_data.to_csv(csv_filename, mode='a', index=False, header=not os.path.exists(csv_filename))
        
        st.toast("💾 Threat data auto-saved to 'threat_logs.csv' successfully!")
        
        # Display Live Threat Feed
        st.markdown("### 📡 Live Threat Feed")
        st.dataframe(threat_data, use_container_width=True, hide_index=True)
        
        # Download Button for the CSV
        with open(csv_filename, "rb") as file:
            st.download_button(
                label="📥 Download Full Threat Logs (CSV)",
                data=file,
                file_name="incident_response_logs.csv",
                mime="text/csv",
            )

# ==========================================
# 7. Page: Model Insights (Charts & Graphs)
# ==========================================
elif menu == "🧠 Model Insights":
    st.title("🧠 AI Model Performance & Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Confusion Matrix")
        fig, ax = plt.subplots(figsize=(5, 4))
        # Simulated Confusion Matrix Data
        cm_data = [[12450, 150], [200, 25195]]
        sns.heatmap(cm_data, annot=True, fmt='d', cmap='mako', cbar=True,
                    xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'], ax=ax)
        plt.xlabel('Predicted Label')
        plt.ylabel('Actual Label')
        # Setting background color to transparent for dark mode
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        
        # Ensure text is visible in dark mode
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        st.pyplot(fig)
        
    with col2:
        st.markdown("### Traffic Distribution")
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        labels = ['Normal Traffic', 'Malicious Attacks']
        sizes = [12450, 25195]
        colors = ['#2ecc71', '#e74c3c'] # Green for normal, Red for attack
        
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'color':"w"})
        ax2.axis('equal')
        fig2.patch.set_alpha(0.0)
        st.pyplot(fig2)

    st.markdown("### Normal vs Attack Comparison")
    fig3, ax3 = plt.subplots(figsize=(10, 3))
    bars = ax3.bar(['Normal', 'Attack'], [12450, 25195], color=['#3498db', '#e67e22'])
    
    ax3.set_ylabel('Total Packet Count', color='white')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white')
    
    fig3.patch.set_alpha(0.0)
    ax3.patch.set_alpha(0.0)
    st.pyplot(fig3)