import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class Sensor(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.pub = self.create_publisher(Int32, '/distance', 10)
        self.timer = self.create_timer(1.0, self.publish_distance)

    def publish_distance(self):
        msg = Int32()
        msg.data = random.randint(0, 100)
        self.pub.publish(msg)
        print("Distance published:", msg.data)

rclpy.init()
node = Sensor()
rclpy.spin(node)
