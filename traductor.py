from antlr4.TokenStreamRewriter import TokenStreamRewriter
from ExprVisitor import ExprVisitor
from conjunto_de_reglas import REGLAS_TRADUCCION

class Traductor(ExprVisitor):
    def __init__(self, tokens, modo_traduccion="HUAWEI_A_CISCO"):
        super().__init__()
        # TokenStreamRewriter nos permite modificar los tokens (texto original) sin perder espacios
        self.rewriter = TokenStreamRewriter(tokens)
        self.reglas = REGLAS_TRADUCCION.get(modo_traduccion, {})
        self.modo_traduccion = modo_traduccion

    def traducir(self, arbol):
        # Visitar el arbol aplicara las reglas y modificara el rewriter
        self.visit(arbol)
        # Devolvemos el texto final modificado
        return self.rewriter.getDefaultText()

    # --- Reglas de Huawei a Cisco ---

    def visitRegla_system_view(self, ctx):
        if "regla_system_view" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_system_view"])
        return self.visitChildren(ctx)

    def visitRegla_sysname(self, ctx):
        if "regla_sysname" in self.reglas:
            # sysname Router1 -> ctx.getChild(1).getText() = Router1
            nombre = ctx.getChild(1).getText()
            nuevo_texto = self.reglas["regla_sysname"].format(nombre)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_undo_shutdown(self, ctx):
        if "regla_undo_shutdown" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_undo_shutdown"])
        return self.visitChildren(ctx)

    def visitRegla_display_current_configuration(self, ctx):
        if "regla_display_current_configuration" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_display_current_configuration"])
        return self.visitChildren(ctx)

    def visitRegla_quit(self, ctx):
        if "regla_quit" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_quit"])
        return self.visitChildren(ctx)

    def visitRegla_port_link_type(self, ctx):
        if "regla_port_link_type" in self.reglas:
            # port link-type (access|trunk)
            tipo = ctx.getChild(2).getText().lower()
            nuevo_texto = self.reglas["regla_port_link_type"].format(tipo)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_port_trunk_allow_pass(self, ctx):
        if "regla_port_trunk_allow_pass" in self.reglas:
            # port trunk allow-pass vlan 10,20
            vlans = ctx.getChild(4).getText() # regla_vlan_list
            nuevo_texto = self.reglas["regla_port_trunk_allow_pass"].format(vlans)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_dot1q_termination(self, ctx):
        if "regla_dot1q_termination" in self.reglas:
            vid = ctx.getChild(3).getText()
            nuevo_texto = self.reglas["regla_dot1q_termination"].format(vid)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_ip_route_static(self, ctx):
        if "regla_ip_route_static" in self.reglas:
            ip1 = ctx.getChild(2).getText()
            ip2 = ctx.getChild(3).getText()
            ip3 = ctx.getChild(4).getText()
            nuevo_texto = self.reglas["regla_ip_route_static"].format(ip1, ip2, ip3)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_traffic_filter(self, ctx):
        if "regla_traffic_filter" in self.reglas:
            # traffic-filter inbound acl 3001
            direccion = ctx.getChild(1).getText().lower()
            if direccion == "inbound": direccion = "in"
            elif direccion == "outbound": direccion = "out"
            acl = ctx.getChild(3).getText()
            nuevo_texto = self.reglas["regla_traffic_filter"].format(direccion, acl)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    # --- Reglas de Cisco a Huawei ---

    def visitRegla_configure_terminal(self, ctx):
        if "regla_configure_terminal" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_configure_terminal"])
        return self.visitChildren(ctx)

    def visitRegla_hostname(self, ctx):
        if "regla_hostname" in self.reglas:
            nombre = ctx.getChild(1).getText()
            nuevo_texto = self.reglas["regla_hostname"].format(nombre)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_no_shutdown(self, ctx):
        if "regla_no_shutdown" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_no_shutdown"])
        return self.visitChildren(ctx)

    def visitRegla_show_running_config(self, ctx):
        if "regla_show_running_config" in self.reglas:
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, self.reglas["regla_show_running_config"])
        return self.visitChildren(ctx)

    def visitRegla_switchport_mode(self, ctx):
        if "regla_switchport_mode" in self.reglas:
            tipo = ctx.getChild(2).getText().lower()
            nuevo_texto = self.reglas["regla_switchport_mode"].format(tipo)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_switchport_trunk_allowed(self, ctx):
        if "regla_switchport_trunk_allowed" in self.reglas:
            vlans = ctx.getChild(4).getText()
            nuevo_texto = self.reglas["regla_switchport_trunk_allowed"].format(vlans)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_encapsulation(self, ctx):
        if "regla_encapsulation" in self.reglas:
            vid = ctx.getChild(2).getText()
            nuevo_texto = self.reglas["regla_encapsulation"].format(vid)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_ip_route(self, ctx):
        if "regla_ip_route" in self.reglas:
            ip1 = ctx.getChild(2).getText()
            ip2 = ctx.getChild(3).getText()
            ip3 = ctx.getChild(4).getText()
            nuevo_texto = self.reglas["regla_ip_route"].format(ip1, ip2, ip3)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)

    def visitRegla_access_group(self, ctx):
        if "regla_access_group" in self.reglas:
            direccion = ctx.getChild(3).getText().lower()
            if direccion == "in": direccion = "inbound"
            elif direccion == "out": direccion = "outbound"
            acl = ctx.getChild(2).getText()
            nuevo_texto = self.reglas["regla_access_group"].format(direccion, acl)
            self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, nuevo_texto)
        return self.visitChildren(ctx)
