#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

long fibonacci(int n) {
    if (n <= 1) return n;
    
    long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
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
    printf("Fibonacci Linear(%d) = %ld\n", n, result);
    return 0;
}