se_user = 'Admin'
se_pass = 'P@ssword'

thermostat_max = '28'
thermostat_min = '18'

occupancy_status = {
    'available': '0',
    'unoccupied': '1',
    'occupied': '2'
}

# Mapping of room ID from webex to room ID in Schneider electric
# key - room id from webex
# value - room id from SE
room_mapping = {
    'test' : '01/Server 1/Cisco Hackathon/Team 4/Conference Room A/Values',
    '' : '',
    '' : ''
}

presentation_mode_presets = {
    'Light Status': '0',
    'Shade': '0',
    'Projector': '0'
}

normal_mode_presets = {
    'Light Status': '1',
    'Shade': '90',
    'Projector': '100'
}

room_occupied_presets = {
    'Light Status': '1',
    'Temp': '21'
}

room_unoccupied_presets = {
    'Light Status': '0',
    'Temp': '24'
}