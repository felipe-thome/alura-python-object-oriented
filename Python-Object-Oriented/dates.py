class Date:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatted(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))
