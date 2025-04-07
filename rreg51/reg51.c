#include<reg51.h> 
#define uint unsigned int
#define uchar unsigned char
void delay(uint z);
void main(){
	uchar code LEDlist[] = {0x3f,0x06,0x5b,0x4f,0x66,0x6f,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71};
	uint xh[] = {2,0,2,2,1,0,1,3,7,2,2,7};
	uchar d1 = 0x01;
	uint i1 = 0;
	while(1){
		d1 = 0x01;
		for(i1=0;i1<6;i1++){
			P3=~d1;P0 = LEDlist[xh[i1]];delay(2);
			d1 = d1 << 1;
		}
		d1 = 0x01;
		for(i1=6;i1<12;i1++){
			P1=d1;P2 = ~LEDlist[xh[i1]];delay(2);
			d1 = d1 << 1;
		}
		
	}
}

void delay(uint z){
	uint x,y;
	for(x=z;x>0;x--)
		for(y=100;y>0;y--);
}
//202210137227 ÄßºÆ¶«