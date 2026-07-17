grammar Expr;

// Reglas Sintacticas
archivo_configuracion: linea_configuracion+ EOF;

linea_configuracion
    : regla_configure_terminal
    | regla_conf
    | regla_hostname
    | regla_domain_name
    | regla_aaa
    | regla_username
    | regla_enable_secret
    | regla_crypto_key
    | regla_line_vty
    | regla_transport_input
    | regla_login
    | regla_password
    | regla_interface_range
    | regla_interface
    | regla_description
    | regla_ip_address
    | regla_no_shutdown
    | regla_undo_shutdown
    | regla_encapsulation
    | regla_switchport_trunk_allowed
    | regla_switchport_mode
    | regla_ipv6_address_eui64
    | regla_ipv6_address
    | regla_router_ospf
    | regla_network
    | regla_ip_route
    | regla_ip_route_static
    | regla_access_list
    | regla_access_group
    | regla_show_running_config
    | regla_system_view
    | regla_port_trunk_allow_pass
    | regla_port_link_type
    | regla_dot1q_termination
    | regla_vlan
    | regla_quit
    | regla_ospf
    | regla_area
    | regla_acl
    | regla_acl_rule
    | regla_traffic_filter
    | regla_display_current_configuration
    | regla_sysname
    | regla_switchport_access_vlan
    | regla_port_default_vlan
    | regla_ping
    | regla_crypto_pki_trustpoint
    | regla_pki_entity
    | regla_logging_host
    | regla_info_center_loghost
    ;

regla_configure_terminal: CONFIGURE TERMINAL;
regla_conf: CONF ID;

regla_hostname: HOSTNAME ID;
regla_domain_name: IP ID ID PUNTO ID;
regla_sysname: SYSNAME ID;

regla_aaa: AAA ID;
regla_username: USERNAME ID PRIVILEGE NUMERO SECRET ID;
regla_enable_secret: ENABLE SECRET ID;
regla_crypto_key: CRYPTO KEY GENERATE RSA NUMERO?;

regla_line_vty: LINE VTY NUMERO NUMERO;
regla_transport_input: TRANSPORT INPUT SSH TELNET;
regla_login: LOGIN ID;
regla_password: PASSWORD ID;

regla_interface: INTERFACE ID;
regla_interface_range: INTERFACE RANGO ID GUION NUMERO;

regla_description: DESCRIPTION (ID | CADENA);

regla_ip_address: IP ADDRESS DIRECCION_IPV4 DIRECCION_IPV4;
regla_no_shutdown: NO SHUTDOWN;
regla_undo_shutdown: UNDO SHUTDOWN;

regla_encapsulation: ENCAPSULATION DOT1Q NUMERO NATIVE?;
regla_dot1q_termination: DOT1Q TERMINATION VID NUMERO;

regla_switchport_mode: SWITCH_PORT MODE (ACCESS | TRUNK);
regla_switchport_trunk_allowed: SWITCH_PORT TRUNK ALLOWED VLAN regla_vlan_list;
regla_switchport_access_vlan: SWITCH_PORT ACCESS VLAN NUMERO;
regla_port_link_type: PORT LINK_TYPE (ACCESS | TRUNK);
regla_port_trunk_allow_pass: PORT TRUNK ALLOW_PASS VLAN regla_vlan_list;
regla_port_default_vlan: PORT DEFAULT VLAN NUMERO;
regla_vlan_list: NUMERO (COMA NUMERO)*;
regla_vlan: VLAN NUMERO;

regla_ping: PING DIRECCION_IPV4;

regla_crypto_pki_trustpoint: CRYPTO PKI TRUSTPOINT ID;
regla_pki_entity: PKI ENTITY ID;

regla_logging_host: LOGGING HOST DIRECCION_IPV4;
regla_info_center_loghost: INFO_CENTER LOGHOST DIRECCION_IPV4;

regla_ipv6_address: IPV6 ADDRESS DIRECCION_IPV6 LINK_LOCAL?;
regla_ipv6_address_eui64: IPV6 ADDRESS ID EUI64;

regla_router_ospf: ROUTER OSPF NUMERO;
regla_ospf: OSPF NUMERO;
regla_area: AREA DIRECCION_IPV4;
regla_network: NETWORK DIRECCION_IPV4 (DIRECCION_IPV4 | DIAGONAL NUMERO) (AREA NUMERO)?;

