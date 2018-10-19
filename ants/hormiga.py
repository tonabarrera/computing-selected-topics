import random

colores_dict = {
    "N": "red",
    "S": "blue",
    "E": "yellow",
    "O": "green",
}

tipos_dict = {
    1: "obrera",
    2: "soldado",
    3: "reina",
}


class Hormiga:
    def __init__(self, x=0, y=0, limite=0):
        """Direcciones:
        N -> Norte
        S -> Sur
        E -> Este
        O -> Oeste
        """
        self.x = x
        self.y = y
        self.limite = limite
        self.orientacion = 'S'
        self.color = "white"
        self.tipo = 1

    def mover(self, direccion):
        if direccion == 0:
            if self.orientacion == 'S':
                self.orientacion = 'O'
            elif self.orientacion == 'O':
                self.orientacion = 'N'
            elif self.orientacion == 'N':
                self.orientacion = 'E'
            else:
                self.orientacion = 'S'
        else:
            if self.orientacion == 'S':
                self.orientacion = 'E'
            elif self.orientacion == 'E':
                self.orientacion = 'N'
            elif self.orientacion == 'N':
                self.orientacion = 'O'
            else:
                self.orientacion = 'S'

        if self.orientacion == 'S':
            self.y += 1
        elif self.orientacion == 'E':
            self.x += 1
        elif self.orientacion == 'N':
            self.y -= 1
        else:
            self.x -= 1

        self.y = self.checar_limite(self.y)
        self.x = self.checar_limite(self.x)

    def checar_limite(self, coord):
        if coord < 0:
            return self.limite - 1
        if coord == self.limite:
            return 0
        return coord

    def cambiar(self):
        if self.orientacion == 'S':
            self.orientacion = 'O'
        elif self.orientacion == 'O':
            self.orientacion = 'N'
        elif self.orientacion == 'N':
            self.orientacion = 'E'
        else:
            self.orientacion = 'S'

    def get_tipo(self):
        return tipos_dict[self.tipo]


class Reina(Hormiga):
    def __init__(self):
        super().__init__()
        self.color = "purple"
        self.tipo = 3


class Soldado(Hormiga):
    def __init__(self):
        super().__init__()
        self.color = "pink"
        self.tipo = 2
