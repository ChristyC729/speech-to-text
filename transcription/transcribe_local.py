import requests
import config
import time

api_key = config.api_key

filename = "./media/Research.mp3"
""" def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
 """
def read_file(filename):
    with open(filename, 'rb') as _file:
        while True:
            data=_file.read()
            if not data:
                break
            yield data 

headers = {'authorization': api_key}
response = requests.post('https://api.assemblyai.com/v2/upload',
                        headers=headers,
                        data=read_file(filename))

#print(response.json())
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

print('Retrieve transcription results')

print(transcriptionResults.json()["text"])
