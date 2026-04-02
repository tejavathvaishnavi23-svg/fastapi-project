from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"

@app.get("/products")
def get_products():
    return products

##path params..
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    ## if product available with the id, return product, else return error message.

    for oneProduct in products:
        if oneProduct["id"] == product_id:
            return oneProduct

    return {
        "error":"Product not found for this ID."
    }


## query params
@app.get("/greet")
def greet_user(request: Request):
    query_params = dict(request.query_params)

    return{
        "greet": f"Hello {query_params.get("name")} Your age is {query_params.get("age")}"
    }


## body, headers - request headers, Query params


## different types of HTTP methods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)

    return {"status":"Product Created Successfully...","data":products}


@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):

    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status":"Product Updated Successfully...","product":product_data}

    return {
        "error": "Product not found for this ID."
    }

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status":"Product Deleted Successfully...", "product":deleted_product}

    return {
            "error": "Product not found for this ID."
    }