from .. import mysql_insert_query

class BayarKadModel:

    def CreateBayarKad(self, payload, bulk_to = False):
        query = "INSERT INTO tbl_creditpayment ("
        query += "c_value, interest, c_p_type, "
        query += "c_resit_no, c_sales_no, stf_id, tenant_id"
        query += ") VALUE ("
        query += "{},".format(payload['nilai'])
        query += "{},".format(payload['faedah'])
        query += "{},".format(payload['jenis'])
        query += "{},".format(payload['no_transaksi'])
        query += "{},".format(payload['no_resit'])
        query += "{},".format(payload['id_kakitangan'])
        query += "{}".format(payload['tag'])
        query += "); "
        return mysql_insert_query(query) if bulk_to == False else query