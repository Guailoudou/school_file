#include<reg51.h> //����51��Ƭ�������ͷ�ļ�
#include<absacc.h> //������Ե�ַ���ʵ�ͷ�ļ�
#define uchar unsigned char 
void main(){
	uchar i;
	for(i=0;i<=15;i++){
		XBYTE[0x2000+i]=i;
	}
}
//202210137227 �ߺƶ