#include <VarSpeedServo.h>

VarSpeedServo servo1, servo2; // Servo with speed control

int angle;
int angle1 = 90;
int angle2 = 90;
int origin1 = 90;
int origin2 = 90;
int MAX_ANGLE1 = 170;
int MIN_ANGLE1 = 10;
int MAX_ANGLE2 = 130;
int MIN_ANGLE2 = 50;
char rcv_char;
String str = "";
String angle1_str = "";
String angle2_str = "";
int mode = 0;
// mode 1: rotate motor
// mode 2: calibrate motor 1
// mode 3: calibrate motor 2
// mode 4: set motor 1 MAX MIN
// mode 5: set motor 2 MAX MIN

void setup()
{
  Serial.begin(9600);
  servo1.attach(9); // 連接數位腳位9，伺服馬達的訊號線
  servo2.attach(3);
  servo1.write(90, 10, true);
  servo2.write(90*180.0/220.0, 10, true);
}

void loop()
{
  if (Serial.available()>0) {
      // read the incoming byte:
      rcv_char = Serial.read();
      if (rcv_char != '\n'){
        str += rcv_char;
      }
      else{
        Serial.print("Rcv: ");
        Serial.println(str);

        for(int i = 0; i < str.length(); ++i) {
          if (str[i] == '#'){
            i++;
            if (str[i] == 'a'){
              Serial.println("MAX_1: ");
            }
            else if (str[i] == 'b'){
              Serial.println("MIN_2: ");
            }
            else if (str[i] == 'c'){
              Serial.println("MAX_1: ");
            }
            else if (str[i] == 'd'){
              Serial.println("MAX_2: ");
            }
            
            else if (str[i] == 'e'){
              Serial.println("Origin_1: ");
              mode = 2;
              String origin_str = "";
              i++;
              while(str[i] != '#' && str[i] != '&'){
                origin_str += str[i];
                i++;
              }
              origin1 = origin_str.toInt();
              Serial.println(origin1);
              i--;
            }
            
            else if (str[i] == 'f'){
              Serial.println("ninety_1: ");
            }
            else if (str[i] == 'g'){
              Serial.println("Origin_2: ");
              mode = 2;
              String origin_str = "";
              i++;
              while(str[i] != '#' && str[i] != '&'){
                origin_str += str[i];
                i++;
              }
              origin2 = origin_str.toInt();
              Serial.println(origin2);
              i--;
            }
            
            else if (str[i] == 'h'){
              Serial.println("ninety_2: ");
            }
            
            else if (str[i] == 'm'){
              Serial.print("Motor1: ");
              mode = 1;
              angle1_str = "";
              i++;
              while(str[i] != '#' && str[i] != '&'){
                angle1_str += str[i];
                i++;
              }
              angle1 = angle1_str.toInt();
              Serial.println(angle1);
              i--;
            }
            
            else if (str[i] == 'n'){
              Serial.print("Motor2: ");
              mode = 1;
              angle2_str = "";
              i++;
              while(str[i] != '#' && str[i] != '&'){
                angle2_str += str[i];
                i++;
              }
              angle2 = angle2_str.toInt();
              Serial.println(angle2);
              i--;
            }
            
            else{
              Serial.println("NONO");
            }
          }
          else if (str[i] == '&'){
            Serial.println("End");
            break;
          }
          else {
            Serial.println("WTF");
            break;
          }
        }
        Serial.println("");
        str = "";

        if (mode == 1){
          move_motor();
        }
        
      }
  }
  
}

void move_motor(){  
  if (angle1 > MAX_ANGLE1){angle1 = MAX_ANGLE1;}
  else if (angle1 < MIN_ANGLE1){angle1 = MIN_ANGLE1;}
  
  if (angle2 > MAX_ANGLE2){angle2 = MAX_ANGLE2;}
  else if (angle2 < MIN_ANGLE2){angle2 = MIN_ANGLE2;}
  
  Serial.print("Received: ");
  Serial.print(angle1);
  Serial.print(", ");
  Serial.println(angle2);

  int angle1_write = angle1-(90.0-origin1);
  int angle2_write = (angle2-(90.0-origin2))*180.0/220.0;
  
  // Speed Control with VarSpeedServo Library
  
  servo1.write(angle1_write, 20, false);
  servo2.write(angle2_write, 20, false);
}
