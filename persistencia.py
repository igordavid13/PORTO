from distutils.log import error
import psycopg2
import psycopg2.extras
from tkinter import *
from PIL import Image
import pathlib

#hostname = 'localhost'
#database = 'Porto'
#username = 'postgres'
#pwd = '030601'
#port_id = 5432

#conn = None
#cur = None

class Table:
    # Initialize a constructor
    def __init__(self, gui, total_rows, total_columns, members):

        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                #print(i)
                if i == 0:
                    self.entry = Entry(gui, width=35, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 9, 'bold'))
                else:
                    self.entry = Entry(gui, width=35, fg='blue',
                               font=('Arial', 9, ''))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, members[i][j])


def connection(SCRIPT, VALUE, members):

    hostname = 'localhost'
    database = 'Porto'
    username = 'postgres'
    pwd = 'Capacete7'
    port_id = 5432

    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if VALUE == None:
                
            gui = Tk()
            gui.geometry("1500x500")

            main_frame = Frame(gui)
            main_frame.pack(fill=BOTH, expand=1)

            my_canvas = Canvas(main_frame)

            my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)

            hor_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
            
            my_scrollbar.pack(side=RIGHT, fill=Y)
            hor_scrollbar.pack(side=BOTTOM, fill=X)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            my_canvas.configure(yscrollcommand=my_scrollbar.set, xscrollcommand=hor_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            second_frame = Frame(my_canvas)

            my_canvas.create_window((0,0), window=second_frame, anchor="nw")
            
            cur.execute(SCRIPT, None)
            for record in cur.fetchall():
                #instance = record
                #instance.pop(-2)
                members.append(record)

            table = Table(second_frame, len(members), len(members[0]), members)
            
            gui.mainloop()
            
        elif VALUE == 'imagem':
                
            cur.execute('SELECT foto_navio FROM navio where codigo_navio = %s',SCRIPT,)
            
            #C:\Users\igord\Desktop\7_SEMESTRE\BD\Projeto\PORTO\Atualizado\Navio1.jpg
            blob = cur.fetchone()
            path = pathlib.Path(__file__).parent.resolve()
            path = str(path)
            path = path + "\\" + "NAVIO_IMAGE.jpg"
            open(path, 'wb').write(blob[0])
            im = Image.open(r"{}".format(path))
            im.show()
            

        else:
            cur.execute(SCRIPT,VALUE)
            conn.commit()
            if(members == 'PROCEDURE'):
                print(conn.notices)
            
      
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:    
            conn.close()
  

# ==============================================================================================

# Areas

def adiciona_areas_persistencia(codigo_espaco_container, regiao, corredor_letra, corredor_numero, setor, id_equipe):

    SCRIPT = ''' INSERT INTO area VALUES(%s,%s,%s,%s,%s,%s);'''
    VALUE = (codigo_espaco_container, regiao, corredor_letra, corredor_numero, setor, id_equipe)

    connection(SCRIPT, VALUE, None)

def mostra_areas_persistencia(members):

    SCRIPT = '''SELECT * FROM area'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_areas_persistencia(codigo_espaco_container, regiao, corredor_letra, corredor_numero, setor, id_equipe):

    SCRIPT = 'UPDATE area SET região = %s, corredor_letra =%s, corredor_numero = %s, setor = %s, equipes_idequipes = %s WHERE codigo_espaco_para_container = %s' 
    VALUE = (regiao, corredor_letra, corredor_numero, setor, id_equipe, codigo_espaco_container)

    connection(SCRIPT, VALUE, None)

def deleta_areas_persistencia(codigo_espaco_container):
    
    SCRIPT = '''DELETE FROM area WHERE codigo_espaco_para_container = %s'''
    VALUE = (codigo_espaco_container,)

    connection(SCRIPT, VALUE, None)

# ==============================================================================================

# Navios

def adiciona_navios_persistencia(codigo_navio, origem, destino, capacidade_container, capacidade_tripulacao, nome_navio, foto_navio, equipes_idequipes):
    image = open(foto_navio, 'rb').read()
    SCRIPT = '''INSERT INTO navio VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'''
    VALUE = (codigo_navio, destino, origem, capacidade_container, capacidade_tripulacao, nome_navio, psycopg2.Binary(image), equipes_idequipes)
    connection(SCRIPT, VALUE, None)

def mostra_navios_persistencia(members):

    SCRIPT = '''SELECT * FROM navio'''
    connection(SCRIPT, None, members)

def mostra_imagem_navio_persistencia(codigo_navio):
    SCRIPT = (codigo_navio)
    VALUE = "imagem"
    connection(SCRIPT, VALUE, None)

def altera_navios_persistencia(codigo_navio, origem, destino, capacidade_container, capacidade_tripulacao, nome_navio, foto_navio, equipes_idequipes):
    image = open(foto_navio, 'rb').read()
    SCRIPT = 'UPDATE navio SET  origem = %s, destino =%s, capacidade_containers = %s, capacidade_tripulacao = %s, nome_navio = %s, foto_navio = %s, equipes_idequipes = %s  WHERE codigo_navio = %s' 
    VALUE = (origem, destino, capacidade_container, capacidade_tripulacao, nome_navio, psycopg2.Binary(image), equipes_idequipes, codigo_navio)

    connection(SCRIPT, VALUE, None)

def deleta_navios_persistencia(codigo_navio):

    SCRIPT = '''DELETE FROM navio WHERE codigo_navio = %s'''
    VALUE = (codigo_navio,)

    connection(SCRIPT, VALUE, None)

# ==============================================================================================

# Equipes

def adiciona_equipes_persistencia(id_equipe, funcao, quant_funcionarios, turno, codinome):

    SCRIPT = ''' INSERT INTO equipes VALUES(%s,%s,%s,%s,%s);'''
    VALUE = (id_equipe, funcao, quant_funcionarios, turno, codinome)

    connection(SCRIPT, VALUE, None)

def mostra_equipes_persistencia(members):

    SCRIPT = '''SELECT * FROM equipes'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_equipes_persistencia(id_equipe, funcao, quant_funcionarios, turno, codinome):

    SCRIPT = 'UPDATE equipes SET funcao = %s, quantidade_funcionarios =%s, turno =%s, codinome = %s WHERE idequipes = %s' 
    VALUE = (funcao, quant_funcionarios, turno, codinome, id_equipe)

    connection(SCRIPT, VALUE, None)

def deleta_equipes_persistencia(id_equipe):
    
    SCRIPT = '''DELETE FROM equipes WHERE idequipes = %s'''
    VALUE = (id_equipe,)

    connection(SCRIPT, VALUE, None)
    
# ==============================================================================================

# Registros atividade navios

def adiciona_atividades_navios_persistencia(id_registros, containers_em, containers_des, dia_chegada, dia_partida, id_navio):

    SCRIPT = ''' INSERT INTO registros_atividade_navios VALUES(%s,%s,%s,%s,%s,%s);'''
    VALUE = (id_registros, containers_em, containers_des, dia_chegada, dia_partida, id_navio)

    connection(SCRIPT, VALUE, None)

def mostra_atividades_navios_persistencia(members):

    SCRIPT = '''SELECT * FROM registros_atividade_navios'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_atividades_navios_persistencia(id_registros, containers_em, containers_des, dia_chegada, dia_partida, id_navio):

    SCRIPT = 'UPDATE registros_atividade_navios SET containers_embarcados =%s, containers_desembarcados =%s, dia_chegada = %s, dia_partida = %s, navio_codigo_navio WHERE idregistros = %s' 
    VALUE = (id_registros, containers_em, containers_des, dia_chegada, dia_partida, id_navio)

    connection(SCRIPT, VALUE, None)

def deleta_atividades_navios_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM registros_atividade_navios WHERE idregistros = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)
    
# ==============================================================================================

# Funcionarios

def adiciona_funcionarios_persistencia(cpf, nome, cargo, tempo, nascimento, id_equipe):

    SCRIPT = ''' INSERT INTO funcionario VALUES(%s,%s,%s,%s,%s,%s);'''
    VALUE = (cpf, nome, cargo, tempo, nascimento, id_equipe)

    connection(SCRIPT, VALUE, None)

def mostra_funcionarios_persistencia(members):

    SCRIPT = '''SELECT * FROM funcionario'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_funcionarios_persistencia(cpf, nome, cargo, tempo, nascimento, id_equipe):

    SCRIPT = 'UPDATE funcionario SET nome =%s, cargo =%s, tempo_de_trabalho = %s, nascimento = %s, equipes_idequipes = %s WHERE cpf = %s' 
    VALUE = (nome, cargo, tempo, nascimento, id_equipe, cpf)

    connection(SCRIPT, VALUE, None)

def deleta_funcionarios_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM funcionario WHERE cpf = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)
        
