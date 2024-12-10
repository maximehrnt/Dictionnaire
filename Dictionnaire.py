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
        
        # Affichage en colonnes
        cols = st.columns(len(suggestions))  # Une colonne par suggestion

        for col, mot in zip(cols, suggestions):
            definition = dictionnaire[mot]["definition"]
            short_definition = (
                definition[:100] + "..." if len(definition) > 100 else definition
            )  # Limite la taille de la définition

            # Carte cliquable
            with col:
                if st.button(f"{mot}\n\n{short_definition}", key=mot):
                    # Afficher les détails complets du mot cliqué
                    details = dictionnaire[mot]
                    st.subheader(f"Détails pour : {mot}")
                    st.write(f"**Définition :** {details['definition']}")
                    st.write(f"**Responsable :** {details['responsable']}")
                    st.write(f"**Origine :** {details['origine']}")
                    st.write(f"**Source :** {details['source']}")
    else:
        st.info("Aucune suggestion trouvée.")
else:
    st.info("Veuillez entrer un terme pour commencer la recherche.")
