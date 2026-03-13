import time
from datetime import datetime

def initiate_pisp_transfer(amount, source_bic, target_bic):
    print(f"\n{'='*60}")
    print(f"🏦 PISP PAYMENT INITIATION | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    print(f"SENDER:   {source_bic} (JPMorgan Chase)")
    print(f"RECEIVER: {target_bic} (Wells Fargo Treasury)")
    print(f"AMOUNT:   ${amount:,.2f} USD")
    print(f"REFERENCE: HORMUZ_HEDGE_MARCH_2026")
    print(f"{'-'*60}")
    
    steps = [
        "Initiating OAuth2.0 Consent Flow...",
        "Validating Source Liquidity (JPM)...",
        "Authorizing via Multi-Factor (MFA) - SMS/Token Verified...",
        "Broadcasting ISO 20022 Message to Clearing House...",
        "Target Credit Confirmed (WFB)..."
    ]
    
    for step in steps:
        time.sleep(0.8)
        print(f"[PROCESS] {step}")
        
    print(f"{'-'*60}")
    print(f"✅ STATUS: PAYMENT SUCCESSFUL")
    print(f"✅ TRANSACTION ID: OB-TXN-8849-2026-X")
    print(f"{'='*60}\n")

# Target 10% of .55M
hedge_amount = 855000.00
initiate_pisp_transfer(hedge_amount, "CHASUS33", "WELSUS66")
