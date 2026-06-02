from pydantic import BaseModel
class product(BaseModel):
    id : int 
    name : str
    disc : str
    price : float
    quant : int

    
