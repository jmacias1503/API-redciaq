from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Modelo para la colección weather_data
class WeatherData(BaseModel):
    datetime: datetime
    rain_intensity: float
    forecast: Optional[str] = None
    station_id: int
    uv_index: float
    date_adq: str
    dew_point: float
    time_adq: str
    solar_radiation: float
    date: str
    wind_direction_degree: int
    wind_velocity: float
    humidity: int
    wind_chill: float
    heat_index: float
    temp: float
    rain: float
    wind_direction: str
    barometer: float

# Modelo para la colección users
class User(BaseModel):
    id: int
    username: str
    password: str
    last_login: Optional[str] = None
    is_superuser: bool
    is_staff: bool
    is_active: bool
    date_joined: str

# Modelo para la colección stations
class Station(BaseModel):
    id: int
    user_name: str
    password: str
    tipo: str
    station_url: str
    city: str
    state: str
    country: str
    dependencia: str
    time_zone: str
    latitude: float
    longitude: float
    elevation: Optional[int] = None
    station_name: str
    station_type: str
    hardware_version: str
    firmware_version: str
    device_id: str
    device_ip: int
    email_contact: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    name_responsable: Optional[str] = None
