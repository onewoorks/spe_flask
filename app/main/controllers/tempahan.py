from flask import request
from flask_restplus import Namespace, Resource, fields
from ..services.transaksi.tempahan import TransaksiTempahanServices

api = Namespace('tempahan',description="Module Tempahan")

@api.route('/semak-tempahan/<no_resit>')
class JualanStok(Resource):
    @api.doc('Semak maklumat tempahan')
    def get(self, no_resit):
        tempahan = TransaksiTempahanServices()
        data = tempahan.GetMaklumatTempahan(no_resit)
        return data