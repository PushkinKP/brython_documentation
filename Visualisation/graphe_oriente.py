import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Lire les données à partir du fichier texte
with open('liens_brython.txt', 'r') as f:
    for line in f:
        src, dest_lang = line.split(' -> ')
        dest, lang = dest_lang.split(' (')
        lang = lang.strip(')\n')
        G.add_edge(src, dest)

# Vérifier les nœuds sans voisins sortants
no_out_neighbors = [node for node in G.nodes() if not any(G.successors(node))]

# Option pour afficher ou non les noms des nœuds
show_node_labels = False

# Fonction pour gérer les clics sur les nœuds
def on_node_click(event):
    if event.xdata is not None and event.ydata is not None:
        for node, (x, y) in pos.items():
            if (x - event.xdata)**2 + (y - event.ydata)**2 < 0.01:  # Rayon de tolérance pour le clic
                print("Nom du nœud:", node)
                break

plt.figure(figsize=(12, 8))

# Dessiner les nœuds avec ou sans labels en fonction de l'option
pos = nx.spring_layout(G, seed=42)
if show_node_labels:
    nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_weight='bold')
else:
    nx.draw(G, pos, node_size=1000, font_size=10, font_weight='bold')

# Colorer les nœuds sans voisins (pages cachées) sortants en rouge
nx.draw_networkx_nodes(G, pos, nodelist=no_out_neighbors, node_color='red', node_size=1000)

plt.title("Graphe orienté des liens Brython")
plt.gca().set_axis_off()
plt.gca().set_aspect('equal')
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())

plt.connect('button_press_event', on_node_click)  # Connecter l'événement de clic de la souris à la fonction on_node_click

plt.show()
