from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api/v1')

from . import Web_Server_Xception
