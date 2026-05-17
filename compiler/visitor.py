from generated.SystemDSLVisitor import SystemDSLVisitor
from .metamodel import (
    SystemModel, EnumDef, EntityDef,
    FieldDef, RelationDef, RuleDef
)

class ModelBuilder(SystemDSLVisitor):

    def visitModel(self, ctx):
        system = self.visit(ctx.systemDecl())

        for enum_ctx in ctx.enumsBlock().enumDecl():
            system.enums.append(self.visit(enum_ctx))

        for entity_ctx in ctx.entitiesBlock().entityDecl():
            system.entities.append(self.visit(entity_ctx))

        for relation_ctx in ctx.relationsBlock().relationDecl():
            system.relations.append(self.visit(relation_ctx))

        for rule_ctx in ctx.rulesBlock().ruleDecl():
            system.rules.append(self.visit(rule_ctx))

        return system

    def visitSystemDecl(self, ctx):
        name    = ctx.ID().getText()
        version = ctx.STRING().getText().strip('"')
        return SystemModel(name=name, version=version)

    def visitEnumDecl(self, ctx):
        name   = ctx.ID().getText()
        values = [v.getText() for v in ctx.valuesDecl().ID()]
        return EnumDef(name=name, values=values)

    def visitEntityDecl(self, ctx):
        name   = ctx.ID().getText()
        fields = [
            self.visit(f)
            for f in ctx.fieldsBlock().fieldDecl()
        ]
        return EntityDef(name=name, fields=fields)

    def visitFieldDecl(self, ctx):
        name  = ctx.ID().getText()
        props = {}

        for prop in ctx.fieldProp():
            key = prop.getChild(0).getText()   # type, required, unique...
            val = prop.getChild(2).getText()   # el valor tras ':'

            if key == 'type':
                props['type'] = val
            elif key == 'required':
                props['required'] = val == 'true'
            elif key == 'unique':
                props['unique'] = val == 'true'
            elif key == 'default':
                props['default'] = val.strip('"')
            elif key == 'min':
                props['min'] = float(val)
            elif key == 'max':
                props['max'] = float(val)

        return FieldDef(name=name, **props)

    def visitRelationDecl(self, ctx):
        props = {}
        for prop in ctx.relationProp():
            key = prop.getChild(0).getText()
            val = prop.getChild(2).getText()

            if key == 'from':
                props['from_entity'] = val
            elif key == 'to':
                props['to_entity'] = val
            elif key == 'type':
                props['type'] = val
            elif key == 'role':
                props['role'] = val
            elif key == 'required':
                props['required'] = val == 'true'

        return RelationDef(**props)

    def visitRuleDecl(self, ctx):
        props = {}
        for prop in ctx.ruleProp():
            key = prop.getChild(0).getText()
            val = prop.getChild(2).getText()

            if key == 'entity':
                props['entity'] = val
            elif key == 'rule':
                props['rule'] = val.strip('"')

        return RuleDef(**props)