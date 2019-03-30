void setup(){
    pinMode(A0, INPUT_PULLUP);
    pinMode(A1, INPUT_PULLUP);
    pinMode(A2, INPUT_PULLUP);
    pinMode(A3, INPUT_PULLUP);
    pinMode(A4, INPUT_PULLUP);
    pinMode(A5, INPUT_PULLUP);
    pinMode(A6, INPUT_PULLUP);
    pinMode(A7, INPUT_PULLUP);

    Serial.begin(115200);
}

void loop() {
    String vals = "";
    vals += analogRead(A0);
    vals += ',';
    vals += analogRead(A1);
    vals += ',';
    vals += analogRead(A2);
    vals += ',';
    vals += analogRead(A3);
    vals += ',';
    vals += analogRead(A4);
    vals += ',';
    vals += analogRead(A5);
    vals += ',';
    vals += analogRead(A6);
    vals += ',';
    vals += analogRead(A7);

    Serial.println(vals);

    delay(100);
}

