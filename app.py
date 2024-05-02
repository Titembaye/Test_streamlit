import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import mymodel as m

st.title("First App")

 #Sélecteur de texte
option = st.selectbox('Choisissez une option', ['Option 1', 'Option 2', 'Option 3'])
st.write('Vous avez sélectionné :', option)

# Curseur
valeur = st.slider('Sélectionnez une valeur', 0, 100, 50)
st.write('Valeur sélectionnée :', valeur)

df = pd.DataFrame({
'Nom': ['Alice', 'Bob', 'Charlie'],
'Âge': [30, 35, 40]
})
st.write(df)

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Graphique de sin(x)')


st.pyplot(fig)


# Changez le thème
st.markdown("""
<style>
body {
background-color: #f0f0ff;
}
</style>
""", unsafe_allow_html=True)

# Texte mis en forme
st.markdown('**Gras** :boom:')
st.write('Texte en _italique_.')
#st.write(m.run(window=window))