regla_ip_route: IP ROUTE DIRECCION_IPV4 DIRECCION_IPV4 DIRECCION_IPV4;
regla_ip_route_static: IP ROUTE_STATIC DIRECCION_IPV4 DIRECCION_IPV4 DIRECCION_IPV4;

regla_access_list: ACCESS_LIST NUMERO (PERMIT | DENY) (TCP | UDP | ICMP) regla_endpoint regla_endpoint regla_port_operator?;
regla_access_group: IP ACCESS_GROUP NUMERO ID;
regla_port_operator
    : (IGUAL | MAYOR_QUE | MENOR_QUE | DIFERENTE) (NUMERO | HTTPS)
    | RANGO NUMERO NUMERO
    ;

regla_acl: ACL NUMERO;
regla_acl_rule: RULE NUMERO (PERMIT | DENY) (IP | TCP | UDP | ICMP) ID regla_endpoint ID ANY regla_port_qualifier?;
regla_endpoint: ANY | HOST DIRECCION_IPV4 | DIRECCION_IPV4 NUMERO?;
regla_port_qualifier: PORT NEGACION? (IGUAL | MAYOR_QUE | MENOR_QUE | DIFERENTE) NUMERO;
regla_traffic_filter: TRAFFIC_FILTER (INBOUND | OUTBOUND) ACL NUMERO;

regla_show_running_config: SHOW RUNNING_CONFIG;
regla_display_current_configuration: DISPLAY CURRENT_CONFIGURATION;
regla_system_view: SYSTEM_VIEW;
regla_quit: QUIT;

// Reglas Lexicas

// Palabras Rervadas para ambos, Cisco IOS y Huawei VRP
INTERFACE: [iI][nN][tT][eE][rR][fF][aA][cC][eE];
IP: [iI][pP];
IPV6: [iI][pP][vV]'6';
ADDRESS: [aA][dD][dD][rR][eE][sS][sS];
OSPF: [oO][sS][pP][fF];
AREA: [aA][rR][eE][aA];
NETWORK: [nN][eE][tT][wW][oO][rR][kK];
VLAN: [vV][lL][aA][nN];
ACCESS: [aA][cC][cC][eE][sS][sS];
TRUNK: [tT][rR][uU][nN][kK];
PERMIT: [pP][eE][rR][mM][iI][tT];
DENY: [dD][eE][nN][yY];
DESCRIPTION: [dD][eE][sS][cC][rR][iI][pP][tT][iI][oO][nN];
LINK_LOCAL: [lL][iI][nN][kK]'-'[lL][oO][cC][aA][lL];
EUI64: [eE][uU][iI]'-''6''4';
SHUTDOWN: [sS][hH][uU][tT][dD][oO][wW][nN];
QUIT: [qQ][uU][iI][tT];
TCP: [tT][cC][pP];
UDP: [uU][dD][pP];
ICMP: [iI][cC][mM][pP];
SSH: [sS][sS][hH];
TELNET: [tT][eE][lL][nN][eE][tT];
HTTPS: [hH][tT][tT][pP][sS];
PING: [pP][iI][nN][gG];
PKI: [pP][kK][iI];

// Operadores
IGUAL: [eE][qQ];
MAYOR_QUE: [gG][tT];
MENOR_QUE: [lL][tT];
DIFERENTE: [nN][eE][qQ];
RANGO: [rR][aA][nN][gG][eE];
NEGACION: [nN][oO][tT];
ANY: [aA][nN][yY];
HOST: [hH][oO][sS][tT];

