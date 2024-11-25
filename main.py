import interface  # Importa a interface gráfica

# Dados e lógica principal
historico = []

def adicionar_transacao(tipo, descricao, valor, data):
    """Adiciona uma transação ao histórico."""
    transacao = {"tipo": tipo, "descricao": descricao, "valor": valor, "data": data}
    historico.append(transacao)

def calcular_saldo():
    """Calcula o saldo total com base no histórico."""
    saldo = sum(transacao["valor"] if transacao["tipo"] == "entrada" else -transacao["valor"]
                for transacao in historico)
    return saldo

def obter_historico():
    """Retorna o histórico de transações."""
    return historico

# Inicia a interface e passa as funções como parâmetros
if __name__ == "__main__":
    interface.iniciar_interface(adicionar_transacao, calcular_saldo, obter_historico)
