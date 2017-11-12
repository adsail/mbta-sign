import requests
import time

query = 'predictionsbystop'
stop = 'stop=place-sbmnl'                      
api_key = 'api_key=lT0DPSlA6EuS2ZgwOW5J-w'
url = 'http://realtime.mbta.com/developer/api/v2/' + query + '?' + api_key + '&' + stop + '&format=json'
direction_id = 1
# http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=lT0DPSlA6EuS2ZgwOW5J-w&stop=place-sbmnl&format=json

while True:
    r = requests.get(url)
    r_json = r.json()

    next_dep_time = int(r_json['mode'][0]['route'][0]['direction'][direction_id]['trip'][0]['pre_dt'])
    next_dep_est = (next_dep_time - int(time.time())) / 60
    stop_name = (r_json['stop_name'])
    route_name = r_json['mode'][0]['route'][0]['direction'][direction_id]['trip'][0]['trip_headsign']


    print 'Current Time: ' + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    print stop_name +': '+ 'Next Departure towards ' + route_name + ' in ' + str(next_dep_est) + ' minutes.'

    time.sleep(55)  #Repeat every 55 seconds