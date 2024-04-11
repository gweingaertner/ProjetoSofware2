from flask import Flask
from Migration.migration import init_db
from Entidades.Ong.Web import ong_routes
from Entidades.Voluntario.Web import voluntario_routes
from Entidades.Evento.Web import evento_routes

app = Flask(__name__)

app.register_blueprint(ong_routes)
app.register_blueprint(voluntario_routes)
app.register_blueprint(evento_routes)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
