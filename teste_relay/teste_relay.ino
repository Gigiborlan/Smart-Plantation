#define RELAY_PIN 7
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int temp_pin = 1;
int soil_pin = 3;

const int AirValue = 780;
const int WaterValue = 410; 

void turn_relay_on() {
  digitalWrite(RELAY_PIN, HIGH);
  Serial.print("Irrigation Started");
}
void turn_relay_off() {
  digitalWrite(RELAY_PIN, LOW);
  Serial.print("Irrigation finished");
}

int get_temp() {
  return (float(analogRead(temp_pin))*5/(1023))/0.01;
}

int get_moisture() {
  return map(analogRead(soil_pin), AirValue, WaterValue, 0, 100);  
}

void lcd_write(int temperature, int moisture) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: " + (String)temperature + "oC");
  lcd.setCursor(0, 1);
  lcd.print("Umidade: " + (String)moisture + "%");
}
void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  int temperature;
  int moisture;
  temperature = get_temp();
  delay(1000);
  moisture = get_moisture();
  lcd_write(temperature,moisture);
  Serial.print((String)temperature + (String)moisture);
  delay(1000);
}
