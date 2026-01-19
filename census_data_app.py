# census_app.py 
# Streamlit Census Data Visualization App

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --------------------------------------------------
# Page Configuration (REQUIRED for deployment)
# --------------------------------------------------
st.set_page_config(
    page_title="Census Data Visualization",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load and Clean Data (Cached)
# --------------------------------------------------
@st.cache_data
def load_data():
    # Load dataset
    df = pd.read_csv("adult.csv", header=None)

    # Assign column names
    df.columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-years',
        'marital-status', 'occupation', 'relationship', 'race', 'gender',
        'capital-gain', 'capital-loss', 'hours-per-week',
        'native-country', 'income'
    ]

    # Replace invalid values
    df.replace(" ?", np.nan, inplace=True)

    # Drop missing values
    df.dropna(inplace=True)

    # Drop unnecessary column
    df.drop(columns="fnlwgt", inplace=True)

    return df


# Load dataset
census_df = load_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("📊 Census Dashboard")
st.sidebar.markdown("Visualize Adult Census Income Data")

# Display raw data
if st.sidebar.checkbox("Show Raw Dataset"):
    st.subheader("Census Dataset")
    st.dataframe(census_df)
    st.write("Rows:", census_df.shape[0])
    st.write("Columns:", census_df.shape[1])

# Plot selection
st.sidebar.subheader("Select Visualizations")
plot_list = st.sidebar.multiselect(
    "Choose charts:",
    ["Pie Charts", "Box Plots", "Count Plot"]
)

# --------------------------------------------------
# Main Title
# --------------------------------------------------
st.title("Census Data Visualization Web App")

# --------------------------------------------------
# Pie Charts
# --------------------------------------------------
if "Pie Charts" in plot_list:
    st.subheader("📌 Pie Charts")

    explode = [0, 0.15]

    # Income Distribution
    fig, ax = plt.subplots(figsize=(7, 5))
    income_data = census_df["income"].value_counts()
    ax.pie(
        income_data,
        labels=income_data.index,
        autopct="%1.2f%%",
        explode=explode,
        startangle=30
    )
    ax.set_title("Income Distribution")
    st.pyplot(fig)

    # Gender Distribution
    fig, ax = plt.subplots(figsize=(7, 5))
    gender_data = census_df["gender"].value_counts()
    ax.pie(
        gender_data,
        labels=gender_data.index,
        autopct="%1.2f%%",
        explode=explode,
        startangle=30
    )
    ax.set_title("Gender Distribution")
    st.pyplot(fig)

# --------------------------------------------------
# Box Plots
# --------------------------------------------------
if "Box Plots" in plot_list:
    st.subheader("📌 Box Plots")

    # Hours per week vs Income
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(
        x="income",
        y="hours-per-week",
        data=census_df,
        ax=ax
    )
    ax.set_title("Hours Worked per Week by Income Group")
    st.pyplot(fig)

    # Hours per week vs Gender
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(
        x="gender",
        y="hours-per-week",
        data=census_df,
        ax=ax
    )
    ax.set_title("Hours Worked per Week by Gender")
    st.pyplot(fig)

# --------------------------------------------------
# Count Plot
# --------------------------------------------------
if "Count Plot" in plot_list:
    st.subheader("📌 Count Plot")

    fig, ax = plt.subplots(figsize=(14, 6))
    sns.countplot(
        x="workclass",
        hue="income",
        data=census_df,
        ax=ax
    )
    ax.set_title("Workclass Distribution by Income Group")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "**📘 Note: " 
    "These projects were created during my learning journey at **WhiteHat Jr**. "
)
# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown("**Built with Streamlit • Census Income Dataset**")
