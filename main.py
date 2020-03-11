from traffic_rule import TrafficRule
from target_platform import TargetPlatform
from target_platform import PLATFORM_GOOGLE
from oauth2client.client import GoogleCredentials
from firewall_inject import inject_firewall_rules


if __name__ == "__main__":
    firewall_rules = []

    rule = TrafficRule()
    rule.port_range_end = "8000"
    rule.cird_block = "0.0.0.0/0"
    rule.protocol = "tcp"

    firewall_rules.append(rule)

    platform = TargetPlatform()
    platform.platform_type = PLATFORM_GOOGLE
    platform.credentials = GoogleCredentials.get_application_default()
    platform.service =  "compute"
    platform.project_version = "v1"
    platform.project_name = "shoreline"

    inject_firewall_rules(firewall_rules, platform)