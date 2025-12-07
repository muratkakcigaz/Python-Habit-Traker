import requests
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

USERNAME=os.getenv('USER_NAME')
TOKEN=os.getenv('TOKEN')
GRAPH_ID=os.getenv('GRAPH_ID')

USER_ENDPOINT="https://pixe.la/v1/users"

today=datetime.now()
today_strf=today.strftime("%Y%m%d")



    

def create_user():
    # --------------Used For User Creation------------------------
    
    user_parameters={
        "token":TOKEN,
        "username":USERNAME,
        "agreeTermsOfService":"yes",
        "notMinor":"yes",
    }
     
    response=requests.post(url=USER_ENDPOINT,json=user_parameters)
    print(response.text)

def create_graph():
    # ---------------Creating Graph-------------------------------------
    graph_endpoint=f"{USER_ENDPOINT}/{USERNAME}/graphs"
    graph_configuration={
        "id":GRAPH_ID,
        "name":"test_graph",
        "unit":"kilogram",
        "type":"float",
        "color":"shibafu"
    }
    header={
        "X-USER-TOKEN":TOKEN
    }
    response=requests.post(url=graph_endpoint,json=graph_configuration,headers=header)
    print(response.text)

    return header

def post_value(header):
    #---------------------------Posting Value To Graph----------------------------------
    value_endpoint=f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    
    value_configuration={
        "date":today.strftime("%Y%m%d"),
        "quantity":input("How many kg are u?"),
    }
    response=requests.post(url=value_endpoint,json=value_configuration,headers=header)
    print(response.text)

def update_pixel(header):
    #---------------------------Updating Pixel (Value of Graph)-----------------------------------
    update_endpoint=f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_strf}"
    update={
        "quantity":input("How many kilos?Update to?"),
    }
    response=requests.put(url=update_endpoint,json=update,headers=header)
    print(response.text)

def delete_pixel(header):
    #--------------------------Deleting Pixel------------------------------------------------------
    delete_endpoint=f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_strf}"
    response=requests.delete(url=delete_endpoint,headers=header)
    print(response.text)


def main():
    create_user()
    header=create_graph()
    #post_value(header)
    #update_pixel(header)
    delete_pixel(header)

    

  
main()
    
    
    