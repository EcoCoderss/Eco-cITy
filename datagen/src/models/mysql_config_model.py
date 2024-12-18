from pydantic import BaseModel

class MySQLConfig(BaseModel):
    host: str
    user: str
    password: str
    database: str
    port: int = 3306