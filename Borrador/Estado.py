from audioop import reverse
import copy


class State():
    def __init__(self, PilaA, PilaB, PilaC, padre):
        self.PilaA = PilaA
        self.PilaB = PilaB
        self.PilaC = PilaC
        self.valoresPilas = [self.PilaA, self.PilaB, self.PilaC]
        self.padreEstado = copy.deepcopy(padre)
        self.VH = self.calcularVH() 
        self.profundidad = self.profundidadReturn()
        self.VHtotal = self.calcularVH() + self.profundidadReturn()
 
        
    def profundidadReturn(self):
        contador = 0
        caminoPadre = copy.deepcopy(self.padreEstado)
        # Contar cuantos padres tiene el estado 
        while caminoPadre != None:
            contador += 1
            caminoPadre = caminoPadre.padreEstado
        return contador
                
      


    def calcularVH(self):
        valueVH = 0
        valueVH += len(self.PilaB)
        valueVH += 2*len(self.PilaC)
        
        # Verificar si la pila  esta ordenada
        if self.verificarOrdenPilas()==False:
            valueVH -= 1000
        return valueVH
    
    def verificarOrdenPilas(self):
        pilasOrdenadas = copy.deepcopy(self.valoresPilas)       
        pilasOrdenadas[0].sort(reverse=True)
        pilasOrdenadas[1].sort(reverse=True)
        pilasOrdenadas[2].sort(reverse=True)
        if pilasOrdenadas == self.valoresPilas:
            return True
        else:
            return False
        
        
        

