# Generated from grammar/SystemDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SystemDSLParser import SystemDSLParser
else:
    from SystemDSLParser import SystemDSLParser

# This class defines a complete generic visitor for a parse tree produced by SystemDSLParser.

class SystemDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SystemDSLParser#model.
    def visitModel(self, ctx:SystemDSLParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#systemDecl.
    def visitSystemDecl(self, ctx:SystemDSLParser.SystemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#enumsBlock.
    def visitEnumsBlock(self, ctx:SystemDSLParser.EnumsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#enumDecl.
    def visitEnumDecl(self, ctx:SystemDSLParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#valuesDecl.
    def visitValuesDecl(self, ctx:SystemDSLParser.ValuesDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#entitiesBlock.
    def visitEntitiesBlock(self, ctx:SystemDSLParser.EntitiesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#entityDecl.
    def visitEntityDecl(self, ctx:SystemDSLParser.EntityDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#fieldsBlock.
    def visitFieldsBlock(self, ctx:SystemDSLParser.FieldsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#fieldDecl.
    def visitFieldDecl(self, ctx:SystemDSLParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#fieldProp.
    def visitFieldProp(self, ctx:SystemDSLParser.FieldPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#typeExpr.
    def visitTypeExpr(self, ctx:SystemDSLParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#defaultValue.
    def visitDefaultValue(self, ctx:SystemDSLParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#relationsBlock.
    def visitRelationsBlock(self, ctx:SystemDSLParser.RelationsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#relationDecl.
    def visitRelationDecl(self, ctx:SystemDSLParser.RelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#relationProp.
    def visitRelationProp(self, ctx:SystemDSLParser.RelationPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SystemDSLParser#cardinality.
    def visitCardinality(self, ctx:SystemDSLParser.CardinalityContext):
        return self.visitChildren(ctx)



del SystemDSLParser