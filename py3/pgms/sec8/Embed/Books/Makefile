# Makefile for Python embedding

CC = gcc
CFLAGS = -I/usr/include/python2.7 -Wall
LDFLAGS = -lpython2.7
.c.o:
	$(CC) $(CFLAGS) -c $<
.c:
	$(CC) $(CFLAGS) $< -o $@

PGMS = mybooks1 mybooks2
all: $(PGMS)
 
mybooks1: mybooks1.o
	$(CC) mybooks1.o -o mybooks1 $(LDFLAGS)

mybooks2: mybooks2.o
	$(CC) mybooks2.o -o mybooks2 $(LDFLAGS)
mybooks2.o: RunTime.h

clean:
	rm -rf $(PGMS) a.out core *.o
