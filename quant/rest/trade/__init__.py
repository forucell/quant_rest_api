import json
from flask import Blueprint, Response, request
from quant.repository import TradeRepository

blueprint = Blueprint("taker_volume", __name__, url_prefix="")


@blueprint.route("/taker_volume", methods=["GET"])
def list_trade():
    from urllib.parse import unquote
    from quant.domain.trade import ListTrade, ListTradeRequestObject
    from quant.serializer import ListTradeEncoder

    source = unquote(request.args.get("exchange", ""))
    limit = unquote(request.args.get("limit", "10"))
    _from = unquote(request.args.get("from", "2020-11-07 05:57:00"))
    print("form:",_from)

    filters = {"source":source, "limit":limit, "_from": _from}
    request_object = ListTradeRequestObject.from_dict(filters)
    trade_repo = TradeRepository()
    use_case = ListTrade(trade_repo=trade_repo)
    response = use_case.execute(request_object)
    return Response(
        json.dumps(response.value, cls=ListTradeEncoder),
        mimetype="application/json",
        status=response.type,
    )