from flask_restplus import Namespace, Resource, fields

from ..services.tetapan.dulang import DulangServices
from ..services.tetapan.mutu import MutuServices

api = Namespace('tetapan',description="Tetapan")

@api.route('/dulang')
class TetapanSenaraiDulang(Resource):
    @api.doc('Dulang')
    def get(self):
        dulang = DulangServices()
        return dulang.GetSenaraiDulang()

@api.route('/mutu')
class TetapanSenaraiMutu(Resource):
    @api.doc('Mutu')
    def get(self):
        mutu = MutuServices()
        return mutu.GetSenaraiMutu()

