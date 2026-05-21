#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker

last_data = "Bekleniyor..."
last_status = "NORMAL"

def callback(msg):
    global last_data, last_status

    last_data = msg.data

    if "FIRE_RISK" in msg.data:
        last_status = "FIRE_RISK"
    elif "FULL" in msg.data:
        last_status = "FULL"
    else:
        last_status = "NORMAL"

def rviz_node():
    rospy.init_node("rviz_bin_marker_node")

    rospy.Subscriber("/bin1/data", String, callback)
    pub = rospy.Publisher("/visualization_marker", Marker, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "smart_bin"
        marker.id = 1
        marker.type = Marker.CUBE
        marker.action = Marker.ADD

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0.5

        marker.pose.orientation.w = 1.0

        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0

        if last_status == "NORMAL":
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
        elif last_status == "FULL":
            marker.color.r = 1.0
            marker.color.g = 1.0
            marker.color.b = 0.0
        else:
            marker.color.r = 1.0
            marker.color.g = 0.0
            marker.color.b = 0.0

        marker.color.a = 1.0

        pub.publish(marker)

        text_marker = Marker()
        text_marker.header.frame_id = "map"
        text_marker.header.stamp = rospy.Time.now()
        text_marker.ns = "smart_bin_text"
        text_marker.id = 2
        text_marker.type = Marker.TEXT_VIEW_FACING
        text_marker.action = Marker.ADD

        text_marker.pose.position.x = 0
        text_marker.pose.position.y = 0
        text_marker.pose.position.z = 1.4

        text_marker.pose.orientation.w = 1.0

        text_marker.scale.z = 0.25
        text_marker.color.r = 1.0
        text_marker.color.g = 1.0
        text_marker.color.b = 1.0
        text_marker.color.a = 1.0

        text_marker.text = last_data

        pub.publish(text_marker)

        rate.sleep()

if __name__ == "__main__":
    try:
        rviz_node()
    except rospy.ROSInterruptException:
        pass
