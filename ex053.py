frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto [letra]
print('O inverso da palavra {} é {}'.format(junto, inverso))
if inverso == junto:
    print('é um palindromo')
else:
    print('não é um palindromo')
#da pra se usar a tecnica do fatiamento no lugar do for in range
#colocando inverso = [::-1], assim substituindo e diminuindo as linhas