from ....models.mysql.tempahan import TempahanModel
from ....models.mysql.cengkeram import CengkeramModels

tempahan_model  = TempahanModel()
cengkeram_model = CengkeramModels()
class TransaksiTempahanServices():

    def GetMaklumatTempahan(self, no_resit):
        tempahan    = tempahan_model.ReadTempahan(no_resit)
        cengkeram   = cengkeram_model.ReadCengkeram(no_resit)

        return {
            "tempahan"  : tempahan,
            "cengkeram" : cengkeram
        }