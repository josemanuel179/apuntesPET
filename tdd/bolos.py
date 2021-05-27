from errorDeFormato import *


def verificar_entrada(partida):
    verificar_tipos(partida)
    verificar_rondas_validas(partida)
    verificar_ronda_extra(partida)


def verificar_tipos(partida):
    for i in range(len(partida)):
        for j in range(len(partida[i])):
            if type(partida[i][j]) != str and type(partida[i][j]) != int:
                raise ErrorTipoDeDato(partida[i][j])

            if type(partida[i][j]) == str and partida[i][j].upper() != "X" and partida[i][j] != "/":
                raise ErrorTipoDeDato(partida[i][j])


def verificar_rondas_validas(partida):
    try:
        for i in range(0, 10):

            # Verifica que un simbolo de spare no esté en la primera tirada de una ronda
            if partida[i][0] == "/":
                raise ErrorDeRonda("Ronda {} inválida".format(i + 1))

            # verifica que una ronda que no sea strike no tenga una sola tirada
            if len(partida[i]) != 2:
                for j in range(len(partida[i])):
                    if partida[i][j] != "x" and partida[i][j] != "X":
                        raise ErrorDeRonda("Ronda {} inválida".format(i + 1))

            # Verifica que una ronda no tenga score > 10
            if type(partida[i][0]) == int and type(partida[i][1]) == int:
                if sum(partida[i]) > 10:
                    raise ErrorDeRonda("Ronda {} inválida".format(i + 1))

            if len(partida) > 11:
                raise ErrorDeFormato("Partida Larga")

            for j in range(len(partida[i])):

                if type(partida[i][j]) == int and partida[i][j] < 0:
                    raise ErrorDeRonda("Ronda {} inválida".format(i + 1))

                if type(partida[i][j]) == int and partida[i][j] > 9:
                    raise ErrorDeRonda("Ronda {} inválida".format(i + 1))

                if partida[i][j] == "X" or partida[i][j] == "x":
                    if len(partida[i]) > 1:
                        raise ErrorDeRonda("Ronda {} inválida".format(i + 1))

    except IndexError:
        raise ErrorDeFormato("Error de formato")


def verificar_ronda_extra(partida):

    tiradas_extra = 0
    if partida[9][0] == "X" or partida[9][0] == "x":
        tiradas_extra += 2

    elif partida[9][1] == "/":
        tiradas_extra += 1

    if len(partida) > 10 and tiradas_extra == 0:
        raise ErrorDeRondaExtra("Partida invalida")

    if len(partida) < 11 and tiradas_extra > 0:
        raise ErrorDeRondaExtra("Partida invalida")

    if tiradas_extra > 0:
        if len(partida[10]) != tiradas_extra:
            raise ErrorDeRondaExtra("error en ultima ronda")

        if partida[10][0] == "/":
            raise ErrorDeRondaExtra("error")

        for j in range(len(partida[10])):
            if type(partida[10][j]) == int and partida[10][j] < 0:
                raise ErrorDeRondaExtra("Ronda 10 inválida")


class Bolos:
    def __init__(self, partida: list):
        verificar_entrada(partida)
        self.partida = partida

    def puntaje(self) -> int:
        self.mayuscula()
        score = 0
        for ronda in range(0, len(self.partida)):
            if ronda == 9:
                score += self.ultima_ronda()
                continue

            if ronda == 10:
                score += self.ronda_extra()
                continue

            if self.partida[ronda][0] == "X":
                score += self.strike(ronda)

            elif self.partida[ronda][1] == "/":
                score += self.spare(ronda)
            else:
                score += sum(self.partida[ronda])

        return score

    def strike(self, ronda: int) -> int:
        score = 10
        # Ultima o rondas extras
        if ronda == 9 or ronda == 10:
            return score

        # Siguiente es Strike
        if self.partida[ronda + 1][0] == "X":
            score += 10
            # 2 siguiente también es strike
            if self.partida[ronda + 2][0] == "X":
                score += 10
            # No es strike
            else:
                score += self.partida[ronda + 2][0]

        # Siguiente no es Strike
        else:
            # spare
            if self.partida[ronda + 1][1] == "/":
                score += 10

            else:
                score += sum(self.partida[ronda + 1])

        return score

    def spare(self, ronda: int) -> int:
        score = 10
        # Ultima o rondas extras
        if ronda == 9 or ronda == 10:
            return score
        # Siguiente es Strike
        if self.partida[ronda + 1][0] == "X":
            score += 10

        else:
            score += self.partida[ronda + 1][0]

        return score

    def ultima_ronda(self) -> int:
        score = 0
        for tirada in range(0, len(self.partida[9])):
            if self.partida[9][tirada] == "X":
                score += 10

            elif self.partida[9][tirada] == "/":
                score += 10 - self.partida[9][tirada - 1]

            else:
                score += self.partida[9][tirada]

        return score

    def ronda_extra(self):
        score = 0
        for tirada in range(0, len(self.partida[10])):
            if self.partida[10][tirada] == "X":
                score += 10

            elif self.partida[10][tirada] == "/":
                score += 10 - self.partida[10][tirada - 1]

            else:
                score += self.partida[10][tirada]

        return score

    def mayuscula(self):
        for i in range(len(self.partida)):
            for j in range(len(self.partida[i])):
                if self.partida[i][j] == "x":
                    self.partida[i][j] = "X"
