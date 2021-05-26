import math
# hacer un diccionario cuyas llaves
# sean los primeros 100 naturales y
# cuyos valores sean esos primeros 
# numeros elevados al cubo 

def run():
    
    # forma que yo entendí
    #my_dict = {}
    #for cont in range(1,101):
    #    my_dict[str(cont)] = cont**3

    #for key, value in my_dict.items():
    #    print(key, "-", value)


    # forma optima pero agregando una condición que no sean divisibles por 3
    #my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    #print(my_dict)


    #otro reto Crear, con un dictionary comprehension, 
    # un diccionario cuyas llaves sean los 1000 primeros
    # números naturales con sus raices cuadradas como valores
    #my_dict1 = {i: math.sqrt(i) for i in range(1,1001)}
    #print(my_dict1)
    
    #otro reto crear una lista de los numero con la potencia elevada de cada numero.
    my_list = [1,2,3,4,5]
    my_list1 = {i**2 for i in my_list }
    square = list(map(lambda x: x**2, my_list))
    print(my_list1)
    print(square)

if __name__ == "__main__":
    run()
