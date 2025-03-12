#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

long fibonacci(int n){
    if (n <= 1) return n;
    else return fibonacci(n - 1) + fibonacci(n - 2);
}

int main(int argc, char *argv[]) {
    if (argc != 2){
        printf("Usage: %s <n>\n", argv[0]);
        return 1;
    }
    int n = atoi(argv[1]);
    if (n < 0) {
        printf("Value of n must be non-negative.\n");
        return 1;
    }
    long result = fibonacci(n);
    printf("Fibonacci(%d) = %ld\n", n, result);
    return 0;
}
