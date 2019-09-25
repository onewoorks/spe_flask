from .. import mysql_execute_query
class CengkeramModels():

    def ReadCengkeram(self, no_resit = None):
        query = "SELECT "
        query += "DATE_FORMAT(ck_date, '%d %M %Y') as tarikh_daftar, "
        query += "ck_value as nilai_cengekeram, "
        query += "tmp_resit as no_resit, "
        query += "stf_id as id_kakitangan, "
        query += "ck_status as status, "
        query += "tenant_id as tag "
        query += "FROM tbl_cengkeram "
        query += "WHERE "
        query += "tmp_resit = {}".format(no_resit)
        return mysql_execute_query(query)
