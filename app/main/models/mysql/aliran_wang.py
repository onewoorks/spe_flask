class AliranWangModel:

    def CreateAliranWang(self, payload):
        query = "INSERT INTO tbl_aliranwang ("
        query += "aw_type, aw_cat, aw_perkara,"
        query += "aw_kp, aw_nobil, aw_value, "
        query += "stf_id, tenant_id, cust_id) VALUE ("
        query += "{},".format(payload['id_jenis_transaksi'])
        query += "{},".format(payload['id_kategori'])
        query += "'{}',".format(payload['perkara'].upper())
        query += "'{}',".format(payload['no_pelanggan'])
        query += "{},".format(payload['no_bil'])
        query += "{},".format(payload['nilai'])
        query += "{},".format(payload['id_kakitangan'])
        query += "{},".format(payload['tag'])
        query += "{}".format(payload['id_pelanggan'] if payload['id_pelanggan'] != '' else "NULL" )
        query += ")"
        print('----TUNAI----')
        print(query)