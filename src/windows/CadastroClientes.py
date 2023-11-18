import tkinter as tk

class CadastroClientes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Clientes")
        self.root.geometry("600x500")

        # Nome do Cliente
        self.lb_nome_do_cliente = tk.Label(self.root, text="Nome do Cliente:")
        self.lb_nome_do_cliente.place(x=15, y=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.place(x=18, y=30)

        # Endereço do Cliente
        self.lb_endereco = tk.Label(self.root, text="Endereço:")
        self.lb_endereco.place(x=15, y=55)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.place(x=18, y=76)


        self.button = tk.Button(self.root, text="Fechar")
        self.button.place(x=540, y=460)


    def abrir_janela(self):
        self.root.mainloop()

if __name__ == "__main__":
    janela = CadastroClientes()
    janela.abrir_janela()