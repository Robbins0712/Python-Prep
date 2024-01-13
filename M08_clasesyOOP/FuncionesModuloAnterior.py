class FuncionesModuloAnterior:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def es_primo(self):
        for i in self.lista:
            if (self.__es_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')
    
    def convertir_temperatura(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__convertir_temperatura(i, origen, destino),'grados',destino)

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))


    def __es_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo
    

    def __convertir_temperatura(self, valor, medida_origen, medida_destino):
        if medida_origen == "C" and medida_destino == "F":
          return (valor * 9/5) + 32
        elif medida_origen == "C" and medida_destino == "K":
             return valor + 273.15
        elif medida_origen == "F" and medida_destino == "C":
            return (valor - 32) * 5 / 9
        elif medida_origen == "F"  and medida_destino == "K":
            return ((valor - 32) * 5 / 9) + 273.15
        elif medida_origen == "K" and medida_destino == "F":
            return ((valor - 273.15) * 9 / 5) + 32
        elif medida_origen == "K"  and medida_destino == "C":
            return valor - 273.15
        else:
            print('Parámetro de Destino incorrecto')

    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero