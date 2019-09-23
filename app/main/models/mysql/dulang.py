from .. import mysql_execute_query

class DulangModel():

    def GetSenaraiDulang(self):
        query = "SELECT "
        query += "dlg_name as kod_dulang, "
        query += "dlg_desc as nama_dulang, "
        query += "tenant_id as tag "
        query += "FROM tbl_dulang "
        query += "WHERE status = 1 "
        query += "ORDER BY tenant_id "
        response = mysql_execute_query(query)
        return response