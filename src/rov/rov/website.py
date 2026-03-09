import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2
from flask import Flask, Response


app = Flask(__name__)

frame = None


class Website(Node):

    def __init__(self):

        super().__init__('website')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            Image,
            '/mavros/camera/image',
            self.callback,
            10
        )

        self.get_logger().info("Website node started")


    def callback(self, msg):

        global frame

        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')


def generate():

    global frame

    while True:

        if frame is not None:

            ret, jpeg = cv2.imencode('.jpg', frame)

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')


@app.route('/video')

def video():

    return Response(
        generate(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


def main(args=None):

    rclpy.init(args=args)

    node = Website()

    import threading

    thread = threading.Thread(
        target=rclpy.spin,
        args=(node,),
        daemon=True
    )

    thread.start()

    app.run(host='0.0.0.0', port=5000)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()