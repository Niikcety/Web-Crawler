from db.db import session_scope, VisitedLinks
from sqlalchemy import func
import json


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
        records = session.query(VisitedLinks.server_type, func.count(VisitedLinks.server_type)).group_by(VisitedLinks.server_type).all()
    return server_type_simplifier(records)
