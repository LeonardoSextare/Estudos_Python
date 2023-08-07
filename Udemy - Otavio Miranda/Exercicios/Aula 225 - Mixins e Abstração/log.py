# Abstração (Um dos pilares a orientação a objeto)
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error:{msg}')

    def log_sucess(self, msg):
        self._log(f'Sucesso:{msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no Log -> {msg_formatada}')
                
        with open(CAMINHO_ARQUIVO, 'a') as arquivo:
            arquivo.write(msg_formatada + '\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    logger = LogPrintMixin()
    logger.log_error('teste')
    logger.log_sucess('')
    
    logger = LogFileMixin()
    logger.log_error('Teste arquivo')
    logger.log_sucess('Sucess')


