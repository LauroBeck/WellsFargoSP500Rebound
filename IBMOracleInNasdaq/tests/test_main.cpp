#include <iostream>
#include <cassert>
#include <cmath>
#include "../src/utils/EarningsParser.cpp"

void test_surprise_calculation() {
    double reported = 4.52;
    double consensus = 4.33;
    double expected_surprise = 4.38799; // roughly 4.39%
    
    double result = EarningsParser::calculate_surprise(reported, consensus);
    
    // Check if result is within 0.01 tolerance
    if (std::abs(result - expected_surprise) < 0.01) {
        std::cout << "[PASS] Earnings Surprise Calculation" << std::endl;
    } else {
        std::cout << "[FAIL] Expected ~4.39, got " << result << std::endl;
    }
}

int main() {
    std::cout << "--- Running Unit Tests ---" << std::endl;
    test_surprise_calculation();
    return 0;
}
