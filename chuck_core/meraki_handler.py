# This python file manages room presets depending on the room occupancy. Called from Meraki Controller

from chuck_core import se_handler
from chuck_core.constants import room_occupied_presets
from chuck_core.constants import room_unoccupied_presets


def room_occupancy_control(space_id, occupied=False):
    '''
    This methods controls room presets based on occupancy
    :param space_id: ID of the space (Meeting room, Office space)
    :param occupancy: Boolean (True - Occupied, False - Unoccupied)
    :return:
    '''

    if occupied:
        se_handler.lights_control(space_id, room_occupied_presets.get('Light Status'))
        se_handler.thermostat_control(space_id, room_occupied_presets.get('Temp'))
        se_handler.room_occupancy_control(space_id, '2')
    else:
        se_handler.lights_control(space_id, room_unoccupied_presets.get('Light Status'))
        se_handler.thermostat_control(space_id, room_unoccupied_presets.get('Temp'))
        se_handler.room_occupancy_control(space_id, '0')