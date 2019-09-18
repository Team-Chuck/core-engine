from ewsrestgatewayclient.ebo import EBO
from chuck_core.constants import se_user
from chuck_core.constants import se_pass
from chuck_core.constants import room_mapping
import urllib.parse

# This python file contains all methods to call Schnieder Electric Connector Methods
# These methods will be called from MindMeld Connector and Meraki Connector to
# control meeting rooms and office space resources


def lights_control(space_id, value):
    '''
    Call this method to control the lights of the given space id
    :param space_id: ID of the space (Meeting room, Office space)
    :param value: Dimmer control of lights from 0 to 100 (O - OFF, 100 - ON)
    :return:
    '''

    se_client = EBO()
    token =se_client.token.get_token(se_user, se_pass)

    #get the room ID of SE
    se_id = room_mapping.get(space_id)+'/Intensity'

    result =se_client.values.update_value(urllib.parse.quote(se_id, safe=''),
                                          new_value=value,
                                          custom_headers={'Authorization':'Bearer ' + token.access_token})


def thermostat_control(space_id, value):
    '''
    Call this method to control thermostat of the given space id
    :param space_id: ID of the space (Meeting room, Office space)
    :param value: Thermostat value
    :return:
    '''
    pass


def blinds_control(space_id, value):
    '''
    Call this method to control blinds of the given space id
    :param space_id: ID of the space (Meeting room, Office space)
    :param value: 0 to 100 (0 - Blinds OFF, 100 - Blinds ON)
    :return:
    '''
    pass


if __name__ == '__main__':

    # This is to test
    lights_control('test', '51')