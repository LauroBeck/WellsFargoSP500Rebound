#!/bin/bash
echo "Stopping existing gateway services..."
fuser -k 8000/tcp 2>/dev/null
sleep 1

echo "Launching AISP v3.1 Multi-Bank Gateway..."
python3 bny_test_project/src/mock_gateway.py &
sleep 3

echo "Executing Treasury Audit..."
# Run the audit logic we just perfected
python3 -c "
import requests
BASE_URL = 'http://localhost:8000/open-banking/v3.1/aisp'
total = 0
for b_id in ['JPM', 'BNY', 'WFB']:
    acc = requests.get(f'{BASE_URL}/accounts', headers={'x-fapi-financial-id': b_id}).json()['Data']['Account'][0]
    bal = requests.get(f'{BASE_URL}/accounts/{acc[\"AccountId\"]}/balances').json()['Data']['Balance'][0]['Amount']['Amount']
    total += float(bal)
    print(f'Verified {b_id} ({acc[\"Servicer\"][\"Identification\"]}): ${float(bal):,.2f}')
print(f'--- TOTAL LIQUIDITY: ${total:,.2f} ---')
"
