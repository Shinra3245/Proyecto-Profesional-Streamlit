from ExprVisitor import ExprVisitor

class AnalizadorSemantico(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.errores = []
        self.current_interface = None
        self.ips_assigned = {}
        self.vlans_declared = set()
        self.acls_declared = set()
        self.native_per_physical = {}

    def obtener_errores(self):
        return self.errores

    def visitRegla_interface(self, ctx):
        self.current_interface = ctx.ID().getText()
        return self.visitChildren(ctx)

    def visitRegla_ip_address(self, ctx):
        ip = ctx.DIRECCION_IPV4(0).getText()
        if ip in self.ips_assigned and self.ips_assigned[ip] != self.current_interface:
            self.errores.append({
                "error": f"La dirección IP {ip} ya está asignada a la interfaz {self.ips_assigned[ip]}, no se puede asignar también a {self.current_interface}."
            })
        if self.current_interface:
            self.ips_assigned[ip] = self.current_interface
        return self.visitChildren(ctx)

    def visitRegla_vlan(self, ctx):
        vlan_id = ctx.NUMERO().getText()
        self.vlans_declared.add(vlan_id)
        return self.visitChildren(ctx)

    def _check_vlan(self, vlan_id, rule_name):
        if vlan_id not in self.vlans_declared:
            self.errores.append({
                "error": f"Se está intentando usar la VLAN {vlan_id} en '{rule_name}', pero nunca fue declarada antes."
            })

    def visitRegla_switchport_access_vlan(self, ctx):
        vlan_id = ctx.NUMERO().getText()
        self._check_vlan(vlan_id, "switchport access vlan")
        return self.visitChildren(ctx)

    def visitRegla_switchport_trunk_allowed(self, ctx):
        for num_node in ctx.regla_vlan_list().NUMERO():
            self._check_vlan(num_node.getText(), "switchport trunk allowed vlan")
        return self.visitChildren(ctx)

    def visitRegla_port_default_vlan(self, ctx):
        vlan_id = ctx.NUMERO().getText()
        self._check_vlan(vlan_id, "port default vlan")
        return self.visitChildren(ctx)

    def visitRegla_port_trunk_allow_pass(self, ctx):
        for num_node in ctx.regla_vlan_list().NUMERO():
            self._check_vlan(num_node.getText(), "port trunk allow-pass vlan")
        return self.visitChildren(ctx)

    def visitRegla_access_list(self, ctx):
        acl_id = ctx.NUMERO().getText()
        self.acls_declared.add(acl_id)
        return self.visitChildren(ctx)

    def visitRegla_acl(self, ctx):
        acl_id = ctx.NUMERO().getText()
        self.acls_declared.add(acl_id)
        return self.visitChildren(ctx)

    def _check_acl(self, acl_id, rule_name):
        if acl_id not in self.acls_declared:
            self.errores.append({
                "error": f"Se está intentando aplicar la lista de acceso {acl_id} en '{rule_name}', pero nunca fue declarada."
            })

    def visitRegla_access_group(self, ctx):
        acl_id = ctx.NUMERO().getText()
        self._check_acl(acl_id, "ip access-group")
        return self.visitChildren(ctx)

    def visitRegla_traffic_filter(self, ctx):
        acl_id = ctx.NUMERO().getText()
        self._check_acl(acl_id, "traffic-filter")
        return self.visitChildren(ctx)

    def visitRegla_encapsulation(self, ctx):
        if ctx.NATIVE():
            if self.current_interface:
                physical = self.current_interface.split(".")[0]
                if physical in self.native_per_physical and self.native_per_physical[physical] != self.current_interface:
                    self.errores.append({
                        "error": f"Se intentó configurar la subinterfaz {self.current_interface} como nativa, pero la subinterfaz {self.native_per_physical[physical]} ya es la nativa para la interfaz física {physical}."
                    })
                self.native_per_physical[physical] = self.current_interface
        return self.visitChildren(ctx)
