from fastapi import FastAPI, Header, HTTPException
from datetime import datetime

app = FastAPI()

# DATABASE ALIGNMENT
ACCOUNTS = {
    "ACC-JPM-001": {"Balance": 4850000.00, "BIC": "CHASUS33", "Bank": "JPM"},
    "ACC-BNY-002": {"Balance": 2500000.00, "BIC": "BONYUS33", "Bank": "BNY"},
    "ACC-WFB-003": {"Balance": 1200000.00, "BIC": "WELSUS66", "Bank": "WFB"}
}

@app.get("/open-banking/v3.1/aisp/accounts")
async def get_accounts(x_fapi_financial_id: str = Header(None)):
    filtered = []
    for acc_id, data in ACCOUNTS.items():
        if not x_fapi_financial_id or data["Bank"] == x_fapi_financial_id:
            filtered.append({
                "AccountId": acc_id,
                "Servicer": {"Identification": data["BIC"]}
            })
    return {"Data": {"Account": filtered}}

@app.get("/open-banking/v3.1/aisp/accounts/{AccountId}/balances")
async def get_balances(AccountId: str):
    if AccountId not in ACCOUNTS:
        raise HTTPException(status_code=404, detail="Account Not Found")
    return {
        "Data": {"Balance": [{"Amount": {"Amount": str(ACCOUNTS[AccountId]["Balance"])}}]}
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
