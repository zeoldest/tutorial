#-*- coding:utf-8 -*-

from math import *
from Tkinter import *


def cercle(x, y, r, coul ='black'):
    """ Trace un cercle de centre (x,y) et de rayon r """
    can.create_oval(x-r, y-r, x+r, y+r, outline=coul)

def point(x, y,r = 3, coul ='black'):
    """ Trace un point noire de centre (x,y) et de rayon 3 """
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)

def Dessine(modulo, table):
    """ Fonction appelé à chaque image, déssine la table pour un modulo donné """
    
    # On efface tout
    can.delete(ALL)
    
    # On creer les lignes du repère (Car l'origine 0,0,0 corespond à la partie en haut à gauche)
    can.create_line(300, 0, 300, 600, fill ='blue')
    can.create_line(0, 300, 600, 300, fill ='blue')
    
    # On met a jour le texte de la table et le modulo et on le place sur le dessin
    var.set("Table de "+str(table)+" modulo "+str(modulo))
    can.create_text(0 + 100, 600 - 50,text = var.get())
    
    # On trace le cercle de centre (300,300) et de rayon 200
    cercle(300, 300, 200)
    
    # Pour chaques entier compris entre 0 et le modulo donné
    for n in range(modulo):
        # On trace le point (x,y) corespondant sur le cercle
        
        
        # Explication mathématique :
        
        # théta = (2*pi)/modulo -> Permet de trouver l'angle pour diviser le cercle en modulo parties
        # On part du point situé à l'angle - pi/2 Z0 = e^i(- pi/2) [en effet ici le repère en reversé horizontalement]
        # Pour obtenir le n suivant on ajoute n*théta à l'angle initial
        # D'où Zn = e^i(- pi/2 + n*théta)
        # En se situant dans un repère complexe, on obtient vite pour un cercle de rayon 200 :
        # x = 200 * cos(- pi/2 + (n*théta) / modulo) <=> x = 200 * cos( pi/2 - (n*théta) / modulo) <=> 200 * sin( (n*théta) / modulo )
        # y = 200 * sin(- pi/2 + (n*théta) / modulo) <=> y = -200 * sin( pi/2 - (n*théta) / modulo) <=> -200 * cos( (n*théta) / modulo )
        # Il ne reste plus qu'à centrer le cercle au point (300,300)
        
        
        
        x = 200*(sin(n*2*pi/modulo))+300
        y = -200*(cos(n*2*pi/modulo))+300
        point(x, y)
        # On trace la droite entre le premier point et le point correspondant à son multiple par la table
        r = n*table
        x2 = 200*(sin(r*2*pi/modulo))+300
        y2 = -200*(cos(r*2*pi/modulo))+300
        can.create_line(x, y, x2, y2, fill ='red')
        # On écrit les numéros au-dessus des points sur un cercle de centre (300,300) de rayon 220 (soit 20 de plus que le cercle sur lequel se trouvent les points)
        can.create_text( 220*(sin(n*2*pi/modulo))+300, -220*(cos(n*2*pi/modulo))+300,text = str(n))

def Play():
    """ Fonction qui appelle les autres """
    
    loop.set(True)
    # On récupère la saisie
    a = re.findall(r'([0-9]*)-?([0-9]*)', entr2.get())
    mod = a[0]
    b = re.findall(r'([0-9]*)-?([0-9]*)', entr1.get())
    tab = b[0]
    
    # On regarde si on a un intervalle '-' ou pas
    # Si il y en a un dans le modulo, on le fait varier du permier modulo au deuxième par incrémentation de 1
    if mod[1] != '' and tab[1] == '' :
        for i in range(int(mod[0]), int(mod[1])+1):
            Dessine(i, int(tab[0]))
            can.update()
            fen.after(int(1000/(float(entr3.get()))))
            # Si on a appuyé sur stop, on stop l'incrementation
            if loop.get() == False : break

    # Si il y en a un dans la table, on la fait varier de la permière table à la deuxième par incrémentation de 1
    if tab[1] != '' and mod[1] == '' :
        for i in range(int(tab[0]), int(tab[1])+1):
            Dessine(int(mod[0]), i)
            can.update()
            fen.after(int(1000/(float(entr3.get()))))
            # Si on a appuyé sur stop, on stop l'incrementation
            if loop.get() == False : break

    # Si il y a deux intervalles, on incrémente la table puis le modulo
    if mod[1] != '' and tab[1] != '' :
        for i in range(int(mod[0]), int(mod[1])+1):
            # Si on a appuyé sur stop, on stop l'incrementation
            if loop.get() == False : break
            for j in range(int(tab[0]), int(tab[1])+1):
                Dessine(i, j)
                can.update()
                fen.after(int(1000/(float(entr3.get()))))
                # Si on a appuyé sur stop, on stop l'incrementation
                if loop.get() == False : break

    # Si il n'y a aucun intervalle, on dessine juste une image
    if mod[1] == '' and tab[1] == '' :
        Dessine(int(mod[0]), int(tab[0]))

def Stop():
    """ Fonction qui arrête le programme et efface """
    loop.set(False)
    can.delete(ALL)
    var.set('')



##### Programme principal : ############
fen = Tk()
fen.title("Arythmétique Modulaire - Les Tables de Multiplications")
can = Canvas(fen, width =600, height =600, bg ='ivory')

# Mise en place des variables, textes, boutons ...
loop = BooleanVar()
loop.set(True)
txt1 = Label(fen, text ='Table :')
txt2 = Label(fen, text ='Modulo :')
var = StringVar()
var.set("")
txt3 = Label(fen, text ='Images par seconde :')
entr1 = Entry(fen)
entr2 = Entry(fen)
entr3 = Entry(fen)
b1 = Button(fen, text ='OK', command = Play)
b2 = Button(fen, text ='STOP', command = Stop)

# Mise en page à l'aide de la méthode 'grid' :
txt1.grid(row =1, sticky =E)
txt2.grid(row =2, sticky =E)
txt3.grid(row =3, sticky =E)
entr1.grid(row =1, column =2)
entr2.grid(row =2, column =2)
entr3.grid(row =3, column =2)
b2.grid(row =4, column =2)
b1.grid(row =4, column =1)
can.grid(row =1, column =3, rowspan =3, padx =10, pady =5)

# On ajoute des valeurs par défauts
entr3.insert(0, "1")
entr2.insert(0, "10")
entr1.insert(0, "2")

fen.mainloop()