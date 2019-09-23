from .. import mysql_execute_query
class MutuModal():
    def GetSenaraiMutu(self):
        query = "SELECT "
        query += "cat_id as kod_mutu, "
        query += "cat_name as mutu, "
        query += "tenant_id as tag "
        query += "FROM tbl_category "
        response = mysql_execute_query(query)
        return response