#include<reg51.h> //引入51单片机定义的头文件
#include<absacc.h> //引入绝对地址访问的头文件
#define uchar unsigned char 
void main(){
	uchar i;
	for(i=0;i<=15;i++){
		XBYTE[0x2000+i]=i;
	}
}
//202210137227 倪浩东