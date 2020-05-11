from .. import mysql_execute_query
import json

class StockModel():
    def read_stock_by_tagn_o(self, tag_no):
        query = "SELECT "
        query += "s.stk_id as id, "
        query += "s.stk_tag as no_tag, "
        query += "DATE_FORMAT(s.stk_register,'%d %M %Y') as tarikh_daftar, "
        query += "s.stk_name as nama_stok, "
        query += "d.dlg_name as dulang, "
        query += "c.cat_name as mutu, "
        query += "s.stk_weight as berat, "
        query += "s.stk_emas as modal_emas, "
        query += "s.stk_permata as modal_permata, "
        query += "s.stk_upah as modal_upah, "
        query += "s.data_attribute as data_tambahan "
        query += "FROM tbl_stock s "
        query += "LEFT JOIN tbl_dulang d on d.dlg_id = s.dlg_id "
        query += "LEFT JOIN tbl_category c on c.cat_id = s.cat_id "
        query += "WHERE "
        query += "s.stk_tag = {}".format(int(tag_no))
        response = mysql_execute_query(query)
        return response
    
    def read_stock_by_tag_no_raw(self, tag_no, tag):
        query = "SELECT * FROM tbl_stock "
        query += "WHERE "
        query += "stk_tag = '{}' ".format(int(tag_no))
        query += "AND tenant_id= '{}'".format(int(tag))
        return mysql_execute_query(query)[0]

    def update_data_attribute_stock(self, stk_id, tag_no, data_attribute):
        query = "UPDATE `tbl_stock` SET `data_attribute` = '{}' ".format(json.dumps(data_attribute))
        query += "WHERE stk_tag = '{}' AND `stk_id`='{}'".format(int(tag_no), int(stk_id))
        mysql_execute_query(query)

