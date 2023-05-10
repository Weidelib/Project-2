from phue import Bridge
import time

def alert_lights():
    # Connect to the Hue bridge
    b = Bridge('10.186.1.137')

    # Get the IDs of the four light bulbs you want to blink
    light_ids = [1, 2, 3, 4]

    # Save the current state of the lights
    initial_states = {}
    for light_id in light_ids:
        initial_states[light_id] = b.get_light(light_id)

    # Blink the lights
    for i in range(25):  # Blink the lights three times
        for light_id in light_ids:
            b.set_light(light_id, 'alert', 'select')
        time.sleep(0.5)  # Wait for one second
        for light_id in light_ids:
            b.set_light(light_id, initial_states[light_id]['state'])
        time.sleep(0.5)  # Wait for one second

if __name__ == '__main__':
    alert_lights()