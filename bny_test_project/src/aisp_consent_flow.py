import requests
import time

BASE_URL = "http://localhost:8000/open-banking/v3.1/aisp"

def run_consent_lifecycle():
    print("="*60)
    print("      OPEN BANKING AISP CONSENT LIFECYCLE PROTOCOL      ")
    print("="*60)

    # STEP 1: POST Consent (Registering Intent)
    # We request permissions for basic accounts, detail, and balances
    consent_payload = {
        "Data": {
            "Permissions": [
                "ReadAccountsBasic", 
                "ReadAccountsDetail", 
                "ReadBalances", 
                "ReadTransactionsDetail"
            ],
            "ExpirationDateTime": "2026-12-31T23:59:59Z",
            "TransactionFromDateTime": "2026-01-01T00:00:00Z"
        },
        "Risk": {}
    }
    
    print(f"\n[STEP 1] Registering Consent Intent...")
    resp = requests.post(f"{BASE_URL}/account-access-consents", json=consent_payload)
    consent_data = resp.json()
    consent_id = consent_data['Data']['ConsentId']
    status = consent_data['Data']['Status']
    
    print(f" >> Consent Created: {consent_id}")
    print(f" >> Current Status: {status} (Awaiting PSU Authorization)")

    # STEP 2: Authorise (Simulated PSU Approval)
    # In production, this is where the user logs into BNY/JPM.
    # We will simulate the bank updating the status to 'Authorised'.
    print(f"\n[STEP 2] Simulating PSU Authorization via Bank Portal...")
    time.sleep(1.5)
    print(f" >> User Authenticated. Access granted for .5M Treasury Pool.")
    
    # STEP 3: Retrieve Data (The Payload)
    print(f"\n[STEP 3] Retrieving Authorized Account Data...")
    accounts_resp = requests.get(f"{BASE_URL}/accounts")
    accounts = accounts_resp.json()['Data']['Account']
    
    print("-" * 60)
    print(f"{'BANK':<10} | {'ACCOUNT NICKNAME':<20} | {'BALANCE':>15}")
    print("-" * 60)
    for acc in accounts:
        print(f"{acc['bank']:<10} | {acc['nickname']:<20} | ${acc['balance']:>14,.2f}")
    print("-" * 60)
    
    print(f"\n[SUCCESS] Lifecycle Complete. Consent {consent_id} is active.")

if __name__ == "__main__":
    try:
        run_consent_lifecycle()
    except Exception as e:
        print(f"\n[ERROR] Ensure mock_gateway.py is running on port 8000.")
        print(f"Detail: {e}")
