from flask import Flask
from Migration.migration import init_db
from Entidades.Ong.Web import ong_routes
from Entidades.Voluntario.Web import voluntario_routes
from Entidades.Evento.Web import evento_routes
from Entidades.Login.Web import login_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(ong_routes)
app.register_blueprint(voluntario_routes)
app.register_blueprint(evento_routes)
app.register_blueprint(login_routes)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
