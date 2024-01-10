import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Infected leaves have clear marks differentiating them from the healthy leaves."
        f"We suspect cherry leaves affected by powdery mildew have clear marks, "
        f"typically the first symptom is a light-green, circular lesion on either leaf surface,"
        f" then a subtle white cotton-like growth develops in the infected area."

    )
