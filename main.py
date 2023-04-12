from dotenv import load_dotenv
import requests
import os

load_dotenv()

headers = {
	"Private-Token": os.getenv("SOURCE_TOKEN")
}
url = os.path.expandvars("$SOURCE_URL/api/v4/projects/$SOURCE_PROJECT_ID/variables")

response = requests.get(url, headers=headers)
data = response.json()
for id in data:
	headers = {
		"Private-Token": os.getenv("TARGET_TOKEN")
	}
	url = os.path.expandvars("$TARGET_URL/api/v4/projects/$TARGET_PROJECT_ID/variables")
	response = requests.post(url, headers=headers, json=id)
	print(response.content)
