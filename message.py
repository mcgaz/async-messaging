import json
import operator

class Message():
    def __init__(self,
                 message_type,
                 craft_id,
                 craft_type,
                 time,
                 latitude,
                 longitude,
                 altitude,
                 course,
                 speed,
                 camera_status,
                 ):
        
        self.message_type = message_type
        self.vessel_id = vessel_id
        self.vessel_type = vessel_type
        self.time = time
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.course = course
        self.speed = speed
        self.camera_status = camera_status

    message_type = property(operator.attrgetter('_message_type'))

    vessel_id
    vessel_type
    time
    latitude
    longitude
    altitude
    course
    speed
    camera_status