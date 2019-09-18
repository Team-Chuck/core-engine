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
    se_handler.room_occupancy_control(space_id, presentation_mode_presets.get('Projector'))


def normal_mode(space_id):
    '''
    This method sets the room to normal mode
    :param space_id: ID of the space (Meeting room, Office space)
    :return:
    '''

    se_handler.lights_control(space_id, normal_mode_presets.get('Light Status'))
    se_handler.blinds_control(space_id, normal_mode_presets.get('Shade'))
    se_handler.room_occupancy_control(space_id, normal_mode_presets.get('Projector'))


if __name__ == '__main__':

    normal_mode('test')