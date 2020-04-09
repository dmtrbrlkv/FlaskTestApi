from flask import Flask, abort

config = {
    "url": "/notes",
    "database": {
        "db1":{
            "filepath": "names.nsf",
            "view": {"view1": "by_id", "view2" : "by_name"},
            "search": True,
            "document": True
        },

        "db2":{
            "filepath": "itcrowd.nsf",
            "view": {"view1": "by_id", "view2" : "by_name"},
            "search": False,
            "document": True
        }
    }
}




app = Flask(__name__)

BASE_URL = config["url"]
databases = config["database"]


@app.route(BASE_URL + '/')
def index():
    return "Hello, World!"


@app.route(BASE_URL + '/<database>/view/<viewname>')
def view(database, viewname):
    if database not in databases:
        return "Not availabale db " + database, 404

    db = databases[database]

    if "view" not in db:
        return "View not availabale", 404

    view = db["view"]

    if viewname not in view:
        return "Not availabale view " + viewname, 404

    return "VIEW CONTENT " + database + " " + viewname


@app.route(BASE_URL + '/<database>/search')
def search(database):
    if database not in databases:
        return "Not availabale db " + database, 404

    db = databases[database]

    if "search" not in db or not db["search"]:
        return "Search not availabale", 404

    return "SEARCH IN " + database


@app.route(BASE_URL + '/<database>/document<doc_id>')
def document(database, doc_id):
    if database not in databases:
        return "Not available db " + database, 404

    db = databases[database]

    if "document" not in db or not db["document"]:
        return "Document not available", 404

    return "DOC FROM " + database


if __name__ == '__main__':
    app.run(debug=True)