from ALGORITHM_1_LFCO_PVMR import generar_cadenas_validas, generar_cadenas_invalidas
from ALGORITHM_2_LFCO_PVMR import PDA
from ALGORITHM_3_LFCO_PVMR import PDAConfig
import random

if __name__ == "__main__":
    print("Algoritmo 1: Generando cadenas Válidas e Inválidas:")
    validas = generar_cadenas_validas()
    invalidas = generar_cadenas_invalidas()
    print("\nCadenas Válidas:", validas)
    print("Cadenas Inválidas:", invalidas)

    todas = validas + invalidas
    random.shuffle(todas)

    print("\nAlgorithm 2: Probando con el PDA")
    for cadena in todas:
        pda = PDA()
        resultado = "ACEPTADA" if pda.aceptar_o_rechazar(cadena) else "RECHAZADA"
        print(f"La cadena '{cadena}' fue {resultado}")

    print("\nAlgorithm 3: Configuraciones de las válidas (Generar Árbol)")
    for cadena in validas:
        pda_conf = PDAConfig()
        configuraciones = pda_conf.mostrar_configuraciones(cadena)
        print(f"\nProceso de la cadena '{cadena}':")
        for config in configuraciones:
            print(f"(Estado: {config[0]}, lo que falta por leer: '{config[1]}', Pila: {config[2]})")
