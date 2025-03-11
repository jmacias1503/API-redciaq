from fastapi import FastAPI, HTTPException, Depends
from database import db
from models import WeatherData, User, Station
from bson import ObjectId
from typing import List

app = FastAPI()

# Ruta de prueba
@app.get("/")
def home():
    return {"message": "API funcionando 🚀"}

# Obtener todos los registros de weather_data
@app.get("/weather_data", response_model=List[WeatherData])
async def get_weather_data():
    weather_list = await db.weather_data.find().to_list(100)
    return weather_list

# Insertar un nuevo registro en weather_data
@app.post("/weather_data")
async def create_weather_data(data: WeatherData):
    new_entry = await db.weather_data.insert_one(data.dict())
    return {"message": "Dato insertado", "id": str(new_entry.inserted_id)}

# Obtener todos los usuarios
@app.get("/users", response_model=List[User])
async def get_users():
    users = await db.users.find().to_list(100)
    return users

# Insertar usuario
@app.post("/users")
async def create_user(user: User):
    new_user = await db.users.insert_one(user.dict())
    return {"message": "Usuario creado", "id": str(new_user.inserted_id)}

# Obtener todas las estaciones
@app.get("/stations", response_model=List[Station])
async def get_stations():
    stations = await db.stations.find().to_list(100)
    return stations

# Insertar estación
@app.post("/stations")
async def create_station(station: Station):
    new_station = await db.stations.insert_one(station.dict())
    return {"message": "Estación creada", "id": str(new_station.inserted_id)}
