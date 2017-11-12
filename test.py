import requests
import time

def get_subway_times(stop, direction_id):
    query = 'predictionsbystop'
    api_key = 'api_key=lT0DPSlA6EuS2ZgwOW5J-w'
    url = 'http://realtime.mbta.com/developer/api/v2/' + query + '?' + api_key + '&' + stop + '&format=json'

    # http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=lT0DPSlA6EuS2ZgwOW5J-w&stop=place-jfk&format=json

    prev_depart_est = 999999999999

    while True:
        r = requests.get(url)
        r_json = r.json()

        if 'mode' in r_json:
            for i, v in enumerate(r_json['mode']):
                if int(v['route_type']) == 1:
                    mode_index = i

            stop_name = (r_json['stop_name'])
            route_name = r_json['mode'][mode_index]['route'][0]['direction'][direction_id]['trip'][0]['trip_headsign']

            cur_time = int(time.time())
            # print cur_time
            next_dep_time = int(r_json['mode'][mode_index]['route'][0]['direction'][direction_id]['trip'][0]['pre_dt'])
            # print next_dep_time

            if next_dep_time - cur_time < 60:
                print stop_name +': '+ 'Next Departure towards ' + route_name + ' is arriving.'
            else:
                next_dep_est = (next_dep_time - int(time.time())) / 60
                if next_dep_est > prev_depart_est:
                    print stop_name +': '+ 'Next Departure towards ' + route_name + ' now in ' + str(next_dep_est) + ' minutes.'
                    prev_depart_est = next_dep_est
                else:
                    print stop_name +': '+ 'Next Departure towards ' + route_name + ' in ' + str(next_dep_est) + ' minutes.'
                    prev_depart_est = next_dep_est

            print 'Current Time: ' + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        
        elif 'alert_headers' in r_json:
            alert = r_json['alert_headers'][0]['header_text']
            print alert


        time.sleep(30)

get_subway_times("stop=place-jfk", 0)