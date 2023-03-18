class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def grau(self):
        return len(self.coeficientes) - 1

    def avaliar(self, x):
        resultado = self.coeficientes[-1]
        for i in range(self.grau() - 1, -1, -1):
            resultado = resultado * x + self.coeficientes[i]
        return resultado

    def __add__(self, outro):
        if self.grau() > outro.grau():
            c = self.coeficientes.copy()
            for i in range(outro.grau() + 1):
                c[-i-1] += outro.coeficientes[-i-1]
        else:
            c = outro.coeficientes.copy()
            for i in range(self.grau() + 1):
                c[-i-1] += self.coeficientes[-i-1]
        return Polinomio(c)

    def __sub__(self, outro):
        if self.grau() > outro.grau():
            c = self.coeficientes.copy()
            for i in range(outro.grau() + 1):
                c[-i-1] -= outro.coeficientes[-i-1]
        else:
            c = [-x for x in outro.coeficientes]
            for i in range(self.grau() + 1):
                c[-i-1] += self.coeficientes[-i-1]
        return Polinomio(c)

    def __mul__(self, outro):
        c = [0] * (self.grau() + outro.grau() + 1)
        for i in range(self.grau() + 1):
            for j in range(outro.grau() + 1):
                c[-i-j-1] += self.coeficientes[-i-1] * outro.coeficientes[-j-1]
        return Polinomio(c)

    def __str__(self):
        s = ""
        for i in range(self.grau(), -1, -1):
            if self.coeficientes[-i-1] == 0:
                continue
            elif self.coeficientes[-i-1] == 1:
                if i == self.grau():
                    s += "x^" + str(i)
                elif i == 1:
                    s += " + x"
                else:
                    s += " + x^" + str(i)
            elif self.coeficientes[-i-1] == -1:
                if i == self.grau():
                    s += "-x^" + str(i)
                elif i == 1:
                    s += " - x"
                else:
                    s += " - x^" + str(i)
            elif self.coeficientes[-i-1] > 0:
                if i == self.grau():
                    s += str(self.coeficientes[-i-1]) + "x^" + str(i)
                elif i == 1:
                    s += " + " + str(self.coeficientes[-i-1]) + "x"
                else:
                    s += " + " + str(self.coeficientes[-i-1]) + "x^" + str(i)
            else:
                if i == self.grau():
                    s += str(self.coeficientes[-i-1]) + "x^" + str
                elif i == 1:
                    s += " - " + str(-self.coeficientes[-i-1]) + "x"
                else:
                    s += " - " + str(-self.coeficientes[-i-1]) + "x^" + str(i)
        if s == "":
            s = "0"
        return s


if __name__ == "__main__":
    p1 = Polinomio([2, 0, -1, 3])  # 2x^3 - x^2 + 3
    p2 = Polinomio([-1, 1, 0, 2])  # -x^3 + x^2 + 2x

    print(p1)  # 2x^3 - x^2 + 3
    print(p2)  # -x^3 + x^2 + 2x

    print(p1.avaliar(2))  # 17
    print(p2.avaliar(-1))  # -1

    p3 = p1 + p2
    print(p3)  # x^2 + 5x + 3

    p4 = p1 - p2
    print(p4)  # 3x^3 - 2x^2 + 2x - 3

    p5 = p1 * p2
    print(p5)  # -2x^6 + 3x^5 + 5x^4 - 8x^3 - 5x^2 + 6x
