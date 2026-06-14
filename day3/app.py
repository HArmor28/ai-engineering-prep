from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FlyRank"}

@app.get("/about")
def about():
    return {
        "name": "Hailey Armor",
        "major": "Statistics"
    }
@app.get("/favorite-class")
def favorite_class():
    return {
        "class": "Math 231"
    }