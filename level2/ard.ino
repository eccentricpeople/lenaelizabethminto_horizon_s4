#include <Servo.h>

Servo myServo;

const int potPin = A0;    // Potentiometer connected to analog pin A0
const int servoPin = 9;   // Servo connected to digital pin 9
const int ledPin = 7;     // LED connected to digital pin 7

const int maxAngle = 68;  // Maximum allowed servo angle

void setup() {
  myServo.attach(servoPin);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Read potentiometer value (0 - 1023)
  int potValue = analogRead(potPin);

  // Map potentiometer value to angle (0 - 180)
  int requestedAngle = map(potValue, 0, 1023, 0, 180);

  if (requestedAngle > maxAngle) {
    // Limit servo to 68 degrees and turn LED ON
    myServo.write(maxAngle);
    digitalWrite(ledPin, HIGH);
    Serial.println("WARNING: Limit exceeded! Servo capped at 68°");
  } else {
    // Move servo to requested angle and turn LED OFF
    myServo.write(requestedAngle);
    digitalWrite(ledPin, LOW);
    Serial.println("Angle: " + String(requestedAngle) + "° - Safe");
  }

  delay(100);
}