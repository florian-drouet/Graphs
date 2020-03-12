def make_set(parent, sommet):
    '''
    La fonction make_set permet de créer un singleton 
    '''
    parent[sommet] = None

def find(parent, sommet):
    '''
    La fonction find permet de remonter l'arbre à partir d'un sommet jusqu'à la racine de l'arbre (une racine nulle n'a
    pas de parent). Elle renvoie le parent du sommet en question.
    '''
    if parent[sommet] == None:
        return sommet
    return find(parent, parent[sommet])

def union(parent, sommet1, sommet2):
    '''
    La fonction union permet de réunir deux sommets par leurs racines
    '''
    racine1 = find(parent, sommet1)
    racine2 = find(parent, sommet2)
    if racine1 != racine2:
        parent[racine2] = racine1

def kruskal(arcs, sommets):
    '''
    Ci-après la deuxième version de l'algorithme de Kruskal codée via la technique union-find.
    
    On commence par créer un singleton par sommet puis on trie les arcs (un arc est un triplé composé de la façon
    suivante : sommet1, sommet2, poids de l'arc sommet1 vers sommet2)
    
    Dans cette liste d'arc trié on cherche les racines des sommets 1 et 2 (pour chaque arc de la liste des arcs triés)
    via la fonction find. Puis, s'ils n'ont pas la même racine, alors on rassemble les deux sommets via la fonction 
    union puis on rajoute l'arc dans l'arc de recouvrement de poids minimal.
    '''
    arbre_poids_minimal = []
    cout = 0
    parent = dict()
    for sommet in sommets:
        make_set(parent, sommet)
    arcs_sorted = sorted(arcs,key=lambda cout: cout[2])
    for arc in arcs_sorted:
        if find(parent, arc[0]) != find(parent, arc[1]):
            union(parent, arc[0], arc[1])
            arbre_poids_minimal.append(arc)
            cout = cout + arc[2]
    return arbre_poids_minimal, cout