import requests
import config
import time
import sys

api_key = config.api_key
uploaded_url = input("Enter file url: ")

post_endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": uploaded_url
}
headers = {
    "authorization":api_key,
    "content-type": "application/json"
}
post_response = requests.post(post_endpoint, json=json, headers=headers)
print('\nTranscribing uploaded file')


try:
    transcriptionID=post_response.json()["id"]
    print('Extract transcript ID')
except:
    sys.exit("Could not find url")

get_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcriptionID}"
headers = {
    "authorization": api_key,
}
transcriptionResults = requests.get(get_endpoint, headers=headers)

while transcriptionResults.json()['status'] != 'completed':
  print('Transcription is processing ...')
  transcriptionResults = requests.get(get_endpoint, headers=headers)
  time.sleep(5)


print('Retrieve transcription results\n')
print('================================\n')
print(transcriptionResults.json()["text"])
print('\n================================\n')