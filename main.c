

/**************************************************


выводим данные с meteoboard в консоль

**************************************************/

#include <stdlib.h>
#include <stdio.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include "rs232.h"
#include "meteoboard.h"

int main()
{
  int cport_nr, bdrate=19200;

  cport_nr = getMeteoBoard_port(); // получаем порт(функция заглушка)

  if(OpenComport(cport_nr, bdrate)) // пробуем открыть порт, не открывается завершаем работу
  {
    printf("Can not open comport\n");
    return(0);
  }

  while(1)
  {
    printf("%d %d %d %d %d\n",getDHT11_temp(cport_nr), getDHT11_Hum(cport_nr), getBMP085_temp(cport_nr),getBMP085_pressure(cport_nr), getBMP085_altitude(cport_nr));
  }
  return 0;
}
