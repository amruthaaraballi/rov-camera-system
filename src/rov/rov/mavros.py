import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image


class MAVROS(Node):

    def __init__(self):

        super().__init__('mavros')

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            Image,
            '/mavros/camera/image',
            10
        )

        self.get_logger().info("MAVROS bridge started")


    def callback(self, msg):

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = MAVROS()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()