# ==============================================================================================

# Caminhoes

def adiciona_caminhoes_persistencia(placa, capacidade, ano_fabricacao, marca, modelo, cor, ultima_revisao, cpf_func):

    SCRIPT = ''' INSERT INTO caminhao VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'''
    VALUE = (placa, capacidade, ano_fabricacao, marca, modelo, cor, cpf_func, ultima_revisao)

    connection(SCRIPT, VALUE, None)

def mostra_caminhoes_persistencia(members):

    SCRIPT = '''SELECT * FROM caminhao'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_caminhoes_persistencia(placa, capacidade, ano_fabricacao, marca, modelo, cor, ultima_revisao, cpf_func):

    SCRIPT = 'UPDATE caminhao SET capacidade_de_containers =%s, ano_fabricacao = %s, marca = %s, modelo = %s, cor = %s, funcionario_cpf = %s, ultima_revisao = %s WHERE placa = %s' 
    VALUE = (capacidade, ano_fabricacao, marca, modelo, cor, cpf_func, ultima_revisao, placa)

    connection(SCRIPT, VALUE, None)

def deleta_caminhoes_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM caminhao WHERE placa = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)
        
# ==============================================================================================

# Gruas

def adiciona_gruas_persistencia(id, altura, alcance, fabricante, capacidade, ultima_revisao, cpf_func):

    SCRIPT = ''' INSERT INTO grua VALUES(%s,%s,%s,%s,%s,%s,%s);'''
    VALUE = (id, altura, alcance, fabricante, capacidade, cpf_func, ultima_revisao)

    connection(SCRIPT, VALUE, None)

def mostra_gruas_persistencia(members):

    SCRIPT = '''SELECT * FROM grua'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_gruas_persistencia(id, altura, alcance, fabricante, capacidade, ultima_revisao, cpf_func):

    SCRIPT = 'UPDATE grua SET altura_metros =%s, alcance_metros = %s, fabricante = %s, capacidade_de_carga_kg = %s, funcionario_cpf = %s, ultima_revisao = %s WHERE idgrua = %s' 
    VALUE = (altura, alcance, fabricante, capacidade, cpf_func, ultima_revisao, id)

    connection(SCRIPT, VALUE, None)

