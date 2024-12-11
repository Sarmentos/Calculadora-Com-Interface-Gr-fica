import tkinter as tk

class Calculadora:
    def __init__(self, mestre):
        self.mestre = mestre
        self.mestre.title("Calculadora") 
        self.resultado = tk.StringVar()

        self.entrada = tk.Entry(self.mestre, textvariable=self.resultado, font=("Arial", 24), justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4)

        botoes = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)  # Botão Limpar
        ]

        for (texto, linha, coluna) in botoes:
            botao = tk.Button(self.mestre, text=texto, font=("Arial", 18), command=lambda t=texto: self.clique(t))
            botao.grid(row=linha, column=coluna)

    def clique(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.resultado.get())
                self.resultado.set(str(resultado))
            except:
                self.resultado.set("Erro")
        elif valor == "C":  # Limpar
            self.resultado.set("")
        else:
            self.resultado.set(self.resultado.get() + valor)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = Calculadora(raiz)
    raiz.mainloop()
