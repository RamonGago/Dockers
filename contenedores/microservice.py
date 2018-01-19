from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/cuentas.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(96), unique=True)
    email = db.Column(db.String(96), unique=True)

@app.route("/")
def server_info():
    return jsonify({
        "server": "My API"
    })

@app.route("/status")
def getStatus():
    return jsonify({
        status: "OK"
    })

@app.route("/usuarios/", endpoint="crear_usuario", methods=["POST"])
def create_user():
    from flask import request
    json = request.get_json()
    email = json.get("email")
    name = json.get("name")
    new_user = Usuario()
    new_user.name = name
    new_user.email = email

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id
    }), 201

@app.route("/usuarios/", endpoint="lista_usuarios", methods=["GET"])
def list_usuarios():
    usuarios = Usuario.query.order_by(Usuario.id).all()

    return jsonify({
        "items": [{"id": x.id, "name": x.name, "email": x.email} for x in usuarios]
    })

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0")
