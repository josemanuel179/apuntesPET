class ErrorBolos(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ErrorDeFormato(ErrorBolos): pass
class ErrorTipoDeDato(ErrorBolos): pass
class ErrorDeRonda(ErrorBolos): pass
class ErrorDeRondaExtra(ErrorBolos): pass
    
