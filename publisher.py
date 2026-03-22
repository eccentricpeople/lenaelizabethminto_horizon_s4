import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Pub(Node):
    def __init__(self):
        super().__init__('publisher')
        self.pub = self.create_publisher(Int32, '/distance', 10)
        self.timer = self.create_timer(1.0, self.send)
        self.value = 0

    def send(self):
        msg = Int32()
        msg.data = self.value
        self.pub.publish(msg)
        print("Publishing:", msg.data)
        self.value += 1

rclpy.init()
node = Pub()
rclpy.spin(node)
