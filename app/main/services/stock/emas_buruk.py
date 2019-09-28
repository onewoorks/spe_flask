from ...models.mysql.emas_buruk import EmasBurukModel

from ..transaksi.aliran_wang import TransaksiAliranWangServices

class EmasBurukServices():
    
    def __PayloadEmasBuruk(self, payloads):
        input = {
            "no_tag"            : payloads['no_tag'] if 'no_tag' in payloads else 0,
            "jenis"             : payloads['jenis'],
            "berat"             : payloads['berat'],
            "harga"             : payloads['harga'],
            "id_mutu"           : payloads['id_mutu'],
            "id_kakitangan"     : payloads['id_kakitangan'],
            "pelanggan_id"      : payloads['id_pelanggan'],
            "status"            : 0,
            "no_resit"          : payloads['no_resit'] if 'no_resit' in payloads else "NULL",
            "untung"            : "0",
            "tag"               : payloads['tag'],
            "nilai_cukai"       : 0,
            "kod_cukai"         : 0,
            "rujukan"           : ""
        }
        return input

    def EmasTradeIn(self, payloads, id_kakitangan, tag):
        print('trade in process')
        for i in payloads:
            i['harga']          = i['harga_emas']
            i['id_kakitangan']  = id_kakitangan
            i['jenis']          = 1
            i['tag']            = tag
            EmasBurukModel().CreateEmasBuruk(self.__PayloadEmasBuruk(i))
            # TransaksiAliranWangServices().DaftarAliranWang()
        pass

    def DaftarEmasBuruk(self):
        print('proses emas buruk in')
        pass