// Motor 1 (Left Front)
int motor1Pin1 = 9;
int motor1Pin2 = 10;

// Motor 2 (Left Rear)
int motor2Pin1 = 11;
int motor2Pin2 = 12;

int angle;
int dist;
String inputString;



void goForward(int time_number_of_loop) {
  // Set both left and right motors to move forward
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);

  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void goBackward(int time_number_of_loop ) {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);

  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void turnLeft(int time_number_of_loop) {
  // Set left motors backward and right motors forward for turning left
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
 
  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void turnRight(int time_number_of_loop) {
  // Set left motors forward and right motors backward for turning right
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);

  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void setup() {
  Serial.begin(115200);
  // Initialize all motor pins as outputs
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(inputd3), toggleA7, CHANGE); // Attach interrupt to pin D3

}

void  loop() {
  while (!Serial.available());

  // Receiving Data from Computer
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n');
  }
  // 3 characters - angle
  // 3 characters - distance
  angle = inputString.substring(0, 3).toInt();
  dist = inputString.substring(3, 7).toInt();

  turnRight(angle * 100);
  goForward(dist * 100);

}


