from tkinter import *

def bruh():
    print("LOL")

def abre_tela_funcionarios():
    janelaFuncionarios = Tk()

    bem_vindo_funcionario = Label(janelaFuncionarios, text="Comanos para mexer com funcionários:")
    bem_vindo_funcionario.grid(column=0, row=0, padx=10, pady=10)

    botaoCreate = Button(janelaFuncionarios, text="Adicionar funcionário", command=bruh, height=5, width=30)
    botaoCreate.grid(column=0, row=1, padx=10, pady=10)

    botaoRead = Button(janelaFuncionarios, text="Mostrar funcionários", command=bruh, height=5, width=30)
    botaoRead.grid(column=1, row=1, padx=10, pady=10)

    botaoUpdate = Button(janelaFuncionarios, text="Atualizar funcionário", command=bruh, height=5, width=30)
    botaoUpdate.grid(column=2, row=1, padx=10, pady=10)

    botaoDelete = Button(janelaFuncionarios, text="Deletar funcionário", command=bruh, height=5, width=30)
    botaoDelete.grid(column=3, row=1, padx=10, pady=10)

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
botaoArea = Button(janelaPrincipal, text="Areas", command=abre_tela_funcionarios, height=5, width=30)
botaoArea.grid(column=0, row=1, padx=10, pady=10)

botaoNavio = Button(janelaPrincipal, text="Navios", command=abre_tela_funcionarios, height=5, width=30)
botaoNavio.grid(column=1, row=1, padx=10, pady=10)

botaoEquipes = Button(janelaPrincipal, text="Equipes", command=abre_tela_funcionarios, height=5, width=30)
botaoEquipes.grid(column=2, row=1, padx=10, pady=10)

botaoProcessos = Button(janelaPrincipal, text="Processos", command=abre_tela_funcionarios, height=5, width=30)
botaoProcessos.grid(column=0, row=2, padx=10, pady=10)

botaoFuncionarios = Button(janelaPrincipal, text="Funcionarios", command=abre_tela_funcionarios, height=5, width=30)
botaoFuncionarios.grid(column=1, row=2, padx=10, pady=10)

botaoCaminhoes = Button(janelaPrincipal, text="Caminhoes", command=abre_tela_funcionarios, height=5, width=30)
botaoCaminhoes.grid(column=2, row=2, padx=10, pady=10)

botaoGuindastes = Button(janelaPrincipal, text="Guindastes", command=abre_tela_funcionarios, height=5, width=30)
botaoGuindastes.grid(column=0, row=3, padx=10, pady=10)

botaoEmpilhadeiras = Button(janelaPrincipal, text="Empilhadeiras", command=abre_tela_funcionarios, height=5, width=30)
botaoEmpilhadeiras.grid(column=1, row=3, padx=10, pady=10)

botaoEquipesInspecao = Button(janelaPrincipal, text="Equipes de Inspeção", command=abre_tela_funcionarios, height=5, width=30)
botaoEquipesInspecao.grid(column=2, row=3, padx=10, pady=10)

botaoContainer = Button(janelaPrincipal, text="Containers", command=abre_tela_funcionarios, height=5, width=30)
botaoContainer.grid(column=1, row=4, padx=10, pady=10)

janelaPrincipal.mainloop()