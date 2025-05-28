
from pathlib import Path
from tkinter import *
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\professor")

# função para funcionamento das imagens
def pasta_imagens(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1440x1024")
window.configure(bg = "#F0F0F0")


canvas = Canvas(
    window,
    bg = "#F0F0F0",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


# Imagem onda do lado inferior da página
img_wave = PhotoImage(
    file = pasta_imagens("wave.png"))
wave = canvas.create_image(
    750.0,
    848.0,
    image = img_wave
)

### TÍTULO

#"Jogo", azul
canvas.create_text(
    507.0,
    15.0,
    anchor = "nw",
    text = "Jogo",
    fill = "#46AEBD",
    font = ("Georgia", 96 * -1, "bold")
)
# "da", amarelo
canvas.create_text(
    780.0,
    15.0,
    anchor = "nw",
    text = "da",
    fill = "#F89E19",
    font = ("Georgia", 96 * -1, "bold")
)
# "Sabedoria", vermelho
canvas.create_text(
    467.0,
    115.0,
    anchor = "nw",
    text = "Sabedoria",
    fill = "#EB2452",
    font = ("Georgia", 96 * -1, "bold")
)

# Final título

# Botões Principais

# Botão Jogar
img_jogar = PhotoImage(
    file=pasta_imagens("button_jogar.png"))
button_jogar = Button(
    image = img_jogar,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_jogar clicked"),
    relief = "flat"
)
button_jogar.place(
    x = 488.0,
    y = 302.0,
    width = 463.0,
    height = 118.0
)

# Botão Editar Questões
img_edit = PhotoImage(
    file=pasta_imagens("button_editar.png"))
button_editar = Button(
    image = img_edit,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda: print("button_editar clicked"),
    relief = "flat"
)
button_editar.place(
    x = 488.0,
    y = 463.0,
    width = 463.0,
    height = 118.0
)

# Botão Ranking
img_rank = PhotoImage(
    file = pasta_imagens("button_ranking.png"))
button_ranking = Button(
    image = img_rank,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_ranking clicked"),
    relief = "flat"
)
button_ranking.place(
    x = 488.0,
    y = 624.0,
    width = 463.0,
    height = 118.0
)

# Final botões principais
# Adicionais

# Imagem Moeda
img_moeda = PhotoImage(
    file = pasta_imagens("moeda.png"))
moeda = canvas.create_image(
    1382.0,
    49.0,
    image = img_moeda
)

# Quantidade de moedas (vincular variável)
canvas.create_text(
    1274.0,
    20.0,
    anchor = "nw",
    text = "25",
    fill = "#F89E19",
    font = ("Georgia", 48 * -1, "bold")
)

# Texto botão de sair
canvas.create_text(
    80.0,
    21.0,
    anchor = "nw",
    text = "Sair",
    fill = "#F89E19",
    font = ("Georgia", 36 * -1, "bold")
)

# Botão Sair
button_img_sair = PhotoImage(
    file = pasta_imagens("button_sair.png"))
button_sair = Button(
    image = button_img_sair,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_sair clicked"),
    relief = "flat"
)
button_sair.place(
    x = 15.0,
    y = 15.0,
    width = 56.0,
    height = 56.0
)


window.resizable(False, False)
window.mainloop()
