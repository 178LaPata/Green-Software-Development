NTIMES=10
FIBREC=20

export NTIMES

compile:
	/usr/bin/gcc -O0 fibonacciRecursiva.c -o fibonacciRecursiva_run
	
measure:
	sudo modprobe msr
	sudo ../../../RAPL/main "./fibonacciRecursiva_run $(FIBREC)" C fibonacciRecursiva $(NTIMES)

run:
	./FIBREC_run $(FIBREC)

mem: 
	{ /usr/bin/time -v ./fibonacciRecursiva_run $(FIBREC) > /dev/null; } 2>&1 | grep "Maximum resident" #| sed "s/[^0-9]\+\([0-9]\+\).*/\1/"

clean:
	rm -f fibonacciRecursiva_run