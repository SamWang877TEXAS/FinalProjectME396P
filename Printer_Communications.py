import requests
import json
import time




def issue_gcode(ip, com, filename=""):
    # response = requests.post(f"{api_url}/machine/control", json={"command": "M0"})
    base_request = ("http://{0}:{1}/rr_gcode?gcode=" + com).format(ip,"")
    r = requests.get(base_request)
    return r


def request_status(ip):

    base_request = ("http://{0}:{1}/rr_status?type=0").format(ip,"")
    return requests.get(base_request).json()


if __name__ == "__main__":

    ip1 = "192.168.0.17"

    status_P1 = request_status(ip1)
    print(status_P1)
    #
    print('------')

    time.sleep(10) # Seconds to pause
    #
    issue_gcode(ip1, "M24")  # M25 = pause print; M24 = resume print

    status_P1 = request_status(ip1)
    print(status_P1)# = request_status(ip_P2)
    # print('---x---')
    # print(type(status_P1))
    # print('coords:' , status_P1['coords'])
    # print('xyz:' , status_P1['coords']['xyz'])
    # print('z value:' , status_P1['coords']['xyz'][2])
    # status_P1['coords']['xyz']