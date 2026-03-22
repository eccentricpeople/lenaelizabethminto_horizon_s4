import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class Decision(Node):
    def __init__(self):
        super().__init__('decision_node')

        self.sub = self.create_subscription(
            Int32,
            '/distance',
            self.callback,
            10
        )

        self.pub = self.create_publisher(String, '/rover_command', 10)

    def callback(self, msg):
        distance = msg.data

        if distance < 30:
            command = "STOP"
        else:
            command = "MOVE_FORWARD"

        cmd_msg = String()
        cmd_msg.data = command

        self.pub.publish(cmd_msg)

        print(f"Distance received: {distance}")
        print(f"Command published: {command}")

rclpy.init()
node = Decision()
rclpy.spin(node)
