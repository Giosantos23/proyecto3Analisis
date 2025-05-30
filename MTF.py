class MTFLista:
    def __init__(self, initial_config):
        self.list = initial_config.copy()
        self.total_cost = 0
        self.operations = []
    
    def buscar_mover(self, key):
        try:
            position = self.list.index(key) + 1  
            cost = position
            
            self.list.remove(key)
            self.list.insert(0, key)
            
            return cost
        except ValueError:
            return 0
    
    def procesar_secuencia(self, sequence):
        print(f"Lista inicial: {self.list}")
        print("-" * 50)
        
        costo_secuencia = 0
        
        for i, request in enumerate(sequence):
            cost = self.buscar_mover(request)
            costo_secuencia += cost
            self.total_cost += cost
            
            info_operaciones = {
                'step': i + 1,
                'request': request,
                'cost': cost,
                'list_after': self.list.copy()
            }
            self.operations.append(info_operaciones)
            
            print(f"Paso {i+1}: Solicitud {request}, Costo: {cost}, Lista: {self.list}")
        
        print("-" * 50)
        print(f"Costo total de la secuencia: {costo_secuencia}")
        return costo_secuencia
    
    def reset(self, initial_config):
        self.list = initial_config.copy()
        self.total_cost = 0
        self.operations = []

class IMTFList(MTFLista):
    def procesar_secuencia(self, sequence):
        print(f"Lista inicial: {self.list}")
        print("-" * 50)
        
        costo_secuencia = 0
        n = len(sequence)
        
        for i, request in enumerate(sequence):
            try:
                position = self.list.index(request) + 1  
                cost = position
                costo_secuencia += cost
                self.total_cost += cost
                
                lookahead_window = sequence[i+1 : i + position]
                should_move = request in lookahead_window

                if should_move:
                    self.list.remove(request)
                    self.list.insert(0, request)
                
                info_operaciones = {
                    'step': i + 1,
                    'request': request,
                    'cost': cost,
                    'list_after': self.list.copy(),
                    'moved': should_move
                }
                self.operations.append(info_operaciones)
                
                print(f"Paso {i+1}: Solicitud {request}, Costo: {cost}, Mover: {should_move}, Lista: {self.list}")
            
            except ValueError:
                print(f"Elemento {request} no encontrado.")
                continue
        
        print("-" * 50)
        print(f"Costo total de la secuencia: {costo_secuencia}")
        return costo_secuencia
    
def problema1():
    print("Problema 1")
    print("=" * 60)
    
    initial_config = [0, 1, 2, 3, 4]
    sequence = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    
    mtf = MTFLista(initial_config)
    total_cost = mtf.procesar_secuencia(sequence)
    
    print(f"\nCosto total de accesos: {total_cost}")
    print("=" * 60)

def problema2():
    print("Problema 2")
    print("=" * 60)
    
    initial_config = [0, 1, 2, 3, 4]
    sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    
    mtf = MTFLista(initial_config)
    total_cost = mtf.procesar_secuencia(sequence)
    
    print(f"\nCosto total de accesos: {total_cost}")
    print("=" * 60)

def problema3():
    print("Problema 3")
    print("=" * 60)
    
    initial_config = [0, 1, 2, 3, 4]

    min_sequence = [0] * 20  
    
    print("Secuencia que minimiza el costo:")
    mtf = MTFLista(initial_config)
    min_cost = mtf.procesar_secuencia(min_sequence)
    
    print(f"\nMínimo costo total: {min_cost}")
    print("=" * 60)

def problema4():
    print("Problema 4")
    print("=" * 60)
    
    initial_config = [0, 1, 2, 3, 4]
    
    worst_sequence = [4] * 20  
    
    print("Secuencia que maximiza el costo:")
    mtf = MTFLista(initial_config)
    worst_cost = mtf.procesar_secuencia(worst_sequence)
    
    print(f"\Peor caso - Costo total: {worst_cost}")
    print("=" * 60)

def problema5():
    print("\n" + "=" * 60)
    print("Problema 5")
    print("=" * 60)
    
    initial_config = [0, 1, 2, 3, 4]
    sequence = [2] * 20  
    
    print("Secuencia:")
    mtf = MTFLista(initial_config)
    cost_2 = mtf.procesar_secuencia(sequence)
    
    print(f"\nCosto total para secuencia de 2's: {cost_2}")
    
    print("\n" + "-" * 40)
    print("Secuencia: 20 repeticiones del elemento 3")
    mtf.reset(initial_config)
    sequence_3 = [3] * 20
    cost_3 = mtf.procesar_secuencia(sequence_3)
    
    print(f"\nCosto total para secuencia de 3's: {cost_3}")
    
    print("\n" + "-" * 40)
    print("- Patrón observado: Costo total = posición_inicial + 19")
    print("=" * 60)

def problema6():
    print("\n" + "=" * 60)
    print("PROBLEMA 6 - ALGORITMO IMTF")
    print("=" * 60)
    
    initial_config = [0, 1, 2, 3, 4]
    
    best_sequence = [0] * 20
    print("Comparación IMTF vs MTF:")
    
    mtf = MTFLista(initial_config)
    mtf_best_cost = mtf.procesar_secuencia(best_sequence)
    
    print("\n" + "-" * 40)
    print("IMTF - Mejor caso:")
    imtf = IMTFList(initial_config)
    imtf_best_cost = imtf.procesar_secuencia(best_sequence)
    
    print(f"\nComparación mejor caso:")
    print(f"MTF:  {mtf_best_cost}")
    print(f"IMTF: {imtf_best_cost}")
    
    print("\n" + "-" * 40)
    worst_sequence = [4] * 20
    print("Comparación IMTF vs MTF:")
    
    mtf.reset(initial_config)
    mtf_worst_cost = mtf.procesar_secuencia(worst_sequence)
    
    print("\n" + "-" * 40)
    print("IMTF - Peor caso:")
    imtf.reset(initial_config)
    imtf_worst_cost = imtf.procesar_secuencia(worst_sequence)
    
    print(f"\nComparación peor caso:")
    print(f"MTF:  {mtf_worst_cost}")
    print(f"IMTF: {imtf_worst_cost}")
    
    print("=" * 60)

def main():
    print("Proyecto 3 algoritmo MTF ")
    print("Análisis Amortizado y Algoritmos Online")
    
    problema1()
    problema2()
    problema3()
    problema4()
    problema5()
    problema6()

if __name__ == "__main__":
    main()
