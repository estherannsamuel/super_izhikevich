# Create each sub class in a separate file:
# intrinsic_burst_cell.py
# chattering_cell.py
#
# Save the files in your repository folder, right next to izhikevich_cells.py
# At the top of each file, import your izhikevich_cells file so that
# the cell class is available to you. Import it by adding the following line:
# import izhikevichcells as izh
#
# Hint: you can now refer to the izhikevich cell object (izhCell) with:
# izh.izhCell
#
# In your intrinsic_burst_cell.py file, define a subclass of the izhCell
# and name it ibCell. Include an __init__ method that calls the izhCell
# __init__ method first and then reassigns any parameters that need to
# be a different value.
#
# When you have finished creating the child class, add a call to create one
# and assign it to the object myCell.
#
# Then run the cell's simulate method
#
# Finally, add a test to check if this new file is running directly:
# if __name__=='__main__':
# and as a substatement (if True), call the plotting function from
# izhikevich_cells.py using dot notation (hint: izh.plot...)
#
# Make sure to run your file to test it.

import izhikevich_cells as izh

class ibCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = "Intrinsic Burst Cell"
        self.C = 150
        self.vr = -75
        self.vt = -45
        self.k = 1.2
        self.a = .01
        self.b = 5
        self.c = -56
        self.d = 130
        self.vpeak = 50

myCell = ibCell(2000)
myCell.simulate()

if __name__=='__main__':
    if True:
        izh.plotMyData(myCell)
