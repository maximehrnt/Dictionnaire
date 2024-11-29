from unicodedata import normalize, category
import unicodedata
import streamlit as st

# Fonction pour supprimer les accents
def supprimer_accents(chaine):
    return ''.join(
        c for c in unicodedata.normalize('NFD', chaine) 
        if unicodedata.category(c) != 'Mn'
    )

# Chargement des données depuis la génération automatique du CSV
def chargement_brut_dictionnaire():
    dictionnaire = {
        "Logement": {
            "definition": "Unité d'habitation destinée à être occupée par une ou plusieurs personnes.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Locataire": {
            "definition": "Personne qui occupe un logement contre paiement d'un loyer.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        # Ajoutez le reste des définitions ici
    }
    return dictionnaire

# Chargement des données
dictionnaire = chargement_brut_dictionnaire()

# Interface utilisateur Streamlit
st.title("Dictionnaire de Données")

# Liste déroulante initiale vide
placeholder_text = "Saisissez un terme ou choisissez dans la liste"
mots_suggérés = sorted(dictionnaire.keys())  # Liste triée des mots
selection = st.selectbox(
    "Suggestions :", 
    options=[""] + mots_suggérés,  # Ajout d'une option vide par défaut
    format_func=lambda x: x if x else placeholder_text  # Texte affiché si rien n'est sélectionné
)

# Afficher les détails du mot sélectionné
if selection:
    if selection in dictionnaire:
        details = dictionnaire[selection]
        st.subheader(f"Définition de **{selection}**")
        st.write(f"**Définition :** {details['definition']}")
        st.write(f"**Responsable :** {details['responsable']}")
        st.write(f"**Origine :** {details['origine']}")
        st.write(f"**Source :** {details['source']}")
else:
    st.info("Aucun terme sélectionné.")
