#include <iostream>
#include <cassert>
#include "volatility_regime.h"

void test_threshold_logic() {
    std::cout << "Running Threshold Logic Tests..." << std::endl;

    // Test Case 1: Below Threshold (Stress Index 1.5)
    double low_risk = MarketRisk::calculate_gap_risk(1.5);
    assert(low_risk == 1.12);
    std::cout << " [PASS] Low Risk Threshold (1.12x)" << std::endl;

    // Test Case 2: Above Threshold (Stress Index 2.5)
    double high_risk = MarketRisk::calculate_gap_risk(2.5);
    assert(high_risk == 1.45);
    std::cout << " [PASS] High Risk Threshold (1.45x)" << std::endl;

    // Test Case 3: Edge Case (Exactly 2.0)
    // Based on (stress_idx > 2.0), 2.0 should return the low risk value
    double edge_case = MarketRisk::calculate_gap_risk(2.0);
    assert(edge_case == 1.12);
    std::cout << " [PASS] Edge Case Threshold (2.0)" << std::endl;

    std::cout << "ALL TESTS PASSED: Volatility Engine is Stable." << std::endl;
}

int main() {
    test_threshold_logic();
    return 0;
}
