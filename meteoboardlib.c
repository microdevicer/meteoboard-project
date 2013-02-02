
/**************************************************

meteobardlib.c
библиотека для работы с устройством meteoboard
v.0.1

**************************************************/

#include <stdlib.h>
#include <stdio.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include "rs232.h"

//unsigned char buf[4096];

int getMeteoBoard_port(void)
{
    return 21; // пока не удалось получить нужный порт в автоматическом режиме
    usleep(10000);
}

int getDHT11_temp(unsigned char cport_num)
{
    int i, n= 0;
    unsigned char buf[64];
    unsigned char data[7];

    SendByte(cport_num, 4);
    SendByte(cport_num, 1);
    SendByte(cport_num, 10);

    usleep(50000);

    n = PollComport(cport_num, buf, 64);
    for(i=0;i<2;i++)
    {
        data[i] = (char *)buf[i + 3 + 1 + 3 +1];
    }
    usleep(50000);
    return atoi(data);
}

int getDHT11_Hum(unsigned char cport_num)
{
    int i, n = 0;
    unsigned char buf[64];
    unsigned char data[7];

    SendByte(cport_num, 4);
    SendByte(cport_num, 2);
    SendByte(cport_num, 10);

    usleep(50000);

    n = PollComport(cport_num, buf, 64);
    for(i=0;i<2;i++)
    {
        data[i] = (char *)buf[i + 3 + 1 + 3 +1];
    }
    usleep(50000);
    return atoi(data);
}

int getBMP085_temp(unsigned char cport_num)
{
    int i, n = 0;
    unsigned char buf[64];
    unsigned char data[7];

    SendByte(cport_num, 5);
    SendByte(cport_num, 1);
    SendByte(cport_num, 10);

    usleep(50000);

    n = PollComport(cport_num, buf, 64);
    for(i=0;i<3;i++)
    {
        data[i] = (char *)buf[i + 3 + 1 + 3 +1];
    }
    usleep(50000);
    return atoi(data);
}

int getBMP085_pressure(unsigned char cport_num)
{
    int i, n = 0;
    unsigned char buf[64];
    unsigned char data[7];

    memset (buf, 0, sizeof(buf));

    SendByte(cport_num, 5);
    SendByte(cport_num, 3);
    SendByte(cport_num, 10);

    usleep(50000);

    n = PollComport(cport_num, buf, 64);
    for(i=0;i<5;i++)
    {
        data[i] = (char *)buf[i + 3 + 1 + 3 +1];
    }
    memset (buf, 0, sizeof(buf));
    usleep(50000);
    return atoi(data);
}

int getBMP085_altitude(unsigned char cport_num)
{
    int i, n = 0;
    unsigned char buf[64];
    unsigned char data[7];

    SendByte(cport_num, 5);
    SendByte(cport_num, 4);
    SendByte(cport_num, 10);

    usleep(50000);

    n = PollComport(cport_num, buf, 64);
    for(i=0;i<3;i++)
    {
        data[i] = (char *)buf[i + 3 + 1 + 3 +1];
    }
    usleep(50000);
    return atoi(data);
}

