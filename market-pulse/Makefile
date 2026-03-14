CXX = g++
CXXFLAGS = -I./include -Wall -std=c++17
TARGET = bin/pulse
SRC = src/main.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

run: all
	./$(TARGET)

clean:
	rm -rf bin/
