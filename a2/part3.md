# Part 3

Websites like Google and Facebook are not vulnerable to the SSLStripping attack. Investigate why, answer these questions (2 points per question):

___

- What is the name of the counter-measure used by these websites? (fullname and abbreviation only)

[your answer goes here]

___HTTP Strict Transport Security

- Does it affects the HTTP request/response? (check one only)

[ ] The HTTP request only
[ ] The HTTP response only
[X] Both of them
[ ] None of them

___

- Does it requires the web server to do something? If yes, explain what the server does in one short sentence? (check one only and justify it if needed)

[X] Yes, [The server who implemented an HSTS policy will supply a header over an HTTPS connection. That for further connections in a fix time the browser can only connect to the server via https]
[ ] No

___

- Does it requires the client (web browser) to do something? If yes, explain what the client does in one short sentence? (check one only and justify it if needed)

[X] Yes, [The browser must kept the information and make the connection in HTTPS for future connections]
[ ] No

___

Using curl, check whether these two websites given below have this counter-measure deployed. For each of them, justify your answer by providing the relevant part of the curl output only.

- Is it in place at `https://www.utoronto.ca/`?
[X] Yes
[ ] No

[your curl extract goes here]

- Is it in place at `https://www.utsc.utoronto.ca/home/`
[ ] Yes
[X] No

[your curl extract goes here]



