#ifndef INSTRUMENT_HPP
#define INSTRUMENT_HPP
#include <string>

struct Instrument {
    std::string symbol;
    double price;
    double change;
};

struct Bank {
    std::string name;
    std::string symbol;
    double liquidity; // Added this to match main.cpp
    double sharePrice;
};
#endif
