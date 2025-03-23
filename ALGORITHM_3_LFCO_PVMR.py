class PDAConfig:
    def __init__(self):
        self.pila = []
        self.estado = "q0"

    def leer_simbolo(self, simbolo):
        if self.estado == "q0":
            if simbolo in ["0", "1"]:
                self.pila.append(simbolo)

    def mostrar_configuraciones(self, cadena):
        configuraciones = []
        self.pila = []
        self.estado = "q0"
        restante = cadena
        mitad = len(cadena) // 2

        for i in range(mitad):
            self.leer_simbolo(cadena[i])
            configuraciones.append((self.estado, restante, list(self.pila)))
            restante = restante[1:]

        i = mitad if len(cadena) % 2 == 0 else mitad + 1

        while i < len(cadena):
            if self.pila and cadena[i] == self.pila.pop():
                configuraciones.append((self.estado, restante, list(self.pila)))
                restante = restante[1:]
            else:
                configuraciones.append(("RECHAZO", restante, list(self.pila)))
                break
            i += 1

        if not self.pila:
            configuraciones.append((self.estado, "", []))
        else:
            configuraciones.append(("RECHAZO", restante, list(self.pila)))
        return configuraciones