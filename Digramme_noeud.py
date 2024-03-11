import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

#G.add_edge("")


page_principale = [("Page Principale", "Tutoriel"),
                    ("Page Principale", "Démo"),
                    ("Page Principale", "Documentation"), 
                    ("Page Principale", "Console"), 
                    ("Page Principale", "Editeur"), 
                    ("Page Principale", "Galerie"), 
                    ("Page Principale", "Ressources"),
                    ("Page Principale", "Vitesse d'exécution"),
                    ("Page Principale", "Wiki"),
                    ("Page Principale", "Présentations brython"),
                    ("Console", "Page Principale"),]

tutoriel = [("Tutoriel", "Page Principale"), ("Tutoriel", "Démo"), ("Tutoriel", "Documentation"), ("Tutoriel", "Console"), ("Tutoriel", "Editeur"), ("Tutoriel", "Galerie"), ("Tutoriel", "Ressources")]

G.add_edges_from(page_principale)
nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.show()


#, "Documentation", "Console", "Editeur", "Galerie", "Ressources",  "Démo"

#Ajouter des couleurs pour les parties non traduites, les parties cachées, etc...

#Faire des listes avec chaque composants et dire a quoi il est relié 
#Mettre toutes ces listes dans une liste (avec des sous listes)

#faire un add_edge_from(nom de la liste)

#choissir correctement le type de graphique
