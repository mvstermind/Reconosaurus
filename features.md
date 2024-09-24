### Features to Include: (just pick sum)
1. **Directory Bruteforcing**:
   - Already in tool, but add **smart wordlists** generation based on domain content.
   - **Recursive directory scanning** (check deeper nested directories automatically).
   - Option to try different extensions (e.g., `.php`, `.html`, `.bak`, etc.). 

2. **Port Scanning**:
   - Fast **multi-threaded** port scanning (with TCP and UDP support).
   - **Service detection** on open ports (what services are running, e.g., HTTP, SSH).
   - **Banner grabbing** for service versions.
   - Detect **hidden services** or non-standard ports (services on unusual ports).

3. **Subdomain Enumeration**:
   - Find subdomains through **brute force** or using OSINT methods (APIs like VirusTotal or Shodan).
   - **Resolve IPs** and check for hosting misconfigurations.

4. **SSL/TLS Analysis**:
   - Scan for weak or outdated SSL/TLS configurations (e.g., check for SSLv3 or RC4 ciphers).
   - Fetch **certificate information**, including expiration dates.

5. **Web Application Fingerprinting**:
   - Detect the underlying web framework (e.g., WordPress, Django, Laravel) and possible vulnerabilities.
   - Identify CMS versions and plugins that may be outdated or vulnerable.

6. **File Inclusion Vulnerabilities**:
   - Detect Local File Inclusion (LFI) and Remote File Inclusion (RFI) vulnerabilities.
   - Crawl the web app and test for known patterns.

7. **Directory Traversal**:
   - Look for common directory traversal bugs (e.g., `../../etc/passwd`).
   
8. **DNS Enumeration**:
   - Bruteforce DNS entries and subdomains.
   - Zone transfer test and check for misconfigured DNS settings.

9. **API Reconnaissance**:
   - Enumerate public-facing APIs.
   - Bruteforce common API endpoints or paths.
   - Check for open GraphQL APIs and enumerate their schema.

10. **Screenshot Utility**:
    - Take screenshots of HTTP(S) responses, useful for quickly identifying admin panels, etc.
    
11. **OS Fingerprinting**:
    - Guess the target’s OS based on open ports, services, and responses (e.g., TTL values, OS banners).

12. **Passive Recon**:
    - Include a module for passive reconnaissance, using public sources like WHOIS, DNS records, etc.

13. **Social Engineering Tools**:
    - Build basic utilities for phishing simulations or harvesting public profiles for usernames/emails.

14. **Automation and Reporting**:
    - Generate reports (HTML/PDF format) with the scan results and potential vulnerabilities.
    - Include an option to auto-save the results in a structured format like JSON for later processing.

15. **Stealth Mode**:
    - Options to perform stealthy scans, like scanning using fragmented packets, slow scanning (evade detection systems).

16. **Vulnerability Scanner Integration**:
    - Optionally include a built-in **vulnerability scanner** to check for well-known CVEs on services you detect.

