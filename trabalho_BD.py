from tkinter import *

from persistencia import *
#IGOR DAVID e LUCA BARBA

def abre_tela_areas():

    def adiciona_areas():
        codigo_espaco_container = e1.get()
        regiao = e2.get()
        corredor_letra = e3.get()
        corredor_numero = e4.get()
        setor = e5.get()
        id_equipe = e6.get()
        
        adiciona_areas_persistencia(codigo_espaco_container, regiao, corredor_letra, corredor_numero, setor, id_equipe)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_areas():
        
        members = [('Código espaço para containers', 'Região', 'Corredor Letra', 'Corredor Numero', 'Setor', 'ID da equipe')]

        mostra_areas_persistencia(members)
        #print("Uau, areas!")

    def altera_areas():
        codigo_espaco_container = e1.get()
        regiao = e2.get()
        corredor_letra = e3.get()
        corredor_numero = e4.get()
        setor = e5.get()
        id_equipe = e6.get()
        
        altera_areas_persistencia(codigo_espaco_container, regiao, corredor_letra, corredor_numero, setor, id_equipe)
        #print("Uau, alterou!")

    def deleta_areas():
        codigo_espaco_container = e1.get()
        deleta_areas_persistencia(codigo_espaco_container)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com áreas:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar area", command=adiciona_areas, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar areas", command=mostra_areas, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar areas", command=altera_areas, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar areas", command=deleta_areas, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="Código de espaço para container:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Região:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Corredor (letra):").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Corredor (numero)").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Setor:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="ID de equipes relacionadas:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    janelaFuncionarios.mainloop()

