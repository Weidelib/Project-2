from phue import Bridge
from ip_address import bridge_ip_address
import time

def access_lights(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_names_list = b.get_light_objects('name')
    return light_names_list

def film_lights():
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = False

if __name__ == '__main__':
    film_lights()