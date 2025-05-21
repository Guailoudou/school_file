#include <reg51.h>
#include <intrins.h>
#define uint unsigned int
#define uchar unsigned char
	void delay(uint z);
uchar count=0;
uchar i=0;
uchar code LEDlist[] = {0x3f,0x06,0x5b,0x4f,0x66,0x6f,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71};
uchar code xh[] = {1,3,7,2,2,7};
void main()
{
    TMOD=0x10;
    TH1=(65536 - 10000)/256; // Éè50ms³õÖµ
    TL1=(65536 - 10000)%256;
    EA=1;
    ET1=1;
    TR1=1;
    P1=0x01;
	//P2 = LEDlist[xh[i]];
    while(1){
		//delay(2);
		
		}
}

void timer1() interrupt 3
{
    TH1=(65536-9500)/256;
    TL1=(65536-9500)%256;
    count++;
    if (count>=2) {
      //count=0;
			P2 = ~LEDlist[xh[i]];
			
      
			P1=_crol_(P1,1);
			i++;
			if(i>=6){
			i=0;
			P1=0x01;
				 //count=0;
			}
			
    }
}
void delay(uint z){
	uint x,y;
	for(x=z;x>0;x--)
		for(y=100;y>0;y--);
}
//ÄßºÆ¶«202210137227