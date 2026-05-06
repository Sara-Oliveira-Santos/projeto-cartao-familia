def cpf_validador(validador, cpf_usuario):
    while len(cpf_usuario) != 11 or not cpf_usuario.isdigit():
        print("O CPF precisa ser apenas números e 11 dígitos")
        cpf_usuario = input("CPF(Apenas números): ").strip()
    cpf_usuario = list(cpf_usuario)
    for i in range(0, 11):
        cpf_usuario[i] = int(cpf_usuario[i])
    cont = 10
    soma = 0
    for i in range(0,9):
        soma = soma + (cpf_usuario[i]*cont)
        cont = cont - 1
    p_digito = (soma*10)%11
    if p_digito > 9:
        p_digito = 0
    cont = 11
    soma = 0
    for i in range(0,10):
        soma = soma + (cpf_usuario[i]*cont)
        cont = cont - 1
    s_digito = (soma*10)%11
    if s_digito > 9:
        s_digito = 0
    if cpf_usuario[9] == p_digito and cpf_usuario[10] == s_digito:
        validador = True
        print("CPF VÁLIDO")
    else: print("CPF INVÁLIDO")
    return validador

def cadastro_CF(qnt_pessoas, lista_membros, lista_CPF_membros):
    for i in range(0, qnt_pessoas):
            membro = input("NOME COMPLETO: ")
            lista_membros.append(membro)
            cpf_membro = ""
            validador = False
            while validador != True:
                cpf_membro = input("CPF(Apenas números): ").strip()
                cpf_junto = cpf_membro
                validador = cpf_validador(validador, cpf_membro)
            lista_CPF_membros.append(cpf_junto)
    return lista_membros, lista_CPF_membros
    
def dados_usuario():
    print("-----DADOS DO USUÁRIO-----")
    nome_usuario = input("NOME COMPLETO: ")
    validador = False
    while validador != True:
        cpf = input("CPF(Apenas números): ").strip()
        cpf_usuario = cpf
        validador = cpf_validador(validador, cpf)
    print("----VERIFICAÇÃO PRONTA----")
    escolha = "0"
    lista_membros = []
    lista_CPF_membros = []
    return nome_usuario, cpf_usuario, escolha, lista_membros, lista_CPF_membros

def vizualizar_membros(lista_membros, nome_usuario, lista_CPF_membros, cpf_usuario):
    print("O CARTÃO FAMÍLIA DESSA CONTA CONTÉM ", len(lista_membros)+1, "MEMBROS INCLUINDO O USUÁRIO RESPONSÁVEL.")
    print("USUÁRIO RESPONSÁVEL -> ", nome_usuario, " - ", cpf_usuario)
    for i in range(0, len(lista_membros)):
        print(i+1, " - ", lista_membros[i], " - ", lista_CPF_membros[i])
    print("TODOS OS CADASTRADOS PODEM COMEÇAR A USAR O CARTÃO FAMÍLIA.")

print("------CARTÃO FAMÍLIA------")
nome_usuario, cpf_usuario, escolha, lista_membros, lista_CPF_membros = dados_usuario()

while escolha != "7":
    print("-----LISTA DE COMANDO-----")
    print("1 - CADASTRAR CF\n2 - ADICIONAR MEMBRO NO CF\n3 - RETIRAR MEMBRO DO CF\n4 - VIZUALIZAR MEMBROS DO CF\n5 - CANCELAR CF\n6 - VOLTAR AO INÍCIO\n7 - FIM DE PROCESSO")
    escolha = input("ESCOLHA A OPÇÃO(1, 2, 3...):")
    if escolha == "1":
        print("CADASTRAR CARTÃO FAMÍLIA")
        print("Olá", nome_usuario, "estamos muito felizes em fazer seu cadastro no CARTÃO FAMÍLIA!")
        qnt_pessoas = int(input("QUANTIDADE DE MEMBROS(Apenas números): "))
        lista_membros, lista_CPF_membros = cadastro_CF(qnt_pessoas, lista_membros, lista_CPF_membros)
        vizualizar_membros(lista_membros, nome_usuario, lista_CPF_membros, cpf_usuario)
    elif escolha == "2":
        print("ADICIONAR MEMBRO NO CARTÃO FAMÍLIA")
        print("Olá", nome_usuario, "quantas pessoas deseja adicionar no CF?")
        qnt_pessoas = int(input("QUANTIDADE DE MEMBROS(Apenas números): "))
        lista_membros, lista_CPF_membros = cadastro_CF(qnt_pessoas, lista_membros, lista_CPF_membros)
        vizualizar_membros(lista_membros, nome_usuario, lista_CPF_membros, cpf_usuario)
    elif escolha == "3":
        print("RETIRAR ALGUÉM DO CARTÃO FAMÍLIA")
        print("MEMBROS DO SEU CARTÃO FAMÍLIA:")
        for i in range(0, len(lista_membros)):
            print(i+1, " - ", lista_membros[i], " - ", lista_CPF_membros[i])
        print("Quantas exclusões de membros deseja fazer:")
        exclusao = int(input())
        for i in range(0, exclusao):
            excluir = int(input("Digite o número do membro que deseja excluir(1, 2, 3...):"))
            del lista_membros[excluir - 1]
            del lista_CPF_membros[excluir - 1]
        vizualizar_membros(lista_membros, nome_usuario, lista_CPF_membros, cpf_usuario)
    elif escolha == "4":
        print("VISUALIZAR MEMBROS DO CARTÃO FAMÍLIA")
        if nome_usuario == "":
            print("Não tem conta! Volte ao início e abra uma conta!")
        elif len(lista_membros) == 0:
            print("O CARTÃO FAMÍLIA SÓ TEM O USUÁRIO RESPONSÁVEL.")
        else:vizualizar_membros(lista_membros, nome_usuario, lista_CPF_membros, cpf_usuario)
    elif escolha == "5":
        print("CANCELAR CARTÃO FAMÍLIA")
        print("Tem certeza do cancelamento?(SIM || NÃO)")
        cancelamento = input()
        if cancelamento.lower() == "sim":
            print("CF cancelado.")
            print("Muito obrigado por ter sido nosso cliente.")
            nome_usuario = ""
            cpf_usuario = ""
            lista_CPF_membros.clear()
            lista_membros.clear()
        else: print("Muito obrigado por repensar a escolha e continuar com nosso serviço.")
    elif escolha == "6":
        print("VOLTAR AO INÍCIO")
        lista_membros.clear()
        lista_CPF_membros.clear()
        nome_usuario, cpf_usuario = "", ""
        nome_usuario, cpf_usuario, escolha, lista_membros, lista_CPF_membros = dados_usuario()
    elif escolha == "7":
        print("FIM DO PROCESSO")