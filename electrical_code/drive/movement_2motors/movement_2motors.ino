// Motor 1 - Left
int leftMotor1 = 8;
int leftMotor2 = 9;

// Motor 2 - Right
int rightMotor1 = 6;
int rightMotor2 = 5;

int LRdirection;
int angle;
int FBdirection;
int dist;
String inputString;



// forward = pin 1 high

void goForward(int delay_time) {
  // Set both left and right motors to move forward
  digitalWrite(leftMotor1, HIGH);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, HIGH);
  digitalWrite(rightMotor2, LOW);

  delay(delay_time);
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, LOW);

}

// backward = pin 2 high
void goBackward(int delay_time ) {
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, HIGH);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, HIGH);

  delay(delay_time);
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, LOW);

}

void turnLeft(int delay_time) {
  // Set left motor backward and right motor forward for turning left
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, HIGH);
  digitalWrite(rightMotor1, HIGH);
  digitalWrite(rightMotor2, LOW);
 
  delay(delay_time);
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, LOW);

}

void turnRight(int delay_time) {
  // Set left motor forward and right motor backward for turning right
  digitalWrite(leftMotor1, HIGH);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, HIGH);

  delay(delay_time);
  digitalWrite(leftMotor1, LOW);
  digitalWrite(leftMotor2, LOW);
  digitalWrite(rightMotor1, LOW);
  digitalWrite(rightMotor2, LOW);

}

void setup() {
  Serial.begin(115200);
  // Initialize all motor pins as outputs
  pinMode(leftMotor1, OUTPUT);
  pinMode(leftMotor2, OUTPUT);
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  //attachInterrupt(digitalPinToInterrupt(inputd3), toggleA7, CHANGE); // Attach interrupt to pin D3

}

void  loop() {
  while (!Serial.available());

  // Receiving Data from Computer
  if (Serial.available() > 0) {
    inputString = Serial.readStringUntil('\n');
  }
  // 1 character - direction (1 as left and 0 as right)
  // 3 characters - angle
  // 1 character - direction (1 as forward and 0 as backward)
  // 3 characters - distance
  LRdirection = inputString.substring(0, 1).toInt();
  angle = inputString.substring(1, 4).toInt();
  FBdirection = inputString.substring(4, 5).toInt();
  String dist_str = inputString.substring(5, 8);
  while (dist_str.length() < 3) {
    dist_str = "0" + dist_str;
  }
  dist = dist_str.toInt();

  if(LRdirection == 1){
    turnLeft(angle * 10);
  }
  else{
    turnRight(angle * 10);
  }
  if(FBdirection == 1){
      goForward(dist * 10);
  }
  else {
  goBackward(dist * 10);
  }
}


