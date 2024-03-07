class FuncionesVarias:
    def __init__(self,lista):
        self.lista=lista

    def vereficaPrimo(self,n):
        primo = True
        for i in range(2,n):
            if n%i==0:
                primo= False
                break
        return primo

    def extraePrimos(self,lista):
        listaPrimo=[]
        for e in lista:
            if self.vereficaPrimo(e):
                listaPrimo.append(e)
        return listaPrimo

    def repetido(self,lista):
        indice=0
        count1=0
        count=0
        elemento=0
        for elem in lista:
            for e in lista:
                if elem==e:
                    count+=1
            if count>count1:
                count1=count
                elemento=elem
                indice=lista.index(elemento)
            count=0
        return elemento, indice, count1

    def conversionGrados(self,grados,tipoEntrada,tipoSalida):
        if(tipoSalida==tipoEntrada):
            return grados
        if(tipoEntrada =='Farenheit'):
            if(tipoSalida=='Celsius'):
                return(grados*(9/5))+32
            if(tipoSalida=='Kelvin'):
                return grados+273.15
        if(tipoEntrada == 'Kelvin'):
            if(tipoSalida=='Celsius'):
                return grados-273.15
            if(tipoSalida=='Farenheit'):
                return ((grados-273.15-32)*(5/9))
        if(tipoEntrada=='Celsius'):
            if(tipoSalida=='Kelvin'):
                return grados+273.15
            if(tipoSalida=='Farenheit'):
                return (grados-32)*5/9
        
    
    def pruebaGrados(self,lis1):
        ckf=['Farenheit','Celsius','Kelvin']
        for c in ckf:
            for b in ckf:
                for a in lis1:
                    Grados=self.conversionGrados(a,b,c)
                    print(Grados," ",c)
        
    def factorial(self,num):
        if num<0 or type(num)!=int:
            print('Error')
            return
        elif num<=1:
            return 1
        else: 
            f=num*self.factorial(num-1)
            return f