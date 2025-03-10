class Transacao:
    def __init__(self, valor, tipo):
        self.valor = valor 
        self.tipo = tipo

    def get_valor(self):
        return self.valor       
    
    def get_tipo(self):
        return self.tipo 
    
    def __str__(self):
        return f"{self.valor} || {self.tipo}"