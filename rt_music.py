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
drum_id0 = drum_result[0]['_id']
drum_id1 = drum_result[1]['_id']
drum_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(drum_id0)
drum_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(drum_id1)
drum_req0 = Request(drum_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
drum_resp0 = urlopen(req)
drum_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
drum_req1 = Request(drum_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
drum_resp1 = urlopen(req)
drum_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

loop1 = urlopen(loop1_url).read()
loop1_result = json.loads(loop1.decode('utf-8'))
loop1_id0 = loop1_result[0]['_id']
loop1_id1 = loop1_result[1]['_id']
loop1_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(loop1_id0)
loop1_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(loop1_id1)
loop1_req0 = Request(loop1_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
loop1_resp0 = urlopen(req)
loop1_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
loop1_req1 = Request(loop1_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
loop1_resp1 = urlopen(req)
loop1_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

loop2 = urlopen(loop2_url).read()
loop2_result = json.loads(loop2.decode('utf-8'))
loop2_id0 = loop2_result[0]['_id']
loop2_id1 = loop2_result[1]['_id']
loop2_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(loop2_id0)
loop2_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(loop2_id1)
loop2_req0 = Request(loop2_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
loop2_resp0 = urlopen(req)
loop2_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
loop2_req1 = Request(loop2_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
loop2_resp1 = urlopen(req)
loop2_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

loop3 = urlopen(loop3_url).read()
loop3_result = json.loads(loop3.decode('utf-8'))
loop3_id0 = loop3_result[0]['_id']
loop3_id1 = loop3_result[1]['_id']
loop3_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(loop3_id0)
loop3_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(loop3_id1)
loop3_req0 = Request(loop3_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
loop3_resp0 = urlopen(req)
loop3_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
loop3_req1 = Request(loop3_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
loop3_resp1 = urlopen(req)
loop3_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

one_shot1 = urlopen(one_shot1_url).read()
one_shot1_result = json.loads(one_shot1.decode('utf-8'))
one_shot1_id0 = one_shot1_result[0]['_id']
one_shot1_id1 = one_shot1_result[1]['_id']
one_shot1_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(one_shot1_id0)
one_shot1_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(one_shot1_id1)
one_shot1_req0 = Request(one_shot1_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
one_shot1_resp0 = urlopen(req)
one_shot1_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
one_shot1_req1 = Request(one_shot1_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
one_shot1_resp1 = urlopen(req)
one_shot1_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

one_shot2 = urlopen(one_shot2_url).read()
one_shot2_result = json.loads(one_shot2.decode('utf-8'))
one_shot2_id0 = one_shot2_result[0]['_id']
one_shot2_id1 = one_shot2_result[1]['_id']
one_shot2_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(one_shot2_id0)
one_shot2_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(one_shot2_id1)
one_shot2_req0 = Request(one_shot2_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
one_shot2_resp0 = urlopen(req)
one_shot2_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
one_shot2_req1 = Request(one_shot2_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
one_shot2_resp1 = urlopen(req)
one_shot2_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

one_shot3 = urlopen(one_shot3_url).read()
one_shot3_result = json.loads(one_shot3.decode('utf-8'))
one_shot3_id0 = one_shot3_result[0]['_id']
one_shot3_id1 = one_shot3_result[1]['_id']
one_shot3_request0 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(one_shot3_id0)
one_shot3_request1 = "https://hackathon.indabamusic.com/samples/{}/download?indaba_uuid=68a4d4da-6e25-11e5-99ff-0e52404cc67c".format(one_shot3_id1)
one_shot3_req0 = Request(one_shot3_request0, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
one_shot3_resp0 = urlopen(req)
one_shot3_dl_link0 = json.loads(resp.read().decode('utf-8'))['download_url']
one_shot3_req1 = Request(one_shot3_request1, headers={'Authorization': base64.b64encode(str.encode("ab68rlMaeCOGKVCA0sqTE0EdxC4IyFjbSCZjic9K:{}".format(int(time.time()*1000)))).decode("ascii")})
one_shot3_resp1 = urlopen(req)
one_shot3_dl_link1 = json.loads(resp.read().decode('utf-8'))['download_url']

