
/* usage: ./send <channel> <switch no> <state>
 * State is 0 for OFF and 1 for ON
 */

#include "RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>
#include "cmdSend.h"


int main(int argc, char *argv[]) {

    /*
     output PIN is hardcoded for testing purposes
     see https://projects.drogon.net/raspberry-pi/wiringpi/pins/
     for pin mapping of the raspberry pi GPIO connector
     */
    int PIN = 0;
    char* cmd = argv[1];
    char* channel = argv[2];
    char* sw = argv[3];
    char* state  = argv[4];

    if (wiringPiSetup () == -1) return 1;

    printf("sending cmd[%s] channel[%s] sw[%s] state[%s]\n", cmd, channel, sw, state);
    RCSwitch mySwitch = RCSwitch();
    mySwitch.enableTransmit(PIN);
    

    
    printf("Envoie de %s\n", genCastoTrame(*channel, *sw, *state));
    mySwitch.send(genCastoTrame(*channel, *sw, *state));
    return 0;
}

