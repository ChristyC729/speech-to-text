import requests

f = open("api.txt", "r")
api_key = f.read()

uploaded_url = "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"

endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": uploaded_url
}
headers = {
    "authorization":api_key,
    "content-type": "application/json"
}
response1 = requests.post(endpoint, json=json, headers=headers)
print('Transcribing uploaded file')

transcriptionID=response1.json()["id"]
print('Extract transcript ID')

import requests
endpoint = f"https://api.assemblyai.com/v2/transcript/{transcriptionID}"
headers = {
    "authorization": api_key,

}
transcriptionResults = requests.get(endpoint, headers=headers)

while transcriptionResults.json()['status'] != 'completed':
  print('Transcription is processing ...')
  transcriptionResults = requests.get(endpoint, headers=headers)

print('Retrieve transcription results')

print(transcriptionResults.json()["text"])
