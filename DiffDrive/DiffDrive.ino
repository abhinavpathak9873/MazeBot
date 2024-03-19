const int enA = 9;
const int in1 = 8;
const int in2 = 7;
const int enB = 3;
const int in3 = 5;
const int in4 = 4;

void setup() {
  Serial.begin(9600);  // Set the baud rate to match the Python program
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    switch (receivedChar) {
      case 'W':
        // Move forward
        analogWrite(enA, 100);  // Full speed for motor A
        analogWrite(enB, 100);  // Full speed for motor B
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in3, HIGH);
        digitalWrite(in4, LOW);
        break;
      case 'S':
        // Move backward
        analogWrite(enA, 100);  // Full speed for motor A
        analogWrite(enB, 100);  // Full speed for motor B
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        digitalWrite(in3, LOW);
        digitalWrite(in4, HIGH);
        break;
      case 'A':
        // Turn left
        analogWrite(enA, 100);  // Adjust speed for turning
        analogWrite(enB,100);  // Adjust speed for turning
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        digitalWrite(in3, HIGH);
        digitalWrite(in4, LOW);
        break;
      case 'D':
        // Turn right
        analogWrite(enA, 100);  // Adjust speed for turning
        analogWrite(enB, 100);  // Adjust speed for turning
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in3, LOW);
        digitalWrite(in4, HIGH);
        break;
      default:
        // Stop motors or do nothing
        analogWrite(enA, 0);  // Stop motor A
        analogWrite(enB, 0);  // Stop motor B
        digitalWrite(in1, LOW);
        digitalWrite(in2, LOW);
        digitalWrite(in3, LOW);
        digitalWrite(in4, LOW);
        break;
    }
  }
}
