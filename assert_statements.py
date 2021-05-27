def divisors(num):
    assert num>0,"No puedes ingresar numeros negativos"
    divisors = [i for i in range(1,num+1) if num % i == 0]
    return divisors     
    

def run():

    num = input("Ingresa un numero:")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("terminó mi programa")

if __name__ == '__main__':
    run()