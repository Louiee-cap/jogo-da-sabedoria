from sqlite3 import Cursor
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from pathlib import Path
import random
import mysql.connector

def conectar_mysql():
   conexao = mysql.connector.connect(
    host="localhost",       
    user="root",            
    password="imtdb",   
    database="jogo_educacional"
     )

# Base de perguntas por matéria
banco_perguntas = { 
    "Matemática": [
        ("Quanto é 7 x 8?", "54", "56", "63", "58", "60", "B"),
        ("Qual é a metade de 50?", "20", "10", "25", "30", "15", "C"),
        ("Quanto é 10²?", "100", "20", "110", "10", "120", "A"),
        ("Qual é a raiz quadrada de 144?", "10", "11", "12", "13", "14", "C"),
        ("Se um carro percorre 60 km em 1 hora, quantos km ele percorre em 3 horas?", "120", "180", "200", "150", "100", "B")
    ],
    "Português": [
        ("Qual é o antônimo de 'feliz'?", "contente", "alegre", "triste", "divertido", "animado", "C"),
        ("Qual é a forma correta: 'há anos atrás' ou 'há anos'?", "'há anos atrás'", "'há anos'", "'anos atrás'", "'há ano atrás'", "'há ano'", "B"),
        ("Qual é a classe gramatical da palavra 'rapidamente'?", "substantivo", "verbo", "adjetivo", "advérbio", "conjunção", "D"),
        ("Qual é o sujeito na frase: 'Os alunos estudam para a prova.'?", "Os alunos", "Estudam", "Para a prova", "Prova", "A frase não tem sujeito", "A"),
        ("A palavra 'cãozinho' é um exemplo de:", "Verbo", "Aumentativo", "Diminutivo", "Pronome", "Substantivo coletivo", "C")
    ],
    "História": [
        ("Quem foi o primeiro presidente do Brasil?", "Getúlio Vargas", "Marechal Deodoro", "Dom Pedro II", "Lula", "Juscelino Kubitschek", "B"),
        ("Em que ano ocorreu a Proclamação da República?", "1889", "1822", "1500", "1989", "1922", "A"),
        ("Quem descobriu o Brasil?", "Pedro Álvares Cabral", "Cristóvão Colombo", "Vasco da Gama", "Dom João VI", "Tiradentes", "A"),
        ("Quem foi Tiradentes?", "Imperador do Brasil", "Líder da Inconfidência Mineira", "Presidente do Brasil", "Explorador português", "Rei de Portugal", "B"),
        ("Qual era o nome da capital do Brasil antes de Brasília?", "São Paulo", "Salvador", "Rio de Janeiro", "Belo Horizonte", "Recife", "C")
    ],
    "Geografia": [
        ("Qual é o maior país do mundo em extensão territorial?", "Canadá", "Brasil", "China", "Estados Unidos", "Rússia", "E"),
        ("Qual é o rio mais extenso do mundo?", "Amazonas", "Nilo", "Yangtzé", "Mississippi", "Danúbio", "B"),
        ("O que é uma ilha?", "Montanha", "Porção de terra cercada de água", "Deserto", "Vale", "Glaciar", "B"),
        ("Qual é o continente onde está localizado o Brasil?", "Ásia", "Europa", "América", "África", "Oceania", "C"),
        ("O que é um deserto?", "Uma floresta densa", "Uma área coberta de neve", "Região com pouca vegetação e pouca chuva", "Montanha com rios", "Região costeira", "C")
    ],
    "Inglês": [
        ("Qual é o tempo verbal usado na frase 'She is reading a book right now'?", "Present Simple", "Past Simple", "Present Continuous", "Past Continuous", "Future Simple", "C"),
        ("Como se diz 'gato' em inglês?", "Dog", "Cat", "Bird", "Mouse", "Fish", "B"),
        ("Complete a frase com a preposição correta: 'He is interested ___ music.'", "in", "on", "at", "for", "about", "A"),
        ("Qual o plural da palavra 'child'?", "Childs", "Childes", "Children", "Childrens", "Child", "C"),
        ("Traduza para o inglês: 'Eu gosto de aprender novas línguas.'", "I like learning new languages.", "I like learn new languages.", "I likes learning new language.", "I liking to learn new languages.", "I like to learning new languages.", "A")
    ], 
    "Ciências": [
        ("Qual é a função principal dos pulmões no corpo humano?", "Filtrar o sangue", "Bombear sangue", "Trocar oxigênio e dióxido de carbono", "Produzir insulina", "Controlar os músculos", "C"),
        ("O que é fotossíntese e qual é a sua importância para as plantas?", "Respiração das plantas", "Transformação da luz em energia química", "Produção de sementes", "Crescimento das raízes", "Absorção de água", "B"),
        ("Cite três estados físicos da matéria.", "Sólido, líquido e gasoso", "Ácido, base e neutro", "Quente, frio e morno", "Pequeno, médio e grande", "Duro, mole e flexível", "A"),
        ("Qual é o planeta mais próximo do Sol?", "Vênus", "Terra", "Marte", "Mercúrio", "Júpiter", "D"),
        ("O que são os músculos e qual o papel deles no corpo?", "Tecidos que armazenam gordura", "Órgãos que produzem hormônios", "Tecidos que permitem o movimento", "Glândulas que controlam o sangue", "Células que combatem doenças", "C")
    ]
}

   

