from pydantic import BaseModel, Field

class MySQLDataModel(BaseModel):
    name: str = Field(..., description="Nome dello spazio")
    dimensions: float = Field(..., gt=0, description="Dimensioni in metri quadrati")
    capacity: int = Field(..., gt=0, description="Capacità massima")