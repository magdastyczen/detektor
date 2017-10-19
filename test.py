import math
import numpy
import numpy as np
import scipy
import scipy.stats as st
from scipy.stats import rv_continuous
import matplotlib.pyplot as plt

# Wielomian odpowiadajcy rozkladowi mionow
class my_pdf(st.rv_continuous):
    def _pdf(self,x):
        return (7.89875 * 10**7 -630481 * x -15940.4 * x**2 + 147.356 * x**3) / (3.09892*10**9)


n = 100

#Zdefiniowanie gestosc prawdopodobienstwa katow   
rozkladkata = my_pdf(a=0, b=90, name='my_pdf')
print rozkladkata
#Generujemy n katow Beta (nachylenie wzgledem osi pionowej)
beta = rozkladkata.rvs(size=(n, 1))

#Generujemy n katow Theta (kat w plasczyznie XY)
alpha = np.random.rand(n, 1)

#generujemy rozklad punktow zaczepienia w osi OX od 0 do R 
anchor_point_R = np.random.uniform(low=0, high=57.5, size=(n,1))

#Generujemy n punktow zaczepienia w osi OY od 0 do 90 stopni  0.785398163
anchor_point_FI = np.random.uniform(low=0, high=1.570796327, size=(n,1))
# np.random.rand(n,2)

#Laczymy w macierz nx5   theta=alpha
rays = np.concatenate((anchor_point_FI, anchor_point_R, beta, alpha), axis=1)

#print rays[1:3, :]
#-----------------------------------------------------------------------------

#test czy rozklad jest wlasciwy

def testrozkladu(r_list, fi_list, beta_list):
    punktprzeciecia = []
    for r, fi, beta in zip(r_list, fi_list, beta_list):
        x = r * math.cos(fi)
        y = r * math.sin(fi)
        A = math.atan(1.570796327 - beta)
        D = math.tan(0.7)
        C = -y + A*x
        z = -(C/A)
        if 0 <= z and z <= 57.5:
  
            punktprzeciecia.append([z, beta]) 
         
    return np.asarray(punktprzeciecia) #przed zwroceniem wartosci, konwertuje jeszcze liste do macierzy NumPy 

#Wywolujemy funkcje z odpowiednimi argumentami, a jej wynik od razu przypisujemy do macierzy punktprzeciecia:
punktprzeciecia = testrozkladu(r_list = rays[:,1], fi_list = rays[:,0], beta_list = rays[:,2]) 
print 'D'

print '\n'.join(map(str, beta))
#Rysowanie wykresu
plt.plot(punktprzeciecia[:, 0], punktprzeciecia[:, 1], 'ro');
#----------------------------------------------------------------
#zdefiniowanie polozenia detektorow
def polozeniedetektoraI(r1, theta1, z1): #to jest deklaracja - nazwa_funkcji(argumenty). zaczyna sie od slowa kluczowego "def"
    #deklarujemy pusta liste wspolrzednych, gdyz bedziemy do niej dodawac nowe elementy w petli
    wspolrzedne = []
    n = 0
    while n < 46:
        wspolrzedne.append([r1, theta1*n, z1]) #uzywamy funkcji append: powoduje ona dodanie nowego elementu do listy
        n = n+1
       
    return wspolrzedne

wspolrzedne_detektora1 = polozeniedetektoraI(r1=42.5, theta1=7.5, z1=0)
wspolrzedne_detektora2 = polozeniedetektoraI(r1=46.75, theta1=7.5, z1=0)
wspolrzedne_detektora3 = polozeniedetektoraI(r1=57.5, theta1=3.75, z1=0)
#print(wspolrzedne_detektora2)
#print(wspolrzedne_detektora1)
'''
def obszarszukania(a, b, c1, c2):
    obszar = []
    while m <= n:        
        m=0
        x = rays[m, 1]
        y = rays[m, 0]
        beta = rays[m, 2]
        d = 1.0124
        b = -1
        a = math.atan(beta)
        c = y - a*x

#prosta y prechodzaca przez punkt x,y pod katem beta
        #y = a*x + c
        #x1 = (2*c) / (2*a + 2)
        #x2 = (-2*c) / (2 - 2*a)

        #y1 = a * x1 + c 
        #y2 = a * x2 + c
# dwie proste ograniczajajace pole poszukiwania
# wzor na odleglosc punktu od prostej => tutaj wzor na prosta w odleglosci pol przekontnej detektora od wylosowanego punktu, a jest stale zmienne C
        from math import sqrt
        c1 = d * sqrt( a**2 + b**2 ) - a * x - b * y 
        c2 = d * sqrt( a**2 + b**2 ) + a * x + b * y 
        obszar.append([a, b, c1, c2])
        m = m + 1
    return obszar
print(obszar)
'''
