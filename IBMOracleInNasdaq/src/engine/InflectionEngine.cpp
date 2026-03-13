#include <vector>
#include <string>
#include "../../include/MarketData.hpp"

class InflectionEngine {
public:
    static bool is_breakout(const MarketData& data, double threshold = 5.0) {
        return data.change_pct >= threshold;
    }

    static std::string analyze_sentiment(const MarketData& data) {
        if (data.sentiment > 0.5) return "STRONG_BULL";
        if (data.sentiment < -0.5) return "BEARISH_DIVERGENCE";
        return "NEUTRAL";
    }
};
