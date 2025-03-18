NTIMES=10
FIBLIN=20

export NTIMES

compile:
	/usr/bin/gcc -O0 fibonacciLinear.c -o fibonacciLinear_run
	
measure:
	sudo modprobe msr
	sudo ../../../RAPL/main "./fibonacciLinear_run $(FIBLIN)" C fibonacciLinear $(NTIMES)

run:
	./fibonacciLinear_run $(FIBLIN)

mem: 
	{ /usr/bin/time -v ./fibonacciLinear_run $(FIBLIN) > /dev/null; } 2>&1 | grep "Maximum resident" #| sed "s/[^0-9]\+\([0-9]\+\).*/\1/"

clean:
	rm -f fibonacciLinear_run