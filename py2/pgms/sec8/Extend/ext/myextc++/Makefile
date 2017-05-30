# Makefile for C functions

CC = g++
CFLAGS = -O
.c.o:
	$(CC) $(CFLAGS) -c $<
.c:
	$(CC) $(CFLAGS) $< -o $@
.cpp.o:
	$(CC) $(CFLAGS) -c $<
.cpp:
	$(CC) $(CFLAGS) $< -o $@

PGMS = main
all: $(PGMS)

main: main.o
	$(CC) $(CFLAGS) main.o -o main
main.o: MyClass.h

clean:
	rm -rf $(PGMS) a.out core *.o
