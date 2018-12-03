
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
1  * 1 2 3 4 5 6 7 8 9 
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

#define  A_Left    4   //16
#define  B_Left    5   //18

#define  A_Right   1  //12
#define  B_Right   16  //10

#define  pwmPinR   0   //3
#define  dirPin_r1 3   //7
#define  dirPin_r2 2   //5	

#define pwmPinL    8   //11
#define dirPin_l1  7   //15
#define dirPin_l2  9   //13

/*GOBAL VARIABLE*/

bool AState_Right,BState_Right;
int pos_r = 0;
int pwmVal_Right;

bool AState_Left,BState_Left;
int pos_l = 0;
int pwmVal_Left;


void Enc_A_Right(){
	AState_Right = digitalRead(A_Right);
	BState_Right = digitalRead(B_Right);

	if(AState_Right==true)
		pos_r+=(BState_Right==LOW)?(1):(-1);

	else
		pos_r+=(BState_Right==HIGH)?(1):(-1);

}

void Enc_B_Right(){
	AState_Right = digitalRead(A_Right);
	BState_Right = digitalRead(B_Right);

	if(BState_Right==true)
		pos_r+=(AState_Right==HIGH)?(1):(-1);
	else
		pos_r+=(AState_Right==LOW)?(1):(-1);
}

void Enc_A_Left(){
	AState_Left = digitalRead(A_Left);
	BState_Left = digitalRead(B_Left);


	if(AState_Left==true)
		pos_l+=(BState_Left==LOW)?(1):(-1);
	else
		pos_l+=(BState_Left==HIGH)?(1):(-1);

}

void Enc_B_Left(){
	AState_Left = digitalRead(A_Left);
	BState_Left = digitalRead(B_Left);

	if(BState_Left==true)
		pos_l+=(AState_Left==HIGH)?(1):(-1);
	else
		pos_l+=(AState_Left==LOW)?(1):(-1);

}

float leftDistance(){
	float l = 3.142 * 60.0 * ( pos_l / 2000.0 ); //distance travelled in mm
	pos_l = 0;
	return l;
}

float rightDistance(){
	float r = 3.142 * 60.0 * ( pos_r / 2000.0 );	//distance travelled in mm
	pos_l = 0;
	return r;
}

void forward(int pwm){
	digitalWrite(dirPin_l1,HIGH);
	digitalWrite(dirPin_r1,HIGH);
	digitalWrite(dirPin_l2,LOW);
	digitalWrite(dirPin_r2,LOW);
	softPwmWrite(pwmPinL,pwm);
	softPwmWrite(pwmPinR,pwm);
}

void backward(int pwm){
	digitalWrite(dirPin_l1,LOW);
	digitalWrite(dirPin_r1,LOW);
	digitalWrite(dirPin_l2,HIGH);
	digitalWrite(dirPin_r2,HIGH);
	softPwmWrite(pwmPinL,pwm);
	softPwmWrite(pwmPinR,pwm);
}

void leftTurn(int pwm){
	digitalWrite(dirPin_l1,LOW);
	digitalWrite(dirPin_r1,HIGH);
	digitalWrite(dirPin_l2,HIGH);
	digitalWrite(dirPin_r2,LOW);
	softPwmWrite(pwmPinL,pwm);
	softPwmWrite(pwmPinR,pwm);
}

void rightTurn(int pwm){
	digitalWrite(dirPin_l1,HIGH);
	digitalWrite(dirPin_r1,LOW);
	digitalWrite(dirPin_l2,LOW);
	digitalWrite(dirPin_r2,HIGH);
	softPwmWrite(pwmPinL,pwm);
	softPwmWrite(pwmPinR,pwm);
}

void stop(){
	digitalWrite(dirPin_l1,LOW);
	digitalWrite(dirPin_r1,LOW);
	digitalWrite(dirPin_l2,LOW);
	digitalWrite(dirPin_r2,LOW);
	softPwmWrite(pwmPinL,0);
	softPwmWrite(pwmPinR,0);
}

int ultrasonicLeft() {

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

int ultrasonicFront() {

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

int ultrasonicRight() {

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

void setup(){
	wiringPiSetup();
	pinMode(A_Left, INPUT);
	pinMode(B_Left, INPUT);
	pinMode(A_Right, INPUT);
	pinMode(B_Right, INPUT);
	pinMode(dirPin_r1, OUTPUT);
	pinMode(dirPin_l1, OUTPUT);
	pinMode(dirPin_r2, OUTPUT);
	pinMode(dirPin_l2, OUTPUT);
	pullUpDnControl(A_Right, PUD_UP);
	pullUpDnControl(B_Right, PUD_UP);
	pullUpDnControl(A_Left, PUD_UP);
	pullUpDnControl(B_Left, PUD_UP);
	wiringPiISR(A_Left,INT_EDGE_BOTH,Enc_A_Left);
	wiringPiISR(B_Left,INT_EDGE_BOTH,Enc_B_Left);
	wiringPiISR(A_Right,INT_EDGE_BOTH,Enc_A_Right);
	wiringPiISR(B_Right,INT_EDGE_BOTH,Enc_B_Right);
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

}

int main(){
	setup();
	while(true)
	{
		cout<<pos_l<<"\t"<<pos_r<<"\t";
	}
	cout<<"\nLeft Ulrasonic"<<ultrasonicLeft();
	cout<<"\nFront Ulrasonic"<<ultrasonicFront();
	cout<<"\nRight Ulrasonic"<<ultrasonicRight();
	return 0;
}
