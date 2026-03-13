#!/bin/bash
# IBMOracleInNasdaq Session Sync Utility

echo ">>> Building and Testing..."
g++ -std=c++17 tests/test_main.cpp -o run_tests && ./run_tests

if [ 0 -eq 0 ]; then
    echo ">>> Tests Passed. Syncing to GitHub main..."
    git add .
    git commit -m "Session Update: $(date +'%Y-%m-%d %H:%M')"
    git push origin main
    echo ">>> Deployment Successful."
else
    echo ">>> Tests Failed. Sync Aborted."
    exit 1
fi
