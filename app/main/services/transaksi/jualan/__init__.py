from ....models.mysql.jualan import JualanModel
from ....models.mysql.stock import StockModel
from ....models.mysql.no_bil import NoBilModel
from ....models.mysql.emas_buruk import EmasBurukModel

from ...umum.kiraan import UmumKiraanServices

from datetime import datetime,date

umum = UmumKiraanServices()

class TransaksiJualanServices():

    """
    1. tbl_stock_purchase - rekod stok yang telah dijual
    2. tbl_purchase - rekod stok yang dijual
    3. tbl_emasburuk - rekod sekiranya ada emas kerat
    4. tbl_cengkeram - update sekiranya jualan dibayar dengan cengkeram
    5. tbl_alirawang - rekod transaksi aliranwang
    """
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
            modal = umum.KiraModalEmasStok(stok_detail)
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
                "modal"             : "{}".format(modal['segram']*input[i]['berat_beli']),
                "berat_beli"        : "{}".format(input[i]['berat_beli']),
                "no_resit_jualan"   : "{}".format(no_resit_jualan),
                "pelanggan_id"      : "1",
                "harga_jualan"      : "{}".format(input[i]['harga_jualan']),
                "harga_emas_segram" : "{}".format(input[i]['harga_emas_segram']),
                "komisen"           : "0",
                "baki_berat"        : stok_detail['stk_weight'] - input[i]['berat_beli'],
                "stok_asal"         : stok_detail,
                "modal_segram"      : modal['segram']
            }
            jualan_model.CreateJualan(jualan)       #tbl_stock_purchase
            jualan_model.CreateJualanStok(jualan)   #tbl_purchases
            if jualan['baki_berat'] > 0 : 
                self.__ProsesEmasBuruk(jualan)
        return True

    def __ProsesEmasBuruk(self,payloads):
        harga = payloads['modal']
        payloads = {
            "no_tag"            : payloads['no_tag'],
            "jenis"             : 2,
            "berat"             : payloads['baki_berat'],
            "harga"             : payloads['modal_segram']*payloads['baki_berat'],
            "id_mutu"           : payloads['mutu_id'],
            "id_kakitangan"     : payloads['kakitangan_id'],
            "pelanggan_id"      : payloads['pelanggan_id'],
            "status"            : 0,
            "no_resit"          : payloads['no_resit_jualan'],
            "untung"            : "0",
            "tag"               : payloads['tag'],
            "nilai_cukai"       : 0,
            "kod_cukai"         : 0,
            "rujukan"           : ""
        }
        emasburuk_model = EmasBurukModel()
        emasburuk_model.CreateEmasBuruk(payloads)
        return True
