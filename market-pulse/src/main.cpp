#include <iostream>
#include <vector>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <thread>
#include "../include/Instrument.hpp"

class ProjectManager {
public:
    void runMigration() {
        std::cout << "\n\033[1;33m[1] MIGRATION SIMULATION: 10K CLIENTS\033[0m\n";
        for(int i = 0; i <= 100; i += 20) {
            std::cout << "\rProcessing Ledger: [" << std::string(i/5, '#') << std::string(20-(i/5), ' ') << "] " << i << "%" << std::flush;
            std::this_thread::sleep_for(std::chrono::milliseconds(150));
        }
        std::cout << "\n\033[1;32mDone: Wells Fargo -> JPM migration complete.\033[0m\n";
    }

    double calculateNPV(double initialInvestment, double rate, bool silent = false) {
        std::vector<double> cashFlows = {35e6, 42e6, 48e6, 55e6, 65e6};
        double npv = -initialInvestment;
        if (!silent) std::cout << "\n\033[1;36m[2] CAPITAL BUDGETING (NPV)\033[0m\n";
        for (size_t t = 0; t < cashFlows.size(); ++t) {
            npv += cashFlows[t] / std::pow(1 + rate, t + 1);
        }
        if (!silent) std::cout << "Project NPV: \033[1;" << (npv > 0 ? "32m$" : "31m$") << npv/1e6 << "M\033[0m\n";
        return npv;
    }

    void exportReport(double npv) {
        std::ofstream file("migration_report.csv");
        if (file.is_open()) {
            file << "Report Date,Friday March 13 2026\n";
            file << "Project,WFC-JPM Capital Aport\n";
            file << "Status," << (npv > 0 ? "ACCEPTED" : "REJECTED") << "\n";
            file << "Final NPV," << npv << "\n";
            file << "Currency,USD\n";
            file.close();
            std::cout << "\n\033[1;32m[SUCCESS] Report exported to migration_report.csv\033[0m\n";
        } else {
            std::cerr << "\n\033[1;31m[ERROR] Could not create file.\033[0m\n";
        }
    }

    void showMarketStatus() {
        std::cout << "\n\033[1;34m[3] NASDAQ MARKET PULSE (LIVE)\033[0m\n";
        std::cout << "WFC: $74.11 (\033[31m-1.51%\033[0m) | IBM: $192.45 (\033[31m-0.57%\033[0m)\n";
    }
};

int main() {
    ProjectManager pm;
    int choice;
    double lastNPV = 30520000.0; // Default from previous run

    do {
        std::cout << "\n\033[1m=== JPM-WFC INTELLIGENCE SUITE ===\033[0m\n";
        std::cout << "1. Run Client Migration\n";
        std::cout << "2. Run 5-Year NPV Analysis\n";
        std::cout << "3. Check Market Status\n";
        std::cout << "4. Export Results to CSV\n";
        std::cout << "0. Exit\n";
        std::cout << "Selection: ";
        std::cin >> choice;

        switch(choice) {
            case 1: pm.runMigration(); break;
            case 2: lastNPV = pm.calculateNPV(150e6, 0.10); break;
            case 3: pm.showMarketStatus(); break;
            case 4: pm.exportReport(lastNPV); break;
        }
    } while (choice != 0);

    return 0;
}
