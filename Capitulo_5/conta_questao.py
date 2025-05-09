# Corretor de questões

# Depurador do código
# import pdb
# pdb.set_trace()

# Variáveis contadoras
pontos = 0
questao = 1

while questao <= 3:
    resposta  = input(f"Resposta da questão {questao}:")
    if questao ==  1 and (resposta == "b" or resposta == "B"):
        pontos += 1
    if questao == 2  and (resposta == "a" or resposta == "A"): # Verifica as entradas são minúsculas ou maiúsculas
        pontos += 1
    if questao ==  3 and (resposta == "d" or resposta == "D"):
        pontos += 1    
    questao += 1 # Incrementa mais 1 a cada loop
    
print(f"O aluno(a) fez {pontos} ponto(s).")
