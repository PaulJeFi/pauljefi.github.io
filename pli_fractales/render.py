import pygame  # Import de Pygame, module graphique
import math # Import du module math. Cela servira pour la triginométrie.

pygame.init() # Initialisation du module Pygame
    
WHITE = (255, 255, 255)   # Définition des couleurs
BLACK = (0, 0, 0)

haut = 755
large = 1000

dis = pygame.display.set_mode((large, haut))    # Création de la fenêtre Pygame.
pygame.display.set_caption(" L-System ")
dis.fill(WHITE)
pygame.display.update()
    
def resize(coord) :         # Sur Pygame, le repère est inversé sur l'axe des Y.
    return (coord[-2], haut - coord[-1])
    
def comprendre(mot, angle=90, size=10) : # Transformer un mot en coordonnées de
                                         # segments
    coord = []
    old_coord = 0
    young_coord = (large/2, haut-haut/4)
    angle_actual = 0
    for i in range(len(mot)) :
        if mot[i] == "F" :
            old_coord = young_coord
            # Trigonométrie pour trouver les coordonnées par rapport à l'angle
            # actuel.
            young_coord = (
                old_coord[-2] - math.sin(math.radians(angle_actual)) * size,
                old_coord[-1] + math.cos(math.radians(angle_actual)) * size
                )
            coord.append((dis, BLACK, resize(old_coord), resize(young_coord)))
        elif mot[i] == "+" :
            angle_actual = (angle_actual+angle)
        elif mot[i] == "-" :
            angle_actual = (angle_actual-angle)
    return coord
    
def trace(liste) :               # Tracer le graphique à partir des coordonnées.
    for i in range(0, len(liste)-1) :
        pygame.draw.line(*liste[i])
    pygame.display.update()

################################################################################
# Code intéressant ici

def plier(feuille: str, iteration: int, nb_plis: int) -> str :

    # Lorsque aucun pli ne doit être fait, on retourne un mot vide.
    if iteration == 0 :
        return ''
    
    folded_feuille = '' # On part d'une feuille à plier, qui sera la feuille
                        # finale
    pli = 'V' # On commence par des plis vallées (à différencier des plis
              # montagnes, en crête et donc dans l'autre sens.)

    # On va, pour cette itération, se baser sur l'itération précedente.
    feuille = plier(feuille, iteration-1, nb_plis)

    ######################
    # Ici commence l'algorithme de pliage
    ######################
    # Pour chaque pli de la feuille :
    for Pli in feuille :
        folded_feuille += pli * nb_plis + Pli # On ajoute le nombre de plis
                                              # entre chaque pli de l'itération
                                              # précédente
        # Puis on chage le type de pli
        if pli == 'V' :
            pli = 'M'
        else : 
            pli = 'V'
    folded_feuille += pli * nb_plis # On n'oublie pas d'ajouter des plis à la
                                    # fin de la bande

    return folded_feuille

################################################################################

def pli_to_l_system(feuille: str) :
    'Convertiseur feuille pliée -> l_système'
    l_sys = feuille.replace('V', 'F+')
    return l_sys.replace('M', 'F-')
        
trace(comprendre(pli_to_l_system(plier('', 10, 2)), int(180/3), 1.5))# Affichage
        
stop = False
while not stop :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            stop = True
pygame.quit()
quit()    