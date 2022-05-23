import requests
import config
import time
import sys

api_key = config.api_key

filename = input("Enter local file path: ")

def read_file(filename):
    with open(filename, 'rb') as _file:
        while True:
            data=_file.read()
            if not data:
                break
            yield data 


headers = {'authorization': api_key}
try: 
    response = requests.post('https://api.assemblyai.com/v2/upload',
                        headers=headers,
                        data=read_file(filename))
except:
    sys.exit("Could not find file path")

uploaded_url = response.json()['upload_url']
print('Audio file has been uploaded to AssemblyAI')

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

endpoint = f"https://api.assemblyai.com/v2/transcript/{transcriptionID}"
headers = {
    "authorization": api_key,

}
transcriptionResults = requests.get(endpoint, headers=headers)

while transcriptionResults.json()['status'] != 'completed':
  print('Transcription is processing ...')
  transcriptionResults = requests.get(endpoint, headers=headers)
  time.sleep(5)

print('Retrieve transcription results\n')
print('================================\n')
print(transcriptionResults.json()["text"])
print('\n================================\n')
