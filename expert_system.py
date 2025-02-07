"""
Name: Ryan Eisenbeis
Section: CYBR363-001 AI for Cybersecurity
Date: 2/10/25
Description: Assignment 3 - IDS Expert System
"""


def intrusion_detection():

    # Define the knowledge base
    knowledge_base = {
    "brute_force": "If login_attempts > 5 and successful_login = True, then severity = HIGH and Trigger Security Alert",
    "sql_injection": "If sql_attempt = 'yes', then severity = HIGH and Trigger Security Alert",
    "suspicious_login": "If access_time = 'night' and geolocation = 'new', then severity = MEDIUM and Notify Security Team",
    "concurrent_session": "If session_count > 1, then severity = MEDIUM and Notify Security Team",
    "unauthorized_device": "If device_status = 'untrusted', then severity = LOW and Require MFA",
    }

    # Get user input
    login_attempts = int(input("Enter number of failed login attempts: "))

    successful_login = input("Enter successful login (yes/no): ")
    successful_login = successful_login.lower()

    sql_attempt = input("Enter SQL attempt (yes/no): ")
    sql_attempt = sql_attempt.lower()

    access_time = input("Enter access time (day/night): ")
    access_time = access_time.lower()

    geolocation = input("Enter geolocation (same/new): ")
    geolocation = geolocation.lower()

    device_status = input("Enter device status (trusted/untrusted): ")
    device_status = device_status.lower()

    session_count = int(input("Enter number of sessions: "))

    print()

    # Initialize boolean variables
    success = False
    brute_force = False
    sql_attack = False
    suspicious_login = False
    unauthorized_device = False
    concurrent_session = False
    session_alert = False
    trigger_alert = False
    sql_alert = False
    notification = False
    mfa = False
    critical = False

    # List to hold severity levels
    severity_list = []

    # Check Successful Login
    if successful_login == "yes":
        success = True

    # Brute Force Check
    if login_attempts > 5 and success == True:
        brute_force = True
        severity_list.append("HIGH")
        trigger_alert = True

    # SQL Injection Check
    if sql_attempt == "yes":
        sql_attack = True
        severity_list.append("HIGH")
        sql_alert = True

    # Suspicious Login Check
    if access_time == "night" and geolocation == "new":
        suspicious_login = True
        severity_list.append("MEDIUM")
        notification = True

    # Unauthorized Device Check
    if device_status == "untrusted":
        unauthorized_device = True
        severity_list.append("LOW")
        mfa = True

    # Check Concurrent Sessions
    if session_count > 1:
        concurrent_session = True
        severity_list.append("MEDIUM")
        session_alert = True

    # Check Critical Vulnerability
    if (successful_login == "yes" and login_attempts > 5 and success == True and sql_attempt == "yes" and
        access_time == "night" and geolocation == "new" and device_status == "untrusted" and session_count > 1):
        critical = True
        severity_list.append("CRITICAL")

    # Check Severity Level
    if "CRITICAL" in severity_list:
        severity = "CRITICAL SEVERITY"
        print("[ALERT] " + severity + " Intrusion Detected!")
    elif "HIGH" in severity_list:
        severity = "HIGH SEVERITY"
        print("[ALERT] " + severity + " Intrusion Detected!")
    elif "MEDIUM" in severity_list:
        severity = "MEDIUM SEVERITY"
        print("[ALERT] " + severity + " Intrusion Detected!")
    elif "LOW" in severity_list:
        severity = "LOW SEVERITY"
        print("[ALERT] " + severity + " Intrusion Detected!")
    else:
        print("No Intrusion Detected!")

    # Check if a brute force attack is detected
    if brute_force:
        print("- Brute Force Attack: Yes")
    else:
        print("- Brute Force Attack: No")

    # Check if an SQL injection attack is detected
    if sql_attack:
        print("- SQL Injection Attack: Yes")
    else:
        print("- SQL Injection Attack: No")

    # Check if a suspicious login attempt is detected
    if suspicious_login:
        print("- Suspicious Login: Yes")
    else:
        print("- Suspicious Login: No")

    # Check if an unauthorized device is detected
    if unauthorized_device:
        print("- Unauthorized Device: Yes")
    else:
        print("- Unauthorized Device: No")

    # Check if there is more than one session active for an individual device
    if concurrent_session:
        print("- Concurrent Session: Yes")
    else:
        print("- Concurrent Session: No")

    # Check the type of security alert detected
    if critical:
        print("- Security Alert: Critical Vulnerability - Immediate Action Required!")
    elif trigger_alert or sql_alert:
        print("- Security Alert: Trigger Security Alert!")
    elif notification or session_alert:
        print("- Security Alert: Send Notification to Security Team")
    elif mfa:
        print("- Security Alert: Require Multi-Factor Authentication")
    else:
        print("- Security Alert: No Security Alert")


if __name__ == '__main__':
    intrusion_detection()
