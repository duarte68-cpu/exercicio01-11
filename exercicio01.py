# faça um programa saolicita ao usuário para adivinha um número.

numero = ''

while numero != '5':
    numero = input('digite um numero: ')
 
print('correto')
    
    
# faça um programa que peça ao usuário um nome de usuário e uma senha. continue solicitando até que os valores corretos sejam fornecidos:

nome = ''
senha = ''

while nome != 'jefferson duarte':
    nome = input('digite o nome de usuario: ') 
    if nome != 'jefferson duarte':
      print('nome invalido')
else:
      print('nome correto ', nome)
      
while senha != '402068':        
      senha = input('insira senha de usuario: ')
      if senha != '402068':
              print('senha invalida')
else:
              print('dados corretos ', senha)             


# faça um programa que o usuário pode inserir número e some-os até que ele digite "0". ao final, mostre a soma total.

soma = 0
while True: 
      numero = int(input('digite um numero: '))
      if numero == 0:
          break
    
      soma += numero

print(f'A soma dos numero {soma}')

            
     
    