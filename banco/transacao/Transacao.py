class Transacao:
    """Classe que representa a Transação. 

    Atributos:
        valor (float): O valor da transaçao.
        tipo (str): O tipo da transação.
    """
    def __init__(self, valor, tipo):
        self.valor = valor 
        self.tipo = tipo

    def get_valor(self):
        """Acessa o valor da transação..

        Retorna:
            float: O valor da transação..
        """
        return self.valor       
    
    def get_tipo(self):
        """Acessa o tipo da transação.

        Retorna:
            str: O tipo da transação..
        """
        return self.tipo 
    
    def __str__(self):
        """Acessa uma representação dos atributos do Depósito.

        Retorna:
            valor (float): O valor da transaçao.
            tipo (str): O tipo da transação.
        """
        return f"{self.valor} || {self.tipo}"