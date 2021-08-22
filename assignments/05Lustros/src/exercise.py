def main():
    #escribe tu código abajo de esta línea
    año= int(input('Dame el año de nacimiento:'))
    año_actual= int(input('Dame el año actual:'))
    
    lustro= (año_actual - año)/5
    print('Los lustros que has vivido son:',lustro)



if __name__ == '__main__':
    main()
