#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import String

def bin_node():
    rospy.init_node("bin_node_1", anonymous=True)

    pub = rospy.Publisher("/bin1/data", String, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        weight = random.randint(10, 120)
        temperature = random.randint(20, 70)

        status = "NORMAL"

        if weight > 100:
            status = "FULL"

        if temperature > 50:
            status = "FIRE_RISK"

        data = f"BIN_ID:1 | Weight:{weight}kg | Temp:{temperature}C | Status:{status}"

        rospy.loginfo(data)
        pub.publish(data)

        rate.sleep()

if __name__ == "__main__":
    try:
        bin_node()
    except rospy.ROSInterruptException:
        pass
