
import requests
p={
    "amount":10,
    "type":"boolean",
}


response=requests.get(url="https://opentdb.com/api.php",params=p)
response.raise_for_status()
data=response.json()
question_data=data["results"]
print(question_data)