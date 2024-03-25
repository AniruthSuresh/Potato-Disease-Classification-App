# use base setup version of python 3.11.7

from fastapi import FastAPI


app = FastAPI()

food = {
    'indian': ["samosa", 'dosa'],
    "us": ["hotdog", 'pie'],
    "italy": ["pizza", 'quesadilla']
}

@app.get("/food_items/{name}")


async def food_items(name):
    if name in food:
        return f"Best options are {food[name]}"
    else:
        return "Food not found for the specified cuisine."

# command in terminal: uvicorn file_name:app --reload
# reload is used so that it saves whenever there is a change


# COMMON END POINTS 

# get : read data
# post : create data
# put : update data 
# delete : delete data 
    
coupon_code = {
    1 : "10%",
    2 : "20%",
    3 : "30%"
}

@app.get("/get_coupon/{code}")


async def get_coupon(code : int):
    return f"discount avai : {coupon_code.get(code)}"


# BENEFITS 

# 1) Inbuild documentaion : just add doc in the end 
# 2) Compact code 
