#include "cmdSend.h"
#include <string>

using namespace std;


// genere la trame au format binaire à passer à RCSwitch.send(char*) 
// sChan correspond au Channel paramétré sur la prise ("A","B","C","D")    a=1,b=2 etc car je n'arrive pas à le faire avec des char...
// nPrise correspond au numero de la prise (1,2,3)

char* genCastoTrame(char cChan, char cPrise, char cStatus){ 
  static char sReturn[25];
//  Serial.println("******");
//  Serial.println(cChan);
//  Serial.println((int)cChan);
//  Serial.println((int)cChan - 'A');
  int intChan = cChan - (int)'A' + 1; // A-D become 1-4
  int intPrise = cPrise - '0';
  int intStatus = cStatus - '0';
  bool  bStatus = (bool)intStatus;
  string res;
  
//  Serial.println(intChan) ;
//  Serial.println(intPrise) ;
//  Serial.println(intStatus) ;
  
  res = string();
  res = PADDING_START;

  switch(intChan){
      case 1:
          res = res + CHAN_A; break;
      case 2:
          res = res +  CHAN_B; break;
      case 3:
          res = res + CHAN_C; break;
      case 4:
          res = res +  CHAN_D; break;
      default:
          return '\0';
  }
  switch (intPrise){
      case 1:
          res = res + PRISE_1; break;
      case 2:
          res = res +  PRISE_2; break;
      case 3:
          res = res + PRISE_3; break;
      default:
          return '\0';
  }
  res = res + PADDING_MIDDLE;
  switch(bStatus){
      case true:
          res = res + CMD_ON; break;
      case false:
          res = res +  CMD_OFF; break;
      default:
          return '\0';
  }
//  res.toCharArray(sReturn,25);
  res.copy(sReturn, res.length()+1);
  return sReturn;  


}
