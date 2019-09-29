from ...models.mysql.emas_buruk import EmasBurukModel

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
        jumlah_trade_in = 0
        for i in payloads:
            i['harga']          = i['harga_emas']
            i['id_kakitangan']  = id_kakitangan
            i['jenis']          = 1
            i['tag']            = tag
            jumlah_trade_in     += i['harga_emas']
            EmasBurukModel().CreateEmasBuruk(self.__PayloadEmasBuruk(i))
        return {
            "jumlah_harga"  : jumlah_trade_in
        }

    def DaftarEmasBuruk(self):
        print('proses emas buruk in')
        pass