import tkinter as tk
from tkinter import messagebox
import datetime

def iniciar_interface(adicionar_transacao, calcular_saldo, obter_historico):
    """Inicializa a interface gráfica do aplicativo."""

    # Funções da interface
    def salvar_transacao(tipo):
        titulo = titulo_entry.get()
        valor = valor_entry.get()
        data = data_entry.get() or datetime.datetime.now().strftime("%d/%m/%Y")

        if not titulo or not valor:
            messagebox.showerror("Erro", "Título e valor são obrigatórios!")
            return

        try:
            valor = float(valor)
        except ValueError:
            messagebox.showerror("Erro", "Valor deve ser um número!")
            return

        adicionar_transacao(tipo, titulo, valor, data)
        messagebox.showinfo("Sucesso", f"Transação de {tipo} adicionada!")
        limpar_campos()

    def mostrar_saldo():
        saldo = calcular_saldo()
        messagebox.showinfo("Saldo Atual", f"Saldo disponível: R${saldo:.2f}")

    def exibir_historico():
        historico = obter_historico()
        if not historico:
            messagebox.showinfo("Histórico", "Nenhuma transação registrada.")
            return

        historico_texto = "Histórico de Transações:\n"
        for i, transacao in enumerate(historico, 1):
            historico_texto += (f"{i}. {transacao['data']} - {transacao['tipo'].capitalize()} - "
                                f"{transacao['descricao']} - R${transacao['valor']:.2f}\n")

        messagebox.showinfo("Histórico", historico_texto)

    def limpar_campos():
        titulo_entry.delete(0, tk.END)
        valor_entry.delete(0, tk.END)
        data_entry.delete(0, tk.END)

    # Efeito de hover nos botões
    def on_enter_green(e):
        e.widget.config(bg="darkgreen")

    def on_leave_green(e):
        e.widget.config(bg="green")

    def on_enter_red(e):
        e.widget.config(bg="darkred")

    def on_leave_red(e):
        e.widget.config(bg="red")

    # Configuração da Janela
    janela = tk.Tk()
    janela.title("Lucro Seguro - Controle Financeiro")

    # Título do App
    tk.Label(
        janela,
        text="Lucro Seguro",
        font=("Arial", 20, "bold"),
        fg="green"
    ).grid(row=0, column=0, columnspan=2, pady=10)

    # Formulário para transações
    tk.Label(janela, text="Título:").grid(row=1, column=0, padx=10, pady=5)
    titulo_entry = tk.Entry(janela, width=30)
    titulo_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela, text="Valor:").grid(row=2, column=0, padx=10, pady=5)
    valor_entry = tk.Entry(janela, width=30)
    valor_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(janela, text="Data (dd/mm/aaaa):").grid(row=3, column=0, padx=10, pady=5)
    data_entry = tk.Entry(janela, width=30)
    data_entry.grid(row=3, column=1, padx=10, pady=5)

    # Botões
    def criar_botao(texto, comando, linha, coluna, cor, hover_enter, hover_leave):
        botao = tk.Button(janela, text=texto, command=comando, bg=cor, fg="white", font=("Arial", 10, "bold"))
        botao.grid(row=linha, column=coluna, padx=10, pady=10)
        botao.bind("<Enter>", hover_enter)
        botao.bind("<Leave>", hover_leave)

    criar_botao("Adicionar Entrada", lambda: salvar_transacao("entrada"), 4, 0, "green", on_enter_green, on_leave_green)
    criar_botao("Adicionar Saída", lambda: salvar_transacao("saída"), 4, 1, "red", on_enter_red, on_leave_red)
    criar_botao("Ver Saldo", mostrar_saldo, 5, 0, "green", on_enter_green, on_leave_green)
    criar_botao("Ver Histórico", exibir_historico, 5, 1, "green", on_enter_green, on_leave_green)

    # Iniciar o loop principal da interface
    janela.mainloop()
