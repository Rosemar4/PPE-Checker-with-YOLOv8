/*
  PPE Detection Indicator
  - Receives '1' from Python if PPE detected → Green LED ON
  - Receives '0' if no PPE → Red LED ON
*/

int greenLed = 7;
int redLed = 8;

void setup() {
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();

    if (signal == '1') {
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
    } 
    else if (signal == '0') {
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
    }
  }
}
