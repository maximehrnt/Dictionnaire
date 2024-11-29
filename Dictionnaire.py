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
        # Ajoutez d'autres définitions ici...
    }
    return dictionnaire

# Chargement des données
dictionnaire = chargement_brut_dictionnaire()

# Interface utilisateur Streamlit
st.title("Dictionnaire de Données")

# Saisie du texte utilisateur
texte_saisi = st.text_input("Que cherchez-vous ?", "").strip().lower()

# Liste des mots suggérés basée sur la saisie
texte_saisi_sans_accents = supprimer_accents(texte_saisi)
mots_suggérés = [
    mot for mot in dictionnaire if texte_saisi_sans_accents in supprimer_accents(mot).lower()
]

# Si des suggestions sont disponibles, afficher une liste déroulante
if mots_suggérés:
    mot_selectionne = st.selectbox(
        "Suggestions :", 
        options=[""] + mots_suggérés,  # Option vide par défaut
        format_func=lambda x: x if x else "Saisissez un terme ou choisissez dans la liste"  # Texte par défaut
    )
else:
    mot_selectionne = ""

# Affichage des détails pour le mot sélectionné
if mot_selectionne:
    details = dictionnaire[mot_selectionne]
    st.subheader(f"Définition de **{mot_selectionne}**")
    st.write(f"**Définition :** {details['definition']}")
    st.write(f"**Responsable :** {details['responsable']}")
    st.write(f"**Origine :** {details['origine']}")
    st.write(f"**Source :** {details['source']}")

# Si aucun mot sélectionné, afficher un message informatif
if not texte_saisi:
    st.info("Veuillez entrer un terme à rechercher.")
