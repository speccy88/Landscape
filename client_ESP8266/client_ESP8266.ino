#include <ESP8266WiFi.h>
 
const char* ssid = "Do2";
const char* password = "dfmms9992";
const char* server = "192.168.2.97";
const int port = 8000;
 
int ledPin = 2; // GPIO2 
 
WiFiClient client;
    
void setup() {  
  Serial.begin(115200);
  delay(10);
  
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  connectWiFi(); 
}
 
 
void loop() {  
  if (client.connect(server,port))
  {
     client.print("GET /api/getState HTTP/1.0\r\n\r\n"); 
     Serial.println("GET request sent");
  }
  
  String response = client.readStringUntil('}');
  Serial.println(response);
  client.stop();
  
  if (response.indexOf("\"ON\"") != -1) {
    digitalWrite(ledPin, HIGH);
    Serial.println("LED ON");
  } 
  if (response.indexOf("\"OFF\"") != -1){
    digitalWrite(ledPin, LOW);
    Serial.println("LED OFF");
  }
  
  //Delay between request   
  delay(500);  
}

void connectWiFi()
{
  WiFi.begin(ssid, password);
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
   
  WiFi.begin(ssid, password);
   
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
}
