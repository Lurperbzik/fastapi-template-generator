# Generated from grammar/SystemDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SystemDSLParser import SystemDSLParser
else:
    from SystemDSLParser import SystemDSLParser

# This class defines a complete listener for a parse tree produced by SystemDSLParser.
class SystemDSLListener(ParseTreeListener):

    # Enter a parse tree produced by SystemDSLParser#model.
    def enterModel(self, ctx:SystemDSLParser.ModelContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#model.
    def exitModel(self, ctx:SystemDSLParser.ModelContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#systemDecl.
    def enterSystemDecl(self, ctx:SystemDSLParser.SystemDeclContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#systemDecl.
    def exitSystemDecl(self, ctx:SystemDSLParser.SystemDeclContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#enumsBlock.
    def enterEnumsBlock(self, ctx:SystemDSLParser.EnumsBlockContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#enumsBlock.
    def exitEnumsBlock(self, ctx:SystemDSLParser.EnumsBlockContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#enumDecl.
    def enterEnumDecl(self, ctx:SystemDSLParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#enumDecl.
    def exitEnumDecl(self, ctx:SystemDSLParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#valuesDecl.
    def enterValuesDecl(self, ctx:SystemDSLParser.ValuesDeclContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#valuesDecl.
    def exitValuesDecl(self, ctx:SystemDSLParser.ValuesDeclContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#entitiesBlock.
    def enterEntitiesBlock(self, ctx:SystemDSLParser.EntitiesBlockContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#entitiesBlock.
    def exitEntitiesBlock(self, ctx:SystemDSLParser.EntitiesBlockContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#entityDecl.
    def enterEntityDecl(self, ctx:SystemDSLParser.EntityDeclContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#entityDecl.
    def exitEntityDecl(self, ctx:SystemDSLParser.EntityDeclContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#fieldsBlock.
    def enterFieldsBlock(self, ctx:SystemDSLParser.FieldsBlockContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#fieldsBlock.
    def exitFieldsBlock(self, ctx:SystemDSLParser.FieldsBlockContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#fieldDecl.
    def enterFieldDecl(self, ctx:SystemDSLParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#fieldDecl.
    def exitFieldDecl(self, ctx:SystemDSLParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#fieldProp.
    def enterFieldProp(self, ctx:SystemDSLParser.FieldPropContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#fieldProp.
    def exitFieldProp(self, ctx:SystemDSLParser.FieldPropContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#typeExpr.
    def enterTypeExpr(self, ctx:SystemDSLParser.TypeExprContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#typeExpr.
    def exitTypeExpr(self, ctx:SystemDSLParser.TypeExprContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#defaultValue.
    def enterDefaultValue(self, ctx:SystemDSLParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#defaultValue.
    def exitDefaultValue(self, ctx:SystemDSLParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#relationsBlock.
    def enterRelationsBlock(self, ctx:SystemDSLParser.RelationsBlockContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#relationsBlock.
    def exitRelationsBlock(self, ctx:SystemDSLParser.RelationsBlockContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#relationDecl.
    def enterRelationDecl(self, ctx:SystemDSLParser.RelationDeclContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#relationDecl.
    def exitRelationDecl(self, ctx:SystemDSLParser.RelationDeclContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#relationProp.
    def enterRelationProp(self, ctx:SystemDSLParser.RelationPropContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#relationProp.
    def exitRelationProp(self, ctx:SystemDSLParser.RelationPropContext):
        pass


    # Enter a parse tree produced by SystemDSLParser#cardinality.
    def enterCardinality(self, ctx:SystemDSLParser.CardinalityContext):
        pass

    # Exit a parse tree produced by SystemDSLParser#cardinality.
    def exitCardinality(self, ctx:SystemDSLParser.CardinalityContext):
        pass



del SystemDSLParser