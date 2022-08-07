from fastapi import FastAPI  

#create FastAPI instance
app = FastAPI()

#returns a list of planets based on their distance from the sun
@app.get("/")
async def root():
    return {
    "Mercury" : "40.065 million miles", 
    "Venus" : "66.921 million miles",
    "Earth" : "94.269 million miles",
    "Mars" : "130.63 million miles", 
    "Jupiter" : "461.08 million miles",  
    "Saturn" : "916.24 million miles",
    "Uranus" : "1.8299 billion miles",
    "Neptune" : "2.7801 billion miles", 
    }