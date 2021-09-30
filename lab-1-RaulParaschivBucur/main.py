'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    if n < 2:
      return False
    for d in range(2,n // 2 + 1):
        if (n % d) == 0:
            return False
    return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def prodNrLst(lst):
    if not lst: # Verific daca lista e goala
        return None
    prod = 1
    for idx in range(0, len(lst)):
        prod *= lst[idx] # prod = prod * ceva
    return prod


def prodNrLstTest():
    lista = [5, 2, 4, 2]
    assert(prodNrLst(lista) == 80)
    lista = []
    assert(not prodNrLst(lista)) # daca nu e none pusca
    lista = [2]
    assert(prodNrLst(lista) == lista[0])
    print("teste rulate !\n") # \n = linie noua




'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    while x != y:
        if x > y:
            x = x - y
        elif y > x:
            y = y - x
    return x
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''

#def get_cmmdc_v2(x, y):

def main():
    '''
    end = False
    while not end:
        print('Alege o optiune')
        print('1. Afla daca un nr introdus este prim')
        print('2. Afla cmmdc a doua nr introduse')
        print('3. Iesi')
        input(int(x))
        if x == 1:
            print('ai ales optiunea 2, alege un nr')
            input(int(x))
            if is_prime(x):
                print('este prim')
            else:
                print('NU este prim')
        elif x == 2:
            print('ai ales optiunea 2, alege 2 nr')
            input(x)
            input(y)
            cmmdc = get_cmmdc_v1(x,y)
            print('cmmdc al numerelor {x} si {y} este {cmmdc}')
        elif x == 3:
            end = True

main()
'''

prodNrLstTest()
n = int(input("n="))
lista = []
for idx in range(0, n):
    lista.append(int(input("Elementul numarul {} :".format(idx+1)))) # lista.pop(index)

print(lista)
print(prodNrLst(lista))


