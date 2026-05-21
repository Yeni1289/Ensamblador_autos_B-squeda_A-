from pathlib import Path

import pandas as pd
import streamlit as st

from src.solver import astar_optimal_assignment, brute_force_optimal

DEFAULT_PRICES = {
    "Empresa 1": {"Tipo T": 20, "Tipo H": 30, "Tipo V": 20, "Tipo W": 40},
    "Empresa 2": {"Tipo T": 30, "Tipo H": 50, "Tipo V": 40, "Tipo W": 50},
    "Empresa 3": {"Tipo T": 60, "Tipo H": 55, "Tipo V": 50, "Tipo W": 60},
    "Empresa 4": {"Tipo T": 100, "Tipo H": 80, "Tipo V": 60, "Tipo W": 70},
}

st.set_page_config(
    page_title="Heurística Admisible - Selección de Ruedas",
    page_icon="🚗",
    layout="wide",
)


def load_css() -> None:
    css_path = Path("assets/styles/main.css")
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def to_prices_dict(df: pd.DataFrame) -> dict:
    clean_df = df.copy()
    for col in clean_df.columns:
        clean_df[col] = pd.to_numeric(clean_df[col], errors="coerce")
    clean_df = clean_df.fillna(0).astype(int).clip(lower=0)
    return {company: {wheel: int(clean_df.loc[company, wheel]) for wheel in clean_df.columns} for company in clean_df.index}


load_css()


def load_html_component(filename: str) -> str:
    component_path = Path(f"assets/components/{filename}")
    if component_path.exists():
        return component_path.read_text(encoding='utf-8')
    return ""


hero_html = load_html_component("hero.html")
st.markdown(hero_html, unsafe_allow_html=True)

st.subheader("1) Edita los precios")
base_df = pd.DataFrame(DEFAULT_PRICES).T
edited_df = st.data_editor(
    base_df,
    use_container_width=True,
    num_rows="fixed",
)
prices = to_prices_dict(edited_df)

st.subheader("2) Solución óptima global")
best_a_star = astar_optimal_assignment(prices)
best_bruteforce = brute_force_optimal(prices)

col1, col2, col3 = st.columns(3)
col1.metric("Costo óptimo (A*)", f"${best_a_star.total_cost}")
col2.metric("Nodos expandidos (A*)", best_a_star.expanded_nodes)
col3.metric("Validación fuerza bruta", f"${best_bruteforce.total_cost}")

optimal_df = pd.DataFrame(
    [
        {"Tipo de rueda": wheel, "Empresa seleccionada": company, "Costo": prices[company][wheel]}
        for wheel, company in best_a_star.assignment.items()
    ]
)
st.dataframe(optimal_df, use_container_width=True, hide_index=True)