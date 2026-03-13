#include <iostream>
#include <string>

class EarningsParser {
public:
    static double calculate_surprise(double reported, double consensus) {
        if (consensus == 0) return 0.0;
        return ((reported - consensus) / consensus) * 100.0;
    }

    static void log_result(std::string ticker, double reported, double consensus) {
        double surprise = calculate_surprise(reported, consensus);
        printf("[%s] EPS Reported: %.2f | Consensus: %.2f | Surprise: %+.2f%%\n", 
               ticker.c_str(), reported, consensus, surprise);
    }
};
