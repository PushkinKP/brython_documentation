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

plt.figure(figsize=(12, 8))

# Dessiner les nœuds avec labels
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_weight='bold')

# Colorer les nœuds sans voisins (pages cachées) sortants en rouge
nx.draw_networkx_nodes(G, pos, nodelist=no_out_neighbors, node_color='red', node_size=1000)

plt.title("Graphe orienté des liens Brython")
plt.show()
