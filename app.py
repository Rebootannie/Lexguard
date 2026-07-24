"""
LexGuard AI — Contract Intelligence Platform
Main Application Entry Point.

This file is the thin orchestrator that:
  1. Configures the page
  2. Loads custom CSS
  3. Renders the sidebar
  4. Combines all 4 dashboard sections in order

Sections are split into separate modules for clean separation:
  - sections/section_overview.py   → Top KPI Metrics
  - sections/section_analysis.py   → Document Viewer + AI Clause Extraction
  - sections/section_analytics.py  → Charts + Playbook RAG Compliance
  - sections/section_footer.py     → Footer & Branding
"""
import streamlit as st
import os


# ================================================================
# PAGE CONFIG (must be the very first Streamlit command)
# ================================================================
st.set_page_config(
    page_title="LexGuard AI — Contract Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ================================================================
# CSS & STYLING
# ================================================================
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), 'assets', 'style.css')
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
# ================================================================
# IMPORTS — Sidebar + All 4 Sections
# ================================================================
from components import sidebar
from sections import section_overview, section_analysis, section_analytics, section_footer


# ================================================================
# RENDER: Sidebar (always visible on the left)
# ================================================================
sidebar.render()


# ================================================================
# RENDER: Section 1 — Dashboard Overview (Top KPI Metrics)
# ================================================================
section_overview.render()


# ================================================================
# RENDER: Section 2 — Contract Analysis (Document + Clauses)
# ================================================================
section_analysis.render()


# ================================================================
# RENDER: Section 3 — Analytics & Compliance (Charts + Playbook)
# ================================================================
section_analytics.render()


# ================================================================
# RENDER: Section 4 — Footer & Branding
# ================================================================
section_footer.render()
