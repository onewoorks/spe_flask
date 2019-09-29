from .. import mysql_insert_query

from ...services.umum.formatting import UmumFormattingServices

umum = UmumFormattingServices()
class EmasBurukModel():

    def CreateEmasBuruk(self, payloads, bulk_to = False):
        query = "INSERT INTO tbl_emasburuk ("\
            "emb_tag, eb_jenis, emb_date,"\
            "emb_weight, emb_price, cat_id,"\
            "stf_id,cust_id,emb_status,"\
            "no_resit, eba_id, tenant_id,"\
            "kos_gst, kod_gst, ref_id) "
        query += "VALUE ("
        query += "{},".format(payloads['no_tag'])
        query += "{},".format(payloads['jenis'])
        query += "now(),"
        query += "{},".format(umum.FixedNumber(payloads['berat']))
        query += "{},".format(umum.FixedNumber(payloads['harga']))
        query += "{},".format(payloads['id_mutu'])
        query += "{},".format(payloads['id_kakitangan'])
        query += "{},".format(payloads['pelanggan_id'])
        query += "{},".format(payloads['status'])
        query += "{},".format(payloads['no_resit'])
        query += "{},".format(payloads['untung'])
        query += "{},".format(payloads['tag'])
        query += "{},".format(umum.FixedNumber(payloads['nilai_cukai']))
        query += "{},".format(payloads['kod_cukai'])
        query += "'{}'".format(payloads['rujukan'])
        query += "); "
        return mysql_insert_query(query) if bulk_to == False else query