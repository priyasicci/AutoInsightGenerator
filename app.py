import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
categories = ['Outerwear & Coats', 'Suits & Sport Coats', 'Blazers & Jackets', 'Dresses', 'Suits']
margins = [82.25, 74.90, 58.03, 46.60, 45.94]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(categories, margins, color='skyblue')
plt.title('Top 5 Product Categories by Average Margin')
plt.xlabel('Product Category')
plt.ylabel('Average Margin (%)')
plt.xticks(rotation=45)

st.pyplot()
