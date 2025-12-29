char userInput;

void setup(){
  Serial.begin(9600);                        //  setup serial
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
if(Serial.available()> 0){ 
    userInput = Serial.read();               // read user input
      if(userInput == 'o'){                
        digitalWrite(LED_BUILTIN, HIGH); 
      }
      if(userInput == 'x'){
       digitalWrite(LED_BUILTIN, LOW);         
      }
  } // Serial.available
} // Void Loop