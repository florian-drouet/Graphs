def make_set(parent, vertex):
    '''
    La fonction make_set permet de créer un singleton 
    '''
    parent[vertex] = None

def find(parent, vertex):
    '''
    La fonction find permet de remonter l'arbre à partir d'un vertex jusqu'à la racine de l'arbre (une racine nulle n'a
    pas de parent). Elle renvoie le parent du vertex en question.
    '''
    if parent[vertex] == None:
        return vertex
    return find(parent, parent[vertex])

def union(parent, vertex1, vertex2):
    '''
    La fonction union permet de réunir deux vertices par leurs racines
    '''
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)
    if root1 != root2:
        parent[root2] = root1

def kruskal(edges, vertices, clusters=1):
    '''
    Ci-après la deuxième version de l'algorithme de Kruskal codée via la technique union-find.
    
    On commence par créer un singleton par vertex puis on trie les edges (un edge est un triplé composé de la façon
    suivante : vertex1, vertex2, poids de l'edge vertex1 vers vertex2)
    
    Dans cette liste d'edge trié on cherche les racines des vertices 1 et 2 (pour chaque edge de la liste des edges triés)
    via la fonction find. Puis, s'ils n'ont pas la même racine, alors on rassemble les deux vertices via la fonction 
    union puis on rajoute l'edge dans l'edge de recouvrement de poids minimal.
    '''
    minimum_spanning_tree = []
    cost = 0
    parent = dict()
    for vertex in vertices:
        make_set(parent, vertex)
    edges_sorted = sorted(edges,key=lambda cost: cost[2])
    for edge in edges_sorted:
        if find(parent, edge[0]) != find(parent, edge[1]):
            union(parent, edge[0], edge[1])
            minimum_spanning_tree.append(edge)
            cost = cost + edge[2]
        if list(parent.values()).count(None) == clusters:
            break
    return minimum_spanning_tree, cost

## Better implementation of union-find below

def make_set_v2(parent, rang, sommet):
    '''
    La fonction make_set permet de créer un singleton 
    '''
    parent[sommet] = sommet
    rang[sommet] = 0

def find_v2(parent, sommet):
    '''
    La fonction find permet de remonter l'arbre à partir d'un sommet jusqu'à la racine de l'arbre (une racine nulle n'a
    pas de parent). Elle renvoie le parent du sommet en question.
    '''
    if parent[sommet] != sommet:
        parent[sommet] = find_v2(parent, parent[sommet])
    return parent[sommet]

def union_v2(parent, rang, sommet1, sommet2):
    '''
    La fonction union permet de réunir deux sommets par leurs racines
    '''
    racine1 = find_v2(parent, sommet1)
    racine2 = find_v2(parent, sommet2)
    if racine1 != racine2:
        if rang[racine1] < rang[racine2]:
            parent[racine1] = racine2
        else:
            parent[racine2] = racine1
            if rang[racine1] == rang[racine2]:
                rang[racine1] = rang[racine1] + 1

def kruskal_v2(arcs, sommets):
    '''
    Ci-après la deuxième version de l'algorithme de Kruskal codée via la technique union-find.
    
    On commence par créer un singleton par sommet puis on trie les arcs (un arc est un triplé composé de la façon
    suivante : sommet1, sommet2, poids de l'arc sommet1 vers sommet2)
    
    Dans cette liste d'arc trié on cherche les racines des sommets 1 et 2 (pour chaque arc de la liste des arcs triés)
    via la fonction find. Puis, s'ils n'ont pas la même racine, alors on rassemble les deux sommets via la fonction 
    union puis on rajoute l'arc dans l'arbre de recouvrement de poids minimal.
    '''
    arbre_poids_minimal = []
    cout = 0
    parent = dict()
    rang = dict()
    for sommet in sommets:
        make_set_v2(parent, rang, sommet)
    arcs_sorted = sorted(arcs,key=lambda cout: cout[2])
    for arc in arcs_sorted:
        if find_v2(parent, arc[0]) != find_v2(parent, arc[1]):
            union_v2(parent, rang, arc[0], arc[1])
            arbre_poids_minimal.append(arc)
            cout = cout + arc[2]
        print(parent)
    return arbre_poids_minimal, cout

if __name__ == "__main__":
    edges = [[1,5,10],[3,5,20],[2,8,30],[1,3,35],[6,7,40],[6,8,50],[7,8,75],
             [2,6,80],[2,4,100],[2,5,150],[4,7,180],[2,3,200],[3,4,200],[1,4,300],[2,7,300]]
    vertices = [1,2,3,4,5,6,7,8]
    clusters = 1
    kruskal_result = kruskal(edges,vertices,clusters)
    print(kruskal_result[0])
    kruskal_result_v2 = kruskal_v2(edges,vertices)
    print(kruskal_result[0])
