from db.db import session_scope, engine, GET_ALL_SERVER_TYPES_BY_TIME_INTERVAL
from VisitedLinks.model import VisitedLinksModel
from sqlalchemy import func
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


def server_type_simplifier(records):
    server_types_dictionary = dict()
    for record in records:
        server, count = record
        s_type = server.split('/', 1)[0]
        if s_type in server_types_dictionary.keys():
            server_types_dictionary[s_type] += count
        else:
            server_types_dictionary[s_type] = count
    return server_types_dictionary


def get_by_server_type():
    with session_scope() as session:
        records = session.query(VisitedLinksModel.server_type, func.count(VisitedLinksModel.server_type)).group_by(
                                VisitedLinksModel.server_type).all()
    return json.dumps(server_type_simplifier(records))


def get_by_server_type_time(year=0, month=0, day=0, hour=0, minute=0, second=0):
    now = datetime.now()
    start = now - relativedelta(years=year, months=month, days=day, hours=hour, minutes=minute, seconds=second)
    with session_scope() as session:
        records = session.query(VisitedLinksModel.server_type, func.count(VisitedLinksModel.server_type)).filter(
                                VisitedLinksModel.saved > start).filter(VisitedLinksModel.saved < now).group_by(
                                VisitedLinksModel.server_type).all()
    return json.dumps(server_type_simplifier(records))