def abre_tela_navios():

    def adiciona_navios():
        codigo_navio = e1.get()
        origem = e2.get()
        destino = e3.get()
        capacidade_container = e4.get()
        capacidade_tripulacao = e5.get()
        nome_navio = e6.get()
        foto_navio = e7.get()
        id_equipe = e8.get()

        adiciona_navios_persistencia(codigo_navio, origem, destino, capacidade_container, capacidade_tripulacao, nome_navio, foto_navio, id_equipe)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_navios():
        
        members = [('Código do Navio', 'Destino', 'Origem', 'Capacidade de containers', 'Capacidade de tripulação', 'Nome do navio', 'Binario foto', 'ID da equipe')]

        mostra_navios_persistencia(members)
        print("Uau, navios!")

    def mostra_imagem_navio():
        codigo_navio = e1.get()
        mostra_imagem_navio_persistencia(codigo_navio)
        print("Uau, navios!")

    def altera_navios():
        codigo_navio = e1.get()
        origem = e2.get()
        destino = e3.get()
        capacidade_container = e4.get()
        capacidade_tripulacao = e5.get()
        nome_navio = e6.get()
        foto_navio = e7.get()
        equipes_idequipes = e8.get()
        print("Uau, alterou!")
        altera_navios_persistencia(codigo_navio, origem, destino, capacidade_container, capacidade_tripulacao, nome_navio, foto_navio, equipes_idequipes)

    def deleta_navios():
        codigo_navio = e1.get()
        deleta_navios_persistencia(codigo_navio)
        print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com navios:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar navio", command=adiciona_navios, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar navios", command=mostra_navios, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostra imagem navio", command=mostra_imagem_navio, height=5, width=30)
    botaoRead.grid(column=2, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar navios", command=altera_navios, height=5, width=30)
    botaoUpdate.grid(column=3, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar navios", command=deleta_navios, height=5, width=30)
    botaoDelete.grid(column=4, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="Código do navio:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Origem:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Destino::").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Capacidade de containeres:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Capacidade de tripulação:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="Nome do navio:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    Label(janelaFuncionarios, text="Foto navio:").grid(row=10, column=0)
    e7 = Entry(janelaFuncionarios)
    e7.grid(row=10, column=1)

    Label(janelaFuncionarios, text="ID da equipe:").grid(row=10, column=0)
    e8 = Entry(janelaFuncionarios)
    e8.grid(row=10, column=1)
    

    janelaFuncionarios.mainloop()

def abre_tela_equipes():

    def adiciona_equipes():
        id_equipe = e1.get()
        funcao = e2.get()
        quant_funcionarios = e3.get()
        turno = e4.get()
        codinome = e5.get()
        
        adiciona_equipes_persistencia(id_equipe, funcao, quant_funcionarios, turno, codinome)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_equipes():

        members = [('ID da equipe', 'Função da equipe', 'Quantidade de funcionários', 'Turno', 'Codinome da equipe')]

        mostra_equipes_persistencia(members)
        #print("Uau, equipes!")

    def altera_equipes():
        id_equipe = e1.get()
        funcao = e2.get()
        quant_funcionarios = e3.get()
        turno = e4.get()
        codinome = e5.get()
        altera_equipes_persistencia(id_equipe, funcao, quant_funcionarios, turno, codinome)
        #print("Uau, alterou!")

    def deleta_equipes():
        id_equipe = e1.get()
        deleta_equipes_persistencia(id_equipe)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com equipes:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar equipes", command=adiciona_equipes, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar equipes", command=mostra_equipes, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar equipes", command=altera_equipes, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar equipes", command=deleta_equipes, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="ID da equipe:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Função da equipe:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Quantidade de funcionários:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Turno:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Codinome:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    janelaFuncionarios.mainloop()

def abre_tela_atividades_navio():

    def adiciona_atividades():
        id_registros = e1.get()
        containers_em = e2.get()
        containers_des = e3.get()
        dia_chegada = e4.get()
        dia_partida = e5.get()
        id_navio = e6.get()
        
        adiciona_atividades_navios_persistencia(id_registros, containers_em, containers_des, dia_chegada, dia_partida, id_navio)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_atividades():

        members = [('ID da atividade', 'Quantidade de containers embarcados', 'Quantidade de containers desembarcados', 'Dia de chegada', 'Dia de partida', 'ID do navio')]

        mostra_atividades_navios_persistencia(members)
        #print("Uau, atividades de navios!")

    def altera_atividades():
        id_registros = e1.get()
        containers_em = e2.get()
        containers_des = e3.get()
        dia_chegada = e4.get()
        dia_partida = e5.get()
        id_navio = e6.get()

        altera_atividades_navios_persistencia(id_registros, containers_em, containers_des, dia_chegada, dia_partida, id_navio)
        #print("Uau, alterou!")

    def deleta_atividades():
        deletar = e1.get()
        deleta_atividades_navios_persistencia(deletar)
        print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com atividades de navios:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar atividade", command=adiciona_atividades, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar atividades", command=mostra_atividades, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar atividades", command=altera_atividades, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar atividades", command=deleta_atividades, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="ID da atividade:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Quantidade de containers embarcados:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Quantidade de containers desembarcados:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Dia de chegada:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Dia de partida:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="ID do navio:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    janelaFuncionarios.mainloop()

def abre_tela_funcionarios():

    def adiciona_funcionarios():
        cpf = e1.get()
        nome = e2.get()
        cargo = e3.get()
        tempo = e4.get()
        nascimento = e5.get()
        id_equipe = e6.get()

        adiciona_funcionarios_persistencia(cpf, nome, cargo, tempo, nascimento, id_equipe)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_funcionarios():

        members = [('CPF do funcionário', 'Nome do funcionário', 'Cargo do funcionário', 'Tempo de trabalho', 'Data de nascimento', 'ID da equipe')]

        mostra_funcionarios_persistencia(members)
        #print("Uau, funcionarios!")

    def altera_funcionarios():
        cpf = e1.get()
        nome = e2.get()
        cargo = e3.get()
        tempo = e4.get()
        nascimento = e5.get()
        id_equipe = e6.get()
        
        altera_funcionarios_persistencia(cpf, nome, cargo, tempo, nascimento, id_equipe)
        #print("Uau, alterou!")

    def deleta_funcionarios():
        deletar = e1.get()
        deleta_funcionarios_persistencia(deletar)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com funcionários:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar funcionário", command=adiciona_funcionarios, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar funcionários", command=mostra_funcionarios, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar funcionário", command=altera_funcionarios, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar funcionário", command=deleta_funcionarios, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="CPF do Funcionário:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Nome do Funcionário:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Cargo do Funcionário:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Tempo de trabalho:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Data de nascimento:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="ID da equipe:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)


    janelaFuncionarios.mainloop()

def abre_tela_caminhoes():

    def adiciona_caminhoes():
        placa = e1.get()
        capacidade = e2.get()
        ano_fabricacao = e3.get()
        marca = e4.get()
        modelo = e5.get()
        cor = e6.get()
        ultima_revisao = e7.get()
        cpf_func = e8.get()

        adiciona_caminhoes_persistencia(placa, capacidade, ano_fabricacao, marca, modelo, cor, ultima_revisao, cpf_func)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_caminhoes():

        members = [('Placa do caminhão', 'Capacidade de containers', 'Ano de fabricação', 'Marca do caminhão', 'Modelo do caminhão', 'Cor do caminhão', 'Última revisão do caminhão', 'CPF do funcionário responsável')]

        mostra_caminhoes_persistencia(members)
        #print("Uau, caminhões!")

    def altera_caminhoes():
        placa = e1.get()
        capacidade = e2.get()
        ano_fabricacao = e3.get()
        marca = e4.get()
        modelo = e5.get()
        cor = e6.get()
        ultima_revisao = e7.get()
        cpf_func = e8.get()
        
        altera_caminhoes_persistencia(placa, capacidade, ano_fabricacao, marca, modelo, cor, ultima_revisao, cpf_func)
        #print("Uau, alterou!")

    def deleta_caminhoes():
        deletar = e1.get()
        deleta_caminhoes_persistencia(deletar)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com caminhões:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar caminhão", command=adiciona_caminhoes, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar caminhões", command=mostra_caminhoes, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar caminhão", command=altera_caminhoes, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar caminhão", command=deleta_caminhoes, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="Placa do caminhão:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Capacidade de containers:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Ano de fabricação:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Marca do caminhão:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Modelo do caminhão:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="Cor do caminhão:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    Label(janelaFuncionarios, text="Ultima revisão do caminhão:").grid(row=10, column=0)
    e7 = Entry(janelaFuncionarios)
    e7.grid(row=10, column=1)

    Label(janelaFuncionarios, text="CPF do funcionário responsável:").grid(row=11, column=0)
    e8 = Entry(janelaFuncionarios)
    e8.grid(row=11, column=1)


    janelaFuncionarios.mainloop()

def abre_tela_gruas():

    def adiciona_gruas():
        id = e1.get()
        altura = e2.get()
        alcance = e3.get()
        fabricante = e4.get()
        capacidade = e5.get()
        ultima_revisao = e6.get()
        cpf_func = e7.get()

        adiciona_gruas_persistencia(id, altura, alcance, fabricante, capacidade, ultima_revisao, cpf_func)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_gruas():

        members =[('ID da grua', 'Altura em metros', 'Alcance em metros', 'Fabricante', 'Capacidade de carga em kg', 'Última revisão', 'CPF do funcionário responsável')]

        mostra_gruas_persistencia(members)
        #print("Uau, gruas!")

    def altera_gruas():
        id = e1.get()
        altura = e2.get()
        alcance = e3.get()
        fabricante = e4.get()
        capacidade = e5.get()
        ultima_revisao = e6.get()
        cpf_func = e7.get()

        altera_gruas_persistencia(id, altura, alcance, fabricante, capacidade, ultima_revisao, cpf_func)
        #print("Uau, alterou!")

    def deleta_gruas():
        deletar = e1.get()
        deleta_gruas_persistencia(deletar)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com gruas:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar grua", command=adiciona_gruas, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar gruas", command=mostra_gruas, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar grua", command=altera_gruas, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar grua", command=deleta_gruas, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="ID da grua:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Altura em metros:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Alcance em metros:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Fabricante:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Capacidade de carga em kg:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="Última revisão:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    Label(janelaFuncionarios, text="CPF do funcionário responsável:").grid(row=11, column=0)
    e7 = Entry(janelaFuncionarios)
    e7.grid(row=11, column=1)

    janelaFuncionarios.mainloop()

def abre_tela_empilhadeiras():

    def adiciona_empilhadeiras():
        placa = e1.get()
        modelo = e2.get()
        fabricante = e3.get()
        capacidade = e4.get()
        alcance = e5.get()
        ultima_revisao = e6.get()
        cpf_func = e7.get()
        
        adiciona_empilhadeiras_persistencia(placa, modelo, fabricante, capacidade, alcance, ultima_revisao, cpf_func)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_empilhadeiras():

        members = [('Placa', 'Modelo', 'Fabricante', 'Capacidade de carga em kg', 'Alcance em metros', 'Última revisão', 'CPF do funcionário responsável')]

        mostra_empilhadeiras_persistencia(members)
        #print("Uau, empilhadeiras!")

    def altera_empilhadeiras():
        placa = e1.get()
        modelo = e2.get()
        fabricante = e3.get()
        capacidade = e4.get()
        alcance = e5.get()
        ultima_revisao = e6.get()
        cpf_func = e7.get()

        altera_empilhadeiras_persistencia(placa, modelo, fabricante, capacidade, alcance, ultima_revisao, cpf_func)
        #print("Uau, alterou!")

    def deleta_empilhadeiras():
        deletar = e1.get()
        deleta_empilhadeiras_persistencia(deletar)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com empilhadeiras:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar empilhadeira", command=adiciona_empilhadeiras, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar empilhadeiras", command=mostra_empilhadeiras, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar empilhadeira", command=altera_empilhadeiras, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar empilhadeira", command=deleta_empilhadeiras, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="Placa:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Modelo:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Fabricante:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Capacidade de carga em kg:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Alcance em metros:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="Última revisão:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    # NAO COLOQUEI FOREIGN KEY DE ID FUNCIONARIO
    Label(janelaFuncionarios, text="CPF do funcionário responsável:").grid(row=11, column=0)
    e7 = Entry(janelaFuncionarios)
    e7.grid(row=11, column=1)

    janelaFuncionarios.mainloop()

def abre_tela_atividades_porto():

    def adiciona_atividades():
        id_atividades = e1.get()
        id_equipe = e2.get()
        atribuicao_equipe = e3.get()
        horario_inicio = e4.get()
        horario_final = e5.get()
        
        adiciona_atividades_porto_persistencia(id_atividades, id_equipe, atribuicao_equipe, horario_inicio, horario_final)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_atividades():

        members = [('ID da atividade', 'ID da equipe', 'Atribuição da equipe', 'Horário de inicio da atribuição', 'Horário de final da atribuição')]

        mostra_atividades_porto_persistencia(members)
        #print("Uau, atividades do porto!")

    def altera_atividades():
        id_atividades = e1.get()
        id_equipe = e2.get()
        atribuicao_equipe = e3.get()
        horario_inicio = e4.get()
        horario_final = e5.get()
        altera_atividades_porto_persistencia(id_atividades, id_equipe, atribuicao_equipe, horario_inicio, horario_final)
        #print("Uau, alterou!")

    def deleta_atividades():
        deletar = e1.get()
        deleta_atividades_porto_persistencia(deletar)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com atividades do porto:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar area", command=adiciona_atividades, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar areas", command=mostra_atividades, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar areas", command=altera_atividades, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar areas", command=deleta_atividades, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="ID da atividade:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="ID da equipe:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Atribuição da equipe:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Horario de inicio da atribuição:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Horario de final da atribuição:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)


    janelaFuncionarios.mainloop()

