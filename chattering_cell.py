import izhikevich_cells as izh

class chattering_cell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = "Chattering Cell"
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = .03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25

myCell = chattering_cell(2000)
myCell.simulate()

if __name__=='__main__':
    if True:
        izh.plotMyData(myCell)