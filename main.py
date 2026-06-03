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
#view
@app.get("/products")
def get_product():
    return products

#view by id
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

#update
@app.put("/product")
def update_product(id:int, product:product):
     for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "Product added Success."
     return "Not Found."

#del
@app.delete("/product")
def del_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product Deleted"
    return "Not Found."
        
        