def abre_tela_container():

    def adiciona_container():
        id = e1.get()
        peso = e2.get()
        tipo_de_carga = e3.get()
        volume = e4.get()
        fornecedor = e5.get()
        codigo_area = e6.get()
        codigo_navio = e7.get()
        adiciona_containers_persistencia(id, peso, tipo_de_carga, volume, fornecedor, codigo_area, codigo_navio)
        #print("Uau, adicionou " + str(e1.get()))

    def mostra_container():

        members = [('ID do container', 'Peso do container em kg', 'Tipo de carga', 'Volume do container', 'Fornecedor do container', 'Código de espaço para container', 'Código de navio associado')]

        mostra_containers_persistencia(members)
        #print("Uau, containers!")

    def altera_container():
        id = e1.get()
        peso = e2.get()
        tipo_de_carga = e3.get()
        volume = e4.get()
        fornecedor = e5.get()
        codigo_area = e6.get()
        codigo_navio = e7.get()
        altera_containers_persistencia(id, peso, tipo_de_carga, volume, fornecedor, codigo_area, codigo_navio)
        #print("Uau, alterou!")

    def deleta_container():
        deletar = e1.get()
        deleta_containers_persistencia(deletar)
        #print("Uau, deletou!")

    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comandos para mexer com caminhões:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)


    # =======================================================================================================
    #Botões

    botaoCreate = Button(janelaFuncionarios, text="Adicionar Container", command=adiciona_container, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar Containers", command=mostra_container, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar Container", command=altera_container, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar Container", command=deleta_container, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

    # =======================================================================================================
    # Inputs de texto

    Label(janelaFuncionarios, text="ID do container:").grid(row=4, column=0)
    e1 = Entry(janelaFuncionarios)
    e1.grid(row=4, column=1)

    Label(janelaFuncionarios, text="Peso do container em kg:").grid(row=5, column=0)
    e2 = Entry(janelaFuncionarios)
    e2.grid(row=5, column=1)

    Label(janelaFuncionarios, text="Tipo de carga:").grid(row=6, column=0)
    e3 = Entry(janelaFuncionarios)
    e3.grid(row=6, column=1)

    Label(janelaFuncionarios, text="Volume do container:").grid(row=7, column=0)
    e4 = Entry(janelaFuncionarios)
    e4.grid(row=7, column=1)

    Label(janelaFuncionarios, text="Fornecedor do container:").grid(row=8, column=0)
    e5 = Entry(janelaFuncionarios)
    e5.grid(row=8, column=1)

    Label(janelaFuncionarios, text="Código de espaço para container:").grid(row=9, column=0)
    e6 = Entry(janelaFuncionarios)
    e6.grid(row=9, column=1)

    Label(janelaFuncionarios, text="Código de navio associado:").grid(row=10, column=0)
    e7 = Entry(janelaFuncionarios)
    e7.grid(row=10, column=1)


    janelaFuncionarios.mainloop()


janelaPrincipal = Tk()

janelaPrincipal.title("Banco de Dados - Porto")

# Titulo
Bem_Vindo = Label(janelaPrincipal, text="Bem vindo ao banco de dados do porto de Suape")
Bem_Vindo.grid(column=1, row=0, padx=10, pady=10)

#lol = 10*['', '','', '','', '','', '','', '' ]
#for i in range(10):
#    lol[i] = Label(janelaPrincipal, text="Bem vindo ao banco de dados do porto de Suape")
#    lol[i].grid(column=1, row=10+i, padx=10, pady=10)

# Botoes
botaoArea = Button(janelaPrincipal, text="Areas", command=abre_tela_areas, height=5, width=30)
botaoArea.grid(column=0, row=1, padx=10, pady=10)

botaoNavio = Button(janelaPrincipal, text="Navios", command=abre_tela_navios, height=5, width=30)
botaoNavio.grid(column=1, row=1, padx=10, pady=10)

botaoEquipes = Button(janelaPrincipal, text="Equipes", command=abre_tela_equipes, height=5, width=30)
botaoEquipes.grid(column=2, row=1, padx=10, pady=10)

botaoProcessos = Button(janelaPrincipal, text="Registros de atividades (Navio)", command=abre_tela_atividades_navio, height=5, width=30)
botaoProcessos.grid(column=0, row=2, padx=10, pady=10)

botaoFuncionarios = Button(janelaPrincipal, text="Funcionarios", command=abre_tela_funcionarios, height=5, width=30)
botaoFuncionarios.grid(column=1, row=2, padx=10, pady=10)

botaoCaminhoes = Button(janelaPrincipal, text="Caminhoes", command=abre_tela_caminhoes, height=5, width=30)
botaoCaminhoes.grid(column=2, row=2, padx=10, pady=10)

botaoGuindastes = Button(janelaPrincipal, text="Gruas", command=abre_tela_gruas, height=5, width=30)
botaoGuindastes.grid(column=0, row=3, padx=10, pady=10)

botaoEmpilhadeiras = Button(janelaPrincipal, text="Empilhadeiras", command=abre_tela_empilhadeiras, height=5, width=30)
botaoEmpilhadeiras.grid(column=1, row=3, padx=10, pady=10)

botaoEquipesInspecao = Button(janelaPrincipal, text="Registros de atividades (Porto)", command=abre_tela_atividades_porto, height=5, width=30)
botaoEquipesInspecao.grid(column=2, row=3, padx=10, pady=10)

botaoContainer = Button(janelaPrincipal, text="Containers", command=abre_tela_container, height=5, width=30)
botaoContainer.grid(column=1, row=4, padx=10, pady=10)

janelaPrincipal.mainloop()
