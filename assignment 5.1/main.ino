#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include "DHT.h"

#define DHTTYPE DHT11
uint8_t DHTPin = 12;
DHT dht(DHTPin, DHTTYPE);

// Replace with your network credentials
const char* ssid = "name";
const char* password = "password";

float data;
const char *URL = "http://192.168.88.254:8080/post_data";
WiFiClient client;
HTTPClient httpClient;

void setup(void) {

  delay(1000);
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  dht.begin();
}

void loop(void) {

  if(WiFi.status()== WL_CONNECTED){ 

    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    String response = "";
    response += "{";
    response += "\"temperature\":";
    response += temperature;
    response += ",\"humidity\":";
    response += humidity;
    response += "}";
    
    httpClient.begin(client, URL);
    httpClient.addHeader("Content-Type", "application/json");
    httpClient.POST(response);
    String content = httpClient.getString();
    httpClient.end();

    Serial.println(content);
    delay(5000);
  
  }
}