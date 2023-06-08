#!/usr/bin/env python3

import rospy
import roslib
from sensor_msgs.msg import PointCloud2


rospy.init_node("tf_restamper")
tfpublisher = rospy.Publisher("/andrew/camera/depth/color/points", PointCloud2)

def tfcallback(msg):
    msg_restamped = msg
    msg_restamped.header.stamp = rospy.Time.now()
    tfpublisher.publish(msg_restamped)

tfproxy = rospy.Subscriber("/camera/depth/color/points", PointCloud2, tfcallback)
rospy.spin()
