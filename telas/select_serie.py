from pathlib import Path
from tkinter import *
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\serie")

# Função para funcionamento das imagens
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

### TÍTULO

canvas.place(x = 0, y = 0)
canvas.create_text(
    480.0,
    15.0,
    anchor = "nw",
    text = "Selecione",
    fill = "#46AEBD",
    font = ("Georgia", 96 * -1, "bold")
)
canvas.place(x = 0, y = 0)
canvas.create_text(
    490.0,
    115.0,
    anchor = "nw",
    text = "sua",
    fill = "#F89E19",
    font = ("Georgia", 96 * -1, "bold")
)
canvas.place(x = 0, y = 0)
canvas.create_text(
    685.0,
    115.0,
    anchor = "nw",
    text = "Série",
    fill = "#EB2452",
    font = ("Georgia", 96 * -1, "bold")
) 
### Final do título

## Início Botões

# Botão quarto ano
button_img_4ano = PhotoImage(
    file = pasta_imagens("button_4ano.png"))
button_4ano = Button(
    image = button_img_4ano,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_4ano clicked"),
    relief = "flat"
)
button_4ano.place(
    x = 31.0,
    y = 301.0,
    width = 430.0,
    height = 148.0
)

# Botão 5 ano
button_img_5ano = PhotoImage(
    file = pasta_imagens("button_5ano.png"))
button_5ano = Button(
    image = button_img_5ano,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_5ano clicked"),
    relief = "flat"
)
button_5ano.place(
    x=31.0,
    y=529.0,
    width=430.0,
    height=148.0
)

# Botão 6 ano
button_img_6ano = PhotoImage(
    file = pasta_imagens("button_6ano.png"))
button_6ano = Button(
    image = button_img_6ano,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_6ano clicked"),
    relief = "flat"
)
button_6ano.place(
    x = 31.0,
    y = 757.0,
    width = 430.0,
    height = 148.0
)

# Botão 7 ano
button_img_7ano = PhotoImage(
    file = pasta_imagens("button_7ano.png"))
button_7ano = Button(
    image = button_img_7ano,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_7ano clicked"),
    relief = "flat"
)
button_7ano.place(
    x = 505.0,
    y = 301.0,
    width = 430.0,
    height = 148.0
)

# Botão 8 ano
button_img_8ano = PhotoImage(
    file = pasta_imagens("button_8ano.png"))
button_8ano = Button(
    image = button_img_8ano,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_8ano clicked"),
    relief = "flat"
)
button_8ano.place(
    x = 505.0,
    y = 529.0,
    width = 430.0,
    height = 148.0
)

# Botão 9 ano
button_img_9ano = PhotoImage(
    file = pasta_imagens("button_9ano.png"))
button_9ano = Button(
    image = button_img_9ano,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_9ano clicked"),
    relief = "flat"
)
button_9ano.place(
    x = 505.0,
    y = 757.0,
    width = 430.0,
    height = 148.0
)

# Botão 1 Ensino Médio
button_img_1em = PhotoImage(
    file = pasta_imagens("button_1em.png"))
button_1em = Button(
    image = button_img_1em,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_1em clicked"),
    relief = "flat"
)
button_1em.place(
    x = 979.0,
    y = 301.0,
    width = 430.0,
    height = 148.0
)

# Botão 2 Ensino Médio
button_img_2em = PhotoImage(
    file = pasta_imagens("button_2em.png"))
button_2em = Button(
    image = button_img_2em,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_2em clicked"),
    relief = "flat"
)
button_2em.place(
    x = 979.0,
    y = 529.0,
    width = 430.0,
    height = 148.0
)

#Botão 3 Ensino Médio
button_img_3em = PhotoImage(
    file = pasta_imagens("button_3em.png"))
button_3em = Button(
    image = button_img_3em,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_3em clicked"),
    relief = "flat"
)
button_3em.place(
    x = 979.0,
    y = 757.0,
    width = 430.0,
    height = 148.0
)

# Imagem moeda
img_moeda = PhotoImage(
    file=pasta_imagens("moeda.png"))
moeda = canvas.create_image(
    1382.0,
    49.0,
    image = img_moeda
)

# Quantidade Moeda
canvas.create_text(
    1274.0,
    20.0,
    anchor="nw",
    text="25",
    fill="#F89E19",
    font=("Georgia", 48 * -1, "bold")
)

# Texto botão sair
canvas.create_text(
    80.0,
    21.0,
    anchor="nw",
    text="Voltar",
    fill="#F89E19",
    font = ("Georgia", 36 * -1, "bold")
)

# Botão sair
button_img_voltar = PhotoImage(
    file = pasta_imagens("button_voltar.png"))
button_voltar = Button(
    image = button_img_voltar,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_voltar clicked"),
    relief = "flat"
)
button_voltar.place(
    x = 15.0,
    y = 15.0,
    width = 56.0,
    height = 56.0
)


window.resizable(False, False)
window.mainloop()
