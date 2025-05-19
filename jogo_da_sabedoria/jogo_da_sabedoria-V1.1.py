import tkinter as tk  
from tkinter import messagebox
import random

# Base de perguntas
perguntas = [
    ("Qual a capital do Brasil?", "São Paulo", "Brasília", "Rio de Janeiro", "Salvador", "Curitiba", "B"),
    ("Quem pintou a Mona Lisa?", "Van Gogh", "Picasso", "Leonardo da Vinci", "Michelangelo", "Rembrandt", "C"),
    ("Qual é o maior planeta do sistema solar?", "Terra", "Marte", "Saturno", "Júpiter", "Netuno", "D"),
    ("Quanto é 2 + 2 (dois mais dois)?", "3", "1", "5", "6", "4", "E")
]

# Lista de jogadores para o ranking
ranking = []

class ShowDoMilhaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Show do Milhão")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#f0f0f0")

        self.usuario = None
        self.tela_login_aluno()

    def tela_login_aluno(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(frame, text="Nome de Usuário:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        self.entry_usuario = tk.Entry(frame, font=("Arial", 14))
        self.entry_usuario.pack(pady=10)

        tk.Label(frame, text="Senha:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        self.entry_senha = tk.Entry(frame, show="*", font=("Arial", 14))
        self.entry_senha.pack(pady=10)

        tk.Button(frame, text="🎮 Entrar", font=("Arial", 14), bg="#d0f0d0", command=self.validar_login_aluno).pack(pady=20)

    def validar_login_aluno(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario and senha:
            self.usuario = usuario
            self.iniciar_jogo_aluno()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def iniciar_jogo_aluno(self):
        ShowDoMilhao(self.root, "Matemática", "1º ano", self.usuario)

class ShowDoMilhao:
    def __init__(self, master, materia, serie, usuario):
        self.master = master
        self.materia = materia
        self.serie = serie
        self.usuario = usuario

        self.pergunta_atual = 0
        self.pontuacao = 0
        self.dica_usada = False
        self.checkpoint = 0

        self.perguntas_embaralhadas = random.sample(perguntas, len(perguntas))

        for widget in self.master.winfo_children():
            widget.destroy()

        self.criar_widgets()

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

        self.label_pontuacao = tk.Label(self.master, text=f"Pontuação: {self.pontuacao}", font=("Arial", 12), bg="#f0f0f0")
        self.label_pontuacao.pack(pady=10, side="bottom")

        self.carregar_pergunta()

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

    def exibir_tela_final(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        final_frame = tk.Frame(self.master, bg="#f0f0f0")
        final_frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(final_frame, text=f"Fim de Jogo!\nPontuação: {self.pontuacao} Reais", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        # Salvar no ranking
        ranking.append((self.usuario, self.pontuacao))

        # Botão "Jogar Novamente"
        tk.Button(final_frame, text="🔁 Jogar Novamente", font=("Arial", 14), bg="#d0f0d0",
                  command=self.jogar_novamente).pack(pady=10)

    def jogar_novamente(self):
        self.pergunta_atual = 0
        self.pontuacao = 0
        self.dica_usada = False
        self.checkpoint = 0
        self.perguntas_embaralhadas = random.sample(perguntas, len(perguntas))
        for widget in self.master.winfo_children():
            widget.destroy()
        self.criar_widgets()

# Inicializar o app
root = tk.Tk()
app = ShowDoMilhaoApp(root)
root.mainloop()






        