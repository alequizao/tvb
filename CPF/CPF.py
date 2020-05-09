vetorcpf = []
def cpf(vetorcpf):
    for x in range(9):
        vetorcpf.append(abs(int(input("Informe um numero: "))))
    soma_digito1=0
    for i in range(len(vetorcpf)):
        soma_digito1+=vetorcpf[i]*(10-i)
    digito1=(11-(soma_digito1%11))%10
    vetorcpf.append(digito1)
    soma_digito2=0
    for i in range(len(vetorcpf)):
        soma_digito2+=vetorcpf[i]*(11-i)
    digito2=(11-(soma_digito2%11))%10
    vetorcpf.append(digito2)
    return vetorcpf
cpf(vetorcpf)
str1 = str
str1 = vetorcpf
print(f'CPF: {str1[0]}{str1[1]}{str1[2]}.{str1[3]}{str1[4]}{str1[5]}.{str1[6]}{str1[7]}{str1[8]}-{str1[9]}{str1[10]}')
