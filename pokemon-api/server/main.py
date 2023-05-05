import uvicorn
from fastapi import FastAPI

from server.routers.trainer_routes import router_trainer
from server.routers.pokemon_routes import router_pokemon
from server.routers.gym_routes import router_gym

from server.sqlalchemy.models.trainer_model import TrainerModel

#Base.metadata.drop_all(bind=engine)
#Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


@app.get('/api')
def home_page():
    return 'Home!'


app.include_router(router_trainer)
app.include_router(router_pokemon)
app.include_router(router_gym)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)
