#define BLYNK_TEMPLATE_ID "TMPL6vtU3qvHr"
#define BLYNK_TEMPLATE_NAME "theftalert"
#define BLYNK_AUTH_TOKEN "HDFSNSiSWYGK7t8K9gi9rd7l4sy3k6kS"

#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = BLYNK_AUTH_TOKEN;

char ssid[] = "well";  // type your wifi name
char pass[] = "qwerty123";  // type your wifi password

#define PIR_SENSOR  D8
BlynkTimer timer;

void notifyOnTheft() {
  int isTheftAlert = digitalRead(PIR_SENSOR);
  Serial.println(isTheftAlert);
  if (isTheftAlert == 1) {
    Serial.println("Theft Alert in Home");
    Blynk.logEvent("theft_alert", "Theft Alert in Home");
  }
}

void setup() {
  pinMode(PIR_SENSOR, INPUT);
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  timer.setInterval(5000L, notifyOnTheft);
}

void loop() {
  Blynk.run();
  timer.run();
}
