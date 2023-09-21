/* 
 * BigClock-lib
 * Copyright (C) 2023-09 Sidpatchy
 * 
 * This code has been specifically designed to run on
 * the Raspberry Pi Pico W. It will likely work on
 * ESP32 and other similar boards, though I haven't
 * tested this.
 *
 * ---------------------------------------------------------------------
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#include <Adafruit_NeoPixel.h>
#include <WiFi.h>

// Data PIN for LEDs
#define LED_PIN 5

// Number of LEDs
#define LED_COUNT 86

const char* ssid = "Caspar";                    //  your network SSID (name)
const char* password = "PoisonParamedicTerry";  // your network password

const char* ntpServer = "time.nist.gov";
const char* ntpServer2 = "pool.ntp.org";

const long gmtOffset_sec = -18000;  // Adjust according to your timezone in seconds. (e.g., -3600 for GMT-1)
const int daylightOffset_sec = 0;   // If your country has Daylight Saving Time, adjust accordingly. E.g., 3600 for +1hr DST
struct tm timeinfo;

// Declare a strip object
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

const int ON_COLOUR = strip.Color(255, 0, 0);
const int OFF_COLOUR = 0;

void setup() {
  Serial.begin(115200);

  // put your setup code here, to run once:
  strip.begin();
  setDigit(1, 11);
  setDigit(2, 11);
  setDigit(3, 11);
  setDigit(4, 11);
  strip.show();

  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");

  NTP.begin(ntpServer, ntpServer2);
  setClock();

  configTime(2000, gmtOffset_sec, ntpServer, ntpServer2);
}

int num = -1;
int seconds = -1;

unsigned long previousMillis_displayUpdate = 0;
const long invertal_displayUpdate = 50;

unsigned long previousMillis_NTPUpdate = 0;
const long invertal_NTPUpdate = 300000;  // 5 minutes

void loop() {

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis_NTPUpdate >= invertal_NTPUpdate) {
    setClock();
    previousMillis_NTPUpdate = currentMillis;
  }

  if (currentMillis - previousMillis_displayUpdate >= invertal_displayUpdate) {
    updateTimeinfo();

    // Extracting hour and minute from the timeinfo structure
    int hours = timeinfo.tm_hour;
    int minutes = timeinfo.tm_min;

    // Determine the individual digits for hours and minutes
    int digit4 = hours / 10;    // First digit of hour
    int digit3 = hours % 10;    // Second digit of hour
    int digit2 = minutes / 10;  // First digit of minute
    int digit1 = minutes % 10;  // Second digit of minute

    //digitOne(digit1);
    //digitTwo(digit2);
    //digitThree(digit3);
    //digitFour(digit4);

    setDigit(1, digit1);
    setDigit(2, digit2);
    setDigit(3, digit3);
    setDigit(4, digit4);

    strip.fill(ON_COLOUR, 42, 2);
    
    strip.show();

    previousMillis_displayUpdate = currentMillis;
  }
}

void setClock() {
  NTP.waitSet();
  updateTimeinfo();
  Serial.print("Current time: ");
  Serial.print(asctime(&timeinfo));
}

void updateTimeinfo() {
  time_t now = time(nullptr);
  adjustTimeZoneAndDST(now);
  gmtime_r(&now, &timeinfo);
}

void adjustTimeZoneAndDST(time_t& epochTime) {
  epochTime += gmtOffset_sec;       // adjust for the timezone
  epochTime += daylightOffset_sec;  // adjust for DST
}

const int DIGIT_STARTS[] = {0, 21, 44, 65}; // Digit 1, 2, 3, 4

/*
 * Digit index starts at 1 and ends at 4. I'd prefer to use 0-3, but
 * then I'd have to rewrite and redraw most of my documentation, and
 * that's more effort than just dealing with this.
 *
 * Integers greater than 9, or less than 0 will cause the segment to
 * display a dash. Code should never specifiy a number like this
 * except to intentionally display a dash.
 */
void setDigit(int digit, int num) {
  int firstLed = DIGIT_STARTS[digit-1];

  strip.fill(OFF_COLOUR, firstLed, 21);

  if (num > 9 || num < 0) {
    strip.fill(ON_COLOUR, firstLed + 9, 3);
  } else {
    switch (num) {
      case 0:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed + 9, 3);
        break;
      case 1:
        strip.fill(ON_COLOUR, firstLed, 3);
        strip.fill(ON_COLOUR, firstLed + 12, 3);
        break;
      case 2:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed + 6, 3);
        strip.fill(OFF_COLOUR, firstLed + 12, 3);
        break;
      case 3:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed + 6, 3);
        strip.fill(OFF_COLOUR, firstLed + 18, 3);
        break;
      case 4:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed + 15, 6);
        strip.fill(OFF_COLOUR, firstLed + 3, 3);
        break;
      case 5:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed, 3);
        strip.fill(OFF_COLOUR, firstLed + 18, 3);
        break;
      case 6:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed, 3);
        break;
      case 7:
        strip.fill(ON_COLOUR, firstLed, 6);
        strip.fill(ON_COLOUR, firstLed + 12, 3);
        break;
      case 8:
        strip.fill(ON_COLOUR, firstLed, 21);
        break;
      case 9:
        strip.fill(ON_COLOUR, firstLed, 21);
        strip.fill(OFF_COLOUR, firstLed + 18, 3);
        break;
    }
  }
}