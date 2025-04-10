from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymongo

app = FastAPI()

#conecting with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["person"]
collection = database["employee"]

#$lt (less than), $gt (greater than), $lte (less than and equal to), $gte (greater than and equal to) operators
dataValue = list(collection.find({"age": {"$gt" : "35"}}))

for item in dataValue:
    print(item)

#delete operation in fast api
record = {"name": "saad"}
collection.delete_many(record)

#limiting get data from database
limit = collection.find().limit(2)
for item in limit:
    print(item)

#updating the data
fil = {"name": "Saad"}
upd = {"age" : 16}
updt = collection.update_many(fil,{"$set": upd})
print(updt.modified_count)

#counting the data
print(collection.count_documents({}))
print(collection.count_documents({"name" : "Saad"}))

#ignore the key of data
data = collection.find({"name": "Saad"}, {"age" : 0, "subject" : 0, "_id": 0})
for item in data:
    print(item)


#selective query gives one data
# data = collection.find_one({"name": "saad"})
# print(data)

#selective query gives all data
# data = collection.find({"name": "Saad"})
# for item in data:
#     print(item)

#read one data
# data = collection.find_one()
# print(data)

#read all data
# data = collection.find()
# for item in data:
#     print(item)
#print(list(data))


#insert data operation
#dictonary = [
#     {
#     "name" : "Saad",
#     "channel": "youtube",
#     "age": "22",
#     "subject": "python"
#     },
#      {
#     "name" : "Saad Nisar",
#     "channel": "youtube",
#     "age": "22",
#     "subject": "python"
#     },
#      {
#     "name" : "Saad BCS",
#     "channel": "youtube",
#     "age": "22",
#     "subject": "python"
#     },
#      {
#     "name" : "Saad Tikki",
#     "channel": "youtube",
#     "age": "22",
#     "subject": "python"
#     }
# ]

# collection.insert_many(dictonary)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/{name}", response_class=HTMLResponse)
def read_item(request: Request, name):
    collection.insert_one({"name": name})
    return templates.TemplateResponse(
        request=request, name="home.html",
    )


@app.get("/about", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="about.html",
    )