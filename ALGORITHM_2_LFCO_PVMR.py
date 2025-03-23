class PDA:
    def __init__(self):
        self.pila = []
        self.estado = "q0"

    def aceptar_o_rechazar(self, cadena):
        self.pila = []
        self.estado = "q0"
        mitad = len(cadena) // 2

        for i in range(mitad):
            self.pila.append(cadena[i])

        i = mitad if len(cadena) % 2 == 0 else mitad + 1

        while i < len(cadena):
            if not self.pila or cadena[i] != self.pila.pop():
                return False
            i += 1
        return not self.pila