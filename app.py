import streamlit as st
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3
import os

# Configuration de la page
st.set_page_config(
    page_title="AttractionRater",
    page_icon="🎢",
    layout="wide"
)

# Initialisation de la base de données
def init_database():
    """Initialise la base de données avec les tables nécessaires"""
    conn = sqlite3.connect('attractions.db')
    c = conn.cursor()
    
    # Table des attractions
    c.execute('''
        CREATE TABLE IF NOT EXISTS attractions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE,
            description TEXT,
            note REAL,
            comparaisons INTEGER,
            victoires INTEGER,
            defaites INTEGER
        )
    ''')
    
    # Table de l'historique des comparaisons
    c.execute('''
        CREATE TABLE IF NOT EXISTS comparaisons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            gagnant TEXT,
            perdant TEXT,
            note_gagnant_avant REAL,
            note_perdant_avant REAL,
            note_gagnant_apres REAL,
            note_perdant_apres REAL
        )
    ''')
    
    # Insérer les données par défaut si la table est vide
    c.execute('SELECT COUNT(*) FROM attractions')
    if c.fetchone()[0] == 0:
        attractions_par_defaut = [
            ('Space Mountain', 'Montagnes russes spatiales à grande vitesse', 1500, 0, 0, 0),
            ('Big Thunder Mountain', 'Montagnes russes minières dans le Far West', 1450, 0, 0, 0),
            ('Pirates of the Caribbean', 'Croisière à travers des scènes de pirates', 1420, 0, 0, 0),
            ('It\'s a Small World', 'Croisière à travers des pays du monde', 1380, 0, 0, 0),
            ('Splash Mountain', 'Chute en flume à travers la Louisiane', 1480, 0, 0, 0),
            ('Indiana Jones Adventure', 'Aventure en Jeep à travers des temples dangereux', 1460, 0, 0, 0)
        ]
        c.executemany('''
            INSERT INTO attractions (nom, description, note, comparaisons, victoires, defaites)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', attractions_par_defaut)
    
    conn.commit()
    conn.close()

# Fonctions de gestion de la base de données
def get_attractions():
    """Récupère toutes les attractions depuis la base de données"""
    conn = sqlite3.connect('attractions.db')
    attractions_df = pd.read_sql_query('SELECT * FROM attractions', conn)
    conn.close()
    return attractions_df

def save_attraction(nom, description, note=1500, comparaisons=0, victoires=0, defaites=0):
    """Sauvegarde une nouvelle attraction dans la base de données"""
    conn = sqlite3.connect('attractions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO attractions (nom, description, note, comparaisons, victoires, defaites)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nom, description, note, comparaisons, victoires, defaites))
    conn.commit()
    conn.close()

def update_attraction(attraction_id, nom, description, note, comparaisons, victoires, defaites):
    """Met à jour une attraction dans la base de données"""
    conn = sqlite3.connect('attractions.db')
    c = conn.cursor()
    c.execute('''
        UPDATE attractions 
        SET nom=?, description=?, note=?, comparaisons=?, victoires=?, defaites=?
        WHERE id=?
    ''', (nom, description, note, comparaisons, victoires, defaites, attraction_id))
    conn.commit()
    conn.close()

def delete_attraction(attraction_id):
    """Supprime une attraction de la base de données"""
    conn = sqlite3.connect('attractions.db')
    c = conn.cursor()
    c.execute('DELETE FROM attractions WHERE id=?', (attraction_id,))
    conn.commit()
    conn.close()

def save_comparaison(gagnant, perdant, note_gagnant_avant, note_perdant_avant, note_gagnant_apres, note_perdant_apres):
    """Sauvegarde une comparaison dans l'historique"""
    conn = sqlite3.connect('attractions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO comparaisons (timestamp, gagnant, perdant, note_gagnant_avant, note_perdant_avant, note_gagnant_apres, note_perdant_apres)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (datetime.now(), gagnant, perdant, note_gagnant_avant, note_perdant_avant, note_gagnant_apres, note_perdant_apres))
    conn.commit()
    conn.close()

def get_comparaisons():
    """Récupère l'historique des comparaisons"""
    conn = sqlite3.connect('attractions.db')
    comparaisons_df = pd.read_sql_query('SELECT * FROM comparaisons ORDER BY timestamp DESC', conn)
    conn.close()
    return comparaisons_df

# Fonctions Elo
def calculate_elo_rating(wins, losses, draws):
    """Calcule la différence Elo basée sur les victoires, défaites et nuls"""
    games = wins + losses + draws
    if games == 0:
        return 0
    winning_fraction = (wins + 0.5 * draws) / games
    return -400 * math.log10(1.0/winning_fraction - 1.0)

def probability_of_winning(elo_diff):
    """Calcule la probabilité de victoire basée sur la différence Elo"""
    return 1 / (1 + 10 ** (-elo_diff / 400))

# Initialisation de la base de données
init_database()

# Initialisation de l'état de session
if 'current_pair' not in st.session_state:
    st.session_state.current_pair = None

# Fonctions utilitaires
def get_random_pair():
    """Sélectionne deux attractions aléatoires pour comparaison"""
    attractions = get_attractions()
    if len(attractions) < 2:
        return None
    
    indices = np.random.choice(len(attractions), 2, replace=False)
    return (attractions.iloc[indices[0]], attractions.iloc[indices[1]])

def update_ratings(winner, loser):
    """Met à jour les notes Elo après une comparaison"""
    K = 32  # Facteur K pour la sensibilité des changements
    
    # Calcul de la différence Elo actuelle
    elo_diff = winner['note'] - loser['note']
    
    # Probabilité attendue que le gagnant gagne
    expected_win = probability_of_winning(elo_diff)
    
    # Mise à jour des notes
    new_winner_rating = winner['note'] + K * (1 - expected_win)
    new_loser_rating = loser['note'] + K * (0 - (1 - expected_win))
    
    # Mise à jour de la base de données
    update_attraction(
        winner['id'], 
        winner['nom'], 
        winner['description'], 
        new_winner_rating, 
        winner['comparaisons'] + 1, 
        winner['victoires'] + 1, 
        winner['defaites']
    )
    
    update_attraction(
        loser['id'], 
        loser['nom'], 
        loser['description'], 
        new_loser_rating, 
        loser['comparaisons'] + 1, 
        loser['victoires'], 
        loser['defaites'] + 1
    )
    
    # Sauvegarde de la comparaison dans l'historique
    save_comparaison(
        winner['nom'], 
        loser['nom'], 
        winner['note'], 
        loser['note'], 
        new_winner_rating, 
        new_loser_rating
    )

# Interface utilisateur
st.title("🎢 AttractionRater")
st.markdown("""
Notez les attractions des parcs d'attractions en les comparant deux à deux, 
comme Mark Zuckerberg l'a fait avec les visages dans *The Social Network*.
Les données sont sauvegardées dans une base de données en ligne.
""")

# Sidebar pour les contrôles
with st.sidebar:
    st.header("Contrôles")
    
    if st.button("Nouvelle comparaison"):
        st.session_state.current_pair = get_random_pair()
        st.rerun()
    
    st.header("Statistiques")
    comparaisons_df = get_comparaisons()
    total_comparisons = len(comparaisons_df)
    st.metric("Comparaisons effectuées", total_comparisons)
    
    if total_comparisons > 0:
        last_comparison = comparaisons_df.iloc[0]
        st.caption(f"Dernière comparaison: {last_comparison['gagnant']} vs {last_comparison['perdant']}")
    
    # Bouton pour réinitialiser les données
    if st.button("Réinitialiser les données", type="secondary"):
        init_database()
        st.session_state.current_pair = None
        st.rerun()

# Section principale
if st.session_state.current_pair is None:
    st.session_state.current_pair = get_random_pair()

if st.session_state.current_pair:
    attraction1, attraction2 = st.session_state.current_pair
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(attraction1['nom'])
        st.write(attraction1['description'])
        st.metric("Note actuelle", f"{attraction1['note']:.0f}")
        st.metric("Victoires", int(attraction1['victoires']))
        
        if st.button(f"Choisir {attraction1['nom']}", key="btn1", use_container_width=True):
            update_ratings(attraction1, attraction2)
            st.session_state.current_pair = None
            st.rerun()

    with col2:
        st.subheader(attraction2['nom'])
        st.write(attraction2['description'])
        st.metric("Note actuelle", f"{attraction2['note']:.0f}")
        st.metric("Victoires", int(attraction2['victoires']))
        
        if st.button(f"Choisir {attraction2['nom']}", key="btn2", use_container_width=True):
            update_ratings(attraction2, attraction1)
            st.session_state.current_pair = None
            st.rerun()
else:
    st.warning("Ajoutez au moins deux attractions pour pouvoir les comparer.")

# Classement des attractions
st.header("Classement des attractions")
attractions_df = get_attractions()
sorted_attractions = attractions_df.sort_values('note', ascending=False)
sorted_attractions['Rang'] = range(1, len(sorted_attractions) + 1)
sorted_attractions['note'] = sorted_attractions['note'].round(0)

st.dataframe(
    sorted_attractions[['Rang', 'nom', 'note', 'victoires', 'defaites', 'comparaisons']],
    use_container_width=True,
    hide_index=True
)

# Graphique des notes
st.header("Évolution des notes")
comparaisons_df = get_comparaisons()
if not comparaisons_df.empty:
    # Créer un graphique d'évolution
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for _, attraction in attractions_df.iterrows():
        attraction_name = attraction['nom']
        attraction_history = []
        
        # Filtrer les comparaisons pour cette attraction
        att_comparaisons = comparaisons_df[
            (comparaisons_df['gagnant'] == attraction_name) | 
            (comparaisons_df['perdant'] == attraction_name)
        ].sort_values('timestamp')
        
        current_rating = 1500  # Note initiale par défaut
        
        for _, comp in att_comparaisons.iterrows():
            if comp['gagnant'] == attraction_name:
                attraction_history.append(comp['note_gagnant_apres'])
                current_rating = comp['note_gagnant_apres']
            elif comp['perdant'] == attraction_name:
                attraction_history.append(comp['note_perdant_apres'])
                current_rating = comp['note_perdant_apres']
        
        # Si l'attraction n'a pas d'historique, utiliser sa note actuelle
        if not attraction_history:
            attraction_history = [attraction['note']]
        
        # Raccourcir l'historique pour n'afficher que les 50 derniers points
        if len(attraction_history) > 50:
            attraction_history = attraction_history[-50:]
        
        ax.plot(attraction_history, label=attraction_name, linewidth=2)
    
    ax.set_xlabel('Comparaisons récentes')
    ax.set_ylabel('Note Elo')
    ax.set_title('Évolution des notes des attractions')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)
else:
    st.info("Effectuez quelques comparaisons pour voir l'évolution des notes.")

# Section pour ajouter de nouvelles attractions
st.header("Ajouter une nouvelle attraction")
with st.form("add_attraction"):
    new_name = st.text_input("Nom de l'attraction")
    new_description = st.text_area("Description")
    
    if st.form_submit_button("Ajouter l'attraction"):
        if new_name and new_description:
            # Vérifier si l'attraction existe déjà
            if new_name in attractions_df['nom'].values:
                st.error("Cette attraction existe déjà!")
            else:
                save_attraction(new_name, new_description)
                st.success(f"Attraction '{new_name}' ajoutée avec succès!")
                st.rerun()
        else:
            st.error("Veuillez remplir tous les champs.")

# Section pour supprimer des attractions
st.header("Gérer les attractions")
if not attractions_df.empty:
    attraction_to_delete = st.selectbox(
        "Sélectionnez une attraction à supprimer",
        attractions_df['nom'].tolist()
    )
    
    if st.button("Supprimer l'attraction", type="secondary"):
        if attraction_to_delete:
            attraction_id = attractions_df[attractions_df['nom'] == attraction_to_delete]['id'].values[0]
            delete_attraction(attraction_id)
            st.success(f"Attraction '{attraction_to_delete}' supprimée avec succès!")
            st.rerun()

# Instructions
with st.expander("Comment utiliser cette application?"):
    st.markdown("""
    1. Cliquez sur "Nouvelle comparaison" pour faire apparaître deux attractions à comparer
    2. Choisissez l'attraction que vous préférez en cliquant sur le bouton correspondant
    3. Les notes Elo seront mises à jour automatiquement et sauvegardées
    4. Consultez le classement pour voir quelle attraction est la mieux notée
    5. Ajoutez de nouvelles attractions si nécessaire
    
    **Fonctionnalités de sauvegarde:**
    - Toutes vos comparaisons sont automatiquement sauvegardées dans une base de données SQLite
    - Les données persistent entre les sessions et sont partagées entre tous les utilisateurs
    - Vous pouvez réinitialiser toutes les données avec le bouton dans la sidebar
    
    Le système de notation utilise un algorithme similaire à Elo, qui ajuste les notes en fonction:
    - De la différence actuelle de notes entre les attractions
    - Du résultat de chaque comparaison
    
    Plus vous effectuez de comparaisons, plus le classement devient précis!
    """)