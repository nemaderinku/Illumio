import pandas as pd
class firewall:
    def __init__(self, filename):
        self.df = pd.DataFrame(pd.read_csv(filename, header=None))
    def accept_packet(self, direction, protocol, port, ip_address):
        for i in self.df:
            if self.df.iloc[i][0] == direction and self.df.iloc[i][1] == protocol:
                rule_port = str(self.df.iloc[i][2])
                rule_ports = None
                if rule_port.count("-") > 0:
                    rule_ports = rule_port.split("-")
                rule_ip = str(self.df.iloc[i][3])
                rule_ips = None
                if rule_ip.count("-") > 0:
                    rule_ips = rule_ip.split("-")
                port_test = False
                if rule_ports and int(rule_ports[0]) <= int(port) <= int(rule_ports[1]):
                    port_test = True
                elif not rule_ports and port == int(rule_port):
                    port_test = True
                if port_test:
                    if rule_ips:
                        ips1 = rule_ips[0].split(".")
                        ips2 = rule_ips[1].split(".")
                        test_ips = ip_address.split(".")
                        if int(ips1[0]) <= int(test_ips[0]) <= int(ips2[0]) and int(ips1[1]) <= int(test_ips[1]) <= int(ips2[1]) \
                                and int(ips1[2]) <= int(test_ips[2]) <= int(ips2[2]) and int(ips1[3]) <= int(test_ips[3]) <= int(ips2[3]):
                            return True
                    elif ip_address == rule_ip:
                        return True
        return False

filepath = input("Please enter rules file path:")
if filepath == "":
    filepath = "networkrules.csv"

f = firewall(filepath)
direction = input("Enter packet direction: ")
protocol = input("Enter packet protocol: ")
port = int(input("Enter port: "))
ip = input("Enter ip address: ")
print(f.accept_packet(direction, protocol, port, ip))

# print(f.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
# #true
# print(f.accept_packet("inbound", "udp", 53, "192.168.2.1"))  # matches third rule
# #true
# print(f.accept_packet("outbound", "tcp", 10234, "192.168.10.11")) # matches second rule
# #true
# print(f.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
# #false
# print(f.accept_packet("inbound", "udp", 24, "52.12.48.92"))
# #false