from sistema import Sistema
sistema = Sistema()
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Excluir usuário")
    print("5 - Atualizar telefone")
    print("6 - Atualizar nome")
    print("7 - Atualizar senha")
    print("8 - Fazer login")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        print("Programa encerrado.")
        break 

    elif opcao == "1":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            telefone = input("Digite seu telefone: ")
            senha = input("Digite sua senha: ")
            confirma_senha = input("Confirme sua senha: ")
            if nome == "" or email == "" or telefone == "" or senha == "" or confirma_senha == "":
                print("Erro: todos os campos devem ser preenchidos.")
            elif "@" not in email:
                print("Erro: e-mail invalido.")
            elif senha != confirma_senha:
                print("Erro: as senhas não são iguais.")
            else:
                email_existe = False
                for usuario in sistema.usuarios:
                    if usuario.email == email:
                          email_existe = True
                          print("Erro: e-mail já cadastrado")
                          break  
            if email_existe == False:   
             usuario1 = sistema.cadastrar_usuario(nome, email, telefone, senha)
             print("cadastro realizado com sucesso!")
             print("total de usuarios cadastrados:", len(sistema.usuarios))


    elif opcao == "2":
            if len(sistema.usuarios) == 0:
                  print("Nenhum usuario cadastrado") 
            else:
             for usuario in sistema.usuarios:
                print("nome:", usuario.nome)
                print("E-mail:", usuario.email)
                print("Telefone:", usuario.telefone)
                print("---------------------------")


    elif opcao == "3":
        email_busca = input("Digite o e-mail que deseja buscar:")
        usuario = sistema.buscar_usuario(email_busca)
        if usuario is not None:
                print("nome", usuario.nome)
                print("E-mail:", usuario.email)
                print("telefone", usuario.telefone)
        else:
            print("Usuário não encontrado")


    elif opcao == "4":
        email_excluir = input("Digite o e-mail do usuário que deseja excluir: ")
        usuario_excluido = sistema.excluir_usuario(email_excluir)
        if usuario_excluido == True:
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado")


    elif opcao == "5":
        email_existente = input("digite seu e-mail: ")
        novo_telefone = input("digite seu novo telefone: ")
        usuario_atualizado = sistema.atualizar_telefone(email_existente, novo_telefone)
        if usuario_atualizado == True:
            print("telefone atualizado com sucesso!")
        else:
            print("E-mail não encontrado")

    elif opcao == "6":
        email_existente = input("digite seu e-mail: ")
        novo_nome = input("digite seu novo nome: ")
        nome_atualizado = sistema.atualizar_nome(email_existente, novo_nome)
        if nome_atualizado == True:
            print("nome do usuário atualizado!")
        else:
            print("E-mail não encontrado")


    elif opcao == "7":
        email_senha = input("digite seu e-mail: ")
        senha_atual = input("Digite sua senha atual: ")
        nova_senha = input("Digite sua nova senha: ")
        confirma_senha = input("confirme sua nova senha: ")
        senha_atualizada = sistema.atualizar_senha(email_senha, senha_atual, nova_senha, confirma_senha)
        if senha_atualizada == True:
            print("Senha atualizada com sucesso!")
        else:
            print("não foi possivel atualizar a senha.")

    elif opcao == "8":
        email = input("digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        resultado = sistema.fazer_login(email, senha)
        if resultado:
            print("Login realizado com sucesso!")
        else:
            print("E-mail ou senha incorretos!")