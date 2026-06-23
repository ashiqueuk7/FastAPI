from fastapi import FastAPI,Depends
from models import product
from database import SessionLocal,engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

#frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

#Home
@app.get('/')
def greet():
    return "Welcome" 

products = [
    product(id=1, name="iPhone 17", disc="Best Phone", price=700000.00, quant=5),
    product(id=2, name="S26 Ultra", disc="Best Phone", price=130000.00, quant=10),
    product(id=3, name="X300 Pro ", disc="Best Phone", price=1000000.00, quant=10),
]

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#connection
def init_db():
    db=SessionLocal()

    count=db.query(database_models.product).count
    if count==0:
        for i in products:
            db.add(database_models.product(**i.model_dump()))
        db.commit()
init_db()

#view
@app.get("/products")
def get_product(db : Session=Depends(get_db)):
    db_products=db.query(database_models.product).all()
    return db_products

#view by id
@app.get("/product/{id}")
def get_product_by_id(id:int, db : Session=Depends(get_db)):
    db_product=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        return db_product
    return "Product not found"

#add
@app.post("/product")
def add_product(product:product, db : Session=Depends(get_db)):
    db.add(database_models.product(**product.model_dump()))
    db.commit()
    return product

#update
@app.put("/product")
def update_product(id:int, product:product, db : Session=Depends(get_db)):
     db_product=db.query(database_models.product).filter(database_models.product.id==id).first()
     if db_product:
         db_product.name=product.name
         db_product.disc=product.disc
         db_product.price=product.price
         db_product.quant=product.quant
         db.commit()
         return "Product Updated."
     else:
        return "Not Found."

#del
@app.delete("/product")
def del_product(id:int, db : Session=Depends(get_db)):
    db_product=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted."
    else:
        return "Not Found."
        
        


