REGLAS_TRADUCCION = {
    "HUAWEI_A_CISCO": {
        "regla_system_view": "configure terminal",
        "regla_sysname": "hostname {0}",
        "regla_undo_shutdown": "no shutdown",
        "regla_display_current_configuration": "show running-config",
        "regla_quit": "exit",
        "regla_port_link_type": "switchport mode {0}",
        "regla_port_trunk_allow_pass": "switchport trunk allowed vlan {0}",
        "regla_dot1q_termination": "encapsulation dot1Q {0}",
        "regla_ip_route_static": "ip route {0} {1} {2}",
        "regla_traffic_filter": "ip access-group {1} {0}", # {0}=in/out, {1}=acl
    },
    "CISCO_A_HUAWEI": {
        "regla_configure_terminal": "system-view",
        "regla_hostname": "sysname {0}",
        "regla_no_shutdown": "undo shutdown",
        "regla_show_running_config": "display current-configuration",
        # cisco usa exit, huawei usa quit
        "regla_exit": "quit", 
        "regla_switchport_mode": "port link-type {0}",
        "regla_switchport_trunk_allowed": "port trunk allow-pass vlan {0}",
        "regla_encapsulation": "dot1q termination vid {0}",
        "regla_ip_route": "ip route-static {0} {1} {2}",
        "regla_access_group": "traffic-filter {0} acl {1}" # asumiendo mapeo simple
    }
}
