from ...models.mysql.aliran_wang import AliranWangModel

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
        AliranWangModel().CreateAliranWang(input)        
        pass