ranking = []

class JogoDaSabedoriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Sabedoria")
        self.root.geometry("1440x1024")
        self.root.configure(bg="#f0f0f0")

        self.usuario = None
        self.materia = None
        self.serie = None

        self.tela_inicial_jogo()


    ### Tela Inicial
    def tela_inicial_jogo(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\inicial") #-----------> Copia isso tudo aqui e cola isso aqui dentro de cada widget, 
        def pasta_imagens(path: str) -> Path:                                   # e ajusta o nome da última pasta pra cada uma
            return ASSETS_PATH / Path(path)
        

        ## Título
        tk.Label(text="Jogo", font=("Georgia", 96 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=507, y = 15, anchor="nw")
        tk.Label(text="da", font=("Georgia", 96 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 780, y = 15, anchor="nw")
        tk.Label(text="Sabedoria", font=("Georgia", 96 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 467, y = 135, anchor="nw")

        # frame = tk.Frame(self.root, bg="#f0f0f0")
        # frame.place(relx=0.5, rely=0.4, anchor="center") ----->> não precisa disso aparentemente, só consegui ajustar a interface sem ele
                                                                ## arranca das outras widgets e arruma a posição com place, já deve ter todas 
                                                                ## as posições dos elementos no código de cada tela

        ## Imagem Botão aluno
        img_login_aluno = PhotoImage(
            file = pasta_imagens("button_aluno.png"))
        label = Label(image = img_login_aluno)
        label.image = img_login_aluno 
        ## Botão aluno
        tk.Button(
            image = img_login_aluno,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_login_aluno).place(x = 422, y = 348)
        
        ## Imagem botão admin
        img_login_admin = PhotoImage(
            file = pasta_imagens("button_admin.png"))
        label = Label(image = img_login_admin)
        label.image = img_login_admin 
        ## Botão Admin
        tk.Button(
            image = img_login_admin,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_login_admin).place(x = 422, y = 544)
        
        ## Imagem Wave
        img_wave = PhotoImage(
            file = pasta_imagens("wave.png"))
        label = Label(image = img_wave)
        label.image = img_wave
        label.place(x = 0, y = 748)
        
        ##=======================================================

    def tela_login_aluno(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\aluno") 
        def pasta_imagens(path: str) -> Path:  
            return ASSETS_PATH / Path(path)

        ## Imagem Botão Voltar
        img_voltar = PhotoImage(
            file = pasta_imagens("button_sair.png"))
        label = Label(image = img_voltar)
        label.image = img_voltar 
        ## Botão Voltar
        tk.Button(
            image = img_voltar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_inicial_jogo).place(x = 15, y = 15, height = 56, width = 56, anchor = "nw")
        ## Texto Botão Voltar
        tk.Label(text="Voltar", font=("Georgia", 36 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x=80, y = 15, anchor="nw")
        
        ## Título
        tk.Label(text="Faça", font=("Georgia", 96 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=507, y = 15, anchor="nw")
        tk.Label(text="Seu", font=("Georgia", 96 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 780, y = 15, anchor="nw")
        tk.Label(text="Login", font=("Georgia", 96 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 587, y = 135, anchor="nw")

        ## Entry Usuário
        tk.Label(text="Usuário:", font=("Georgia", 28, "bold"), fg = "#46AEBD", bg="#f0f0f0").place(x = 560, y= 350, anchor = "center")
        self.entry_usuario = tk.Entry(font=("Georgia", 24))
        self.entry_usuario.place(x = 725, y = 400, width = 500, anchor = "center")

        ## Entry senha
        tk.Label(text="Senha:", font=("Georgia", 28, "bold"), fg = "#F89E19", bg="#f0f0f0").place(x = 545, y = 470, anchor = "center")
        self.entry_senha = tk.Entry(show = "*", font=("Georgia", 24))
        self.entry_senha.place(x = 725, y = 520, width = 500, anchor = "center")

        ## Imagem Botão Confirmar
        img_confirmar = PhotoImage(
            file = pasta_imagens("button_confirmar.png"))
        label = Label(image = img_confirmar)
        label.image = img_confirmar 
        ## Botão Confirmar
        tk.Button(
            image = img_confirmar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.validar_login_aluno).place(x = 720, y = 670, anchor = "center")
        
        ## Imagem Wave
        img_wave = PhotoImage(
            file = pasta_imagens("wave.png"))
        label = Label(image = img_wave)
        label.image = img_wave
        label.place(x = 0, y = 748)

    ##=======================================================

    def validar_login_aluno(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario and senha:
            self.usuario = usuario
            self.tela_aluno()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")


    ##=======================================================


    def tela_aluno(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\aluno")  
        def pasta_imagens(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        ## Imagem Botão Sair
        img_voltar = PhotoImage(
            file = pasta_imagens("button_sair.png"))
        label = Label(image = img_voltar)
        label.image = img_voltar 
        ## Botão Sair
        tk.Button(
            image = img_voltar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_inicial_jogo).place(x = 15, y = 15, height = 56, width = 56, anchor = "nw")
        ## Texto Botão Sair
        tk.Label(text="Sair", font=("Georgia", 36 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x=80, y = 15, anchor="nw")

        ## Título
        tk.Label(text="Jogo", font=("Georgia", 96 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=507, y = 15, anchor="nw")
        tk.Label(text="da", font=("Georgia", 96 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 780, y = 15, anchor="nw")
        tk.Label(text="Sabedoria", font=("Georgia", 96 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 467, y = 135, anchor="nw")

        ## Imagem Botão Jogar
        img_jogar = PhotoImage(
            file = pasta_imagens("button_jogar.png"))
        label = Label(image = img_jogar)
        label.image = img_jogar 
        ## Botão Jogar
        tk.Button(
            image = img_jogar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.iniciar_jogo_aluno).place(x = 488, y = 308)
        
        ## Imagem Botão Selecionar Matéria
        img_materia = PhotoImage(
            file = pasta_imagens("button_materia.png"))
        label = Label(image = img_materia)
        label.image = img_materia 
        ## Botão Selecionar Matéria
        tk.Button(
            image = img_materia,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_selecao_materia).place(x = 488, y = 463)
        
        ## Imagem Botão Selecionar Série
        img_serie = PhotoImage(
            file = pasta_imagens("button_serie.png"))
        label = Label(image = img_serie)
        label.image = img_serie 
        ## Botão Selecionar Série
        tk.Button(
            image = img_serie,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_selecao_serie).place(x = 488, y = 624)
        
        ## Imagem Wave
        img_wave = PhotoImage(
            file = pasta_imagens("wave.png"))
        label = Label(image = img_wave)
        label.image = img_wave
        label.place(x = 0, y = 748)


    ##=======================================================


    def tela_selecao_materia(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\materias")  
        def pasta_imagens(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        ## Imagem Botão Voltar
        img_voltar = PhotoImage(
            file = pasta_imagens("button_voltar.png"))
        label = Label(image = img_voltar)
        label.image = img_voltar 
        ## Botão Voltar
        tk.Button(
            image = img_voltar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 15, y = 15, height = 56, width = 56, anchor = "nw")
        ## Texto Botão Voltar
        tk.Label(text="Voltar", font=("Georgia", 36 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x=80, y = 15, anchor="nw")

        ## Título
        tk.Label(text="Mat", font=("Georgia", 128 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=405, y = 15, anchor="nw")
        tk.Label(text="ér", font=("Georgia", 128 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 660, y = 15, anchor="nw")
        tk.Label(text="ias", font=("Georgia", 128 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 804, y = 15, anchor="nw")

        ## Imagem Botão Matemática
        img_mat = PhotoImage(
            file = pasta_imagens("button_mat.png"))
        label = Label(image = img_mat)
        label.image = img_mat 
        ## Botão Selecionar Matemática
        tk.Button(
            image = img_mat,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 31, y = 301)  #---> Adicionar comando certo, cada um selecionando cada matéria
        
        ## Imagem Botão Português
        img_port = PhotoImage(
            file = pasta_imagens("button_port.png"))
        label = Label(image = img_port)
        label.image = img_port
        ## Botão Selecionar Português
        tk.Button(
            image = img_port,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 31, y = 580)
        
        ## Imagem Botão História
        img_hist = PhotoImage(
            file = pasta_imagens("button_hist.png"))
        label = Label(image = img_hist)
        label.image = img_hist
        ## Botão Selecionar História
        tk.Button(
            image = img_hist,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 505, y = 301)
        
        ## Imagem Botão Geografia
        img_geo = PhotoImage(
            file = pasta_imagens("button_geo.png"))
        label = Label(image = img_geo)
        label.image = img_geo
        ## Botão Selecionar Geografia
        tk.Button(
            image = img_geo,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 505, y = 580)
        
        ## Imagem Botão Ciências
        img_cie = PhotoImage(
            file = pasta_imagens("button_cie.png"))
        label = Label(image = img_cie)
        label.image = img_cie
        ## Botão Selecionar Ciências
        tk.Button(
            image = img_cie,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 979, y = 301)
        
        ## Imagem Botão Inglês
        img_ing = PhotoImage(
            file = pasta_imagens("button_ing.png"))
        label = Label(image = img_ing)
        label.image = img_ing
        ## Botão Selecionar Inglês
        tk.Button(
            image = img_ing,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 979, y = 580)


    ##=======================================================


    def tela_selecao_serie(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\serie")  
        def pasta_imagens(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        ## Imagem Botão Voltar
        img_voltar = PhotoImage(
            file = pasta_imagens("button_sair.png"))
        label = Label(image = img_voltar)
        label.image = img_voltar 
        ## Botão Voltar
        tk.Button(
            image = img_voltar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 15, y = 15, height = 56, width = 56, anchor = "nw")
        ## Texto Botão Voltar
        tk.Label(text="Voltar", font=("Georgia", 36 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x=80, y = 15, anchor="nw")

        ## Título
        tk.Label(text="Selecione", font=("Georgia", 96 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=480, y = 15, anchor="nw")
        tk.Label(text="Sua", font=("Georgia", 96 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 485, y = 115, anchor="nw")
        tk.Label(text="Série", font=("Georgia", 96 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 690, y = 115, anchor="nw")


        ## Imagem Botão 4º Ano
        img_4ano = PhotoImage(
            file = pasta_imagens("button_4ano.png"))
        label = Label(image = img_4ano)
        label.image = img_4ano
        ## Botão Selecionar 4º Ano
        tk.Button(
            image = img_4ano,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 31, y = 301)
        
        ## Imagem Botão 5º Ano
        img_5ano = PhotoImage(
            file = pasta_imagens("button_5ano.png"))
        label = Label(image = img_5ano)
        label.image = img_5ano
        ## Botão Selecionar 5º Ano
        tk.Button(
            image = img_5ano,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 31, y = 529)
        
        ## Imagem Botão 6º Ano
        img_6ano = PhotoImage(
            file = pasta_imagens("button_6ano.png"))
        label = Label(image = img_6ano)
        label.image = img_6ano
        ## Botão Selecionar 6º Ano
        tk.Button(
            image = img_6ano,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 31, y = 757)
        
        ## Imagem Botão 7º Ano
        img_7ano = PhotoImage(
            file = pasta_imagens("button_7ano.png"))
        label = Label(image = img_7ano)
        label.image = img_7ano
        ## Botão Selecionar 7º Ano
        tk.Button(
            image = img_7ano,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 505, y = 301)
        
        ## Imagem Botão 8º Ano
        img_8ano = PhotoImage(
            file = pasta_imagens("button_8ano.png"))
        label = Label(image = img_8ano)
        label.image = img_8ano
        ## Botão Selecionar 8º Ano
        tk.Button(
            image = img_8ano,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 505, y = 529)
        
        ## Imagem Botão 9º Ano
        img_9ano = PhotoImage(
            file = pasta_imagens("button_9ano.png"))
        label = Label(image = img_9ano)
        label.image = img_9ano
        ## Botão Selecionar 9º Ano
        tk.Button(
            image = img_9ano,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 505, y = 757)
        
        ## Imagem Botão 1º Ensino Médio
        img_1em = PhotoImage(
            file = pasta_imagens("button_1em.png"))
        label = Label(image = img_1em)
        label.image = img_1em
        ## Botão Selecionar 1º Ensino Médio
        tk.Button(
            image = img_1em,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 979, y = 301)
        
        ## Imagem Botão 2º Ensino Médio
        img_2em = PhotoImage(
            file = pasta_imagens("button_2em.png"))
        label = Label(image = img_2em)
        label.image = img_2em
        ## Botão Selecionar 2º Ensino Médio
        tk.Button(
            image = img_2em,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 979, y = 529)
        
        ## Imagem Botão 3º Ensino Médio
        img_3em = PhotoImage(
            file = pasta_imagens("button_3em.png"))
        label = Label(image = img_3em)
        label.image = img_3em
        ## Botão Selecionar 3º Ensino Médio
        tk.Button(
            image = img_3em,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_aluno).place(x = 979, y = 757)


    ##=======================================================


    def tela_selecao_materia_serie(self): 
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(frame, text="Escolha a Matéria:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        self.var_materia = tk.StringVar(value="Matemática")
        materias = ["Matemática", "Português", "História", "Geografia, Ciências, Inglês"]
        for materia in materias:
            tk.Radiobutton(frame, text=materia, variable=self.var_materia, value=materia, font=("Arial", 12), bg="#f0f0f0").pack()

        tk.Label(frame, text="Escolha a Série:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        self.var_serie = tk.StringVar(value="1º ano")
        series = ["1º ano", "2º ano", "3º ano"]
        for serie in series:
            tk.Radiobutton(frame, text=serie, variable=self.var_serie, value=serie, font=("Arial", 12), bg="#f0f0f0").pack()

        tk.Button(frame, text="✅ Iniciar Jogo", font=("Arial", 14), bg="#d0f0d0", command=self.iniciar_jogo_aluno).pack(pady=20)


    ##=======================================================


    def iniciar_jogo_aluno(self):
        materia = self.var_materia.get()
        serie = self.var_serie.get()
        JogoDaSabedoria(self.root, materia, serie, self.usuario, self.tela_selecao_materia_serie)


    ##=======================================================


    # ========== ADMIN ==========
    def tela_login_admin(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\professor") 
        def pasta_imagens(path: str) -> Path:  
            return ASSETS_PATH / Path(path)

        ## Imagem Botão Voltar
        img_voltar = PhotoImage(
            file = pasta_imagens("button_sair.png"))
        label = Label(image = img_voltar)
        label.image = img_voltar 
        ## Botão Voltar
        tk.Button(
            image = img_voltar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_inicial_jogo).place(x = 15, y = 15, height = 56, width = 56, anchor = "nw")
        ## Texto Botão Voltar
        tk.Label(text="Voltar", font=("Georgia", 36 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x=80, y = 15, anchor="nw")
        
        ## Título
        tk.Label(text="Faça", font=("Georgia", 96 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=507, y = 15, anchor="nw")
        tk.Label(text="Seu", font=("Georgia", 96 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 780, y = 15, anchor="nw")
        tk.Label(text="Login", font=("Georgia", 96 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 587, y = 135, anchor="nw")

        ## Entry Usuário
        tk.Label(text="Usuário:", font=("Georgia", 28, "bold"), fg = "#46AEBD", bg="#f0f0f0").place(x = 560, y= 350, anchor = "center")
        self.entry_admin_user = tk.Entry(font=("Georgia", 24))
        self.entry_admin_user.place(x = 725, y = 400, width = 500, anchor = "center")

        ## Entry senha
        tk.Label(text="Senha:", font=("Georgia", 28, "bold"), fg = "#F89E19", bg="#f0f0f0").place(x = 545, y = 470, anchor = "center")
        self.entry_admin_pass = tk.Entry(show = "*", font=("Georgia", 24))
        self.entry_admin_pass.place(x = 725, y = 520, width = 500, anchor = "center")

        ## Imagem Botão Confirmar
        img_confirmar = PhotoImage(
            file = pasta_imagens("button_confirmar.png"))
        label = Label(image = img_confirmar)
        label.image = img_confirmar 
        ## Botão Confirmar
        tk.Button(
            image = img_confirmar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.validar_login_admin).place(x = 720, y = 670, anchor = "center")
        
        ## Imagem Wave
        img_wave = PhotoImage(
            file = pasta_imagens("wave.png"))
        label = Label(image = img_wave)
        label.image = img_wave
        label.place(x = 0, y = 748)


    ##=======================================================


    def validar_login_admin(self):
        usuario = self.entry_admin_user.get()
        senha = self.entry_admin_pass.get()

        if usuario == "admin" and senha == "1234":
            self.tela_admin()
        else:
            messagebox.showerror("Erro", "Credenciais de administrador inválidas.")

        
    ##=======================================================


    def tela_admin(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\professor")  
        def pasta_imagens(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        ## Imagem Botão Sair
        img_voltar = PhotoImage(
            file = pasta_imagens("button_sair.png"))
        label = Label(image = img_voltar)
        label.image = img_voltar 
        ## Botão Sair
        tk.Button(
            image = img_voltar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_inicial_jogo).place(x = 15, y = 15, height = 56, width = 56, anchor = "nw")
        ## Texto Botão Sair
        tk.Label(text="Sair", font=("Georgia", 36 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x=80, y = 15, anchor="nw")

        ## Título
        tk.Label(text="Jogo", font=("Georgia", 96 * -1, "bold"), fg = "#46AEBD" , bg="#f0f0f0").place(x=507, y = 15, anchor="nw")
        tk.Label(text="da", font=("Georgia", 96 * -1, "bold"), fg = "#F89E19" , bg="#f0f0f0").place(x = 780, y = 15, anchor="nw")
        tk.Label(text="Sabedoria", font=("Georgia", 96 * -1, "bold"), fg = "#EB2452" , bg="#f0f0f0").place(x = 467, y = 135, anchor="nw")

        ## Imagem Botão Jogar
        img_jogar = PhotoImage(
            file = pasta_imagens("button_jogar.png"))
        label = Label(image = img_jogar)
        label.image = img_jogar 
        ## Botão Jogar
        tk.Button(
            image = img_jogar,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.iniciar_jogo_aluno).place(x = 488, y = 308)
        
        ## Imagem Botão Editar Questões
        img_editar_quest = PhotoImage(
            file = pasta_imagens("button_editar.png"))
        label = Label(image = img_editar_quest)
        label.image = img_editar_quest 
        ## Botão Editar Questões
        tk.Button(
            image = img_editar_quest,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_editar_questoes).place(x = 488, y = 463)
        
        ## Imagem Botão Ranking
        img_ranking = PhotoImage(
            file = pasta_imagens("button_ranking.png"))
        label = Label(image = img_ranking)
        label.image = img_ranking 
        ## Botão Ranking
        tk.Button(
            image = img_ranking,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.tela_ranking).place(x = 488, y = 624)
        
        ## Imagem Wave
        img_wave = PhotoImage(
            file = pasta_imagens("wave.png"))
        label = Label(image = img_wave)
        label.image = img_wave
        label.place(x = 0, y = 748)


    ##=======================================================


    def tela_editar_questoes(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(frame, text="Edição de Questões", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

        self.var_materia_editar = tk.StringVar(value="Matemática")
        tk.Label(frame, text="Escolha a Matéria:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        materias = ["Matemática", "Português", "História", "Geografia"]
        for materia in materias:
            tk.Radiobutton(frame, text=materia, variable=self.var_materia_editar, value=materia, font=("Arial", 12), bg="#f0f0f0").pack()

        self.entry_pergunta = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_pergunta.pack(pady=10)
        self.entry_resposta_a = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_resposta_a.pack(pady=10)
        self.entry_resposta_b = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_resposta_b.pack(pady=10)
        self.entry_resposta_c = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_resposta_c.pack(pady=10)
        self.entry_resposta_d = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_resposta_d.pack(pady=10)
        self.entry_resposta_e = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_resposta_e.pack(pady=10)
        self.entry_resposta_correta = tk.Entry(frame, font=("Arial", 14), width=50)
        self.entry_resposta_correta.pack(pady=10)

        tk.Button(frame, text="Adicionar Pergunta", font=("Arial", 14), bg="#d0ff90", command=self.adicionar_pergunta).pack(pady=10)
        tk.Button(frame, text="⬅ Voltar", font=("Arial", 12), command=self.tela_admin).pack(pady=10)


    ##=======================================================


    def adicionar_pergunta(self):
        pergunta = self.entry_pergunta.get()
        resposta_a = self.entry_resposta_a.get()
        resposta_b = self.entry_resposta_b.get()
        resposta_c = self.entry_resposta_c.get()
        resposta_d = self.entry_resposta_d.get()
        resposta_e = self.entry_resposta_e.get()
        resposta_correta = self.entry_resposta_correta.get()

        if pergunta and resposta_a and resposta_b and resposta_c and resposta_d and resposta_e and resposta_correta:
            materia = self.var_materia_editar.get()
            banco_perguntas[materia].append((pergunta, resposta_a, resposta_b, resposta_c, resposta_d, resposta_e, resposta_correta))
            messagebox.showinfo("Sucesso", "Pergunta adicionada com sucesso!")
            self.limpar_campos_edicao()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


    ##=======================================================


    def limpar_campos_edicao(self):
        self.entry_pergunta.delete(0, tk.END)
        self.entry_resposta_a.delete(0, tk.END)
        self.entry_resposta_b.delete(0, tk.END)
        self.entry_resposta_c.delete(0, tk.END)
        self.entry_resposta_d.delete(0, tk.END)
        self.entry_resposta_e.delete(0, tk.END)
        self.entry_resposta_correta.delete(0, tk.END)


    ##=======================================================


    def tela_ranking(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(relx=0.5, rely=0.3, anchor="center")

        tk.Label(frame, text="Ranking de Pontuação", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)
        ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)
        for i, (nome, pontos) in enumerate(ranking_ordenado[:10], start=1):
            tk.Label(frame, text=f"{i}. {nome} - {pontos} pts", font=("Arial", 12), bg="#f0f0f0").pack()

        tk.Button(frame, text="⬅ Voltar", command=self.tela_admin).pack(pady=20)


    ##=======================================================


class JogoDaSabedoria:
    def __init__(self, master, materia, serie, usuario, voltar_menu_callback):
        self.master = master
        self.materia = materia
        self.serie = serie
        self.usuario = usuario
        self.voltar_menu_callback = voltar_menu_callback

        self.pergunta_atual = 0
        self.pontuacao = 0
        self.dica_usada = False
        self.checkpoint = 0

        perguntas_da_materia = banco_perguntas.get(materia, [])
        self.perguntas_embaralhadas = random.sample(perguntas_da_materia, len(perguntas_da_materia))

        for widget in self.master.winfo_children():
            widget.destroy()

        self.criar_widgets()


    ##=======================================================


    def criar_widgets(self):
        self.frame_central = tk.Frame(self.master, bg="#f0f0f0")
        self.frame_central.place(relx=0.5, rely=0.1, anchor="n")

        self.label_pergunta = tk.Label(self.frame_central, text="", font=("Arial", 16), wraplength=700, justify="center", bg="#f0f0f0")
        self.label_pergunta.pack(pady=20)

        self.botoes = []
        self.letras = ["A", "B", "C", "D", "E"]
        for i in range(5):
            botao = tk.Button(self.frame_central, text="", width=50, font=("Arial", 12),
                              command=lambda letra=self.letras[i], idx=i: self.verificar_resposta(letra, idx))
            botao.pack(pady=5)
            self.botoes.append(botao)

        self.botao_dica = tk.Button(self.master, text="💡 Usar Dica (eliminar 2)", command=self.usar_dica, font=("Arial", 12), bg="#ffffcc")
        self.botao_dica.pack(pady=10)

        self.botao_sair = tk.Button(self.master, text="🚪 Sair", command=self.voltar_menu_callback, font=("Arial", 12), bg="#f0d0d0")
        self.botao_sair.pack(pady=10)

        self.label_pontuacao = tk.Label(self.master, text=f"Pontuação: {self.pontuacao}", font=("Arial", 12), bg="#f0f0f0")
        self.label_pontuacao.pack(pady=10, side="bottom")

        self.carregar_pergunta()


    ##=======================================================


    def carregar_pergunta(self):
        if self.pergunta_atual < len(self.perguntas_embaralhadas):
            pergunta = self.perguntas_embaralhadas[self.pergunta_atual]
            self.label_pergunta.config(text=pergunta[0])
            for i in range(5):
                self.botoes[i].config(text=f"{self.letras[i]}) {pergunta[i+1]}", state="normal", bg="SystemButtonFace")
            if not self.dica_usada:
                self.botao_dica.config(state="normal")
        else:
            self.exibir_tela_final()


    ##=======================================================


    def verificar_resposta(self, letra_escolhida, idx_escolhido):
        correta = self.perguntas_embaralhadas[self.pergunta_atual][6]
        letra_correta_idx = self.letras.index(correta)

        for botao in self.botoes:
            botao.config(state="disabled")
        self.botao_dica.config(state="disabled")

        if letra_escolhida == correta:
            self.pontuacao += 100
            self.botoes[idx_escolhido].config(bg="#32CD32")
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
            self.pergunta_atual += 1

            if self.pergunta_atual % 3 == 0:
                self.checkpoint = self.pergunta_atual
                messagebox.showinfo("Checkpoint", "Checkpoint alcançado!")

            self.master.after(1000, self.carregar_pergunta)
        else:
            self.botoes[idx_escolhido].config(bg="red")
            self.botoes[letra_correta_idx].config(bg="#32CD32")
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
            self.master.after(1000, self.exibir_tela_final)


    ##=======================================================


    def usar_dica(self):
        if self.dica_usada:
            return
        self.dica_usada = True
        self.botao_dica.config(state="disabled")

        correta = self.perguntas_embaralhadas[self.pergunta_atual][6]
        letra_correta_idx = self.letras.index(correta)
        erradas = [i for i in range(5) if i != letra_correta_idx and self.botoes[i]['state'] == "normal"]
        eliminar = random.sample(erradas, 2)

        for i in eliminar:
            self.botoes[i].config(state="disabled")


    ##=======================================================


    def exibir_tela_final(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        final_frame = tk.Frame(self.master, bg="#f0f0f0")
        final_frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(final_frame, text=f"Fim de Jogo!\nPontuação: {self.pontuacao} Reais", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        # ranking.append((self.usuario, self.pontuacao))
        # salvar_ranking_mysql(self.usuario, self.pontuacao)


        tk.Button(final_frame, text="🔁 Jogar Novamente", font=("Arial", 14), bg="#d0f0d0", command=self.jogar_novamente).pack(pady=10)
        tk.Button(final_frame, text="🚪 Sair", font=("Arial", 14), bg="#f0d0d0", command=self.voltar_menu_callback).pack(pady=10)


    ##=======================================================


    def jogar_novamente(self):
        self.pergunta_atual = 0
        self.pontuacao = 0
        self.dica_usada = False
        self.checkpoint = 0
        perguntas_da_materia = banco_perguntas.get(self.materia, [])
        self.perguntas_embaralhadas = random.sample(perguntas_da_materia, len(perguntas_da_materia))
        for widget in self.master.winfo_children():
            widget.destroy()
        self.criar_widgets()


# Inicializar o app
# carregar_perguntas_do_banco()
root = tk.Tk()
app = JogoDaSabedoriaApp(root)
root.mainloop()
