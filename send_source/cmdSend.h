#ifndef cmdSend_h
#define cmdSend_h

#define CHAN_A "00101010"
#define CHAN_B "10001010"
#define CHAN_C "10100010"
#define CHAN_D "10101000"

#define PRISE_1 "001010"
#define PRISE_2 "100010"
#define PRISE_3 "101000"

//#define PADDING_START "000000000"
#define PADDING_START "0"
#define PADDING_MIDDLE "1010101"

#define CMD_ON "11"
#define CMD_OFF "00"

char* genCastoTrame(char, char, char);


#endif
