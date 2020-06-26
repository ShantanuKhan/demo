import yaml 
from yaml import load, load_all

stream = open('sample.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

for doc in documents:
    print("Person ID:", doc['people'][0]['Id'])
    print("First Name:", doc['people'][0]['FirstName'])
    print("Last Name:", doc['people'][0]['LastName'])
    print("City of Action:", doc['people'][0]['Place'])