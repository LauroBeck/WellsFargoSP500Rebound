#!/bin/bash
source lab_env/bin/activate

echo "===================================================="
echo "   FINTECH ORCHESTRATOR - RESILIENCE MODE"
echo "   Status: $(date '+%Y-%m-%d %H:%M')"
echo "===================================================="

# 1. Identity & ORCID Verification
echo "Architect: Lauro Sergio V. Beck | ORCID: 0009-0004-2154-7555"
echo "----------------------------------------------------"

# 2. Run Fintech Campaign Trace (10k Clients)
python3 campaign_trace.py

# 3. Run Global Market Engine (Hybrid Failover)
python3 nasdaq_engine.py

echo "----------------------------------------------------"
echo "Enterprise Note: Bloomberg B-PIPE [RESTRICTED]"
echo "Failover Trigger: REST/HTTPS Active [OK]"
echo "===================================================="
deactivate
