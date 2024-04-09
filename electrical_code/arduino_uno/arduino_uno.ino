/*
Arduino Uno handles Lidar data
*/

#include <SoftwareSerial.h>

const int stepPin = 4;
const int enPin = 2;
const int dirPin = 3;
int totalSteps = 0;
float currentAngle = 0;
const int STEPS = 1600; // resolution || 1600 steps per rev (on motor driver)
const float angle_per_step = 360.0 / float(STEPS);

const int HEADER = 0x59;
// Variables
int TF01_pix;
int dist, strength;
int a, b, c, d, e, f, check, i;

const byte rxPin = 10;
const byte txPin = 11;
SoftwareSerial mySerial (rxPin, txPin);

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW);
  digitalWrite(dirPin, LOW); // default counter clockwise

  Serial.begin(115200);
  Serial.print("serial started");
  mySerial.begin(115200);
  setAngle(0);
}

void loop() {
  // rotate a step
  rotate(1);

  // get distance 
  Serial.println("dist : " + String(getDist()));

  // serial print angle
  if (currentAngle >= 360.0) {
    currentAngle = currentAngle - 360.0;
  }

  Serial.println("angle : " + String(currentAngle));
}

int getDist(){
  delay(1);
  if (mySerial.available() >= 9)
  {
    // Check for first header byte
    if(mySerial.read() == HEADER)
    {
    // Check for second header byte
      if(mySerial.read() == HEADER)
      {
        // Read all 6 data bytes
        a = mySerial.read();
        b = mySerial.read();
        c = mySerial.read();
        d = mySerial.read();
        e = mySerial.read();
        f = mySerial.read();

        // Read checksum byte
        check = (a + b + c + d + e + f + HEADER + HEADER);
        // Compare lower 8 bytes of checksum
        if(mySerial.read() == (check & 0xff))
        {
          // Calculate distance
          dist = (a + (b * 256));
          // return result
          return dist;
        }
      }
    }
  }
  else{return 0;}
}

// 1600 is one full rotation
void setAngle(int angleDegrees) {
  currentAngle = totalSteps/STEPS *360;

  int moveSteps = (currentAngle - angleDegrees)*STEPS/360;
  if(moveSteps > 0) {
        // clockwise
        digitalWrite(dirPin, LOW);
      }
      else {
        digitalWrite(dirPin, HIGH);
      }
  for(int x = 0; x < abs(moveSteps); x++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(500);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(500);
  }
  totalSteps += moveSteps;
}

void rotate(float moveSteps) {
  // rotate by moveSteps
  for (int x = 0; x < abs(moveSteps); x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
  
  // increment total steps 
  // reference angle
  totalSteps += int(moveSteps);
  totalSteps %= STEPS; // capping @ # steps per rev
  currentAngle += moveSteps * angle_per_step;
}