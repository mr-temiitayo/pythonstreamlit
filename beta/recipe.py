import streamlit as st
import pandas as pd

# Load the recipes CSV file into a DataFrame
data = pd.read_csv('recipes.csv')

# Sidebar with filters
st.sidebar.title('Filter Recipes')
cuisine = st.sidebar.selectbox('Cuisine', data['Cuisine'].unique())
meal_type = st.sidebar.selectbox('Meal Type', data['Meal Type'].unique())

# Filter the data based on user selection
filtered_data = data[(data['Cuisine'] == cuisine) & (data['Meal Type'] == meal_type)]

st.title('Recipe Finder')

if not filtered_data.empty:
    st.write(f"Showing {cuisine} {meal_type} Recipes:")
    st.dataframe(filtered_data, use_container_width=True)
else:
    st.warning("No recipes found. Please adjust your filters.")

