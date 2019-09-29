from ...models.mysql.aliran_wang import AliranWangModel
from ...models.mysql.bayar_kad import BayarKadModel
from ...models.mysql import TempahanModel
from ..stock.emas_buruk import EmasBurukServices

from ..umum import UmumFormattingServices

formatting = UmumFormattingServices()

class TransaksiAliranWangServices:

    def __PayloadAliranWang(self, payload):
        input = {
            "id_jenis_transaksi": payload['jenis_transaksi'],
            "id_kategori"       : payload['id_kategori'],
            "perkara"           : payload['perkara'],
            "no_pelanggan"      : payload['no_pelanggan'] if 'no_pelanggan' in payload else "",
            "no_bil"            : payload['no_bil'],
            "nilai"             : payload['nilai'],
            "id_kakitangan"     : payload['id_kakitangan'],
            "tag"               : payload['tag'],
            "id_pelanggan"      : payload['id_pelanggan']
        }
        return input

    def DaftarAliranWang(self, payloads):
        input = self.__PayloadAliranWang(payloads)
        return AliranWangModel().CreateAliranWang(input, bulk_to=True)

    def BayarDebitKredit(self, payload, no_bil, staff_id, tag):
        input_bayarkad = {
            "nilai"         : payload["jumlah"],
            "faedah"        : payload['faedah'],
            "jenis"         : payload['jenis'] if 'jenis' in payload else "NULL",
            "no_transaksi"  : payload['no_transaksi'],
            "no_resit"      : no_bil,
            "id_kakitangan" : staff_id,
            "tag"           : tag
        }
        input_alirawang = {
            "jenis_transaksi"   : 0,
            "id_kategori"       : 13,
            "perkara"           : "({}) BAYAR KAD".format(formatting.NumberRange(no_bil)),
            "no_pelanggan"      : "",
            "no_bil"            : no_bil,
            "nilai"             : payload['jumlah'],
            "id_kakitangan"     : staff_id,
            "tag"               : tag,
            "id_pelanggan"      : ""
        }
        sql_statement = BayarKadModel().CreateBayarKad(input_bayarkad, bulk_to=True)
        sql_statement += self.DaftarAliranWang(input_alirawang)
        return sql_statement

    def BayarCengkeram(self, payload, no_bil, staff_id, tag):
        input_aliranwang = {
            "jenis_transaksi"   : 2,
            "id_kategori"       : 13,
            "perkara"           : "({}) CENGKERAM TEMPAHAN NO {}".format(formatting.NumberRange(no_bil), formatting.NumberRange(payload['no_resit_tempahan'])),
            "no_pelanggan"      : "",
            "no_bil"            : no_bil,
            "nilai"             : payload['nilai_tempahan'],
            "id_kakitangan"     : staff_id,
            "tag"               : tag,
            "id_pelanggan"      : ""
        }
        input_tempahan = {
            "status"            : 5,
            "tag"               : tag,
            "no_resit_tempahan" : payload['no_resit_tempahan']
        }
        sql_statement = self.DaftarAliranWang(input_aliranwang)
        sql_statement += TempahanModel().UpdateStatusTempahan(input_tempahan, bulk_to= True)
        return sql_statement

    def BayarTunai(self, payload, no_bil):
        input = {
            "jenis_transaksi"   : 3,
            "id_kategori"       : 13,
            "perkara"           : "({}) JUALAN STOK".format(formatting.NumberRange(no_bil)),
            "no_pelanggan"      : "",
            "no_bil"            : no_bil,
            "nilai"             : payload['tunai'],
            "id_kakitangan"     : payload['id_kakitangan'],
            "tag"               : payload['tag'],
            "id_pelanggan"      : ""
        }
        return self.DaftarAliranWang(input)
    
    def EmasTradeIn(self, payload, no_bil, staff_id, tag):
        trade_in    = EmasBurukServices().EmasTradeIn(payload, staff_id, tag)
        input = {
            "jenis_transaksi"   : 4,
            "id_kategori"       : "NULL",
            "perkara"           : "({}) EMAS TRADE IN".format(formatting.NumberRange(no_bil)),
            "no_pelanggan"      : "",
            "no_bil"            : no_bil,
            "nilai"             : trade_in['jumlah_harga'],
            "id_kakitangan"     : staff_id,
            "tag"               : tag,
            "id_pelanggan"      : ""
        }
        return self.DaftarAliranWang(input)
