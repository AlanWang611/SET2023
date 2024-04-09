// Motor 1 - Left
int leftMotor1 = 8;
int leftMotor2 = 7;

// Motor 2 - Right
int rightMotor1 = 6;
int rightMotor2 = 5;

int angle;
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

}

void  loop() {
  while (!Serial.available());

  // Receiving Data from Computer
  if (Serial.available() > 0) {
    inputString = Serial.readStringUntil('\n');
  }
  // 3 characters - angle
  // 3 characters - distance
  angle = inputString.substring(0, 3).toInt();
  dist = inputString.substring(3, 7).toInt();

  turnRight(angle * 100);
  goForward(dist * 100);

}