def deleta_gruas_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM grua WHERE idgrua = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)
     
# ==============================================================================================

# Empilhadeiras

def adiciona_empilhadeiras_persistencia(placa, modelo, fabricante, capacidade, alcance, ultima_revisao, cpf_func):

    SCRIPT = ''' INSERT INTO empilhadeira VALUES(%s,%s,%s,%s,%s,%s,%s);'''
    VALUE = (placa, modelo, fabricante, capacidade, alcance, ultima_revisao, cpf_func)

    connection(SCRIPT, VALUE, None)

def mostra_empilhadeiras_persistencia(members):

    SCRIPT = '''SELECT * FROM empilhadeira'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_empilhadeiras_persistencia(placa, modelo, fabricante, capacidade, alcance, ultima_revisao, cpf_func):

    SCRIPT = 'UPDATE empilhadeira SET modelo = %s, fabricante = %s, capacidade_carga_kg = %s, alcance_metros = %s, ultima_revisao = %s, funcionario_cpf = %s WHERE placa = %s' 
    VALUE = (modelo, fabricante, capacidade, alcance, ultima_revisao, cpf_func, placa)

    connection(SCRIPT, VALUE, None)

def deleta_empilhadeiras_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM empilhadeira WHERE placa = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)
     
# ==============================================================================================

# Registros de atividade de porto

def adiciona_atividades_porto_persistencia(id_atividades, id_equipe, atribuicao_equipe, horario_inicio, horario_final):

    SCRIPT = ''' INSERT INTO registro_de_trabalhos VALUES(%s,%s,%s,%s,%s,%s,%s);'''
    VALUE = (id_atividades, id_equipe, atribuicao_equipe, horario_inicio, horario_final)

    connection(SCRIPT, VALUE, None)

def mostra_atividades_porto_persistencia(members):

    SCRIPT = '''SELECT * FROM registro_de_trabalhos'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_atividades_porto_persistencia(id_atividades, id_equipe, atribuicao_equipe, horario_inicio, horario_final):

    SCRIPT = 'UPDATE registro_de_trabalhos SET equipes_idequipes = %s, atribuicao_equipe = %s, horario_inicio_atribuicao = %s, horario_final_atribuicao = %s WHERE idtrabalho = %s' 
    VALUE = (id_equipe, atribuicao_equipe, horario_inicio, horario_final, id_atividades)

    connection(SCRIPT, VALUE, None)

def deleta_atividades_porto_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM registro_de_trabalhos WHERE idtrabalho = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)
     
# ==============================================================================================

# Containers

def adiciona_containers_persistencia(id, peso, tipo_de_carga, volume, fornecedor, codigo_area, codigo_navio):

    SCRIPT = ''' INSERT INTO container VALUES(%s,%s,%s,%s,%s,%s,%s);'''
    VALUE = (id, peso, tipo_de_carga, volume, fornecedor, codigo_area, codigo_navio)

    connection(SCRIPT, VALUE, None)

def mostra_containers_persistencia(members):

    SCRIPT = '''SELECT * FROM container'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

def altera_containers_persistencia(id, peso, tipo_de_carga, volume, fornecedor, codigo_area, codigo_navio):

    SCRIPT = 'UPDATE container SET peso_kg = %s, tipo_de_carga = %s, volume_container_litros = %s, fornecedor = %s, area_codigo_espaço_para_container = %s, navio_codigo_navio = %s WHERE idcontainer = %s' 
    VALUE = (peso, tipo_de_carga, volume, fornecedor, codigo_area, codigo_navio, id)

    connection(SCRIPT, VALUE, None)

def deleta_containers_persistencia(deletar):
    
    SCRIPT = '''DELETE FROM container WHERE idcontainer = %s'''
    VALUE = (deletar,)

    connection(SCRIPT, VALUE, None)

# ==============================================================================================

# View
 
def mostra_tela_view(members):

    SCRIPT = '''SELECT * FROM vw_container_area_navio'''
    # VALUE = ''''''
    connection(SCRIPT, None, members)

# ==============================================================================================

# Procedure

def consulta_experiencia_persistencia(pk):
    SCRIPT = '''CALL proc_experiencia_func(%s)'''
    VALUE = (pk)
    connection(SCRIPT, VALUE, 'PROCEDURE')





