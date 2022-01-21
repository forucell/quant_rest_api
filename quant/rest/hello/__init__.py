import json
from flask import Blueprint, Response, request

from quant.repository import TradeRepository

blueprint = Blueprint("", __name__, url_prefix="")


@blueprint.route("/", methods=["GET"])
def hello():
    return Response(
        json.dumps('Hello'),
        mimetype="application/json",
        status='200',
    )