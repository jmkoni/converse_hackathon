import json
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
import time
import base64

url = urlopen('http://hackathon.indabamusic.com/samples?filters_only=true').read()
result = json.loads(url.decode('utf-8'))

types = result['type']
types = [var for var in types if (var and var != None and var != '' and var != 'None')]

instruments = result['instruments']
instruments = [var for var in instruments if (var and var != None and var != '' and var != 'None')]

genres = result['genres']
genres = [var for var in genres if (var and var != None and var != '' and var != 'None')]

musical_key = result['musical_key']
musical_key = [var for var in musical_key if (var and var != None and var != '' and var != 'None')]

tempo_range = result['tempo']
tempo_range = [var for var in tempo_range if (var and var != None and var != '' and var != 'None')]

# user input
print("Below is a list of musical keys that you can choose: ")
print(", ".join(musical_key))
musical_key_input = quote_plus(input("Enter a musical key from the list above: "))
print('\r')
print("Below is a list of genres that you can choose: ")
print(", ".join(genres))
genre_input = quote_plus(input("Enter a genre from the list above: "))
print('\r')
print("Below is a list of instrument types that you can choose: ")
print(", ".join(instruments))
print("Please choose your instruments.")
instrument_input1 = quote_plus(input("Instrument 1: "))
instrument_input2 = quote_plus(input("Instrument 2: "))
instrument_input3 = quote_plus(input("Instrument 3: "))
# 1) one backing drum loop
drum_url = "http://hackathon.indabamusic.com/samples?instruments=Drums&type=loop&genres={}&per_page=1".format(genre_input)

# 2) 3 instruments with 2 loops per instrument
loop1_url = "http://hackathon.indabamusic.com/samples?instruments={}&type=loop&musical_key={}&genres={}&per_page=2".format(instrument_input1, musical_key_input, genre_input)
loop2_url = "http://hackathon.indabamusic.com/samples?instruments={}&type=loop&musical_key={}&genres={}&per_page=2".format(instrument_input, musical_key_input2, genre_input)
loop3_url = "http://hackathon.indabamusic.com/samples?instruments={}&type=loop&musical_key={}&genres={}&per_page=2".format(instrument_input, musical_key_input3, genre_input)

# 3) 3 instruments with 2 one_shots per instrument
one_shot1_url = "http://hackathon.indabamusic.com/samples?instruments={}&type=one_shot&musical_key={}&genres={}&per_page=2".format(instrument_input1, musical_key_input, genre_input)
one_shot2_url = "http://hackathon.indabamusic.com/samples?instruments={}&type=one_shot&musical_key={}&genres={}&per_page=2".format(instrument_input2, musical_key_input, genre_input)
one_shot3_url = "http://hackathon.indabamusic.com/samples?instruments={}&type=one_shot&musical_key={}&genres={}&per_page=2".format(instrument_input3, musical_key_input, genre_input)

# get the drums
drum = urlopen(drum_url).read()
drum_result = json.loads(drum.decode('utf-8'))
drum_id = drum_result[0]['_id']
drum_request = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(drum_id)

drum_req = Request(drum_request, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
drum_resp = urlopen(req)
drum_dl_link = json.loads(resp.read().decode('utf-8'))['download_url']

loop1 = urlopen(loop1_url).read()
loop1_result = json.loads(loop1.decode('utf-8'))

loop2 = urlopen(loop2_url).read()
loop2_result = json.loads(loop2.decode('utf-8'))

loop3 = urlopen(loop3_url).read()
loop3_result = json.loads(loop3.decode('utf-8'))

one_shot1 = urlopen(one_shot1_url).read()
one_shot1_result = json.loads(one_shot1.decode('utf-8'))

one_shot2 = urlopen(one_shot2_url).read()
one_shot2_result = json.loads(one_shot2.decode('utf-8'))

one_shot3 = urlopen(one_shot3_url).read()
one_shot3_result = json.loads(one_shot3.decode('utf-8'))

