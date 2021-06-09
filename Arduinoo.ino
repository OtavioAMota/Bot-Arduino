#include "Mouse.h"
#include "Keyboard.h"

String cod;

void setup() {
  Mouse.begin();
  Keyboard.begin();
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()){
    char aux = Serial.read();
    cod += aux;
    delay(10);
  }
  if(cod == "001"){//move para cima
    Mouse.move(0,-10,0);
    cod = "";
  }
  if(cod == "002"){//move para baixo
    Mouse.move(0,10,0);
    cod = "";
  }
  if(cod == "003"){//move para direita
    Mouse.move(10,0,0);
    cod = "";
  }
  if(cod == "004"){//move para esquerda
    Mouse.move(-10,0,0);
    cod = "";
  }
  if(cod == "005"){
    Mouse.click(MOUSE_LEFT);
    cod = "";
  }
  if(cod == "006"){
    Keyboard.println("i");
    cod = "";
  }
}
