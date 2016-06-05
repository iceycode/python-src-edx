from enum import Enum
import Field

class FieldType(Enum):
    planet = 1
    solidWall = 2
    warpedWord = 3
    backHome = 4
    enclosedField = 5

    def __init__(self):
        self.field = Field # Field type


    def FieldFromInt(self):
        if self.FieldType == 1:
            self.field = Field.SmallPlanetField
        elif self.FieldType == 2:
            self.field = Field.SolidWallField
        elif self.FieldType == 3:
            self.field = Field.WarpedWorld
        elif self.FieldType == 4:
            self.field = Field.BackHomeField

    def getField(self):
        return self.field