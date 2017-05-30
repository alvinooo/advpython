# Makefile for Python embedding

CC = gcc
CFLAGS = -I/usr/include/python2.7 -Wall
LDFLAGS = -lpython2.7
.c.o:
	$(CC) $(CFLAGS) -c $<
.c:
	$(CC) $(CFLAGS) $< -o $@

PGMS = mypython mypython1 mypython2 mypython3 
all: $(PGMS)
 
mypython: mypython.o
	$(CC) mypython.o -o mypython $(LDFLAGS)

mypython1: mypython1.o
	$(CC) mypython1.o -o mypython1 $(LDFLAGS)

mypython2: mypython2.o
	$(CC) mypython2.o -o mypython2 $(LDFLAGS)

mypython3: mypython3.o
	$(CC) mypython3.o -o mypython3 $(LDFLAGS)
mypython3.o: RunTime.h

clean:
	rm -rf $(PGMS) a.out core *.o
