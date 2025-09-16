import uvicorn
import sys
import os
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Добавляем текущую папку в путь Python для импортов
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from models import FruitDB
from database import SessionLocal, Base, engine
from schemas import Fruit, Fruits

# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(debug=True)



origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]




app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/fruits", response_model=Fruits)
def get_fruits(db: Session = Depends(get_db)):
    fruits = db.query(FruitDB).all()
    return Fruits(fruits=[Fruit(name=f.name) for f in fruits])



@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit, db: Session = Depends(get_db)):
    db_fruit = FruitDB(name=fruit.name)
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return Fruit(name=db_fruit.name)

@app.delete("/fruits")
def remove_fruit(fruit: Fruit, db: Session = Depends(get_db)):
    db_fruit = db.query(FruitDB).filter(FruitDB.name == fruit.name).first()
    if db_fruit:
        db.delete(db_fruit)
        db.commit()
        return {"message": f"Fruit {fruit.name} deleted successfully"}
    return {"message": f"Fruit {fruit.name} not found"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)