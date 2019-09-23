from ...models.mysql.jualan import JualanModel


class TrasaksiJualanServices():

    def ProsesJualan(self,post_data):
        jualan = JualanModel()  
        input_jualan = self.InputJualan(post_data)
        jualan.CreateJualan(input_jualan)
        pass

    def InputJualan(self, input):
        jualan = {
            "stk_color": "".format(input['']),
            "no_tag": "".format(input['']),
            "tarikh_jualan": "".format(input['']),
            "mutu_id": "".format(input['']),
            "pembekal_id": "".format(input['']),
            "upah": "".format(input['']),
            "emas": "".format(input['']),
            "permata": "".format(input['']),
            "upahdisplay": "".format(input['']),
            "kakitangan_id": "".format(input['']),
            "status": "".format(input['']),
            "harga_pasaran": "".format(input['']),
            "tag": "".format(input['']),
            "kod_cukai": "".format(input[''])
        }
        return jualan