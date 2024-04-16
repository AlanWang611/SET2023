int servo1_pin = 12;
int servo2_pin = 13;
int motor_pin1 = 5;
int motor_pin2 = 6;
int motor_pin3 = 7;
int motor_pin4 = 8;
int pin_input = 1;

void setup() {
    pinMode(servo1_pin, OUTPUT);
    pinMode(servo2_pin, OUTPUT);
    pinMode(motor_pin1, OUTPUT);
    pinMode(motor_pin2, OUTPUT);
    pinMode(motor_pin3, OUTPUT);
    pinMode(motor_pin4, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(pin_input), moveArm, CHANGE);
}

void loop() {
    //lidar is running
}

void moveArm() {
    // Run motor driver for 2 seconds
    digitalWrite(motor_pin1, HIGH);
    digitalWrite(motor_pin2, LOW);
    digitalWrite(motor_pin3, HIGH);
    digitalWrite(motor_pin4, LOW);
    delay(3000);
    

    // Use servo for 120 degrees
    for (int angle = 0; angle <= 120; angle++) {
        int pulse_width = map(angle, 0, 120, 1000, 2000);
        digitalWrite(servo1_pin, HIGH);
        digitalWrite(servo2_pin, HIGH);

        delayMicroseconds(pulse_width);
        digitalWrite(servo1_pin, LOW);
        digitalWrite(servo2_pin, LOW);
        delay(15);
    }

    digitalWrite(motor_pin1, LOW);
    digitalWrite(motor_pin2, LOW);
    digitalWrite(motor_pin3, LOW);
    digitalWrite(motor_pin4, LOW);

    // Return servo to initial position
    for (int angle = 0; angle <= 120; angle++) {
        int pulse_width = map(angle, 0, 120, 1000, 2000);
        digitalWrite(servo1_pin, LOW);
        digitalWrite(servo2_pin, LOW);

        delayMicroseconds(pulse_width);
        digitalWrite(servo1_pin, HIGH);
        digitalWrite(servo2_pin, HIGH);
        delay(15);
    }
}