#!/usr/bin/env python3
# # ROS imports
import rospy
from std_msgs.msg import uint8
import time 
from smbus2 import SMBus



topic_sistema_extraccion_b = '/robocol/interfaz/brazo/sistema_extraccion_b'  #creacion topico

# def mandar_i2c(data):

#     with SMBus(1) as bus:
#         address = 0x24  #direccion arduino
#         bus.write_byte(address, data)
#         time.sleep(0.2)
        
#         var = bus.read_byte(0x25)
#         print(var)
              

def callback(data):
    print("Mensaje recibido del topico del sistema de extraccion B")
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # await self.send(text_data=json.dumps({'id': 'sistema_extraccion_b', "orden": param.data}))
    #mandar_i2c(data)
    
    
    
def listener():

    rospy.init_node("nodo_sistema_extraccion_b")
    rospy.Subscriber(topic_sistema_extraccion_b, uint8, callback) #topico, tipo de dato, correr funcion
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


    
if __name__ == '__main__':
	try:
            listener()
	except rospy.ROSInterruptException:
		print('Nodo detenido')

#
