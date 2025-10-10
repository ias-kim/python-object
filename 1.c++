#include <stdio.h>

int main(void)
{
    char a = 'f';
    char str[20] = "BlockDMask";
    char* PStr = str;
    int num1 = 10;
    int num2 = 20;

    printf("문자 출력: %c\n", a);
    printf("문자열 출력: %s\n", str);

    printf("10진 정수 출력(부호0) : %d\n", num1);
    printf("10진 정수 출력(부호X) : %d\n", num2);
    printf("10진 정수 출력(부호X) : %u\n", num1);

}