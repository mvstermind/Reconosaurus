### Features to Include: (just pick sum)
1. **Directory Bruteforcing**:
   - Already in tool, but add **smart wordlists** generation based on domain content.
   - **Recursive directory scanning** (check deeper nested directories automatically).
   - Option to try different extensions (e.g., `.php`, `.html`, `.bak`, etc.). 

4. **SSL/TLS Analysis**:
   - Scan for weak or outdated SSL/TLS configurations (e.g., check for SSLv3 or RC4 ciphers).
   - Fetch **certificate information**, including expiration dates.

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

    
11. **OS Fingerprinting**:
    - Guess the target’s OS based on open ports, services, and responses (e.g., TTL values, OS banners).

12. **Passive Recon**:
    - Include a module for passive reconnaissance, using public sources like WHOIS, DNS records, etc.

15. **Stealth Mode**:
    - Options to perform stealthy scans, like scanning using fragmented packets, slow scanning (evade detection systems).

16. **Vulnerability Scanner Integration**:
    - Optionally include a built-in **vulnerability scanner** to check for well-known CVEs on services you detect.

