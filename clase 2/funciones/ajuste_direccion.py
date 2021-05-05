def ajuste_direccion(direccion):
    '''
    Funcion que seprar la direccion en dos listas, una de la calle y la otra el numero
    '''
    if type(direccion) == list: #Primero comprobar que la direcciones que se entregan es del tipo que esperamos recibir, donde se basaran todos los oasis.
        resultado_direccion = [] #Inicio una lista vacia donde se almacenaran las direcciones
        resultado_numero = [] #IDEM pero el numero
        for i in direccion: #Para cada elemento en direccion
            direccion_ajustada = i.split(' ') #Separo la direccion por espacios.
            direccion = ""
            for j in direccion_ajustada: #Para cada espacio que separé
                if j.isnumeric(): #Si el segmento es numerico
                    resultado_numero.append(int(j)) #Lo agregaro a los numeros
                else: #De lo contrario 
                    direccion = direccion + ' ' + j #Uno la piezas para tener la direccion completa.
            resultado_direccion.append(direccion) #Lo agrego a las direccion
        return resultado_direccion, resultado_numero
    else:
        raise Exception(f'Se esperaba un elemto de tipo lista pero se recibio un elemento de tipo: {type(direccion)}')