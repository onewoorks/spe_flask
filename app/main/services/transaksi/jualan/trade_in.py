class TransaksiJualanTradeIn:

    def PayloadEmasBuruk(self, payloads):
        input = {
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
        return input

    def EmasTradeIn(self, payloads):
        print('trade in process')
        print(payloads)
        pass

    def DaftarEmasBuruk(self):
        print('proses emas buruk in')
        pass