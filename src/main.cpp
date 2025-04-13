#include <Arduino.h>

const int buttonPin = 2;
const int ledPin = 13;

bool ledState = false;
bool lastButtonState = HIGH;
bool currentButtonState;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  Serial.begin(9600);
  Serial.println("Arduino is ready!");
}

void loop() {
  // --- Обработка кнопки ---
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != currentButtonState) {
      currentButtonState = reading;

      if (currentButtonState == LOW) {
        ledState = !ledState;
        digitalWrite(ledPin, ledState ? HIGH : LOW);
        Serial.println(ledState ? "LED ON (button)" : "LED OFF (button)");
      }
    }
  }

  lastButtonState = reading;

  // --- Обработка команд из Serial ---
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // убираем пробелы и переносы

    if (command == "LED ON") {
      ledState = true;
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON (serial)");
    } else if (command == "LED OFF") {
      ledState = false;
      digitalWrite(ledPin, LOW);
      Serial.println("LED OFF (serial)");
    } else {
      Serial.println("Unknown command: " + command);
    }
  }
}