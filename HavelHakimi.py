import networkx as nx
import matplotlib.pyplot as plt
from random import choice

def test(lst, vathmos):
    G = nx.Graph()
    for i in range(len(lst)):
        x = choice(lst)
        while vathmos[x] == 0:
            x = choice(lst)
        tmp = vathmos[:]
        tmp[x] = 0           #για να μην συνδεθεί ο κόμβος με τον εαυτό του
        for j in range(vathmos[x]):
            ind = tmp.index(max(tmp))
            G.add_edge(x, ind)
            tmp[ind] -=1
            vathmos[ind] = tmp[ind] #αντιγράφω την αλλαγή στο original array
            tmp[ind] = 0       #για να μην συνδεθεί ο κόμβος με έναν άλλο πάνω από μία φορά (με παίδεψε πολύ αυτό!)
        vathmos[x] = 0
        if all(v==0 for v in vathmos):
            nx.draw_networkx(G)
            break

def check(lst):
    while True:
        lst.sort(reverse=True)
        x = lst[0]
        lst.pop(0)
        for i in range(x):
            try:
                lst[i] -= 1
            except IndexError:
                return False
        if any(v<0 for v in lst):
            return False
        if all(v==0 for v in lst):
            return True

def insert(n):
    lst = [i for i in range(n)]
    vathmos =[]
    for i in range(n):
        x = int(input(f"Εισάγετε αριθμό δεσμών για τον {i + 1}ο κόμβο: "))
        vathmos.append(x)
    if check(vathmos[:]):   #ελέγχω αν η ακολουθία είναι γραφική, περνάω ένα αντίγραφο της λίστας με call by value
        test(lst, vathmos)
    else:
        print("Αυτή η ακολουθία δεν είναι γραφική.")

def main():
    while True:
        x = input("Εισάγετε αριθμό κόμβων: ")
        try:
            n = int(x)
            if n <=1:
                print("Ο αριθμός πρέπει να είναι μεγαλύτερος του 1. ", end='')
                continue
            insert(n)
            plt.show()
            break
        except ValueError:
            print("Απαιτείται ακέραιος αριθμός. ", end='')

if __name__ == '__main__':
    main()