#include <stdio.h>
#include <stdlib.h>
int  distx=0,disty=0; //x -coordinate  y coordinate calculation
int x_bar=1, y_bar=1;
float encoderdistance=0;
int a[8];
int v=1;   //no. of nodes
int r=0;   // how many times should be visited or not
int count1,count2,count3;  // to store whether there is left or forward or right
int mb=4;
int mb1=5;
int ma=7;
int ma1=6;
int ma1s=0;
int mbs=0;
double gg=0;
unsigned long currentmillis=0;    //global
unsigned long lastmillis=0;     //global
unsigned long time1=0;
int sp=0;          //set point, set to zero(centre of the line)
int kp=10;
int ki=15;
int kd=50;         //derivative gain must be low, otherwise rapid motor changes,kd should be 20 times of kp
double prev_error=0;
int setspeed=150;
int endpoint=0;
int iterationtime=0;
double pos;
double proportional=0;
double integral=0;
double derivative=0;

struct node
{
  int count1,count2,count3,r;
  int distx=0,disty=0;
  node* next;
};

struct adjlist
{
  node*  head;
};

struct graph
{
  int v;   // number of vertices
  adjlist* arr[];
};

struct node* updatenode(struct graph *g,int v,int distx,int disty,int count1,int count2,int count3,int r){

  if(g->arr[v]->head==NULL)
  {

  node* newnode=(node*)malloc(sizeof(node));
  newnode->count1=count1;
  newnode->count2=count2;
  newnode->count3=count3;
  newnode->distx;
  newnode->disty;
  newnode->r;
  newnode->next=NULL;
  g->arr[v]->head=newnode;
  Serial.println( g->arr[v]->head->count1);
  v++;
  return newnode;
   }
  else
  {
    if(g->arr[v]->head->count1==1)
    {
      g->arr[v]->head->count1=0;
      g->arr[v]->head->r=r--;


    }
    if(g ->arr[v]->head->count2==1)
     {
      g->arr[v]->head->count2=0;
      g->arr[v]->head->r=r--;
     }
    if( g->arr[v]->head->count3==1)
     {
      g->arr[v]->head->count3=0;
      g->arr[v]->head->r=r--;
     }
}
};

struct graph* creategraph(int v)
{
 struct graph* g =(struct graph*)malloc(sizeof(graph));
  g->v=v;
  g->arr[v]=(adjlist*)malloc(sizeof(adjlist)*v);
  for(int i=0;i<v;i++)
  {
  g->arr[i]->head=NULL;
  }
  return g;
};

void rotateright()
{

}

void rotateleft()
{

}

void rotate(int thetha)
{
  x_bar=cos(thetha)-sin(thetha);
  y_bar=sin(thetha)+cos(thetha);

}

float encoder()
{
  return encoderdistance;
}

int motiondistance(graph* g)
{
  if((x_bar==1 && y_bar==-1 )|| (x_bar==-1 && y_bar==1))
  {
    distx = distx+ (encoderdistance*x_bar);
  }
  else if((x_bar==1 && y_bar==1)|| (x_bar==-1 && y_bar==-1))

    disty = disty + (encoderdistance*x_bar);

    updatenode(g,v,distx,disty,count1,count2,count3,r);
    r=0;
  encoderdistance=0;
}

int sensor(int j)
{
  a[j]=digitalRead(j+30);
  return a[j];
}

int lfrpriority(int a[],int i,graph* g)
{
  if(a[0]==0)
  {
    r++;
    count1++;
    Serial.println("left path Entered into the info");
  }
  if(a[2]==0)
  {
    r++;
    count2++;
    Serial.println("forwardpath entered into the info");

  }
  if(a[4]==0)
  {
    r++;
    count3++;
    Serial.println(" right path entered into the info");

  }
  updatenode(g,v,distx,disty,count1,count2,count3,r);

  if(a[0] == 1)
  {
    //marks the left track going as 1
    rotateleft();   //point rotation to left
    rotate(90);

    count1--;
  }
  else if(a[2] == 0)
  {
    count2--;   //marks the straight track going as 1 acc to lfr
                //motion(g);

  }

  else if(a[7] == 1)
  {
    count3--;
    rotateright();
    rotate(-90);
  }
}
void avpid()
{
  for(int j=0; j<6; j++)
  a[j]=digitalRead(30+j);

  double error=(1000*a[0]+2000*a[1]+3500*a[2]+3500*a[3]+5000*a[4]+6000*a[5])/(a[0]+a[1]+a[2]+a[3]+a[4]+a[5])-3500;  //changed to 3500 from 4500
  currentmillis=millis();
  time1 = currentmillis - lastmillis;

  if(currentmillis-lastmillis==10)
  {
    iterationtime=time1;
  }

  lastmillis=currentmillis;
  proportional=error;
  integral=integral;//+(error*iterationtime);
  derivative=(error-prev_error);///iterationtime;
  int pid=(kp*proportional)+(ki*integral)+(kd*derivative);
  Serial.println("pid entered");
  prev_error=error;
  gg=map(pid,-3500,3500,-20,+20);

  if(gg>100)
  {
    gg=0;
  }

  if(error<0)       //deviation towards the right
   {
     ma1s=setspeed+gg;
     mbs=setspeed;
   }

  if(error>0)       //devation towards the left
   {
     ma1s=setspeed;
     mbs=setspeed+gg;
   }
  analogWrite(ma1,ma1s); //FORWARD
  digitalWrite(ma,LOW);
  analogWrite(mb,mbs);
  digitalWrite(mb1,LOW);
}

