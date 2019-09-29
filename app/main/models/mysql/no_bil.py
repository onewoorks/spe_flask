from .. import mysql_execute_query

class NoBilModel():

    def ReadNobil(self, no_bil,tag):
        query = "SELECT "
        query += "{} ".format(no_bil)
        query += "FROM tbl_nobil "
        query += "WHERE "
        query += "tenant_id = '{}'".format(tag)
        return mysql_execute_query(query)[0][no_bil]

    def UpdateNobil(self, column_bil, no_bil, tag):
        query = "UPDATE tbl_nobil SET {} = {} ".format(column_bil, no_bil)
        query += "WHERE tenant_id = {}; ".format(tag)
        mysql_execute_query(query)
