# makefile for shared dynamic libraries

CC = gcc
CFLAGS = -fPIC -Wall
LDFLAGS = -shared
%.o: %.c
	$(CC) $(CFLAGS) -c $<

TARGET = mylib.so
SOURCES = $(wildcard *.c)
HEADERS = $(wildcard *.h)
OBJECTS = $(SOURCES:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(LDFLAGS) $(CFLAGS) -o $(TARGET) $(OBJECTS)

clean:
	rm -f $(TARGET) *.o core a.out
