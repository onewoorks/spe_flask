from .. import mysql_execute_query

class TempahanModel():

    def ReadTempahan(self, no_resit):
        query = "SELECT "
        query += "tmp_cat as kategori, "
        query += "DATE_FORMAT(tmp_date,'%d %M %Y') as tarikh_tempah, "
        query += "tmp_namabarang as nama_tempahan, "
        query += "tmp_permata as permata, "
        query += "tmp_asal as asal, "
        query += "tmp_tambah as tambah, "
        query += "DATE_FORMAT(tmp_hari, '%d %M %Y') as hari, "
        query += "tmp_nota as nota, "
        query += "tmp_cengemas as cengkeram_emas, "
        query += "tmp_cengtunai as cengkeram_tunai, "
        query += "tmp_mutu as id_mutu, "
        query += "cust_id as id_pelanggan, "
        query += "tmp_resit as no_resit, "
        query += "tmp_status as status, "
        query += "stf_id as id_kakitangan, "
        query += "tmp_tupah as upah_tukang, "
        query += "tmp_kupah as upah_kedai, "
        query += "tenant_id as tag, "
        query += "resit_manual as resit_manual "
        query += "FROM tbl_tempahan "
        query += "WHERE "
        query += "tmp_resit = '{}'".format(no_resit)
        return mysql_execute_query(query)[0]
