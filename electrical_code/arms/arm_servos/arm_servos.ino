#include <Servo.h>

Servo myservo;  // Create a servo object
Servo myservo2;
int lastAngleValue = 90; // Initial angle value

void setup() {
  myservo.attach(9);  // Attach the servo to digital pin 9
  myservo2.attach(8);
  Serial.begin(9600);
}

int returnAngleValue() {
  delay(1000);

  // Receiving Data from Computer
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n');
    int value = inputString.toInt();
    return value;
  }
  // Return the last angle value if no new value is received
  return lastAngleValue;
}

void loop() {
  int newAngleValue = returnAngleValue();

  // Update servo position only if a new angle value is received
  if (newAngleValue != lastAngleValue) {
    myservo.write(newAngleValue);
    myservo2.write(newAngleValue);  
    lastAngleValue = newAngleValue;
  }
}
