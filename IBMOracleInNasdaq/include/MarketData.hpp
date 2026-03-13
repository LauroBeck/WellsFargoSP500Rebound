#ifndef MARKET_DATA_HPP
#define MARKET_DATA_HPP

#include <string>
#include <chrono>

struct MarketData {
    std::string ticker;
    double price;
    double change_pct;
    double sentiment; // -1.0 to 1.0
    
    void print_status() const {
        printf("[%s] Price: %.2f | Change: %+.2f%% | Sent: %.2f\n", 
               ticker.c_str(), price, change_pct, sentiment);
    }
};

#endif
