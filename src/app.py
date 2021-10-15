from sanic import Sanic
from sanic.request import Request
from sanic import response
from src.routes import routes
from src.database import connection
from src.models import tables

app = Sanic(__name__)
app.blueprint(routes)



@app.listener('before_server_start')
async def create_tables(server: Sanic, _):
    try:
        connection.create_tables(
            tables
        )
    except Exception as e:
        print("Error ao setar o db: ", str(e))
        pass

@app.listener('after_server_start')
async def depois(server: Sanic, _):
    print('depois do server iniciar')