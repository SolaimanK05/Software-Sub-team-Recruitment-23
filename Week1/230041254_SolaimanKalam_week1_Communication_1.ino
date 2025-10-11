
int channels[8] = {1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500}; // Default center values which are neutral positions
String buffer = "";

void readChannel() {
    while (Serial1.available() > 0) {
        char c = Serial1.read();
        buffer += c;
    }
    
    int startIndex = buffer.indexOf('<');
    int endIndex = buffer.indexOf('>');
    
    if (startIndex >= 0 && endIndex > startIndex) {
        String message = buffer.substring(startIndex + 1, endIndex);
        buffer = buffer.substring(endIndex + 1);
        
        int channelIndex = 0;
        int startPos = 0;
        
        for (int i = 0; i <= message.length() && channelIndex < 8; i++) {
            if (i == message.length() || message.charAt(i) == ' ') {    // Checks if we are at the end of the message or a space is encountered 
                if (startPos < i) { 
                    String valueStr = message.substring(startPos, i);
                    channels[channelIndex] = valueStr.toInt();
                    channelIndex++;
                }
                startPos = i + 1;
            }
        }
    }
}