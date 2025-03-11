import logging

class Logging:
    """Gerenciamento dos logs do sistema."""
    
    def __init__(self, arquivo_log='app.log'):
        self.logger = logging.getLogger("Logging")
        self.logger.setLevel(logging.DEBUG)

        # Criar um manipulador de arquivo
        manipulador_arquivo = logging.FileHandler(arquivo_log)
        manipulador_arquivo.setLevel(logging.DEBUG)

        # Definir o formato dos logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        manipulador_arquivo.setFormatter(formatter)

        # Adicionar os manipuladores ao logger
        self.logger.addHandler(manipulador_arquivo)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)