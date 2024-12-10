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
        "Surface corrigée": {
            "definition": "La surface corrigée est une mesure pondérée tenant compte de la surface réelle et des caractéristiques du logement comme le confort ou la localisation.",
            "regles_de_gestion": "Tout lot maison ou appartement a une surface utile ou une surface corrigée. Aucun lot n'a à la fois une surface utile et une surface corrigée actives",
            "plan_de_controle": "P4, P5",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Secteur ou Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Patrimoine/Descriptif Patrimoine/Descriptif/Recherche liste patrimoine/Code ESI",
            "champ_ulis": "PA_MONCODE"
        },
        "Surface Habitable": {
            "definition": "La surface habitable est la superficie d'un logement utilisable pour y vivre hors murs ou caves et garages.",
            "regles_de_gestion": "Tout lot a une surface habitable",
            "plan_de_controle": "P3",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Secteur ou Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Patrimoine/Descriptif Patrimoine/Descriptif/Recherche liste patrimoine/Code ESI",
            "champ_ulis": "PA_MONCODE"
        },
        "Surface utile": {
            "definition": "La surface utile désigne la surface totale d'un logement, incluant toutes les pièces utilisables, mais excluant les murs, cloisons, escaliers et espaces non habitables (comme les balcons ou les caves).",
            "regles_de_gestion": "Tout lot maison ou appartement a une surface utile ou une surface corrigée. Aucun lot n'a à la fois une surface utile et une surface corrigée actives",
            "plan_de_controle": "P4, P5",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Secteur ou Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Patrimoine/Descriptif Patrimoine/Descriptif/Recherche liste patrimoine/Code ESI",
            "champ_ulis": "PA_MONCODE"
        },
        "Adresse": {
            "definition": "Emplacement géographique d'un logement ou d'une propriété, comprenant les informations suivantes : numéro de rue, le nom de la rue, la ville, et le code postal.",
            "regles_de_gestion": "Tous les lots ont un code postal présent dans le référentiel. Tous les lots ont un code commune INSEE présent dans le référentiel",
            "plan_de_controle": "P1, P2",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Secteur ou Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Patrimoine/Descriptif Patrimoine/Descriptif/Recherche liste patrimoine/Code ESI",
            "champ_ulis": "PA_MONCODE"
        },
        "Code ESI": {
            "definition": "Le code ESI est l'identifiant permettant de codifier le patrimoine. Il est composé de 5 niveaux de hiérarchie maximum : Lotissement, Ensemble similaires (ex: même année), Immeuble, Porte, Appartement.",
            "regles_de_gestion": "Le 8ème caractère est cohérent avec sa nature",
            "plan_de_controle": "P10, P11",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Secteur ou Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Patrimoine/Descriptif Patrimoine/Descriptif/Recherche liste patrimoine",
            "champ_ulis": "PA_MONCODE"
        },
        "Typologie (T2, T3…)​": {
            "definition": "Définit la taille d'un logement en fonction de son nombre de pièces. Un T3 est un appartement avec trois chambres à coucher, salon et cuisine.",
            "regles_de_gestion": "Tous les lots ont une typologie. Typologie supérieure > T7 rare, à valider au cas par cas",
            "plan_de_controle": "P14",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Secteur ou Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Patrimoine/Descriptif Patrimoine/Descriptif/Recherche liste patrimoine",
            "champ_ulis": "PA_MONCODE"
        },
        "Date de naissance signataire de bail": {
            "definition": "La date de naissance d'un tiers est saisie lors de la signature d'un bail.",
            "regles_de_gestion": "L'âge à la signature du bail est compris entre 16 ans et 109 ans. Son âge actuel n'est pas supérieur à 109 ans",
            "plan_de_controle": "C8, C17",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Tiers et Organisation/Personne Physique/ R. personne physique",
            "champ_ulis": "TO_MONCODE"
        },
        "Numéro Siret": {
            "definition": "Un numéro SIRET correspond à un identifiant unique attribué à une entreprise ou organisation, permettant de la distinguer légalement dans les bases de données administratives. Il se compose de 14 chiffres, dont le numéro SIREN à 9 chiffres suivi d'un numéro NIC à 5 chiffres, pour identifier précisément l'entité gestionnaire des biens locatifs.",
            "regles_de_gestion": "Un SIRET doit être renseigné pour les tiers avec une activité. Tous les siret ont 14 caractères",
            "plan_de_controle": "C9, C7",
            "responsable": "Antoine Dupont",
            "origine": "Gestionnaire Locatif",
            "source": "Ulis",
            "chemin": "Tiers et Organisation/Personne Physique/ R. personne physique",
            "champ_ulis": "TO_MONCODE"
        }
    }
    return dictionnaire

# Chargement des données
dictionnaire = chargement_brut_dictionnaire()

# Interface utilisateur Streamlit
st.title("Dictionnaire de Données")

# Champ de saisie avec rafraîchissement automatique
input_text = st.text_input("Recherchez un terme :", "", key="input")

# Suggestions basées sur l'entrée utilisateur
if input_text:
    input_text_normalized = supprimer_accents(input_text).lower()
    suggestions = [
        mot for mot in dictionnaire.keys()
        if input_text_normalized in supprimer_accents(mot).lower()
    ][:3]  # Limiter à 5 suggestions

    if suggestions:
        st.subheader("Suggestions")

        # Gestion de l'affichage des colonnes
        cols = st.columns(len(suggestions))
        mot_selectionne = None

        for idx, mot in enumerate(suggestions):
            definition = dictionnaire[mot]["definition"]
            short_definition = (
                definition[:100] + "..." if len(definition) > 100 else definition
            )  # Limite la taille de la définition

            with cols[idx]:
                if st.button(f"**{mot}**\n\n{short_definition}", key=mot):
                    mot_selectionne = mot

        # Affichage des détails au centre si une carte est cliquée
        if mot_selectionne:
            details = dictionnaire[mot_selectionne]
            st.markdown("---")
            st.markdown(f"### Détails pour : **{mot_selectionne}**")
            st.write(f"**Définition :** {details['definition']}")
            st.write(f"**Règles de Gestion :** {details['regles_de_gestion']}")
            st.write(f"**Plan de Controle :** {details['plan_de_controle']}")
            st.write(f"**Responsable :** {details['responsable']}")
            st.write(f"**Origine :** {details['origine']}")
            st.write(f"**Source :** {details['source']}")
            st.write(f"**Chemin :** {details['chemin']}")
            st.write(f"**Champ Ulis :** {details['champ_ulis']}")
    else:
        st.info("Aucune suggestion trouvée.")
else:
    st.info("Veuillez entrer un terme pour commencer la recherche.")
