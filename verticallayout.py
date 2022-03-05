from control import Control

class VerticalLayout(Control):
    def __init__(self):
        self.controls = []
    
    def addControl(self, control):
        self.controls.append(control)
    
    def removeControl(self, cID):
        control = [c for c in self.controls if c.id == cID]
        self.controls.remove(control)