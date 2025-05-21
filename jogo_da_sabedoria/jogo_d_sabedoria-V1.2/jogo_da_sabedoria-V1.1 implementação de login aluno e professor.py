import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

# Conectar ou criar banco de dados
conn = sqlite3.connect("show_do_milhao.db")
cursor = conn.cursor()
perguntas_iniciais = [
    ("Qual é a capital do Brasil?", "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Belo Horizonte", "C"),
    ("Quanto é 2 + 2?", "3", "4", "5", "6", "7", "B"),
    ("Qual é a cor do céu em um dia claro?", "Vermelho", "Amarelo", "Azul", "Verde", "Laranja", "C"),
    ("Qual o maior planeta do Sistema Solar?", "Terra", "Marte", "Júpiter", "Saturno", "Vênus", "C"),
    ("Quem escreveu 'Dom Casmurro'?", "Machado de Assis", "Carlos Drummond", "Clarice Lispector", "José de Alencar", "Graciliano Ramos", "A"),
    ("Qual é o elemento químico representado por H?", "Hélio", "Hidrogênio", "Mercúrio", "Ferro", "Oxigênio", "B"),
    ("Em que continente está o Egito?", "África", "Ásia", "Europa", "América", "Oceania", "A"),
    ("Quem descobriu o Brasil?", "Dom Pedro I", "Cristóvão Colombo", "Pedro Álvares Cabral", "Vasco da Gama", "Fernão Dias", "C"),
    ("Quanto é 10 dividido por 2?", "3", "4", "5", "6", "7", "C"),
    ("Qual é a língua oficial do Brasil?", "Inglês", "Espanhol", "Português", "Francês", "Italiano", "C"),
]
# Criar tabelas se não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS perguntas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        enunciado TEXT,
        alt_a TEXT,
        alt_b TEXT,
        alt_c TEXT,
        alt_d TEXT,
        alt_e TEXT,
        correta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ranking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        pontuacao INTEGER
    )
