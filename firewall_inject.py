from traffic_rule import TrafficRule
from target_platform import TargetPlatform
from target_platform import PLATFORM_AWS, PLATFORM_AZURE, PLATFORM_GOOGLE, PLATFORM_VMware
from google_cloud_inject import inject_rule_google
from aws_inject import inject_rule_aws


def inject_firewall_rules(firewall_rules, target_platform):

    for rule in firewall_rules:    
        if target_platform.platform_type == PLATFORM_GOOGLE:
            inject_rule_google(rule, target_platform)
        elif target_platform.platform_type == PLATFORM_AWS:
            inject_rule_aws(rule, target_platform)