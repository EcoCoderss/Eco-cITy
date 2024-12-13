from fastapi import FastAPI
from routers import people_flow_router, emergency_exit_router, staff_estimation_router

app = FastAPI(
    title="Citizen_engagement",
    description="Gestione cittadini",
    version="1.0.0"
)

# Include Routers
app.include_router(people_flow_router.router, prefix="/people-flow", tags=["People Flow"])
app.include_router(emergency_exit_router.router, prefix="/emergency-exit", tags=["Emergency Exit"])
app.include_router(staff_estimation_router.router, prefix="/staff-estimation", tags=["Staff Estimation"])

@app.get("/")
async def root():
    return {"message": "Simulation Project is running"}
