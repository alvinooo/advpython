# Makefile for Python embedding

CC = gcc
CFLAGS = -I/usr/include/python2.7 -Wall
LDFLAGS = -lpython2.7
.c.o:
	$(CC) $(CFLAGS) -c $<
.c:
	$(CC) $(CFLAGS) $< -o $@

PGMS = mypython
all: $(PGMS)
 
mypython: mypython.o
	$(CC) mypython.o -o mypython $(LDFLAGS)
mypython.o: RunTime.h

clean:
	rm -rf $(PGMS) a.out core *.o
