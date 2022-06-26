class ListPriority:
    def __init__(self):
        self.listOpen = []
        self.listClose = []

    def insert(self, state):
        if len(self.listOpen) == 0:
            self.listOpen.append(state)
            self.listClose.append(state)
        else:
            for i in range(len(self.listOpen)):
                if state.FH < self.listOpen[i].FH and state.name != self.listOpen[i].name:
                    self.listOpen.insert(i, state)
                    break
                elif i == len(self.listOpen)-1 and state.name != self.listOpen[i].name:
                    self.listOpen.append(state)
                    break
    def printStates(self):
        print("Lista de Estados Abiertos:")
        for i in range(len(self.listOpen)):
            print(self.listOpen[i].name, self.listOpen[i].FH)
        print("Lista de Estados Cerrados:")
        for i in range(len(self.listClose)):
            print(self.listClose[i].name, self.listClose[i].FH)



