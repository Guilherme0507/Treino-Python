class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        print("Construindo Triângulo.")
        self.constroi_triangulo(lado_a, lado_b, lado_c)

    def calcular_perimetro(self):
        perimetro = self.__lado_a + self.__lado_b + self.__lado_c
        print("O perimetro é: %d" % (perimetro))
        return perimetro

    def constroi_triangulo(self, lado_a, lado_b, lado_c):
        tipo = {'isosceles':False, 'escaleno':False, 'equilatero':False}
        n1 = lado_b - lado_c
        n2 = lado_a - lado_c
        n3 = lado_a - lado_b
        if n1 < 0:
            n1 =- n1
        if n2 < 0:
            n2 =- n2
        if n3 < 0:
            n3 =-n3
        if ((n1 < lado_a and lado_a < (lado_b + lado_c)) and (n2 < lado_b and lado_b < (lado_a + lado_c)) and (n3 < lado_c and lado_c < (lado_a + lado_b))):
            if(((lado_a == lado_b) and (lado_a != lado_c)) or ((lado_a==lado_c) and (lado_a != lado_b)) or ((lado_b == lado_c) and (lado_b != lado_a))):
                tipo['isosceles'] = True
                print('O tipo do Triangulo é: isosceles')
            elif ((lado_a != lado_b) and (lado_a != lado_c) and (lado_b != lado_c)):
                tipo['escaleno'] = True
                print('O tipo do Triangulo é: escaleno')

            elif ((lado_a == lado_b) and (lado_a==lado_c)):
                tipo['equilatero'] = True
                print('O tipo do Triangulo é: escaleno')
            else:
                print('Não é um triângulo')

        else:
            print("Não é um triângulo")


    @property
    def lado_a (self):
        return self.__lado_a

    @property
    def lado_b (self):
        return self.__lado_b

    @property
    def lado_c (self):
        return self.__lado_c


    @lado_a.setter
    def lado_a(self, lado_a):
        if lado_a < 0:
           lado_a =- lado_a
        self.__lado_a = lado_a

    @lado_b.setter
    def lado_b(self, lado_b):
        if lado_b < 0:
           lado_b =- lado_b
        self.__lado_b = lado_b

    @lado_c.setter
    def lado_c(self, lado_c):
        if lado_c < 0:
           lado_c =- lado_c
        self.__lado_c = lado_c

