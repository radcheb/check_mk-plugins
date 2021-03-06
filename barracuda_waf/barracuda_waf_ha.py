#!/usr/bin/env python

# Monitor the HA status of a pair of Barracuda WAFs via SNMP
# Herward Cooper <coops@fawk.eu> - 2012

# When run against each of the members of the pair, a response of
# 'Primary:Active' or 'Backup:Standby' is considered healthy.

def inventory_barracuda_waf_ha(checkname, info):
    inventory=[]
    status = info[0][0]
    if status:
        inventory.append( (None, None) )
    return inventory


def check_barracuda_waf_ha(item, params, info):
    state = info[0][0]
    if state == "Primary:Active" or state == "Backup:Standby":
        return (0, "OK - Currently %s" % state)
    else:
        return (2, "CRITICAL - Currently %s" % state)
    return (3, "UNKNOWN - unhandled problem")

check_info["barracuda_waf_ha"] = (check_barracuda_waf_ha, "Barracuda WAF HA Status", 0, inventory_barracuda_waf_ha)

snmp_info["barracuda_waf_ha"] = ( ".1.3.6.1.4.1.20632.8", [ "14" ] )