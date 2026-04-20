import requests

def get_mclaren_status():
    # Attempting to pull from the 2026 live telemetry mirror
    try:
        # 2026 Season Constructor Standings Endpoint
        url = "https://api.jolpi.ca/ergast/f1/2026/constructorStandings"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            standings = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
            mclaren = next(item for item in standings if item["Constructor"]["constructorId"] == "mclaren")
            
            pos = mclaren.get('position', 'N/A')
            pts = mclaren.get('points', '0')
            wins = mclaren.get('wins', '0')
            return f"Pos:{pos} | Pts:{pts} | Wins:{wins}"
        
        return "McLaren Engine: Connecting..."
    except Exception:
        # Fallback to a static placeholder if the API is in maintenance between races
        return "Season Status: Active | Data: Re-syncing"

if __name__ == "__main__":
    print(get_mclaren_status())
