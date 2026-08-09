#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <time.h>
#include <pthread.h>
#include <signal.h>

int main() {
    int num1, num2, num3;
    bool result0;
    bool result;
    // printf("Enter three integers:", num1, num2, num3);
    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    result0 = (num1 > num2) > num3; 
    printf("the wrong expression of (%d>%d)>%d is: %d\n", num1, num2, num3, result0);
    result = (num1 > num2) && (num2 > num3);
    printf("the result of %d>%d>%d is: %d\n", num1, num2, num3, result);
    return 0; 
}