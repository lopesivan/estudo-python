class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
        
    def grau(self):
        return len(self.coeficientes) - 1
    
    def avaliar(self, x):
        resultado = 0
        for i in range(len(self.coeficientes)):
            resultado += self.coeficientes[i] * (x ** (self.grau() - i))
        return resultado
    
    def __add__(self, outro):
        if self.grau() > outro.grau():
            coeficientes = self.coeficientes.copy()
            for i in range(outro.grau() + 1):
                coeficientes[self.grau() - i] += outro.coeficientes[outro.grau() - i]
        else:
            coeficientes = outro.coeficientes.copy()
            for i in range(self.grau() + 1):
                coeficientes[outro.grau() - i] += self.coeficientes[self.grau() - i]
        return Polinomio(coeficientes)
    
    def __sub__(self, outro):
        if self.grau() > outro.grau():
            coeficientes = self.coeficientes.copy()
            for i in range(outro.grau() + 1):
                coeficientes[self.grau() - i] -= outro.coeficientes[outro.grau() - i]
        else:
            coeficientes = [-c for c in outro.coeficientes]
            for i in range(self.grau() + 1):
                coeficientes[outro.grau() - i] += self.coeficientes[self.grau() - i]
        return Polinomio(coeficientes)
    
    def __mul__(self, outro):
        grau = self.grau() + outro.grau()
        coeficientes = [0] * (grau + 1)
        for i in range(self.grau() + 1):
            for j in range(outro.grau() + 1):
                coeficientes[grau - (i + j)] += self.coeficientes[self.grau() - i] * outro.coeficientes[outro.grau() - j]
        return Polinomio(coeficientes)
    
    def __str__(self):
        s = ""
        for i in range(self.grau() + 1):
            if self.coeficientes[self.grau() - i] != 0:
                if s != "":
                    s += " + "
                if self.coeficientes[self.grau() - i] == -1:
                    s += "-"
                elif self.coeficientes[self.grau() - i] != 1:
                    s += str(self.coeficientes[self.grau() - i])
                if i > 0:
                    s += "x"
                    if i > 1:

