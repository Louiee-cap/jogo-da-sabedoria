from pathlib import Path
from tkinter import *
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\imagens\materias")

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

# Título
canvas.place(x = 0, y = 0)
canvas.create_text(
    405.0,
    15.0,
    anchor = "nw",
    text = "Mat",
    fill = "#46AEBD",
    font = ("Georgia", 128 * -1, "bold")
)
canvas.place(x = 0, y = 0)
canvas.create_text(
    660.0,
    15.0,
    anchor = "nw",
    text = "ér",
    fill = "#F89E19",
    font = ("Georgia", 128 * -1, "bold")
)
canvas.place(x = 0, y = 0)
canvas.create_text(
    804.0,
    15.0,
    anchor = "nw",
    text = "ias",
    fill = "#EB2452",
    font = ("Georgia", 128 * -1, "bold")
)

# Botão Matemática
button_img_mat = PhotoImage(
    file = pasta_imagens("button_mat.png"))
button_mat = Button(
    image = button_img_mat,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_mat clicked"),
    relief = "flat"
)
button_mat.place(
    x = 31.0,
    y = 301.0,
    width = 430.0,
    height = 205.0
)

# Botão Português
button_img_port = PhotoImage(
    file = pasta_imagens("button_port.png"))
button_port = Button(
    image = button_img_port,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_port clicked"),
    relief = "flat"
)
button_port.place(
    x=31.0,
    y=628.0,
    width=430.0,
    height=205.0
)

# Botão História
button_img_hist = PhotoImage(
    file = pasta_imagens("button_hist.png"))
button_hist = Button(
    image = button_img_hist,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_hist clicked"),
    relief = "flat"
)
button_hist.place(
    x = 505.0,
    y = 301.0,
    width = 430.0,
    height = 205.0
)

# Botão Geografia
button_img_geo = PhotoImage(
    file = pasta_imagens("button_geo.png"))
button_geo = Button(
    image = button_img_geo,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_geo clicked"),
    relief = "flat"
)
button_geo.place(
    x = 505.0,
    y = 628.0,
    width = 430.0,
    height = 205.0
)

# Botão Ciências
button_img_cie = PhotoImage(
    file = pasta_imagens("button_cie.png"))
button_cie = Button(
    image = button_img_cie,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_cie clicked"),
    relief = "flat"
)
button_cie.place(
    x = 979.0,
    y = 301.0,
    width = 430.0,
    height = 205.0
)

# Botão Inglês
button_img_ing = PhotoImage(
    file = pasta_imagens("button_ing.png"))
button_ing = Button(
    image = button_img_ing,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_ing clicked"),
    relief = "flat"
)
button_ing.place(
    x = 979.0,
    y = 628.0,
    width = 430.0,
    height = 205.0
)

## Final Botões


# Imagem moeda
img_moeda = PhotoImage(
    file = pasta_imagens("moeda.png"))
moeda = canvas.create_image(
    1382.0,
    49.0,
    image = img_moeda
)

# Quantidade Moedas (adicionar variável)
canvas.create_text(
    1274.0,
    20.0,
    anchor = "nw",
    text = "25",
    fill = "#F89E19",
    font = ("Georgia", 48 * -1, "bold")
)

# Texto botão voltar
canvas.create_text(
    80.0,
    21.0,
    anchor = "nw",
    text = "Voltar",
    fill = "#F89E19",
    font = ("Georgia", 36 * -1, "bold")
)

# Botão Voltar
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
