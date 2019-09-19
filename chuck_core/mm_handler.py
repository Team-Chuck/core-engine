# This python file manages various presets of the room, called from MindMeld Voice Commands

from chuck_core import se_handler
from chuck_core.constants import presentation_mode_presets
from chuck_core.constants import normal_mode_presets


def presentation_mode(space_id):
    '''
    This method sets the room to presentation mode
    :param space_id: ID of the space (Meeting room, Office space)
    :return:
    '''

    se_handler.lights_control(space_id, presentation_mode_presets.get('Light Status'))
    se_handler.blinds_control(space_id, presentation_mode_presets.get('Shade'))
    se_handler.projector_control(space_id, presentation_mode_presets.get('Projector'))
    se_handler.room_occupancy_control(space_id, '2')


def normal_mode(space_id):
    '''
    This method sets the room to normal mode
    :param space_id: ID of the space (Meeting room, Office space)
    :return:
    '''

    se_handler.lights_control(space_id, normal_mode_presets.get('Light Status'))
    se_handler.blinds_control(space_id, normal_mode_presets.get('Shade'))
    se_handler.projector_control(space_id, normal_mode_presets.get('Projector'))


def increase_temperature(space_id):
    '''
    This methods increases the temperature by 2 degrees celsius
    :param space_id: ID of the space (Meeting room, Office space)
    :return:
    '''

    current_temperature = se_handler.retrieve_current_thermostat(space_id)

    se_handler.thermostat_control(space_id, str(int(current_temperature) + 2))


def decrease_temperature(space_id):
    '''
    This method decreases the temperature by 2 degrees
    :param space_id: ID of the space (Meeting room, Office space)
    :return:
    '''

    current_temperature = se_handler.retrieve_current_thermostat(space_id)

    se_handler.thermostat_control(space_id, str(int(current_temperature) - 2))


if __name__ == '__main__':

    decrease_temperature('room a')