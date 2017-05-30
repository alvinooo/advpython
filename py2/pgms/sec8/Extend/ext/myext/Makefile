# Makefile for C functions

CC = gcc
CFLAGS = -O
.c.o:
	$(CC) $(CFLAGS) -c $<
.c:
	$(CC) $(CFLAGS) $< -o $@

PGMS = main
all: $(PGMS)

main: main.o myfuncs.o
	$(CC) $(CFLAGS) main.o myfuncs.o -o main
main.o myfuncs.o: myfuncs.h

clean:
	rm -rf $(PGMS) a.out core *.o
