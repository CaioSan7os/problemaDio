#A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam,
#respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

#Saída
#Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.
#Exemplos de Entrada	Exemplos de Saída
#200 3 8	
#18.18

distancia = float(input("digite a distancia: ") or 200)
diametro1 = float(input("digite o diametro 1: ") or 3)
diametro2 = float(input("digite o diametro 2: ") or 8)
icm = distancia / (diametro1 + diametro2)
print(f"o ICM é {icm:.2f}")
