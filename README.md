## Firewall Problem
##### Implementation
The solution is implemented using python3. <br/>
firewall.py: implements the solution using dataframe for rules.<br/>
firewall_approach2.py: implements the solution using a static dictionary for saving rules. This will reduce the search time but is not dynamic for protocols.
##### Installations:
pandas (>= 0.25.1)
##### How to Install:
pip install pandas
##### How to Run?
python3 firewall.py<br/>
python3 firewall_approach2.py<br/>
#####Inputs:
Rules file path: Enter full path to csv file containing rules (eg path\\\to\\\file\\\networkrules.csv) If not entered, it is defaulted to networkrules.csv file in the same folder<br/>
direction: Enter packet direction ("inbound" or "outbound")<br/>
protocol: Enter packet protocol ("tcp" or "udp")<br/>
port: Enter port (integer in range [1, 65535])<br/>
ip: Enter ip address (IPv4 address) <br/>

#####Output:
Returns boolean value. True if packet satisfies any of the rules; False otherwise.

