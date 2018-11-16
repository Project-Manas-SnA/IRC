
/******************
* Name: Encoder.cpp
* Description: Calculate velocity and ticks
********************/
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<ros.h>
#include<interfacing/Velocity.h>
#include <unistd.h>

using namespace std;

/*GOBAL VARIABLE*/

ros::NodeHandle  nh;



char *rosSrvrIp = "192.168.43.233";

interfacing::Velocity data;

ros::Publisher Feedback("Feedback", &data);

int setVel_Left;
int setVel_Right;

void callback(const interfacing::Velocity &msg)
  {
  	setVel_Left = msg.leftwheel;
		setVel_Right =  msg.rightwheel;
  }

ros::Subscriber<interfacing::Velocity> sub("Velocity", callback );


int main(){


	nh.initNode(rosSrvrIp);
	nh.subscribe(sub);
	nh.advertise(Feedback);

	while(1)
		{
        usleep(10000);
				data.leftwheel = setVel_Left;
				data.rightwheel = setVel_Right;
				Feedback.publish(&data);

				nh.spinOnce();

		}
		return 0;
}
