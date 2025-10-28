import tkinter as tk

def capturar_click(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f"Último clique: X={x}, Y={y}"

# Criando a janela
janela = tk.Tk()
janela.title("Tratamento de Eventos - Captura de Clique Esquerdo")

# Criando o widget de rótulo
label_coordenadas = tk.Label(janela, text="Clique em qualquer lugar da janela.")
label_coordenadas.pack(padx=200, pady=100)

# Ligando o evento de clique do mouse à função
janela.bind("<Button-1>", capturar_click)

# Rodadando o loop principal
janela.mainloop()