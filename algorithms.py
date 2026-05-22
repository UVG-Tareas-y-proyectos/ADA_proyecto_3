def mtf(config, requests, verbose=True):
    total_cost = 0
    actual = config[:] 
    
    for req in requests:
        idx = actual.index(req)
        cost = idx + 1
        total_cost += cost
        
        lista_previa = actual[:]
        
        item = actual.pop(idx)
        actual.insert(0, item)
        
        if verbose:
            print(f"Configuración: {lista_previa} | Solicitud: {req} | Costo: {cost} | Nueva CFG: {actual}")
            
    if verbose:
        print(f"Costo total de accesos (MTF): {total_cost}\n")
        
    return total_cost

def imtf(config, requests, verbose=True):
    total_cost = 0
    actual = config[:]
    n_reqs = len(requests)
    
    for req_idx in range(n_reqs):
        req = requests[req_idx]
        idx = actual.index(req)
        cost = idx + 1 
        total_cost += cost
        
        lista_previa = actual[:]
        
        i = cost
        elementos_siguientes = requests[req_idx + 1 : req_idx + 1 + (i - 1)]
        
        if req in elementos_siguientes:
            item = actual.pop(idx)
            actual.insert(0, item)
            
        if verbose:
            print(f"Configuración: {lista_previa} | Solicitud: {req} | Costo: {cost} | Nueva CFG: {actual}")
            
    if verbose:
        print(f"Costo total de accesos (IMTF): {total_cost}\n")
        
    return total_cost