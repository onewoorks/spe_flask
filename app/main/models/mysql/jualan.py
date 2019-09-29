from .. import mysql_execute_query, mysql_insert_query

class JualanModel():

    def CreateJualan(self,input, bulk_to = False):
        query = "INSERT INTO tbl_stock_purchase ("
        query += "stk_color, stk_tag, stk_register, "
        query += "stk_name, cat_id, dlg_id, stk_weight, "
        query += "spl_id, stk_upah, stk_permata, "
        query += "stk_upahdisplay, stk_status, stk_market, "
        query += "tenant_id, tax_gst"
        query += ") VALUE ("
        query += "null," 
        query += "{},".format(int(input['no_tag']))
        query += "now(),"
        query += "'{}',".format(input['nama_barang'])
        query += "{},".format(input['mutu_id'])
        query += "{},".format(input['pembekal_id'])
        query += "{},".format(input['upah'])
        query += "{},".format(input['emas'])
        query += "{},".format(input['permata'])
        query += "{},".format(input['upahdisplay'])
        query += "{},".format(input['kakitangan_id'])
        query += "{},".format(input['status'])
        query += "{},".format(input['harga_emas_segram'])
        query += "{},".format(input['tag'])
        query += "{}".format(input['kod_cukai'])
        query += "); "
        return mysql_insert_query(query) if bulk_to == False else query

    def CreateJualanStok(self, input, bulk_to = False):
        query = "INSERT INTO tbl_purchase ("
        query += "pch_tag, cat_id, pch_name, "
        query += "pch_date, pch_price, pch_modal, "
        query += "pch_weight, pch_resit, cust_id, "
        query += "stf_id, pch_hes, komisen, "
        query += "dlg_id, spl_id, stk_upah, stk_emas, "
        query += "stk_permata, stk_upahdisplay, "
        query += "tenant_id, tax_gst"
        query += ") VALUE ("
        query += "{},".format(input['no_tag'])
        query += "{},".format(input['mutu_id'])
        query += "'{}',".format(input['nama_barang'])
        query += "now(),"
        query += "{},".format(input['harga_jualan'])
        query += "{},".format(input['modal'])
        query += "{},".format(input['berat_beli'])
        query += "{},".format(input['no_resit_jualan'])
        query += "{},".format(input['pelanggan_id'])
        query += "{},".format(input['kakitangan_id'])
        query += "{},".format(input['harga_emas_segram'])
        query += "{},".format(input['komisen'])
        query += "{},".format(input['dulang_id'])
        query += "{},".format(input['pembekal_id'])
        query += "{},".format(input['upah'])
        query += "{},".format(input['emas'])
        query += "{},".format(input['permata'])
        query += "{},".format(input['upah'])
        query += "{},".format(input['tag'])
        query += "{}".format(input['kod_cukai'])
        query += ");"
        return mysql_insert_query(query) if bulk_to == False else query