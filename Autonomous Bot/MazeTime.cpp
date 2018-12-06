#include<iostream>
#include"wiringPi.h"
#include<stdio.h>
#include<stdlib.h>
#include"softPwm.h"
#include<math.h>
#include<signal.h>
#include<unistd.h>

using namespace std;

/*******PINS Left*****
0  * 1 * * * * 6 * * 0 
1  * 1 2 3 4 5 6 7 8 9 current
2  0 * * * * * 6 7 8 9 
3  * 1
*********************/

/*Define*/

#define TRIG_FRONT 30  //27
#define ECHO_FRONT 21  //29
#define TRIG_RIGHT 22  //31
#define ECHO_RIGHT 23  //33
#define TRIG_LEFT  24  //35
#define ECHO_LEFT  25  //37

#define  pwmPinR   0   //3
#define  dirPin_r1 3   //7
#define  dirPin_r2 2   //5	

#define pwmPinL    8   //11
#define dirPin_l1  7   //15
#define dirPin_l2  9   //13

/*GOBAL VARIABLE*/

int pwmVal_Right;

int pwmVal_Left;

int distx=0, disty=0;
int x_bar=1, y_bar=1;
int x = 1 ,y = 1;
int Direction = 0;
int dist = 0;

int TurnTimeLeft = 633000;
int TurnTimeRight = 633000;
float circumference = 6.0 * 22 / 7.0;

void rotateAxis(int sign){
  x_bar = -y*sign;
  y_bar = x*sign;
  x = x_bar;
  y = y_bar;
}

void updateCoOrdinate(int i){
  if((x_bar == 1 && y_bar == -1 )|| (x_bar == -1 && y_bar == 1))
   distx = distx + i*(dist * y_bar);

  else if((x_bar == 1 && y_bar == 1)|| (x_bar == -1 && y_bar == -1))
    disty = disty + i*(dist * x_bar);
}
void safeStop(int a){
  softPwmWrite(pwmPinR,0);
  softPwmWrite(pwmPinL,0);
  usleep(100000);
  softPwmWrite(pwmPinR,0);
  softPwmWrite(pwmPinL,0);
  usleep(100000);
}

int ultrasonicLeft(){

	digitalWrite(TRIG_LEFT, HIGH);
	delayMicroseconds(20);
	digitalWrite(TRIG_LEFT, LOW);


	while(digitalRead(ECHO_LEFT) == LOW);


	long startTime = micros();
	while(digitalRead(ECHO_LEFT) == HIGH);
	long travelTime = micros() - startTime;


	int distance = travelTime * 10 / 58;

	return distance;
}

int ultrasonicFront(){

        digitalWrite(TRIG_FRONT, HIGH);
        delayMicroseconds(20);
        digitalWrite(TRIG_FRONT, LOW);


        while(digitalRead(ECHO_FRONT) == LOW);


        long startTime = micros();
        while(digitalRead(ECHO_FRONT) == HIGH);
        long travelTime = micros() - startTime;


        int distance = travelTime * 10 / 58;

        return distance;
}

int ultrasonicRight(){

        digitalWrite(TRIG_RIGHT, HIGH);
        delayMicroseconds(20);
        digitalWrite(TRIG_RIGHT, LOW);


        while(digitalRead(ECHO_RIGHT) == LOW);


        long startTime = micros();
        while(digitalRead(ECHO_RIGHT) == HIGH);
        long travelTime = micros() - startTime;


        int distance = travelTime   * 10 / 58;

        return distance;
}
void stop(){
	digitalWrite(dirPin_l1,LOW);
	digitalWrite(dirPin_r1,LOW);
	digitalWrite(dirPin_l2,LOW);
	digitalWrite(dirPin_r2,LOW);
	softPwmWrite(pwmPinL,0);
	softPwmWrite(pwmPinR,0);
}

void backward(){
	digitalWrite(dirPin_l1,LOW);
	digitalWrite(dirPin_r1,HIGH);
	digitalWrite(dirPin_l2,HIGH);
	digitalWrite(dirPin_r2,LOW);
	softPwmWrite(pwmPinL,150);
	softPwmWrite(pwmPinR,150);
	usleep(100000);
	dist = 10;
	stop();
	updateCoOrdinate(-1);
}

void forward(){
	digitalWrite(dirPin_l1,HIGH);
	digitalWrite(dirPin_r1,LOW);
	digitalWrite(dirPin_l2,LOW);
	digitalWrite(dirPin_r2,HIGH);
	softPwmWrite(pwmPinL,150);
	softPwmWrite(pwmPinR,150);
	usleep(255000);
	dist = 10;
	stop();
	updateCoOrdinate(1);
}

void rightTurn(){
	digitalWrite(dirPin_l1,LOW);
	digitalWrite(dirPin_r1,LOW);
	digitalWrite(dirPin_l2,HIGH);
	digitalWrite(dirPin_r2,HIGH);
	softPwmWrite(pwmPinL,50);
	softPwmWrite(pwmPinR,50);
	usleep(TurnTimeRight);
	stop();
	usleep(100000);
	rotateAxis(1);
	Direction = (++Direction) % 4;
}

void leftTurn(){
	digitalWrite(dirPin_l1,HIGH);
	digitalWrite(dirPin_r1,HIGH);
	digitalWrite(dirPin_l2,LOW);
	digitalWrite(dirPin_r2,LOW);
	softPwmWrite(pwmPinL,50);
	softPwmWrite(pwmPinR,50);
	usleep(TurnTimeLeft);
	stop();
	usleep(100000);
	rotateAxis(-1);
	Direction = --Direction ;
	if (Direction == -1)
		Direction = 3;
}


void setup(){
	wiringPiSetup();
	pinMode(dirPin_r1, OUTPUT);
	pinMode(dirPin_l1, OUTPUT);
	pinMode(dirPin_r2, OUTPUT);
	pinMode(dirPin_l2, OUTPUT);
	softPwmCreate(pwmPinR, 0, 225);
	softPwmCreate(pwmPinL, 0, 225);
	pinMode(TRIG_FRONT, OUTPUT);
	pinMode(ECHO_FRONT, INPUT);
	pinMode(TRIG_RIGHT, OUTPUT);
	pinMode(ECHO_RIGHT, INPUT);
	pinMode(TRIG_LEFT, OUTPUT);
	pinMode(ECHO_LEFT, INPUT);
	digitalWrite(TRIG_FRONT, LOW);
	digitalWrite(TRIG_LEFT, LOW);
	digitalWrite(TRIG_RIGHT, LOW);
	signal(SIGINT,safeStop);
}

int main(){
	setup();
	rightTurn();
	forward();
	cout<<distx<<" "<<disty;
	return 0;
}

