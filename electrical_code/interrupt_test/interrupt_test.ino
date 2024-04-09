const int inputd3 = 3;  // Define pin D3 as input
const int outputd7 = 7; // Define pin D7 as output
const int inputa1 = A1; // Define analog pin A7 as input

volatile bool d3State = LOW; // Variable to store the state of pin D3

void setup() {
  pinMode(outputd7, OUTPUT); // Set pin D7 as output
  pinMode(inputd3, INPUT);    // Set pin D3 as input
  pinMode(inputa1, OUTPUT);    // Set pin A7 as input
  attachInterrupt(digitalPinToInterrupt(inputd3), toggleA7, CHANGE); // Attach interrupt to pin D3
}

void loop() {
  // d7 toggle from high to low every 2 seconds
  digitalWrite(outputd7, HIGH); // Set pin D7 HIGH
  delay(2000);                   // Wait for 2 seconds
  digitalWrite(outputd7, LOW);  // Set pin D7 LOW
  delay(2000);                   // Wait for 2 seconds
}

void toggleA7() {

    digitalWrite(inputa1, !digitalRead(inputa1)); // Toggle pin A7 state

}

