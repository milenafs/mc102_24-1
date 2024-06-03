k = int(input())
palavra = input().strip()

def get_palindromo(palavra):
    if len(palavra) == 1:
        return palavra
    
    palindromo = palavra[-1] + get_palindromo(palavra[0:len(palavra)-1])
    return palindromo

palindromo = get_palindromo(palavra)
for i in range(len(palavra)):
    if palavra[i] != palindromo[i]:
        k -= 1

if k >= 0:
    print('sim')
else:
    print('nao')