''')
conn.commit()

# Função para carregar perguntas do banco
def carregar_perguntas():
    cursor.execute("SELECT * FROM perguntas")
    return cursor.fetchall()

class ShowDoMilhaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Show do Milhão")
        self.root.geometry("900x600")
        self.usuario = None
        self.tela_login()

    def tela_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(frame, text="Usuário:", font=("Arial", 14)).pack(pady=5)
        self.entry_usuario = tk.Entry(frame, font=("Arial", 14))
        self.entry_usuario.pack()

        tk.Label(frame, text="Senha:", font=("Arial", 14)).pack(pady=5)
        self.entry_senha = tk.Entry(frame, show="*", font=("Arial", 14))
        self.entry_senha.pack()

        tk.Button(frame, text="Entrar", font=("Arial", 14), command=self.validar_login).pack(pady=20)

    def validar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "admin" and senha == "admin":
            self.tela_admin()
        elif usuario and senha:
            self.usuario = usuario
            self.iniciar_jogo_aluno()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def iniciar_jogo_aluno(self):
        ShowDoMilhao(self.root, self.usuario)

    def tela_admin(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(frame, text="Bem-vindo, Administrador!", font=("Arial", 18)).pack(pady=10)

        tk.Button(frame, text="Editar Questões", font=("Arial", 14), command=self.editar_questoes).pack(pady=10)
        tk.Button(frame, text="Visualizar Ranking", font=("Arial", 14), command=self.visualizar_ranking).pack(pady=10)

    def editar_questoes(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Enunciado").grid(row=0, column=0)
        tk.Label(frame, text="A").grid(row=1, column=0)
        tk.Label(frame, text="B").grid(row=2, column=0)
        tk.Label(frame, text="C").grid(row=3, column=0)
        tk.Label(frame, text="D").grid(row=4, column=0)
        tk.Label(frame, text="E").grid(row=5, column=0)
        tk.Label(frame, text="Correta").grid(row=6, column=0)

        self.entrys = [tk.Entry(frame, width=80) for _ in range(7)]
        for i, e in enumerate(self.entrys):
            e.grid(row=i, column=1)

        tk.Button(frame, text="Salvar", command=self.salvar_pergunta).grid(row=7, column=1, pady=10)
        tk.Button(frame, text="Voltar", command=self.tela_admin).grid(row=8, column=1)

    def salvar_pergunta(self):
        dados = [e.get() for e in self.entrys]
        if len(dados) == 7 and all(dados):
            cursor.execute('''
                INSERT INTO perguntas (enunciado, alt_a, alt_b, alt_c, alt_d, alt_e, correta)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', tuple(dados))
            conn.commit()
            messagebox.showinfo("Sucesso", "Pergunta salva com sucesso!")
            for e in self.entrys:
                e.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def visualizar_ranking(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Ranking de Jogadores", font=("Arial", 16)).pack(pady=10)

        cursor.execute("SELECT usuario, pontuacao FROM ranking ORDER BY pontuacao DESC")
        for usuario, pontuacao in cursor.fetchall():
            tk.Label(frame, text=f"{usuario} - {pontuacao} pontos").pack()

        tk.Button(frame, text="Voltar", command=self.tela_admin).pack(pady=20)

class ShowDoMilhao:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario
        self.perguntas = carregar_perguntas()
        if not self.perguntas:
            messagebox.showerror("Erro", "Sem perguntas no banco de dados.")
            return
        self.perguntas_embaralhadas = random.sample(self.perguntas, len(self.perguntas))
        self.pergunta_atual = 0
        self.pontuacao = 0
        self.dica_usada = False
        self.letras = ["A", "B", "C", "D", "E"]

        for widget in self.master.winfo_children():
            widget.destroy()

        self.criar_widgets()

    def criar_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=30)

        self.label_pergunta = tk.Label(self.frame, text="", font=("Arial", 14), wraplength=700)
        self.label_pergunta.pack(pady=20)

        self.botoes = []
        for i in range(5):
            b = tk.Button(self.frame, text="", font=("Arial", 12), width=60,
                          command=lambda i=i: self.verificar_resposta(i))
            b.pack(pady=5)
            self.botoes.append(b)

        self.botao_dica = tk.Button(self.frame, text="Usar Dica", command=self.usar_dica)
        self.botao_dica.pack(pady=10)

        self.label_pontuacao = tk.Label(self.frame, text="Pontuação: 0")
        self.label_pontuacao.pack()

        self.carregar_proxima()

    def carregar_proxima(self):
        if self.pergunta_atual >= len(self.perguntas_embaralhadas):
            self.fim_jogo()
            return

        p = self.perguntas_embaralhadas[self.pergunta_atual]
        self.id_pergunta = p[0]
        self.label_pergunta.config(text=p[1])
        for i in range(5):
            self.botoes[i].config(text=f"{self.letras[i]}) {p[i + 2]}", state="normal", bg="SystemButtonFace")
        self.botao_dica.config(state="normal")
        self.dica_usada = False

    def verificar_resposta(self, i):
        correta = self.perguntas_embaralhadas[self.pergunta_atual][7]
        if self.letras[i] == correta:
            self.pontuacao += 100
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
            self.botoes[i].config(bg="green")
        else:
            self.botoes[i].config(bg="red")
            idx_correto = self.letras.index(correta)
            self.botoes[idx_correto].config(bg="green")

        for b in self.botoes:
            b.config(state="disabled")
        self.botao_dica.config(state="disabled")
        self.pergunta_atual += 1
        self.master.after(1000, self.carregar_proxima)

    def usar_dica(self):
        if self.dica_usada:
            return
        self.dica_usada = True
        correta = self.perguntas_embaralhadas[self.pergunta_atual][7]
        idx_correto = self.letras.index(correta)
        alternativas = [i for i in range(5) if i != idx_correto]
        remover = random.sample(alternativas, 2)
        for i in remover:
            self.botoes[i].config(state="disabled")
        self.botao_dica.config(state="disabled")

    def fim_jogo(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text=f"Fim de jogo!\nPontuação: {self.pontuacao}", font=("Arial", 18)).pack(pady=20)
        cursor.execute("INSERT INTO ranking (usuario, pontuacao) VALUES (?, ?)", (self.usuario, self.pontuacao))
        conn.commit()
        tk.Button(self.master, text="Jogar Novamente", command=lambda: ShowDoMilhaoApp(self.master)).pack(pady=10)

# Inicializar app
root = tk.Tk()
app = ShowDoMilhaoApp(root)
root.mainloop()








        
