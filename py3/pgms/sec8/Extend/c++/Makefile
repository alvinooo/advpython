# makefile for shared dynamic libraries

CC = g++
CFLAGS = -fPIC -Wall
LDFLAGS = -shared
%.o: %.cpp
	$(CC) $(CFLAGS) -c $<

TARGET = libcpp.so
SOURCES = $(wildcard *.cpp)
HEADERS = $(wildcard *.h)
OBJECTS = $(SOURCES:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(LDFLAGS) $(CFLAGS) -o $(TARGET) $(OBJECTS)

clean:
	rm -f $(TARGET) *.o core a.out
