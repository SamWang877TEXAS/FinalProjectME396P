import requests
import json
import time


ip1 = "192.168.0.187"

def issue_gcode(ip, com='', filename=""):
    # response = requests.post(f"{api_url}/machine/control", json={"command": "M0"})
    base_request = ("http://{0}:{1}/rr_gcode?gcode=" + com).format(ip,"")
    lol = 'http://192.168.0.187/api/v1/auth/verify'
    r = requests.get(lol)
    return r


def request_z_position(ip):

    # ef='http://192.168.0.187/api/v1/printer/status'
    # ef = 'http://192.168.0.187/api/v1/printer/heads/0/position'
    base_request = ("http://{0}:{1}/api/v1/printer/heads/0/position").format(ip,"")
    return requests.get(base_request).json()['z']

def request_printing_status(ip):

    # ef='http://192.168.0.187/api/v1/printer/status'
    ef = 'http://192.168.0.187/api/v1/printer/heads/0/position'
    base_request = ("http://{0}:{1}/api/v1/printer/status").format(ip,"")


    return requests.get(base_request).json() == 'printing'


if __name__ == "__main__":

    print(request_printing_status(ip1))
    print(request_z_position(ip1))
    print(issue_gcode(ip1))
    # status_P1 = request_status(ip1)
    # print(type(status_P1))
    # print(status_P1)
    # print(status_P1[0]['extruders'][0])
    # print((status_P1[0]['extruders'][0]['hotend']))
    # print('------')

    #
    #
    # time.sleep(10)
    #
    # issue_gcode(ip1, "M24")
    #
    # status_P1 = request_status(ip1)
    # print(status_P1)# = request_status(ip_P2)
