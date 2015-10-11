import json
from urllib.request import urlopen, Request, urlretrieve
from urllib.parse import quote_plus
import time
import base64
import os, shutil
from random import randint

def create_folders():
  # create/clear out folders
  folders = ['./drums', './inst1', './inst2', './inst3']
  for folder in folders:
    if not os.path.exists(folder):
      os.makedirs(folder)
    else:
      for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
          os.unlink(file_path)

def get_filters():
  # get and then display available filters
  url = urlopen('http://hackathon.indabamusic.com/samples?filters_only=true').read()
  result = json.loads(url.decode('utf-8'))

  filters = {'genre': limit_results(result['genres']), 'instrument': limit_results(result['instruments'])}

  input_needs = [('genre', 1), ('instrument', 3)]
  user_inputs = []
  for k,v in input_needs:
    print("Below is a list of {}s that you can choose: ".format(k))
    print(", ".join(filters[k]))
    print("Please choose.")
    for i in range(v):
      user_inputs.append(quote(i+1, k))
  return user_inputs

def quote(n, k):
  return quote_plus(input("{} {}: ".format(k.title(), n)))

def limit_results(arr):
  return [var for var in arr if (var and var != None and var != '' and var != 'None')]

def get_urls(inputs):
  num_types = {'drum': 1, 'loop': 3, 'one_shot': 3}
  urls = {'drum': [], 'loop': [], 'one_shot': []}

  for k,v in num_types.items():
    if k == 'drum':
      urls[k].append("http://hackathon.indabamusic.com/samples?instruments=Drums&type=loop&genres={}&per_page=50".format(inputs[0]))
    else:
      for i in range(v):
        url = "http://hackathon.indabamusic.com/samples?instruments={}&type={}&genres={}&per_page=50".format(inputs[i+1], k, inputs[0])
        urls[k].append(url)
  return urls

def get_samples(urls):
  for k,v in urls.items():
    for i, url in enumerate(v):
      response = urlopen(url).read()
      result = json.loads(response.decode('utf-8'))
      if k == 'drum':
        sample_id = result[randint(0, len(result) - 1)]['_id']
        retrieve_sample(sample_id, i, 1, k)
      else:
        random_num = randint(0, len(result) - 2)
        sample_id = result[random_num]['_id']
        retrieve_sample(sample_id, i, 1, k)
        sample_id2 = result[random_num + 1]['_id']
        retrieve_sample(sample_id2, i, 2, k)

def retrieve_sample(sample_id, i, num, k):
  dl_request_url = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(sample_id)
  dl_req = Request(dl_request_url, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
  dl_resp = urlopen(dl_req)
  dl_url = json.loads(dl_resp.read().decode('utf-8'))['download_url']
  if k == 'drum':
    folder_name = "drums"
  else:
    folder_name = "inst{}".format(str(i + 1))
  file_name = k + str(num)
  urlretrieve(dl_url, "./{}/{}.wav".format(folder_name, file_name))

def main():
  create_folders()
  inputs = get_filters()
  urls = get_urls(inputs)
  get_samples(urls)

main()