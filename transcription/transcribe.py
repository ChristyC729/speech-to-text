import requests
import time
audio_url= 'https://cdn.kapwing.com/samples/5c4231d44d02e3ffa24640d6.mp4'
endpoint= f'https://interview.kapwing.com/api/transcription?url={audio_url}'

# 'SAg43dk8PQSGomv2PCyTiN'
response = requests.put(endpoint)

transcriptionJobID=response.json()['jobId']

get_endpoint = f'https://interview.kapwing.com/api/transcription?jobId={transcriptionJobID}'
get_response =requests.get(get_endpoint)

while (get_response.json()['status'] != 'done'):
    time.sleep(5)
    get_response= requests.get(get_endpoint)
    print('Progress: ', get_response.json()['progress'])


transcriptionText = [{"text":"Back here LIVE at the waterfront village","startTime":0,"endTime":2.75},{"text":"with my friend the zombie, Jonathan","startTime":2.75,"endTime":5.21},{"text":"You're looking good! Jonathan just got an awesome face-paint job, what do you think?","startTime":5.21,"endTime":8.78},{"text":"I LIKE TURTLES!!!","startTime":8.78,"endTime":10.18},{"text":"...Alright! You're a great zombie.","startTime":10.18,"endTime":12.9},{"text":"And good times here at the Waterfront Village, open for the next 11 days ....","startTime":12.9,"endTime":17.08}]

index=0
for text in transcriptionText:
    index=index+1
    words=text['text']
    startTime=text['startTime']
    endTime=text['endTime']
    print(index)
    print(startTime, ' --> ', endTime)
    print(words)
    print('')



