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
    return {
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
        "Loyer": {
            "definition": "Somme d'argent versée périodiquement par le locataire au propriétaire.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        # Ajoutez les autres termes ici
    }

# Chargement des données
dictionnaire = chargement_brut_dictionnaire()

# Interface utilisateur Streamlit
st.title("Dictionnaire de Données")

# Champ de saisie
input_text = st.text_input("Recherchez un terme :", "")

# Suggestions basées sur l'entrée utilisateur
if input_text:
    input_text_normalized = supprimer_accents(input_text).lower()
    suggestions = [
        mot for mot in dictionnaire.keys()
        if input_text_normalized in supprimer_accents(mot).lower()
    ][:5]  # Limiter à 5 suggestions

    if suggestions:
        st.subheader("Suggestions")
        # Afficher chaque suggestion dans une carte
        for mot in suggestions:
            definition = dictionnaire[mot]["definition"]
            
            # Créer une carte pour chaque suggestion
            st.markdown(
                f"""
                <div style="
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 10px;
                    margin-bottom: 10px;
                    background-color: #f9f9f9;
                    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
                ">
                    <h4 style="margin: 0; color: #333;">{mot}</h4>
                    <p style="margin: 5px 0 0; font-size: 14px; color: #555;">{definition[:150]}{'...' if len(definition) > 150 else ''}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("Aucune suggestion trouvée.")
else:
    st.info("Veuillez entrer un terme pour commencer la recherche.")
