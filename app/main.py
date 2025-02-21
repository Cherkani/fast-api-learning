from fastapi import FastAPI
from .db.database import init_db
from .controllers.developer_controller import router as developer_router
from .controllers.ticket_controller import router as ticket_router

app = FastAPI(
    title="Developer and Ticket Management API",
    description="A CRUD API for managing developers and their tickets.",
    version="1.0.0",
)

# Initialize database
init_db()

app.include_router(developer_router, prefix="/api/developers", tags=["Developers"])
app.include_router(ticket_router, prefix="/api/tickets", tags=["Tickets"])

@app.get("/")
async def root():
    return {"message": "Developer and Ticket API"}
