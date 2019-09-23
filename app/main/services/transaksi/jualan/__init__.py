from ....models.mysql.jualan import JualanModel
from ....models.mysql.stock import StockModel
from ....models.mysql.no_bil import NoBilModel
from ....models.mysql.emas_buruk import EmasBurukModel

from datetime import datetime,date

class TransaksiJualanServices():

    def ProsesJualan(self,payloads):
        jualan = JualanModel()  
        input_jualan = self.__QueryInputJualan(payloads['item_jualan'], payloads['kakitangan_id'])
        return input_jualan

    def __QueryInputJualan(self, input, staff_id):
        jualan_model = JualanModel()
        stok_model = StockModel()
        nobil_model = NoBilModel()
        for i in range(len(input)):
            stok_detail = stok_model.ReadStockByTagNoRaw(input[i]['no_tag'], input[i]['tag'])
            modal = stok_detail['stk_emas'] + stok_detail['stk_permata'] + stok_detail['stk_upah']        
            no_resit_jualan = nobil_model.ReadNobil('no_jualan',stok_detail['tenant_id'])
            jualan = {
                "stk_color"         : "",
                "no_tag"            : "{}".format(input[i]['no_tag']),
                "nama_barang"       : "{}".format(stok_detail['stk_name']),
                "tarikh_jualan"     : "{}".format(datetime.now()),
                "mutu_id"           : "{}".format(stok_detail['cat_id']),
                "dulang_id"         : "{}".format(stok_detail['dlg_id']),
                "pembekal_id"       : "{}".format(stok_detail['spl_id']),
                "upah"              : "{}".format(input[i]['harga_upah']),
                "emas"              : "{}".format(input[i]['harga_emas']),
                "permata"           : "{}".format(input[i]['harga_permata']),
                "upahdisplay"       : "{}".format(input[i]['harga_upah']),
                "kakitangan_id"     : "{}".format(staff_id),
                "status"            : "{}".format(0),
                "tag"               : "{}".format(input[i]['tag']),
                "kod_cukai"         : "{}".format(input[i]['kod_cukai']),
                "modal"             : "{}".format(modal),
                "berat_beli"        : "{}".format(input[i]['berat_beli']),
                "no_resit_jualan"   : "{}".format(no_resit_jualan),
                "pelanggan_id"      : "1",
                "harga_jualan"      : "{}".format(input[i]['harga_jualan']),
                "harga_emas_segram" : "{}".format(input[i]['harga_emas_segram']),
                "komisen"           : "0"
            }
            jualan_model.CreateJualan(jualan)
            jualan_model.CreateJualanStok(jualan)
            self.__ProsesEmasBuruk(jualan)
        return True

    def __ProsesEmasBuruk(self, payloads):
        emasburuk_model = EmasBurukModel()
        emasburuk_model.CreateEmasBuruk()
        print('proses emas buruk')
        pass
