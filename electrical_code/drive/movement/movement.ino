// Motor 1 (Left Front)
int motor1Pin1 = 6;
int motor1Pin2 = 7;

// Motor 2 (Left Rear)
int motor2Pin1 = 4;
int motor2Pin2 = 5;

// Motor 3 (Right Front)
int motor3Pin1 = 9;
int motor3Pin2 = 10;

// Motor 4 (Right Rear)
int motor4Pin1 = 11;
int motor4Pin2 = 12;

void goForward(int time_number_of_loop) {
  // Set both left and right motors to move forward
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
  digitalWrite(motor3Pin1, HIGH);
  digitalWrite(motor3Pin2, LOW);
  digitalWrite(motor4Pin1, HIGH);
  digitalWrite(motor4Pin2, LOW);
  delay(time_number_of_loop);
digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, LOW);
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, LOW);
}

void goBackward(int time_number_of_loop ) {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, HIGH);
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, HIGH);
  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, LOW);
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, LOW);

}

void turnLeft(int time_number_of_loop) {
  // Set left motors backward and right motors forward for turning left
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
 
  digitalWrite(motor3Pin1, HIGH);
  digitalWrite(motor3Pin2, LOW);
  digitalWrite(motor4Pin1, HIGH);
  digitalWrite(motor4Pin2, LOW);
  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, LOW);
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, LOW);

}

void turnRight(int time_number_of_loop) {
  // Set left motors forward and right motors backward for turning right
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, HIGH);
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, HIGH);
  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
  digitalWrite(motor3Pin1, LOW);
  digitalWrite(motor3Pin2, LOW);
  digitalWrite(motor4Pin1, LOW);
  digitalWrite(motor4Pin2, LOW);
}

void setup() {
   Serial.begin(9600);
  // Initialize all motor pins as outputs
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  pinMode(motor3Pin1, OUTPUT);
  pinMode(motor3Pin2, OUTPUT);
  pinMode(motor4Pin1, OUTPUT);
  pinMode(motor4Pin2, OUTPUT);
}
void loop(){
  // int x = 3000;
  // goForward(x);
  // goBackward(x);
  // turnLeft(x);
  // turnRight(x);
  delay(1000); // Wait for 1 second

  // Receiving Data from Computer
  if (Serial.available() > 0) {
    // Read the incoming string until newline character
    String inputString = Serial.readStringUntil('\n');
    
    // Find the index of the space character
    int spaceIndex = inputString.indexOf(' ');

    // Extract the command character and the number from the string
    char command = inputString.substring(0, spaceIndex).charAt(0);
    int value = inputString.substring(spaceIndex + 1).toInt();

    if( command == 'w'){
      goForward(value);

    }
    else if( command == 'd'){
      turnRight(value);
      
    }
    else if( command == 'a'){
      turnLeft(value);

    }
    else if( command == 's'){
      goBackward(value);

    }
    
  command = " ";
  value = 0;
}}

