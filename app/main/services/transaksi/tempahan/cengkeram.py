from ....models.mysql.cengkeram import CengkeramModels

model = CengkeramModels()
class TransaksiTempahanCengkeram():
    def MaklumatTempahan(self, no_resit):
        cengkeram = CengkeramModels.ReadCengkeram(no_resit)
        return cengkeram
