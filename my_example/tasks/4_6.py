ospf_template = """
Prefix                {}
AD/Metric             {}/{}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ip = ospf_route.split()[0]
# pref = ip.split("/")[-1]
ad = ospf_route.split()[1].split("/")[0].strip("[]")
met = ospf_route.split()[1].split("/")[1].strip("[]")
nh = ospf_route.split()[3].strip(',')
lu = ospf_route.split()[4].strip(',')
oi = ospf_route.split()[-1]

print(ospf_template.format(ip, ad, met, nh, lu, oi))
