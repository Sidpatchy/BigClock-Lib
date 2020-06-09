#include <Adafruit_NeoPixel.h>

// Data PIN for LEDs
#define LED_PIN 6

// Number of LEDs
#define LED_COUNT 86

// Declare a strip object
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  int gColor = strip.Color(255, 0, 0);
}

int num = -1;
int seconds = -1;

unsigned long previousMillis = 0;
const long invertal = 1000;

int digit1;
int digit2;
int digit3;
int digit4;

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= invertal) {
    previousMillis = currentMillis;

    num = num + 1;
    seconds = seconds + 1;

    if (seconds >= 10) {
      seconds = 0;
      digit1 = 0;
      digit2 = digit2 + 1;
    }
    else {
      digit1 = seconds;
    }
    
    if (num >= 60) {
      num = 0;
      digit1 = 0;
      digit2 = 0;

      if (digit3 > 9) {
        digit4 = digit4 + 1;
        digit3 = 0;
      }
        else {
          digit3 = digit3 + 1;
        }
      }
    digitOne(digit1);
    digitTwo(digit2);
    digitThree(digit3);
    digitFour(digit4);    
  }
}

void digitOne(int num) {
  if (num == 0) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 18, 3);
    strip.show();
  }
  if (num == 1) {
    strip.fill(0, 0, 21);
    strip.fill(16711680, 15, 3);
    strip.fill(16711680, 0, 3);
    strip.show();
  }
  if (num == 2) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 6, 3);
    strip.fill(0, 15, 3);
    strip.show();
  }
  if (num == 3) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 6, 6);
    strip.show();
  }
  if (num == 4) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 9, 6);
    strip.fill(0, 3, 3);
    strip.show();
  }
  if (num == 5) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 0, 3);
    strip.fill(0, 9, 3);
    strip.show();
  }
  if (num == 6) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 0, 3);
    strip.show();
  }
  if (num == 7) {
    strip.fill(0, 0, 21);
    strip.fill(16711680, 0, 6);
    strip.fill(16711680, 15, 3);
    strip.show();
  }
  if (num == 8) {
      strip.fill(16711680, 0, 21);
      strip.show();
  }
  if (num == 9) {
    strip.fill(16711680, 0, 21);
    strip.fill(0, 9, 3);
    strip.show();
  }
}

void digitTwo(int num) {
  if (num == 0) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 30, 3);
    strip.show();
  }
  if (num == 1) {
    strip.fill(0, 21, 21);
    strip.fill(16711680, 33, 3);
    strip.fill(16711680, 21, 3);
    strip.show();
  }
  if (num == 2) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 27, 3);
    strip.fill(0, 33, 3);
    strip.show();
  }
  if (num == 3) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 27, 3);
    strip.fill(0, 39, 3);
    strip.show();
  }
  if (num == 4) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 36, 6);
    strip.fill(0, 24, 3);
    strip.show();
  }
  if (num == 5) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 21, 3);
    strip.fill(0, 39, 3);
    strip.show();
  }
  if (num == 6) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 21, 3);
    strip.show();
  }
  if (num == 7) {
    strip.fill(0, 21, 21);
    strip.fill(16711680, 21, 6);
    strip.fill(16711680, 33, 3);
    strip.show();
  }
  if (num == 8) {
      strip.fill(16711680, 21, 21);
      strip.show();
  }
  if (num == 9) {
    strip.fill(16711680, 21, 21);
    strip.fill(0, 39, 3);
    strip.show();
  }
}

void digitThree(int num) {
  if (num == 0) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 53, 3);
    strip.show();
  }
  if (num == 1) {
    strip.fill(0, 44, 21);
    strip.fill(16711680, 56, 3);
    strip.fill(16711680, 44, 3);
    strip.show();
  }
  if (num == 2) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 50, 3);
    strip.fill(0, 56, 3);
    strip.show();
  }
  if (num == 3) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 50, 3);
    strip.fill(0, 62, 3);
    strip.show();
  }
  if (num == 4) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 59, 6);
    strip.fill(0, 47, 3);
    strip.show();
  }
  if (num == 5) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 44, 3);
    strip.fill(0, 62, 3);
    strip.show();
  }
  if (num == 6) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 44, 3);
    strip.show();
  }
  if (num == 7) {
    strip.fill(0, 44, 21);
    strip.fill(16711680, 44, 6);
    strip.fill(16711680, 56, 3);
    strip.show();
  }
  if (num == 8) {
      strip.fill(16711680, 44, 21);
      strip.show();
  }
  if (num == 9) {
    strip.fill(16711680, 44, 21);
    strip.fill(0, 62, 3);
    strip.show();
  }
}

void digitFour(int num) {
  if (num == 0) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 74, 3);
    strip.show();
  }
  if (num == 1) {
    strip.fill(0, 65, 21);
    strip.fill(16711680, 77, 3);
    strip.fill(16711680, 65, 3);
    strip.show();
  }
  if (num == 2) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 71, 3);
    strip.fill(0, 77, 3);
    strip.show();
  }
  if (num == 3) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 71, 3);
    strip.fill(0, 83, 3);
    strip.show();
  }
  if (num == 4) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 80, 6);
    strip.fill(0, 68, 3);
    strip.show();
  }
  if (num == 5) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 65, 3);
    strip.fill(0, 83, 3);
    strip.show();
  }
  if (num == 6) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 65, 3);
    strip.show();
  }
  if (num == 7) {
    strip.fill(0, 65, 21);
    strip.fill(16711680, 65, 6);
    strip.fill(16711680, 77, 3);
    strip.show();
  }
  if (num == 8) {
      strip.fill(16711680, 65, 21);
      strip.show();
  }
  if (num == 9) {
    strip.fill(16711680, 65, 21);
    strip.fill(0, 83, 3);
    strip.show();
  }
}
