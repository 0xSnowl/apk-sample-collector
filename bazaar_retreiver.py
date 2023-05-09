import requests
import json

data = {
    'query': 'get_file_type',
    'file_type': 'apk',
    'limit': '100'
}

list_response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data)
list_response_json = json.loads(list_response.text)

sample_count = 1
for sample in list_response_json['data']:
    data = {
        'query': 'get_file',
        'sha256_hash': sample['sha256_hash']
    }

    response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data)
    with open(f'zipped/sample{sample_count:03d}.zip', 'wb') as f:
        f.write(response.content)
    sample_count += 1