class Retangulo:

    def __init__(self, base, altura):
        print("Formando retangulo")
        self.__b = base
        self.__a = altura
        print("Base: %d" % (self.__b))
        print("Altura: %d\n" % (self.__a))


    def setBase(self, base):
        self.__b = base
        print("A novo valor da base é %d\n" % (base))

    def getBase(self):
        print("O valor da base é %d\n" % (self.__b))
        return self.__b

    def setAltura(self, altura):
        self.__a = altura
        return self.__a

    def getAltura(self):
        print("O valor da altura é %d\n" % (self.__a))
        return self.__a
        pass

    def getArea(self):
        area = self.__a * self.__b
        print("A área é: %d\n" % (area))
        return area

    def getPerimetro(self):
        perimetro = 2 * self.__a + 2 * self.__b
        print("O perimetro é: %d\n" % (perimetro))
        return perimetro

r = Retangulo(2,4)
Retangulo.getBase(r)
Retangulo.getAltura(r)

Retangulo.getArea(r)

Retangulo.getPerimetro(r)
#Retangulo.setBase(r)

