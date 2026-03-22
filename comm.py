import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('command_listener')

        self.sub = self.create_subscription(
            String,
            '/rover_command',
            self.callback,
            10
        )

    def callback(self, msg):
        print(f"Received command: {msg.data}")
        if msg.data == "MOVE_FORWARD":
            print("Rover wheels moving")
        elif msg.data == "STOP":
            print("Rover stopped")

rclpy.init()
node = Listener()
rclpy.spin(node)
