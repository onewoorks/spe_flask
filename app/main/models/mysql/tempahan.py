from .. import mysql_execute_query, mysql_insert_query

class TempahanModel():

    def ReadTempahan(self, no_resit):
        query = "SELECT "
        query += "tmp_cat as kategori, "
        query += "DATE_FORMAT(tmp_date,'%Y-%m-%d') as tarikh_tempah, "
        query += "tmp_namabarang as nama_tempahan, "
        query += "tmp_permata as permata, "
        query += "tmp_asal as asal, "
        query += "tmp_tambah as tambah, "
        query += "DATE_FORMAT(tmp_hari,'%Y-%m-%d') as hari, "
        query += "tmp_nota as nota, "
        query += "tmp_cengemas as cengkeram_emas, "
        query += "tmp_cengtunai as cengkeram_tunai, "
        query += "tmp_mutu as id_mutu, "
        query += "cust_id as id_pelanggan, "
        query += "tmp_resit as no_resit, "
        query += "tmp_status as status, "
        query += "stf_id as id_kakitangan, "
        query += "spl_id as id_pembekal, "
        query += "stk_id as id_stock, "
        query += "tmp_tupah as upah_tukang, "
        query += "tmp_kupah as upah_kedai, "
        query += "tenant_id as tag, "
        query += "tuk_modal as modal_tukang, "
        query += "resit_manual as resit_manual "
        query += "FROM tbl_tempahan "
        query += "WHERE "
        query += "tmp_resit = '{}'".format(no_resit)
        return mysql_execute_query(query)[0]

    def UpdateStatusTempahan(self, payload, bulk_to = False):
        query = "UPDATE tbl_tempahan SET "
        query += "tmp_status = {} ".format(payload['status'])
        query += "WHERE "
        query += "tenant_id = {} ".format(payload['tag'])
        query += "AND tmp_resit = {}".format(payload['no_resit_tempahan'])
        query += "; "
        if payload['status'] == 5:
            item_tempahan = self.ReadTempahan(payload['no_resit_tempahan'])
            item_tempahan['status'] = 5
            query += self.CreateTempahanAmbil(item_tempahan, bulk_to)
        return mysql_execute_query(query) if bulk_to == False else query

    def CreateTempahanAmbil(self, payload, bulk_to = False):
        query = "INSERT INTO tbl_tempahan_ambil ("
        query += "tmp_cat, tmp_date, tmp_namabarang, tmp_permata, "
        query += "tmp_asal, tmp_tambah, tmp_hari, tmp_nota, "
        query += "tmp_cengemas, tmp_cengtunai, tmp_mutu, cust_id, tmp_resit, "
        query += "tmp_status, stf_id, spl_id, stk_id, tmp_tupah, tmp_kupah, "
        query += "tuk_modal, t_dateambil, tenant_id"
        query += ") VALUE ("
        query += "{}, ".format(payload['kategori'])
        query += "'{}', ".format(payload['tarikh_tempah'])
        query += "'{}', ".format(payload['nama_tempahan'])
        query += "{}, ".format(payload['permata'] if payload['permata'] != None else 0)
        query += "{}, ".format(payload['asal'] if payload['asal'] != None else 0)
        query += "{}, ".format(payload['tambah'] if payload['tambah'] != None else 0)
        query += "'{}', ".format(payload['hari'])
        query += "'{}', ".format(payload['nota'])
        query += "{}, ".format(payload['cengkeram_emas'])
        query += "{}, ".format(payload['cengkeram_tunai'])
        query += "{}, ".format(payload['id_mutu'])
        query += "{}, ".format(payload['id_pelanggan'])
        query += "{}, ".format(payload['no_resit'])
        query += "{}, ".format(payload['status'])
        query += "{}, ".format(payload['id_kakitangan'])
        query += "{}, ".format(payload['id_pembekal'] if payload['id_pembekal'] != None else 0)
        query += "{}, ".format(payload['id_stock'] if payload['id_stock'] != None else "NULL")
        query += "{}, ".format(payload['upah_tukang'] if payload['upah_tukang'] != None else 0)
        query += "{}, ".format(payload['upah_kedai'] if payload['upah_kedai'] != None else 0)
        query += "{}, ".format(payload['modal_tukang'] if payload['modal_tukang'] != None else 0)
        query += "now(), "
        query += "{}".format(payload['tag'])
        query += "); "
        return mysql_insert_query(query) if bulk_to == False else query
