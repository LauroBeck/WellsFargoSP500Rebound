import blpapi
import os

def start_enterprise_session():
    # In 2026 Enterprise Mode, we use the Web API Anycast IP
    # Required: Client ID/Secret from Bloomberg Enterprise Console {EC <GO>}
    client_id = os.getenv("BBG_CLIENT_ID", "BBG_ARCHITECT_LAURO")
    
    options = blpapi.SessionOptions()
    options.setServerHost("open-api-anycast.bloomberg.com")
    options.setServerPort(8295)
    options.setAuthenticationOptions(f"AuthenticationType=GRSS;ApplicationName={client_id}")
    
    session = blpapi.Session(options)
    
    # Non-blocking start for cloud-native orchestration
    if not session.start():
        return "Bloomberg Enterprise: Connection Pending (Check IP Allowlist)"
        
    return "Bloomberg Enterprise: LINKED [OK]"

if __name__ == "__main__":
    print(start_enterprise_session())
