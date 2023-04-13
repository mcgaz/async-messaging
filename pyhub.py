from . import bsa
import copy
from kafka import KafkaConsumer, KafkaProducer, KafkaAdminClient
import sys

bootstrap = "localhost:9092"

# for i in range(1, len(sys.argv)):
#     if sys.srgv[i] == "local":
#         bootstrap = "localhost:9092"

admin_client = KafkaAdminClient(bootstrap_servers=bootstrap)

consumer = KafkaConsumer(bootstrap_servers=bootstrap,
                            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                            key_deserializer=lambda a: a.decode('utf-8'),
                            auto_commit_interval_ms=1000, enable_auto_commit=True,
                            auto_offset_reset='latest')

producer = KafkaProducer(bootstrap_servers=bootstrap,
                            value_serializer=lambda v: json.dumps(v.decode('utf-8')),
                            key_serializer=lambda v: v.encode('utf-8'))

def main():
    
    for message in consumer:
        
        mess = Message()

        if not health_status():
            if vessel_type() == "ship":
                if major_change_1():
                    update_heartbeat()
                    send_mess()
                    update_sent_mess()
            # if vessel_type() == "jetski":
            #     if major_change_2():
            #         update_heartbeat()
            #         send_mess()
            #         update_sent_mess()
            # if vessel_type() == "tugboat":
            #     if major_change_3():
            #         update_heartbeat()
            #         send_mess()
            #         update_sent_mess()


def send_mess():
    producer.send("mess", mess)
    producer.flush()

def update_heartbeat():
    heartbeat = copy.deepcopy(mess)

def update_sent_mess():
    send_mess = copy.deepcopy(mess)


def health_status():
    if mess.health_status != sent_bsa.health_status
        return True
    else:
        return False
    
def unit_name_type(bsa_sample):
    if bsa_sample.unit_name_type == 1:
        return
    if bsa_sample.unit_name_type == 2:
        return "2"
    if bsa_sample.unit_name_type == 3:
        return 
    
def major_change_ship():
    if course_diff() > 10:
        return True
    if depth_diff() > 5:
        return True
    if distance_diff() > 200:
        return True
    if speed_diff() > 5:
        return True
    else:
        return False
    
# accessor methods within Message class
def course_conversion():
    #integer to degrees
    return

def lat_conversion():
    #integer to degrees
    return

def lon_conversion():
    #integer to degrees
    return
# accessor methods within Message class

def course_diff():
    course_conversion()
    # diff with weird coefficient

def depth_diff():
    # tens to metres
    return

def distance_diff():
    lat_conversion()
    lon_conversion()
    #haversine
    return

def speed_diff():
    #knots to metres or vice versa and diff
    return

if __name__ == "__main__":
    main()