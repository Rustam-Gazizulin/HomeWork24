import os

from flask import Flask

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def build_query(it, query):
    query_items = query.split('|')
    res = map(lambda v: v.strip(), it)
    for item in query_items:
        split_item = item.split(':')
        cmd = split_item[0]
        if cmd == 'filter':
            arg = split_item[1]
            res = filter(lambda v, txt=arg: txt in v, res)
        if cmd == 'map':
            arg = split_item[1]
            res = map(lambda v, idx=arg: v.split(" ")[idx], res)
        if cmd == 'unique':
            res = set(res)
        if cmd == 'sort':
            arg = split_item[1]
            reverse = arg == 'desc'
            res = sorted(res, reverse=reverse)
        if cmd == 'limit':
            arg = int(split_item[1])
            res = list(res)[:arg]
    return res


@app.post("/perform_query")
def perform_query():
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    return app.response_class('', content_type="text/plain")
