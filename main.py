from fastapi import FastAPI 

demo_app = FastAPI()

# POST, PUT, DELETE, GET
# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.

# @app.post()
# @app.put()
# @app.delete()
@demo_app.get("/")
async def root():
    return {"message":"Hello World from FastApi"}

@demo_app.get("/demo")
def demo():
    return {"message":"This is output from demo function"}

@demo_app.post("/post_demo")
def post_demo():
    return {"message":"This is output from post demo function"}