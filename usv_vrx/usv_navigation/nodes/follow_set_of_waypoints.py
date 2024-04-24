#!/usr/bin/env python
# Ensure this shebang line matches your environment

import rospy
from usv_msg.msg import WaypointRoute, Waypoint
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import String

def publish_waypoints():
    rospy.init_node('waypoint_route_publisher', anonymous=True)

    pub = rospy.Publisher('/waypoints_cmd', WaypointRoute, queue_size=10)
    end_pub = rospy.Publisher('/course_ended', String, queue_size=10)
    rospy.sleep(1)  # Give ROS time to establish the connection to subscribers

    # Define the WaypointRoute message
    route = WaypointRoute()
    route.speed = 5.0  # Specify the desired speed

    # Populate the route with multiple Waypoints
     # all turn right
     #	{'x': 121.16, 'y': 88.299},
     #	{'x': 106.16, 'y': 114.203},
     #	{'x': 139.66, 'y': 137.997},
     #	{'x': 156.82, 'y': 106.800},
     
     # all turn left
      #  {'x': 121.16, 'y': 88.299},
      #  {'x': 133.69, 'y': 62.592},
      #  {'x': 170.01, 'y': 80.592},
      #  {'x': 156.8, 'y': 110.128},
    
    waypoints = [
    	{'x': 139.66, 'y': 137.997}, 
    	{'x': 156.82, 'y': 106.800}, 
    	{'x': 170.01, 'y': 80.592}, 
    	{'x': 156.82, 'y': 106.800},
    	{'x': 106.16, 'y': 114.203}, 
    	{'x': 121.16, 'y': 88.299},
    	{'x': 133.69, 'y': 62.592},
    	{'x': 121.16, 'y': 88.299},
     	{'x': 156.82, 'y': 106.800},
    
     
        # Add more waypoints as needed
    ]

    for wp_info in waypoints:
        wp = Waypoint()
        # Correctly assign position to the Point message
        wp.pose.position = Point(x=wp_info['x'], y=wp_info['y'])
        # Correctly assign orientation to the Quaternion message
        #wp.pose.orientation = Quaternion(*wp_info['orientation'])
        wp.nav_type = Waypoint.NAV_WAYPOINT  # Adjust based on your use case
        wp.station_duration = 0.5  # Specify how long to wait at the waypoint
        route.waypoints.append(wp)


    pub.publish(route)
    rospy.loginfo("Published WaypointRoute with %d waypoints." % len(route.waypoints))
    
    rospy.sleep(1)  # Small delay to ensure message order
    end_pub.publish("Course has ended")
    rospy.loginfo("Course completion message sent.")

if __name__ == '__main__':
    try:
        publish_waypoints()
    except rospy.ROSInterruptException:
        pass

