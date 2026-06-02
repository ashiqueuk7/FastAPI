from fastapi import FastAPI
from models import product
app=FastAPI()

#Home
@app.get('/')
def greet():
    return "Welcome" 

products = [
    product(id=1, name="iPhone 17", disc="Best Phone", price=700000.00, quant=10),
    product(id=2, name="S26 Ultra", disc="Best Phone", price=130000.00, quant=10),
    product(id=3, name="X300 Pro", disc="Best Phone", price=1000000.00, quant=10),
]

@app.get("/products")
def get_product():
    return products

#view
@app.get("/product/{id}")
def get_product_by_id(id:int):
    for i in products:
        if i.id==id:
            return i
    return "Product not found"

#add
@app.post("/product")
def add_product(product:product):
    products.append(product)
    return product