// Palabras Reservadas de Cisco IOS
ROUTER: [rR][oO][uU][tT][eE][rR];
SWITCH_PORT: [sS][wW][iI][tT][cC][hH][pP][oO][rR][tT];
MODE: [mM][oO][dD][eE];
ALLOWED: [aA][lL][lL][oO][wW][eE][dD];
ENCAPSULATION: [eE][nN][cC][aA][pP][sS][uU][lL][aA][tT][iI][oO][nN];
NATIVE: [nN][aA][tT][iI][vV][eE];
NO: [nN][oO];
CONFIGURE: [cC][oO][nN][fF][iI][gG][uU][rR][eE];
TERMINAL: [tT][eE][rR][mM][iI][nN][aA][lL];
CONF: [cC][oO][nN][fF];
HOSTNAME: [hH][oO][sS][tT][nN][aA][mM][eE];
ROUTE: [rR][oO][uU][tT][eE];
SHOW: [sS][hH][oO][wW];
RUNNING_CONFIG: [rR][uU][nN][nN][iI][nN][gG]'-'[cC][oO][nN][fF][iI][gG];
ACCESS_LIST: [aA][cC][cC][eE][sS][sS]'-'[lL][iI][sS][tT];
ACCESS_GROUP: [aA][cC][cC][eE][sS][sS]'-'[gG][rR][oO][uU][pP];
LINE: [lL][iI][nN][eE];
VTY: [vV][tT][yY];
TRANSPORT: [tT][rR][aA][nN][sS][pP][oO][rR][tT];
INPUT: [iI][nN][pP][uU][tT];
LOGIN: [lL][oO][gG][iI][nN];
USERNAME: [uU][sS][eE][rR][nN][aA][mM][eE];
PASSWORD: [pP][aA][sS][sS][wW][oO][rR][dD];
SECRET: [sS][eE][cC][rR][eE][tT];
ENABLE: [eE][nN][aA][bB][lL][eE];
PRIVILEGE: [pP][rR][iI][vV][iI][lL][eE][gG][eE];
AAA: [aA][aA][aA];
CRYPTO: [cC][rR][yY][pP][tT][oO];
KEY: [kK][eE][yY];
GENERATE: [gG][eE][nN][eE][rR][aA][tT][eE];
RSA: [rR][sS][aA];
TRUSTPOINT: [tT][rR][uU][sS][tT][pP][oO][iI][nN][tT];
LOGGING: [lL][oO][gG][gG][iI][nN][gG];

// Palabras Reservadas de Huawei VRP
PORT: [pP][oO][rR][tT];
LINK_TYPE: [lL][iI][nN][kK]'-'[tT][yY][pP][eE];
ALLOW_PASS: [aA][lL][lL][oO][wW]'-'[pP][aA][sS][sS];
DOT1Q: [dD][oO][tT]'1'[qQ];
TERMINATION: [tT][eE][rR][mM][iI][nN][aA][tT][iI][oO][nN];
VID: [vV][iI][dD];
UNDO: [uU][nN][dD][oO];
SYSTEM_VIEW: [sS][yY][sS][tT][eE][mM]'-'[vV][iI][eE][wW];
SYSNAME: [sS][yY][sS][nN][aA][mM][eE];
ROUTE_STATIC: [rR][oO][uU][tT][eE]'-'[sS][tT][aA][tT][iI][cC];
DISPLAY: [dD][iI][sS][pP][lL][aA][yY];
CURRENT_CONFIGURATION: [cC][uU][rR][rR][eE][nN][tT]'-'[cC][oO][nN][fF][iI][gG][uU][rR][aA][tT][iI][oO][nN];
ACL: [aA][cC][lL];
TRAFFIC_FILTER: [tT][rR][aA][fF][fF][iI][cC]'-'[fF][iI][lL][tT][eE][rR];
INBOUND: [iI][nN][bB][oO][uU][nN][dD];
OUTBOUND: [oO][uU][tT][bB][oO][uU][nN][dD];
RULE: [rR][uU][lL][eE];
DEFAULT: [dD][eE][fF][aA][uU][lL][tT];
ENTITY: [eE][nN][tT][iI][tT][yY];
INFO_CENTER: [iI][nN][fF][oO]'-'[cC][eE][nN][tT][eE][rR];
LOGHOST: [lL][oO][gG][hH][oO][sS][tT];

// Demas reglas lexicas generales

// Identificadores
ID: [a-zA-Z] [a-zA-Z0-9_-]* ('/' [0-9]+)* ('.' [0-9]+)?;

// Direcciones IP
DIRECCION_IPV4: [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+;
DIRECCION_IPV6: [0-9a-fA-F]+ (':' [0-9a-fA-F]*)+ ('/' [0-9]+)?;

// Numeros
NUMERO: [0-9]+;

// Cadenas de texto
CADENA: '"' ~["\r\n]* '"';

// Delimitadores
DIAGONAL: '/';
PUNTO: '.';
COMA: ',';
GUION: '-';
PARENTESIS_IZQ: '(';
PARENTESIS_DER: ')';

// Comentarios
COMENTARIO: ('!' | '#') ~[\r\n]* -> channel(HIDDEN);

// Espacios en blanco
WS: [ \t\r\n]+ -> channel(HIDDEN);
