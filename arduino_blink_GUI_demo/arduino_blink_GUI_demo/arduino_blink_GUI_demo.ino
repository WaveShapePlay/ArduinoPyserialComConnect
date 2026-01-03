char userInput; // Stores the user input for command interpretation

void setup(){
  Serial.begin(9600);                        // Serial BAUD rate
  pinMode(LED_BUILTIN, OUTPUT);              // Default Arduino function for Pin Mode
}

void loop(){
if(Serial.available()> 0){                   // Detect incoming byte loop until detected
    userInput = Serial.read();               // Read incoming byte
      if(userInput == 'o'){                  // Turn LED on if 'o' is received
        digitalWrite(LED_BUILTIN, HIGH); 
      }
      if(userInput == 'x'){                  // Turn LED off if 'x' is received
       digitalWrite(LED_BUILTIN, LOW);         
      }
  } 
}