void  motion(graph *g)
 {
  while(a[0]==1 && a[5]==1 && a[2]==0 )
  {                            //dont change this
    avpid();

    //encoderdistance=encoder();
    for(int j=0;j<6;j++)
   {
     a[j]= sensor(j);
    Serial.println(a[j]);
   }

 }

  brake();
  Serial.println("forwardmotion completed");
//  motiondistance(g);
  Serial.println("distance stored as coordinates");
}

//int loopdetect(graph* g)
//{
//  if(g->arr[v]->head->distx!=0 || g->arr[v]->head->disty!=0)
//  back(g);
//}

//int back(graph *g)
//{
//  //back movement motors
//  g->arr[v-1]->head;
//}

void brake()
{
  analogWrite(ma1,0);
  digitalWrite(ma,LOW);
  analogWrite(mb,0);
  digitalWrite(mb1,LOW);
}

int deadend(graph *g,int count1,int count2,int count3)
{
  Serial.print("Deadend detected");
  brake();
  //back(g);
  //display nullto  address of that node
  g->arr[v]->head=NULL;
  g->arr[v-1]->head;
  updatenode(g,v,distx,disty,count1,count2,count3,r);
  Serial.print("Deadend");
//  if(g->arr[v]->head->count2==0)
//  {
//    if(x_bar==1 && y_bar==1)
//
//    rotateleft();
//    rotate(90);
//  }
//  else if(x_bar==-1 && y_bar==1)
//  {
//
//    rotateright();
//    rotate(-90);
//  }
//
//  if(g->arr[v]->head-> count2==1)
//  {
//    if(x_bar==1 && y_bar==1)
//
//    rotateleft();
//    rotate(90);
//  }
//  else if(x_bar==-1 && y_bar==1)
//  {
//
//    rotateright();
//    rotate(-90);
//  }
// }
//  else
//  {
//       continue;//if onthe left side      rotate right if on the positive x axis
//  }
 }

int forwardmotion(graph *g)
{
    while(a[0]==1 && a[5]==1)
    {
    motion(g);
    for(int j=0;j<6;j++)
     {
      a[j]=sensor(j);
      Serial.println(a[j]);
     }
    }
    brake();
}

void start(graph* g,int count1, int count2,int count3)
{
 while(1)
 {
   for(int i=0;i<6;i++)
   {
    a[i]=sensor(i);

   }
   for(int i=0;i<5;i++)
   {
    Serial.print(a[i]);

   }
   Serial.println(a[5]);


   while(1)
  {                                                         //a[0]=left sensor  a[1]=leftboundary  a[2]=front sensor   a[3]=back sensor  a[4]=right boundary
    if(a[0]==1 && a[5]==1 && a[2]==0)
    forwardmotion(g);
    else if(a[0]==0 || a[5]==0)
     {
        lfrpriority(a,6,g);
        for(int i=0;i<6;i++)
   {
    a[i]=sensor(i);

   }
        motion(g);
     }

  }
  brake();
  if(a[0]==1 && a[2]==1 && a[5]==1)
  deadend(g,count1,count2,count3);
  if(a[0]==0 && a[2]==0 && a[5]==0)
  {

    break;
  }
 }
}

int printgraph(graph* g)
{
  int k;
  for (k = 0; k < g->v; ++k)
    {
      Serial.println("\n Adjacency list of vertex %d\n head ");
      while (k<=v)
      {
        Serial.println(g->arr[k]->head->count1);
        Serial.println( g->arr[k]->head->count2);
        Serial.println( g->arr[k]->head->count3);
        Serial.println( g->arr[k]->head->r);
        Serial.println( g->arr[k]->head->distx);
        Serial.println( g->arr[k]->head->disty);
      }
      Serial.println("\n");
    }
  }

void setup()
{
    Serial.begin(9600);
    for(int i=0;i<6;i++) pinMode((i+30),INPUT);
    pinMode(ma,OUTPUT);
    pinMode(ma1,OUTPUT);
    pinMode(mb,OUTPUT);
    pinMode(mb1,OUTPUT);
}

void loop()
{
    graph* g=NULL;
    g=creategraph(v);
    start(g,count1,count2,count3);
    printgraph(g);
// if(but=HIGH)
// {
//  for(k=0;k<=v;k++)
//    for(i=0;i<5;i++)
//    {
//      a[i]=sensor(i);
//    }
//   if(//sensor condition)
//   {
//    forward()
//   else
//   {
//      brake();
//   }
//    if(g->arr[k]->head!=NULL)
//    {
//      if(g->arr[k]->count1){}
//      if(g->arr[k]->count2){}
//      if(g->arr[k]->count3){}
//      }
//    }
// }
}
