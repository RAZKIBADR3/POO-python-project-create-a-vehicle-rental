from datetime import datetime
import re
import os
class vehicule:
    def __init__(self,imma,marq,anneeAch,type):
        self.imma = imma
        self.marq = marq
        self.anneeAch = anneeAch
        self.type = type
    
    def anciennete(self):
        return (2022 - self.anneeAch)
    
    def saisie(self):
        self.imma = input('entrer immatricule\n')
        self.marq = input('entrer la marque\n')
        self.anneeAch = int(input('entrer l\'annee d\'achat\n'))
        self.type = input('entrer le type\n')

    def __str__(self):
        return f'le immatricule est : {self.imma} , la marque est : {self.marq} , la annee d\'achat est : {self.anneeAch} , le type est : {self.type}'


class location:
    def __init__(self,veh,dateD,nbj,PrixUPJ):
        self.veh = veh
        self.dateD = dateD
        self.nbj = nbj
        self.PrixUPJ = PrixUPJ
veh1 = vehicule("m0","comercial",2018,"moto")
veh2 = vehicule("v0","comercial",2017,"voiture")
veh3 = vehicule("v1","comercial",2010,"voiture")
veh4 = vehicule("b0","comercial",2020,"mini-bus")
catalogue = [veh1,veh2,veh3,veh4]
Tloc = []

def dateValidation():
    #year validation
    y = input('entrer l\'annee de location\n')
    testY=re.search(r"[0-9]{4}",y)
    if testY and int(y)<=2022:
        y = int(y)
    else:
        print('invalid annee!')
        x = input('entrer *Enter* pour countinue')
        menu()

    #mounth validation
    m = input('entrer le mois de location\n')
    testM=re.search(r"[0-9]{1,2}",m)
    if testM and int(m)<=12:
        m = int(m)
    else:
        print('invalid mois!')
        x = input('entrer *Enter* pour countinue')
        menu()

    #day validation
    d = input('entrer le jour de location\n')
    testD=re.search(r"[0-9]{1,2}",d)
    if testD and int(d)<=31:
        d = int(d)
    else:
        print('invalid jour!')
        x = input('entrer *Enter* pour countinue')
        menu()
    T=[y,m,d]
    return T


def ajoutLocation():
    exist = False
    im = input('entrer immatricule pour recherche a vehicule\n')
    for veh in catalogue:
        if im == veh.imma:
            exist = True
            T = dateValidation()
            date = datetime(T[0],T[1],T[2],12)
            nbj = int(input('entrer le nombre de jour de location\n'))
            PrixUPJ = int(input('entrer le prix unitaire par jour de location\n'))
            loc = location(veh,date,nbj,PrixUPJ)
            Tloc.append(loc)
            print('location ajouter avec succes')
    if exist==False:
        print('cette immatricule pas exist')

def recherche():
    if len(Tloc)==0:
        print("n'a pas de location exist")
    else:
        T = dateValidation()
        date = datetime(T[0],T[1],T[2],12)
        os.system('cls')
        for loc in Tloc:
            exist=False
            if loc.dateD == date:
                exist=True
                print(loc.veh.__str__())
                print('la date de location est: '+str(loc.dateD.year)+'-'+str(loc.dateD.month)+'-'+str(loc.dateD.day))
                print('le nombre de jour :',loc.nbj)
                print('le prix unitaire par jour :',loc.PrixUPJ)
                print('--------------------')
        if exist==False:
            print('cette location pas exist')

def afficheAnciennete():
    exist=False
    for veh in catalogue:
        if veh.type == 'voiture' and veh.anciennete()>10:
            exist=True
            print(veh.__str__())
    if exist==False:
        print("n'a pas de voiture depase 10ans")

def affichePrix():
    if len(Tloc)==0:
        print("n'a pas de location exist")
    else:
        im = input('entrer immatricule pour recherche a vehicule\n')
        T = dateValidation()
        date = datetime(T[0],T[1],T[2],12)
        exist = False
        for loc in Tloc:
            if loc.veh.imma == im and loc.dateD == date:
                exist=True
                print("le prix total est :",loc.nbj*loc.PrixUPJ)
        if exist==False:
            print('cette location pas exist pour afficher le prix')

def menu():
    while True:
        os.system('cls')
        ch = int(input("1-ajoutLocation\n\n2-rechercheLocation\n\n3-affiche-Voiture-Depass-10Ans\n\n4-affichePrix-Location\n\n5-sortir\n\n"))
        if ch == 1:
            os.system('cls')
            ajoutLocation()
            x = input('entrer *Enter* pour countinue')
        elif ch == 2:
            os.system('cls')
            recherche()
            x = input('entrer *Enter* pour countinue')
        elif ch == 3:
            os.system('cls')
            afficheAnciennete()
            x = input('entrer *Enter* pour countinue')
        elif ch == 4:
            os.system('cls')
            affichePrix()
            x = input('entrer *Enter* pour countinue')
        else:
            os.system('cls')
            print('fin de programme')
            exit()

menu()