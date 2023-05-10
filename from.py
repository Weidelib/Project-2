from phue import Bridge
from ip_address import bridge_ip_address

def set_lights():
    # Connect to the Hue bridge
    b = Bridge(bridge_ip_address)

    # Turn on the four lights and set their brightness to full brightness
    for i in range(1, 5):
        b.set_light(i, 'on', True)
        b.set_light(i, 'bri', 247)
        b.set_light(i, 'ct', 200)

if __name__ == '__main__':
    set_lights()