from flask import request
from flask_restplus import Namespace, Resource, fields
from ..services.transaksi.jualan import TransaksiJualanServices

api = Namespace('transaksi',description="Transaksi SPE")

item_jualan = api.model('Item Jualan',{
    "no_tag"            : fields.Integer(),
    "no_id"             : fields.Integer(),
    "berat_beli"        : fields.Float(),
    "harga_emas_segram" : fields.Float(),
    "harga_upah"        : fields.Float(),
    "harga_emas"        : fields.Float(),
    "harga_permata"     : fields.Float(),
    "harga_jualan"      : fields.Float(),
    "kod_cukai"         : fields.Integer(),
    "jumlah_cukai"      : fields.Float(),
    "tag"               : fields.Integer()
})
item_servis = api.model('Item Servis',{
    "no_id": fields.Integer(),
    "nama_servis"       : fields.String(),
    "harga_servis"      : fields.Float()
})
maklumat_pelanggan = api.model('Maklumat Pelanggan', {
    "no_id"             : fields.Integer(),
    "no_kad"            : fields.String(),
    "no_kad_pengenalan" : fields.String(),
    "nama"              : fields.String()
})
debit_kredit = api.model('Bayaran Debit Kredit',{
    "jenis_bayaran" : fields.String(),
    "no_transaksi"  : fields.String(),
    "jumlah"        : fields.Float()
})

cengkeram   = api.model('Maklumat Cengekera', {
    "no_resit_tempahan "    : fields.String(description = "No resit tempahan"),
    "nilai_tempahan"        : fields.Float()
})

emas_buruk_trade_in  = api.model('Emas Buruk', {
    "jenis"         : fields.Integer(description = "emas kerat, emas beli, atau emas tradein"),
    "berat"         : fields.Float(),
    "harga_emas"    : fields.Float(),
    "id_mutu"       : fields.Integer(),
    "id_pelanggan"  : fields.Integer()
}) 

kaedah_bayaran = api.model('Kaedah Bayaran',{
    "tunai"         : fields.Float(),
    "debit_kredit"  : fields.Nested(debit_kredit),
    "cengkeram"     : fields.Nested(cengkeram),
    "trade_in"      : fields.List(fields.Nested(emas_buruk_trade_in))
})
harga_keseluruhan = api.model('Harga Keseluruhan',{
    "harga_barang"  : fields.Float(),
    "harga_cukai"   : fields.Float()
})

info_jualan = api.model('Maklumat Jualan',{
    "item_jualan"           : fields.List(fields.Nested(item_jualan)),
    "item_servis"           : fields.List(fields.Nested(item_servis), description="Maklumat kadar bayaran servis"),
    "maklumat_pelanggan"    : fields.Nested(maklumat_pelanggan),
    "kakitangan_id"         : fields.Integer(description="Kakitangan yang menjalankan transaksi ini"),
    "harga_keseluruhan"     : fields.Nested(harga_keseluruhan, description="Maklumat Jualan"),
    "kaedah_bayaran"        : fields.Nested(kaedah_bayaran),
    "tag"                   : fields.Integer(description="Session tag")
})

@api.route('/jualan-stok')
class JualanStok(Resource):
    @api.doc('Jualan stok dan servis')
    @api.doc(parser=info_jualan)
    def post(self):
        tjs = TransaksiJualanServices()
        response = tjs.ProsesJualan(request.json)
        return response