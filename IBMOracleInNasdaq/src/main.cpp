#include <iostream>
#include <vector>
#include "../include/MarketData.hpp"
#include "engine/InflectionEngine.cpp"
#include "engine/Sub1nmTracker.cpp"
#include "utils/EarningsParser.cpp"

int main() {
    std::cout << "--- IBMOracleInNasdaq Intelligence Suite ---" << std::endl;

    // 1. Market Intelligence
    MarketData ibm = {"IBM", 248.87, 0.45, 0.65};
    MarketData orcl = {"ORCL", 163.12, 9.15, 0.88};

    std::vector<MarketData> watchlist = {ibm, orcl};

    for (const auto& stock : watchlist) {
        stock.print_status();
        if (InflectionEngine::is_breakout(stock)) {
            std::cout << ">>> ALERT: Breakout Detected for " << stock.ticker << std::endl;
        }
    }

    std::cout << "------------------------------------------" << std::endl;

    // 2. Fundamental & Tech Scaling Analysis
    Sub1nmTracker::log_node_status();
    
    // Simulating Sub-1nm Yield for IBM/Lam Partnership
    Sub1nmTracker::YieldMetrics ibm_yield = {50.0, 1.25, 0.15}; // 50% mask reduction, 1.25x High-NA efficiency
    double projected_yield = Sub1nmTracker::predict_yield(ibm_yield);
    
    std::cout << "Projected Manufacturing Yield: " << projected_yield << "%" << std::endl;
    EarningsParser::log_result("IBM", 4.52, 4.33);

    std::cout << "------------------------------------------" << std::endl;

    return 0;
}
