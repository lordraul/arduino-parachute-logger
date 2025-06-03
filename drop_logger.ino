// MPU-6050 Short Example Sketch
//www.elegoo.com
//2016.12.9

#include<Wire.h>
const int sampleRateHz = 5;
const int sampleDuration = 5;
const int numSamples = sampleRateHz * sampleDuration;

bool dumped = false;

struct Sample {
  unsigned long timestamp;
  int16_t ax, ay, az;
};

Sample data[numSamples];

const int MPU_addr=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ;
void setup(){
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600);

  for(int i = 0; i < numSamples; i++) {
    Wire.beginTransmission(MPU_addr);
    Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
    AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
    AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
    AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
    data[i].timestamp = millis();
    data[i].ax = AcX;
    data[i].ay = AcY;
    data[i].az = AcZ;
    delay(1000 / sampleRateHz);
  }
}
void loop(){
  if(Serial && !dumped) {
    Serial.println("time(ms),ax_raw,ay_raw,az_raw");
    for(int i = 0; i < numSamples; i++) {
      Serial.print(data[i].timestamp);
      Serial.print(",");
      Serial.print(data[i].ax);
      Serial.print(",");
      Serial.print(data[i].ay);
      Serial.print(",");
      Serial.println(data[i].az);
    }
    dumped = true;
  }
}
