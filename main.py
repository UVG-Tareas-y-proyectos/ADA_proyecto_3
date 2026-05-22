from algorithms import mtf, imtf

def pregunta_1():
    print("--- PREGUNTA 1 ---")
    config = [0, 1, 2, 3, 4]
    seq = [0, 1, 2, 3, 4] * 4 
    mtf(config, seq)

def pregunta_2():
    print("--- PREGUNTA 2 ---")
    config = [0, 1, 2, 3, 4]
    seq = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    mtf(config, seq)

def pregunta_3():
    print("--- PREGUNTA 3 (Mejor caso) ---")
    config = [0, 1, 2, 3, 4]
    seq = [0] * 20
    print(f"Secuencia: {seq}")
    costo = mtf(config, seq, verbose=False)
    print(f"Costo total por este acceso: {costo}\n")
    return seq

def pregunta_4():
    print("--- PREGUNTA 4 (Peor caso) ---")
    config = [0, 1, 2, 3, 4]
    actual = config[:]
    seq = []
    
    for _ in range(20):
        ultimo_elemento = actual[-1]
        seq.append(ultimo_elemento)
        actual.pop()
        actual.insert(0, ultimo_elemento)
        
    print(f"Secuencia: {seq}")
    costo = mtf(config, seq, verbose=False)
    print(f"Costo total por este acceso: {costo}\n")
    return seq

def pregunta_5():
    print("--- PREGUNTA 5 ---")
    config = [0, 1, 2, 3, 4]
    seq_2 = [2] * 20
    print("Resultados secuencia de 2:")
    mtf(config, seq_2)
    
    seq_3 = [3] * 20
    costo_3 = mtf(config, seq_3, verbose=False)
    print(f"Costo total secuencia de 3: {costo_3}\n")
    
    print("Patrón para secuencia repetida:")
    print("El primer acceso toma el costo de su posicion original.")
    print("A partir del segundo, el costo es 1 porque el elemento ya está al frente.")
    print()

def pregunta_6(mejor_seq, peor_seq):
    print("--- PREGUNTA 6 (IMTF Look-ahead) ---")
    config = [0, 1, 2, 3, 4]
    
    print("IMTF con MTF Mejor caso:")
    imtf(config, mejor_seq)
    
    print("IMTF con MTF Peor caso:")
    imtf(config, peor_seq)

if __name__ == "__main__":
    pregunta_1()
    pregunta_2()
    seq_mejor = pregunta_3()
    seq_peor = pregunta_4()
    pregunta_5()
    pregunta_6(seq_mejor, seq_peor)
