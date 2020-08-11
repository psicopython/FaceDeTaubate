#alguem ajudaria nesse código aqui:
mi_list = ['Ruan', 'lucas', 'meu', 'grande', 'amigo']

while True:
    variavel = input('Digite um nome: ')
    for i in mi_list:
        if variavel[:2] in i[:2]:
            print('teste')
            break
        else:
            print('n tem add agora!')
            mi_list.append(variavel)
        print(mi_list)
