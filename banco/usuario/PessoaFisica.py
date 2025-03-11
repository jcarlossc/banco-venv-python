class PessoaFisica:
    """Classe que representa Pessoa Física. 

    Atributos:
        nome (str): O usuário do sistema.
        cpf (str): O cpf do usuário.
    """
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def get_nome(self):
        """Acessa o nome do usuário.

        Retorna:
            str: O nome usuário.
        """
        return self.nome   

    def get_cpf(self):
        """Acessa o cpf do usuário.

        Retorna:
            str: O cpf do usuário.
        """
        return self.cpf      

    def __str__(self):
        """Acessa uma representação dos atributos de usuário.

        Retorna:
            str: O nome e cpf do usuário.
        """
        return f"{self.nome} {self.cpf}"  
