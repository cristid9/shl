from pprint import pprint
from googleapiclient import discovery

def generate_firewall_body(rule):
    
    # build the body of the rule to inject in the firewall
    body = {}
    body["sourceRanges"] = [rule.cidr_block]
    body["allowed"] = {
        "IPProtocol": rule.protocol,
        "ports": [
            rule.port_range_start,
            rule.port_range_end
        ]
    }

    return body

def inject_rule_google(rule, target_platform):
    service = discovery.build(target_platform.service, target_platform.service_version, credentials=target_platform.credentials)

    firewall_body = generate_firewall_body(rule)

    request = service.firewalls().insert(project=target_platform.project_name, body=firewall_body)
    response = request.execute()

    pprint(response)