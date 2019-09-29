from ....models.mysql import mysql_execute_bulk_query, JualanModel, StockModel, NoBilModel, EmasBurukModel, BayarKadModel
from ...umum import UmumKiraanServices, UmumFormattingServices
from ...transaksi.aliran_wang import TransaksiAliranWangServices
from datetime import datetime,date

umum        = UmumKiraanServices()
formatting = UmumFormattingServices()

class TransaksiJualanServices():

    """
    1. tbl_stock_purchase - rekod stok yang telah dijual
    2. tbl_purchase - rekod stok yang dijual
    3. tbl_emasburuk - rekod sekiranya ada emas kerat
    4. tbl_cengkeram - update sekiranya jualan dibayar dengan cengkeram
    5. tbl_alirawang - rekod transaksi aliranwang
    """
    def ProsesJualan(self, payloads):
        jualan = JualanModel()  
        tag                         = payloads['tag']
        staff_id                    = payloads['kakitangan_id']
        no_bil                      = self.__NoBilJualan(tag)
        input_jualan                = self.__QueryInputJualan(payloads['item_jualan'], staff_id ,tag, no_bil)
        kaedah_bayaran              = self.__KaedahBayaran(payloads['kaedah_bayaran'], staff_id, tag, no_bil)
        return input_jualan

    def __NoBilJualan(self, tag):
        no_resit_jualan = NoBilModel().ReadNobil('no_jualan',tag)
        return no_resit_jualan

    def __QueryInputJualan(self, input, staff_id, tag, no_resit_jualan):
        jualan_model = JualanModel()
        stok_model = StockModel()
        for i in range(len(input)):
            stok_detail = stok_model.ReadStockByTagNoRaw(input[i]['no_tag'], input[i]['tag'])
            modal = umum.KiraModalEmasStok(stok_detail)
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
        EmasBurukModel().CreateEmasBuruk(payloads)
        return True
    
    def __KaedahBayaran(self, payloads, staff_id, tag, no_bil):
        payloads['id_kakitangan']   = staff_id
        taw                         = TransaksiAliranWangServices()
        payloads['tag']             = tag
        sql_statement               = ""
        if payloads['tunai'] > 0:
            sql_statement   += taw.BayarTunai(payloads, no_bil)
        if payloads['debit_kredit']['jumlah'] > 0 :
            sql_statement   += taw.BayarDebitKredit(payloads['debit_kredit'], no_bil, staff_id, tag)
        if payloads['cengkeram']['nilai_tempahan'] > 0:
            sql_statement   += taw.BayarCengkeram(payloads['cengkeram'], no_bil, staff_id, tag)
        if payloads['trade_in'][0]['harga_emas'] > 0:
            sql_statement   += taw.EmasTradeIn(payloads['trade_in'], no_bil, staff_id, tag)
        mysql_execute_bulk_query(sql_statement)