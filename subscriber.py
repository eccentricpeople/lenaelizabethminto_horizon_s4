import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Sub(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.sub = self.create_subscription(
            Int32,
            '/distance',
            self.callback,
            10
        )

    def callback(self, msg):
        print("Received distance:", msg.data)

rclpy.init()
node = Sub()
rclpy.spin(node)
