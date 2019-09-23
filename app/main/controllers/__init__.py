from flask_restplus import Api

from .stock import api as stock_api
from .tetapan import api as tetapan_api
from .transaksi import api as transaksi_api

api = Api(
    title="Sistem Pengurusan Emas API",
    version="1.0",
    description="An API for related sistem pengurusan emas inventory <style>.models {display: none !important}</style>"
)

api.add_namespace(stock_api)
api.add_namespace(tetapan_api)
api.add_namespace(transaksi_api)