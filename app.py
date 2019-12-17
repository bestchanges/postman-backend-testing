import uuid

from flask import Flask, jsonify, request, redirect

app = Flask(__name__)


def gen_id(data):
    return len(data) + 1


global_todolists = {}

def todolist_to_dto(todolist: dict):
    todolist_dto = dict(todolist)
    del todolist_dto['items']
    return todolist_dto

@app.route("/lists", methods=('GET',))
def get_lists():
    lists = global_todolists.values()
    return jsonify([todolist_to_dto(todolist) for todolist in lists])


@app.route("/lists", methods=('POST',))
def create_list():
    todolist = request.get_json()
    assert 'id' not in todolist
    list_id = gen_id(global_todolists)
    todolist['id'] = list_id
    todolist.setdefault('items', {})
    global_todolists[list_id] = todolist
    return jsonify(todolist_to_dto(todolist))


@app.route("/lists/<int:list_id>", methods=('GET',))
def get_list(list_id):
    todolist = global_todolists[list_id]
    return jsonify(todolist_to_dto(todolist))


@app.route("/lists/<int:list_id>", methods=('PUT',))
def update_list(list_id):
    todolist = request.get_json()
    assert todolist['id'] == list_id
    assert list_id in global_todolists
    todolist.setdefault('items', {})
    global_todolists[list_id] = todolist
    return jsonify(todolist_to_dto(todolist))


@app.route("/lists/<int:list_id>", methods=('DELETE',))
def delete_list(list_id):
    assert list_id in global_todolists
    todolist = global_todolists[list_id]
    del global_todolists[list_id]
    return jsonify(todolist_to_dto(todolist))


@app.route("/lists/<int:list_id>/items", methods=('GET',))
def get_items(list_id: int):
    items = global_todolists[list_id]['items'].values()
    return jsonify(list(items))


@app.route("/lists/<int:list_id>/items", methods=('POST',))
def create_item(list_id: int):
    item = request.get_json()
    assert 'id' not in item
    items = global_todolists[list_id]['items']
    item_id = gen_id(items)
    item['id'] = item_id
    item.setdefault('completed', False)
    items[item_id] = item
    return jsonify(item)


@app.route("/lists/<int:list_id>/items/<int:item_id>", methods=('GET',))
def get_item(list_id: int, item_id: int):
    items = global_todolists[list_id]['items']
    assert item_id in items
    item = items[item_id]
    return jsonify(item)


@app.route("/lists/<int:list_id>/items/<int:item_id>", methods=('PUT',))
def update_item(list_id, item_id):
    item = request.get_json()
    assert item['id'] == item_id
    assert item_id in global_todolists[list_id]['items']
    existing_item = global_todolists[list_id]['items'][item_id]
    existing_item.update(item)
    return jsonify(existing_item)


@app.route("/lists/<int:list_id>/items/<int:item_id>", methods=('DELETE',))
def delete_item(list_id, item_id):
    assert item_id in global_todolists[list_id]['items']
    item = global_todolists[list_id]['items'][item_id]
    del global_todolists[list_id]['items'][item_id]
    return jsonify(item)


@app.route("/")
def root():
    return """
    CRUD: /lists
    CRUD: /lists/N/items
    """


def start_server(port: int):
    app.run(port=port)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8807)
    args = parser.parse_args()
    start_server(port=args.port)
