### scanner to-do list

1. **define target input**
   - implement command-line argument parsing *
   - allow user to input a URL *

2. **send http request**
   - use the net/http package to send GET requests
   - handle response and errors

3. **check response status**
   - log the HTTP status code
   - categorize responses (e.g., 200, 404, 500)

4. **scan for common vulnerabilities**
   - create a list of endpoints to test (e.g., /admin, /login)
   - check for existence of these endpoints by sending requests

5. **check for open ports**
   - implement a simple TCP port scanner
   - check common ports (e.g., 80, 443, 22)

6. **output results**
   - format and display the findings clearly
   - log findings to a file if desired

7. **implement basic error handling**
   - handle network errors gracefully
   - provide user-friendly error messages

8. **add comments and documentation**
   - comment your code for clarity
   - write a README file explaining usage

9. **test and refine**
    - test the scanner on various websites (with permission!)
    - refine based on feedback and findings

