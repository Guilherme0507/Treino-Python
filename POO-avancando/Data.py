class Data:

    def __init__(self, dia, mes, ano):
        self.set_data(dia, mes, ano)

    def set_data(self, d, m ,a):
        if(m >= 1 and m <= 12):
            self.__mes = m
        else:
            self.__mes = 1

        self.__ano = a

        self.__dia = self.check_dia(d , a)

    def check_dia(self, d, a):
        dias_mes = [0, 31, 28, 31 , 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(self.bissexto(a)):
                dias_mes[2] = 29
        if (d > 0 and d <= dias_mes[d]):
                return d

        print("Dia %d inválido. Configurado dia = 1" % (d))
        return 1

    def bissexto(self, a):
        if( a % 4 == 0):
            return True
        else:
            return False

    @property
    def get_data(self):
        print("Dia: %d, Mês: %d, Ano: %d" % (self.__dia, self.__mes, self.__ano))
        return self.__dia, self.__mes, self.__ano

    @property
    def get_dia(self):
        print("Ano:", self.__dia)
        return self.__dia

    @property
    def get_mes(self):
        print("Ano:", self.__mes)
        return self.__mes

    @property
    def get_ano(self):
        print("Ano:", self.__ano)
        return self.__ano



teste = Data(5, 7,2002)
teste.get_ano
teste.get_mes
teste.get_dia
teste.get_data