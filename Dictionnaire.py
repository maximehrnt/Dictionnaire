from unicodedata import normalize, category
from tkinter import Tk, Label, Listbox, Entry
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import os

# Obtenir le chemin correct pour les fichiers en fonction de l'environnement
def chemin_relatif(fichier):
    if getattr(sys, 'frozen', False):  # Cas de l'exécutable compilé
        base_path = sys._MEIPASS  # Répertoire temporaire PyInstaller
    else:
        base_path = os.path.abspath(".")  # Répertoire courant en mode développement
    return os.path.join(base_path, fichier)

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
        "Loyer": {
            "definition": "Somme d'argent versée périodiquement par le locataire au propriétaire.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Bail": {
            "definition": "Contrat qui lie un locataire et un propriétaire pour un logement.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Quittance": {
            "definition": "Reçu délivré pour attester du paiement d'un loyer.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Caution": {
            "definition": "Somme d'argent déposée en garantie au début d'un bail.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Charges": {
            "definition": "Coût des services associés au logement (eau, chauffage, etc.).",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Immeuble": {
            "definition": "Bâtiment regroupant plusieurs logements.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Résidence": {
            "definition": "Ensemble de logements regroupés en une même localisation.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Appartement": {
            "definition": "Logement composé de plusieurs pièces dans un immeuble.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Studio": {
            "definition": "Petit appartement d'une seule pièce avec commodités.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "T1": {
            "definition": "Appartement avec une chambre à coucher, salon et cuisine.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "T2": {
            "definition": "Appartement avec deux chambres à coucher, salon et cuisine.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "T3": {
            "definition": "Appartement avec trois chambres à coucher, salon et cuisine.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "T4": {
            "definition": "Appartement avec quatre chambres à coucher, salon et cuisine.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "T5": {
            "definition": "Appartement avec cinq chambres à coucher, salon et cuisine.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "T6": {
            "definition": "Appartement avec six chambres à coucher, salon et cuisine.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Maison": {
            "definition": "Logement individuel souvent destiné à une seule famille.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Villa": {
            "definition": "Maison de standing généralement entourée d'un jardin.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Loft": {
            "definition": "Logement atypique souvent aménagé dans un ancien bâtiment industriel.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Garage": {
            "definition": "Espace couvert destiné au stationnement d'un véhicule.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Parking": {
            "definition": "Espace ouvert ou couvert destiné au stationnement.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Terrain": {
            "definition": "Terrain destiné à la construction d'un logement ou autre.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Lotissement": {
            "definition": "Ensemble de terrains ou bâtiments regroupés pour être aménagés.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Syndic": {
            "definition": "Organisme en charge de la gestion d'un immeuble.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Co-propriété": {
            "definition": "Propriété partagée entre plusieurs copropriétaires.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Entretien": {
            "definition": "Action de maintenir un bâtiment ou équipement en bon état.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Réhabilitation": {
            "definition": "Travaux visant à remettre un bâtiment en bon état.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Rénovation": {
            "definition": "Travaux destinés à moderniser un bâtiment.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Démolition": {
            "definition": "Action de détruire un bâtiment ou une structure.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Construction": {
            "definition": "Action de bâtir une structure ou un bâtiment.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Urbanisme": {
            "definition": "Discipline qui organise l'utilisation des sols et des espaces.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Aménagement": {
            "definition": "Action de modifier ou structurer un espace urbain ou rural.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Concession": {
            "definition": "Contrat ou accord pour l'utilisation d'un espace ou bien.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Prêt locatif": {
            "definition": "Crédit spécifique pour financer la location d'un logement.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Subvention": {
            "definition": "Aide financière accordée pour soutenir un projet de logement.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Agence Nationale de l'Habitat(ANAH)": {
            "definition": "Agence Nationale de l'Habitat, dédiée à l'amélioration des logements.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Caisse d'Allocations Familiales(CAF)": {
            "definition": "Caisse d'Allocations Familiales, apportant des aides financières.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Aide Personnalisée au Logement (APL)": {
            "definition": "Aide personnalisée au logement pour réduire le coût du loyer.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Prêt Locatif Aidé d'Intégration (PLAI)": {
            "definition": "Prêt Locatif Aidé d'Intégration pour financer le logement social.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Prêt Locatif Social (PLS)": {
            "definition": "Prêt Locatif Social pour logements intermédiaires.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Assurance": {
            "definition": "Contrat assurant contre les risques pour un logement.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Défiscalisation": {
            "definition": "Avantage fiscal accordé pour investir dans l'immobilier.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Investissement locatif": {
            "definition": "Action de placer de l'argent dans des biens immobiliers à louer.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Fonds propres": {
            "definition": "Capitaux propres d'une entreprise pour financer des projets.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Bailleur": {
            "definition": "Organisme ou entreprise qui met des logements à disposition.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Gestionnaire": {
            "definition": "Personne ou entité qui administre des biens immobiliers.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Patrimoine": {
            "definition": "Ensemble des biens immobiliers appartenant à un bailleur.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Charge locative": {
            "definition": "Charges liées à l'usage des parties communes d'un immeuble.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Surface Habitable": {
            "definition": "La surface habitable est la superficie d'un logement utilisable pour y vivre hors murs ou caves et garages.",
            "responsable": "Patrimoine",
            "origine": " Gesionnaire Secteur",
            "source": " Ulis",
        },
        "Surface Corrigée": {
            "definition": "La surface corrigée est une mesure pondérée tenant compte de la surface réelle et des caractéristiques du logement comme le confort ou la localisation.",
            "responsable": "Patrimoine",
            "origine": " Gesionnaire Secteur",
            "source": " Ulis",
        },
        "Vacance Stratégique": {
            "definition": " Un bien vacant peut l'être de manière volontaire pour différentes raisons (Etude/Sinistre/Démolition/Dommage Ouvrage/Autre).",
            "responsable": "Patrimoine",
            "origine": " Gesionnaire Secteur",
            "source": " Ulis",
        },
        "ESI": {
            "definition": "Numéro permettant de situer un bien dans l'arborescence SIA. Un logement peut être situé dans une arborescence à 5 niveaux maximum : Residence/Lot de logements (regroupés par caractéristiques communes), Immeuble, Porte d'entrée, Logement",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Prêt Locatif Aidé d'Intégration (PLAI)": {
            "definition": "Prêt Locatif Aidé d'Intégration pour financer le logement social.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Prêt Locatif Social (PLS)": {
            "definition": "Prêt Locatif Social pour logements intermédiaires.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Plan Local d'Urbanisme(PLU)": {
            "definition": "Plan Local d'Urbanisme définissant les règles de construction.",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
        "Surface Utile": {
            "definition": "La surface utile désigne la surface totale d'un logement, incluant toutes les pièces utilisables, mais excluant les murs, cloisons, escaliers et espaces non habitables (comme les balcons ou les caves).",
            "responsable": "Patrimoine",
            "origine": "Gestionnaire Secteur",
            "source": "Ulis",
        },
    }
    return dictionnaire


# Fonction pour supprimer les accents d'une chaîne
def supprimer_accents(chaine):
    return ''.join(
        c for c in normalize('NFD', chaine) if category(c) != 'Mn'
    )

# Fonction pour rechercher des mots correspondant au texte saisi
def rechercher_mots(event): 
    texte_saisi = barre_recherche.get().strip().lower()
    texte_saisi_sans_accents = supprimer_accents(texte_saisi)

    if not texte_saisi:
        liste_suggestions.delete(0, 'end')
        liste_suggestions.place_forget()
        label_definition.config(text="")
        return

    mots_suggérés = [
        mot for mot in dictionnaire 
        if texte_saisi_sans_accents in supprimer_accents(mot).lower()
    ]

    liste_suggestions.delete(0, 'end')
    if mots_suggérés:
        for mot in mots_suggérés:
            liste_suggestions.insert('end', mot)

        max_lignes = 5
        hauteur = min(len(mots_suggérés), max_lignes)
        liste_suggestions.configure(height=hauteur)
        liste_suggestions.place(relx=0.5, rely=0.35, anchor="center")
    else:
        liste_suggestions.place_forget()

    label_definition.config(text="")

# Fonction pour afficher la définition d'un mot sélectionné
def afficher_definition(event):
    selection = liste_suggestions.curselection()
    if selection:
        mot_selectionne = liste_suggestions.get(selection)
        barre_recherche.delete(0, 'end')
        barre_recherche.insert(0, mot_selectionne)

        details = dictionnaire.get(mot_selectionne, {})
        definition = details.get("definition", "Définition non-renseignée.")
        responsable = details.get("responsable", "Responsable non-renseigné.")
        origine = details.get("origine", "Origine non-renseignée.")
        source = details.get("source", "Source non-renseignée.")
        texte_affiche = (
            f"Définition : {definition}\n\n\n"
            f"Responsable donnée : {responsable}\n\n"
            f"Origine de la donnée : {origine}\n\n"
            f"Source référence : {source}"
        )
        label_definition.config(text=texte_affiche)

# Chargement des données
dictionnaire = chargement_brut_dictionnaire()

# Création de l'interface graphique
root = Tk()
root.title("Dictionnaire de données")
root.geometry("800x600")
root.configure(background="lightblue")

# Affichage du logo
logo_img = Image.open(chemin_relatif('Logo.png'))
logo_img = logo_img.resize((300, 200), Image.Resampling.LANCZOS)
logo_tk = ImageTk.PhotoImage(logo_img)

label_logo = Label(root, image=logo_tk, background="lightblue")
label_logo.place(relx=0.5, rely=0.1, anchor="center")

label_question = ttk.Label(root, text="Que cherchez-vous ?", font=("Arial", 16), background="lightblue")
label_question.place(relx=0.49, rely=0.2, anchor="e")

barre_recherche = ttk.Entry(root, font=("Arial", 14))
barre_recherche.place(relx=0.51, rely=0.2, anchor="w")

liste_suggestions = Listbox(root, font=("Arial", 14), background="lightblue", width=40)
label_definition = ttk.Label(root, text="", font=("Arial", 14), wraplength=650, justify="left", background="lightblue")
label_definition.place(relx=0.1, rely=0.5)

barre_recherche.bind("<KeyRelease>", rechercher_mots)
liste_suggestions.bind("<<ListboxSelect>>", afficher_definition)

root.mainloop()