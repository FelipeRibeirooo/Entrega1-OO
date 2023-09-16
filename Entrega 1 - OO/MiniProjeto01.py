import math

class Ponto:
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0

    def Quadrante(self,x0,y0):
        if self.x0 == 0 and self.y0 == 0:
            print("O ponto está na origem")
        elif self.x0 == 0:
            print("O ponto está sobre o eixo Y")
        elif self.y0 == 0:
            print("O ponto está na parte negativa do eixo X")
        elif self.x0 > 0 and self.y0 > 0:
            print("O ponto está no primeiro quadrante")
        elif self.x0 > 0 and self.y0 < 0:
            print("O ponto está no quarto quadrante")
        elif self.x0 < 0 and self.y0 > 0:
            print("O ponto está no segundo quadrante")
        elif self.x0 < 0 and self.y0 < 0:
            print("O ponto está no terceiro quadrante")
        
    def Distancia(self,x0,y0):
        dist = (x0**2 + y0**2)**(1/2)
        return dist
        
    def Coordenadas(self,x0,y0):
        return print(f"A coordenada desse ponto é: {[x0,y0]}")
        
    def PontoCircunscrito(self,x0,y0,centro,raio):
        if centro[0] + raio >= x0 >= centro[0] - raio and centro[1] + raio >= y0 >= centro[1] - raio:
            return print("Ponto dentro do círculo")
        else:
            return print("Ponto fora do círculo")

class Linha:
    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def Comprimento(self,x0,y0,x1,y1):
        comprimento = ((x1 - x0)**2 + (y1-y0)**2)**(1/2)
        return comprimento

class Retangulo:
    def __init__(self,linha1,linha2):
        self.linha1 = linha1
        self.linha2 = linha2
    def Area(self,linha1,linha2):
        area = linha1.Comprimento(linha1.x0,linha1.y0,linha1.x1,linha1.y1) * linha2.Comprimento(linha2.x0,linha2.y0,linha2.x1,linha2.y1)
        return area
        
    def Perimetro(self, linha1, linha2):
        perimetro = linha1.Comprimento(linha1.x0,linha1.y0,linha1.x1,linha1.y1) * 2 + linha2.Comprimento(linha2.x0,linha2.y0,linha2.x1,linha2.y1) * 2
        return perimetro

class Circulo:
    def __init__(self,x0,y0,raio):
        self.centro = [x0,y0]
        self.raio = raio

    def Area(self,raio):
        area = math.pi * raio**2
        return area
        
    def Circunferencia(self,raio):
        circunferencia = 2 * math.pi * raio 
        return circunferencia

class Triangulo:
    def __init__(self,x0,y0,x1,y1,x2,y2):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.l0 = ((x1 - x0)**2 + (y1-y0)**2)**(1/2)
        self.l1 = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)
        self.l2 = ((x2 - x0)**2 + (y2-y0)**2)**(1/2)
        self.h = (self.l1**2 - (self.l0/2)**2)**(1/2)

    def Tipo(self,l0,l1,l2):
        if l0 == l1 == l2:
            tipo = "Equilátero"
        elif l0 != l1 != l2 != l0:
            tipo = "Escaleno"
        else:
            tipo = "Isósceles"
        return tipo
    
    def Perimetro(self,l0,l1,l2):
        perimetro = l0 + l1 + l2
        return perimetro

    def Area(self,l0,h):
        area = l0 * h/2
        return area

#Exemplos de uso
#Criação de Objetos
p = Ponto(1.0,1.0)
l = Linha(-5.0,-4.0,-20.0,12.0)
c = Circulo(2.0,2.0,8.0)
r = Retangulo(Linha(1.0,0,1.0,5.0),Linha(1.0,0,10.0,0))
t = Triangulo(6.0,4.0,9.0,2.0,15.0,7.0)

#Uso de métodos do ponto
p.Quadrante(p.x0,p.y0)
p.PontoCircunscrito(p.x0,p.y0,c.centro,c.raio)
p.Coordenadas(p.x0,p.y0)
print(f"A distância do ponto até a origem é de: {p.Distancia(p.x0,p.y0):,.2f}")

#Uso de métodos da Linha
print(f"Essa linha possui comprimento = {l.Comprimento(l.x0,l.y0,l.x1,l.y1):,.2f}")

#Uso de métodos do Retângulo
print(f"O perímetro do retângulo é de {r.Perimetro(r.linha1,r.linha2):,.2f}")
print(f"A área do retângulo é de {r.Area(r.linha1,r.linha2):,.2f}")

#Uso de métodos do Círculo
print(f"A área desse círculo é de {c.Area(c.raio):,.2f}")
print(f"A circunfêrencia do círculo é de {c.Circunferencia(c.raio):,.2f}")

#Uso de métodos do Triângulo
print(f"Esse é um triângulo {t.Tipo(t.l0,t.l1,t.l2)}")
print(f"A área desse triângulo é de {t.Area(t.l0,t.h):,.2f}")
print(f"O perímetro desse triângulo é de {t.Perimetro(t.l0,t.l1,t.l2):,.2f}")