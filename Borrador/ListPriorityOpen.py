class ListPriority:
    def __init__(self):
        self.listOpen = []

    def insert(self, state):
        if len(self.listOpen) == 0:
            self.listOpen.append(state)
        else:
            for i in range(len(self.listOpen)):
                if state.VH < self.listOpen[i].VH:
                    self.listOpen.insert(i, state)
                    break
                elif i == len(self.listOpen)-1 :
                    self.listOpen.append(state)
                    break

    def returnLast(self):
        return self.listOpen[-1]
    

    def remove(self, state):
        self.listOpen.remove(state) 

    def printStates(self):
        print("Lista de Estados Abiertos:")
        for i in range(len(self.listOpen)):
            print(self.listOpen[i].VH, self.listOpen[i].PilaA, self.listOpen[i].PilaB, self.listOpen[i].PilaC)


