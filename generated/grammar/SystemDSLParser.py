# Generated from grammar/SystemDSL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,173,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,68,8,4,10,4,12,4,71,
        9,4,1,4,1,4,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,94,8,7,10,7,12,7,97,9,7,1,7,
        1,7,1,8,1,8,1,8,1,8,4,8,105,8,8,11,8,12,8,106,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,
        9,129,8,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,138,8,12,10,12,
        12,12,141,9,12,1,12,1,12,1,13,1,13,1,13,4,13,148,8,13,11,13,12,13,
        149,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,169,8,14,1,15,1,15,1,15,0,0,16,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,3,2,0,22,26,38,38,2,0,27,
        27,37,40,1,0,33,36,172,0,32,1,0,0,0,2,38,1,0,0,0,4,45,1,0,0,0,6,
        55,1,0,0,0,8,61,1,0,0,0,10,74,1,0,0,0,12,84,1,0,0,0,14,90,1,0,0,
        0,16,100,1,0,0,0,18,128,1,0,0,0,20,130,1,0,0,0,22,132,1,0,0,0,24,
        134,1,0,0,0,26,144,1,0,0,0,28,168,1,0,0,0,30,170,1,0,0,0,32,33,3,
        2,1,0,33,34,3,4,2,0,34,35,3,10,5,0,35,36,3,24,12,0,36,37,5,0,0,1,
        37,1,1,0,0,0,38,39,5,1,0,0,39,40,5,2,0,0,40,41,5,38,0,0,41,42,5,
        3,0,0,42,43,5,2,0,0,43,44,5,39,0,0,44,3,1,0,0,0,45,46,5,4,0,0,46,
        50,5,5,0,0,47,49,3,6,3,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,
        0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,6,0,0,54,5,1,
        0,0,0,55,56,5,7,0,0,56,57,5,38,0,0,57,58,5,5,0,0,58,59,3,8,4,0,59,
        60,5,6,0,0,60,7,1,0,0,0,61,62,5,8,0,0,62,63,5,2,0,0,63,64,5,9,0,
        0,64,69,5,38,0,0,65,66,5,10,0,0,66,68,5,38,0,0,67,65,1,0,0,0,68,
        71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,
        0,72,73,5,11,0,0,73,9,1,0,0,0,74,75,5,12,0,0,75,79,5,5,0,0,76,78,
        3,12,6,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,
        80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,6,0,0,83,11,1,0,0,0,84,85,5,
        13,0,0,85,86,5,38,0,0,86,87,5,5,0,0,87,88,3,14,7,0,88,89,5,6,0,0,
        89,13,1,0,0,0,90,91,5,14,0,0,91,95,5,5,0,0,92,94,3,16,8,0,93,92,
        1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,
        97,95,1,0,0,0,98,99,5,6,0,0,99,15,1,0,0,0,100,101,5,15,0,0,101,102,
        5,38,0,0,102,104,5,5,0,0,103,105,3,18,9,0,104,103,1,0,0,0,105,106,
        1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,
        5,6,0,0,109,17,1,0,0,0,110,111,5,16,0,0,111,112,5,2,0,0,112,129,
        3,20,10,0,113,114,5,17,0,0,114,115,5,2,0,0,115,129,5,37,0,0,116,
        117,5,18,0,0,117,118,5,2,0,0,118,129,5,37,0,0,119,120,5,19,0,0,120,
        121,5,2,0,0,121,129,3,22,11,0,122,123,5,20,0,0,123,124,5,2,0,0,124,
        129,5,40,0,0,125,126,5,21,0,0,126,127,5,2,0,0,127,129,5,40,0,0,128,
        110,1,0,0,0,128,113,1,0,0,0,128,116,1,0,0,0,128,119,1,0,0,0,128,
        122,1,0,0,0,128,125,1,0,0,0,129,19,1,0,0,0,130,131,7,0,0,0,131,21,
        1,0,0,0,132,133,7,1,0,0,133,23,1,0,0,0,134,135,5,28,0,0,135,139,
        5,5,0,0,136,138,3,26,13,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,
        1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,
        5,6,0,0,143,25,1,0,0,0,144,145,5,29,0,0,145,147,5,5,0,0,146,148,
        3,28,14,0,147,146,1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,151,1,0,0,0,151,152,5,6,0,0,152,27,1,0,0,0,153,154,5,
        30,0,0,154,155,5,2,0,0,155,169,5,38,0,0,156,157,5,31,0,0,157,158,
        5,2,0,0,158,169,5,38,0,0,159,160,5,16,0,0,160,161,5,2,0,0,161,169,
        3,30,15,0,162,163,5,32,0,0,163,164,5,2,0,0,164,169,5,38,0,0,165,
        166,5,17,0,0,166,167,5,2,0,0,167,169,5,37,0,0,168,153,1,0,0,0,168,
        156,1,0,0,0,168,159,1,0,0,0,168,162,1,0,0,0,168,165,1,0,0,0,169,
        29,1,0,0,0,170,171,7,2,0,0,171,31,1,0,0,0,9,50,69,79,95,106,128,
        139,149,168
    ]

class SystemDSLParser ( Parser ):

    grammarFileName = "SystemDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'system'", "':'", "'version'", "'enums'", 
                     "'{'", "'}'", "'enum'", "'values'", "'['", "','", "']'", 
                     "'entities'", "'entity'", "'fields'", "'field'", "'type'", 
                     "'required'", "'unique'", "'default'", "'min'", "'max'", 
                     "'String'", "'Integer'", "'Float'", "'Boolean'", "'DateTime'", 
                     "'now()'", "'relations'", "'relation'", "'from'", "'to'", 
                     "'role'", "'one-to-one'", "'one-to-many'", "'many-to-one'", 
                     "'many-to-many'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "ID", "STRING", "NUMBER", "WS", 
                      "COMMENT" ]

    RULE_model = 0
    RULE_systemDecl = 1
    RULE_enumsBlock = 2
    RULE_enumDecl = 3
    RULE_valuesDecl = 4
    RULE_entitiesBlock = 5
    RULE_entityDecl = 6
    RULE_fieldsBlock = 7
    RULE_fieldDecl = 8
    RULE_fieldProp = 9
    RULE_typeExpr = 10
    RULE_defaultValue = 11
    RULE_relationsBlock = 12
    RULE_relationDecl = 13
    RULE_relationProp = 14
    RULE_cardinality = 15

    ruleNames =  [ "model", "systemDecl", "enumsBlock", "enumDecl", "valuesDecl", 
                   "entitiesBlock", "entityDecl", "fieldsBlock", "fieldDecl", 
                   "fieldProp", "typeExpr", "defaultValue", "relationsBlock", 
                   "relationDecl", "relationProp", "cardinality" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    BOOL=37
    ID=38
    STRING=39
    NUMBER=40
    WS=41
    COMMENT=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def systemDecl(self):
            return self.getTypedRuleContext(SystemDSLParser.SystemDeclContext,0)


        def enumsBlock(self):
            return self.getTypedRuleContext(SystemDSLParser.EnumsBlockContext,0)


        def entitiesBlock(self):
            return self.getTypedRuleContext(SystemDSLParser.EntitiesBlockContext,0)


        def relationsBlock(self):
            return self.getTypedRuleContext(SystemDSLParser.RelationsBlockContext,0)


        def EOF(self):
            return self.getToken(SystemDSLParser.EOF, 0)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = SystemDSLParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.systemDecl()
            self.state = 33
            self.enumsBlock()
            self.state = 34
            self.entitiesBlock()
            self.state = 35
            self.relationsBlock()
            self.state = 36
            self.match(SystemDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SystemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def STRING(self):
            return self.getToken(SystemDSLParser.STRING, 0)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_systemDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystemDecl" ):
                listener.enterSystemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystemDecl" ):
                listener.exitSystemDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystemDecl" ):
                return visitor.visitSystemDecl(self)
            else:
                return visitor.visitChildren(self)




    def systemDecl(self):

        localctx = SystemDSLParser.SystemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_systemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SystemDSLParser.T__0)
            self.state = 39
            self.match(SystemDSLParser.T__1)
            self.state = 40
            self.match(SystemDSLParser.ID)
            self.state = 41
            self.match(SystemDSLParser.T__2)
            self.state = 42
            self.match(SystemDSLParser.T__1)
            self.state = 43
            self.match(SystemDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemDSLParser.EnumDeclContext)
            else:
                return self.getTypedRuleContext(SystemDSLParser.EnumDeclContext,i)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_enumsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumsBlock" ):
                listener.enterEnumsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumsBlock" ):
                listener.exitEnumsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumsBlock" ):
                return visitor.visitEnumsBlock(self)
            else:
                return visitor.visitChildren(self)




    def enumsBlock(self):

        localctx = SystemDSLParser.EnumsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_enumsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SystemDSLParser.T__3)
            self.state = 46
            self.match(SystemDSLParser.T__4)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 47
                self.enumDecl()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def valuesDecl(self):
            return self.getTypedRuleContext(SystemDSLParser.ValuesDeclContext,0)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_enumDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDecl" ):
                listener.enterEnumDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDecl" ):
                listener.exitEnumDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = SystemDSLParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SystemDSLParser.T__6)
            self.state = 56
            self.match(SystemDSLParser.ID)
            self.state = 57
            self.match(SystemDSLParser.T__4)
            self.state = 58
            self.valuesDecl()
            self.state = 59
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SystemDSLParser.ID)
            else:
                return self.getToken(SystemDSLParser.ID, i)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_valuesDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValuesDecl" ):
                listener.enterValuesDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValuesDecl" ):
                listener.exitValuesDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuesDecl" ):
                return visitor.visitValuesDecl(self)
            else:
                return visitor.visitChildren(self)




    def valuesDecl(self):

        localctx = SystemDSLParser.ValuesDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valuesDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SystemDSLParser.T__7)
            self.state = 62
            self.match(SystemDSLParser.T__1)
            self.state = 63
            self.match(SystemDSLParser.T__8)
            self.state = 64
            self.match(SystemDSLParser.ID)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 65
                self.match(SystemDSLParser.T__9)
                self.state = 66
                self.match(SystemDSLParser.ID)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(SystemDSLParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntitiesBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemDSLParser.EntityDeclContext)
            else:
                return self.getTypedRuleContext(SystemDSLParser.EntityDeclContext,i)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_entitiesBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitiesBlock" ):
                listener.enterEntitiesBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitiesBlock" ):
                listener.exitEntitiesBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntitiesBlock" ):
                return visitor.visitEntitiesBlock(self)
            else:
                return visitor.visitChildren(self)




    def entitiesBlock(self):

        localctx = SystemDSLParser.EntitiesBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_entitiesBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SystemDSLParser.T__11)
            self.state = 75
            self.match(SystemDSLParser.T__4)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 76
                self.entityDecl()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def fieldsBlock(self):
            return self.getTypedRuleContext(SystemDSLParser.FieldsBlockContext,0)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_entityDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityDecl" ):
                listener.enterEntityDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityDecl" ):
                listener.exitEntityDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityDecl" ):
                return visitor.visitEntityDecl(self)
            else:
                return visitor.visitChildren(self)




    def entityDecl(self):

        localctx = SystemDSLParser.EntityDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entityDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SystemDSLParser.T__12)
            self.state = 85
            self.match(SystemDSLParser.ID)
            self.state = 86
            self.match(SystemDSLParser.T__4)
            self.state = 87
            self.fieldsBlock()
            self.state = 88
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemDSLParser.FieldDeclContext)
            else:
                return self.getTypedRuleContext(SystemDSLParser.FieldDeclContext,i)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_fieldsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldsBlock" ):
                listener.enterFieldsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldsBlock" ):
                listener.exitFieldsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldsBlock" ):
                return visitor.visitFieldsBlock(self)
            else:
                return visitor.visitChildren(self)




    def fieldsBlock(self):

        localctx = SystemDSLParser.FieldsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fieldsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SystemDSLParser.T__13)
            self.state = 91
            self.match(SystemDSLParser.T__4)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 92
                self.fieldDecl()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def fieldProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemDSLParser.FieldPropContext)
            else:
                return self.getTypedRuleContext(SystemDSLParser.FieldPropContext,i)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_fieldDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDecl" ):
                listener.enterFieldDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDecl" ):
                listener.exitFieldDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = SystemDSLParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fieldDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SystemDSLParser.T__14)
            self.state = 101
            self.match(SystemDSLParser.ID)
            self.state = 102
            self.match(SystemDSLParser.T__4)
            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 103
                self.fieldProp()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                    break

            self.state = 108
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeExpr(self):
            return self.getTypedRuleContext(SystemDSLParser.TypeExprContext,0)


        def BOOL(self):
            return self.getToken(SystemDSLParser.BOOL, 0)

        def defaultValue(self):
            return self.getTypedRuleContext(SystemDSLParser.DefaultValueContext,0)


        def NUMBER(self):
            return self.getToken(SystemDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_fieldProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldProp" ):
                listener.enterFieldProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldProp" ):
                listener.exitFieldProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldProp" ):
                return visitor.visitFieldProp(self)
            else:
                return visitor.visitChildren(self)




    def fieldProp(self):

        localctx = SystemDSLParser.FieldPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fieldProp)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(SystemDSLParser.T__15)
                self.state = 111
                self.match(SystemDSLParser.T__1)
                self.state = 112
                self.typeExpr()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(SystemDSLParser.T__16)
                self.state = 114
                self.match(SystemDSLParser.T__1)
                self.state = 115
                self.match(SystemDSLParser.BOOL)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(SystemDSLParser.T__17)
                self.state = 117
                self.match(SystemDSLParser.T__1)
                self.state = 118
                self.match(SystemDSLParser.BOOL)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.match(SystemDSLParser.T__18)
                self.state = 120
                self.match(SystemDSLParser.T__1)
                self.state = 121
                self.defaultValue()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.match(SystemDSLParser.T__19)
                self.state = 123
                self.match(SystemDSLParser.T__1)
                self.state = 124
                self.match(SystemDSLParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.match(SystemDSLParser.T__20)
                self.state = 126
                self.match(SystemDSLParser.T__1)
                self.state = 127
                self.match(SystemDSLParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_typeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpr" ):
                listener.enterTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpr" ):
                listener.exitTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpr" ):
                return visitor.visitTypeExpr(self)
            else:
                return visitor.visitChildren(self)




    def typeExpr(self):

        localctx = SystemDSLParser.TypeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 275007930368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def STRING(self):
            return self.getToken(SystemDSLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SystemDSLParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(SystemDSLParser.BOOL, 0)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_defaultValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValue" ):
                listener.enterDefaultValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValue" ):
                listener.exitDefaultValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultValue" ):
                return visitor.visitDefaultValue(self)
            else:
                return visitor.visitChildren(self)




    def defaultValue(self):

        localctx = SystemDSLParser.DefaultValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_defaultValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2061718519808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemDSLParser.RelationDeclContext)
            else:
                return self.getTypedRuleContext(SystemDSLParser.RelationDeclContext,i)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_relationsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationsBlock" ):
                listener.enterRelationsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationsBlock" ):
                listener.exitRelationsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationsBlock" ):
                return visitor.visitRelationsBlock(self)
            else:
                return visitor.visitChildren(self)




    def relationsBlock(self):

        localctx = SystemDSLParser.RelationsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_relationsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(SystemDSLParser.T__27)
            self.state = 135
            self.match(SystemDSLParser.T__4)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 136
                self.relationDecl()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemDSLParser.RelationPropContext)
            else:
                return self.getTypedRuleContext(SystemDSLParser.RelationPropContext,i)


        def getRuleIndex(self):
            return SystemDSLParser.RULE_relationDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationDecl" ):
                listener.enterRelationDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationDecl" ):
                listener.exitRelationDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationDecl" ):
                return visitor.visitRelationDecl(self)
            else:
                return visitor.visitChildren(self)




    def relationDecl(self):

        localctx = SystemDSLParser.RelationDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relationDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(SystemDSLParser.T__28)
            self.state = 145
            self.match(SystemDSLParser.T__4)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.relationProp()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516389376) != 0)):
                    break

            self.state = 151
            self.match(SystemDSLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemDSLParser.ID, 0)

        def cardinality(self):
            return self.getTypedRuleContext(SystemDSLParser.CardinalityContext,0)


        def BOOL(self):
            return self.getToken(SystemDSLParser.BOOL, 0)

        def getRuleIndex(self):
            return SystemDSLParser.RULE_relationProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationProp" ):
                listener.enterRelationProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationProp" ):
                listener.exitRelationProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationProp" ):
                return visitor.visitRelationProp(self)
            else:
                return visitor.visitChildren(self)




    def relationProp(self):

        localctx = SystemDSLParser.RelationPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relationProp)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(SystemDSLParser.T__29)
                self.state = 154
                self.match(SystemDSLParser.T__1)
                self.state = 155
                self.match(SystemDSLParser.ID)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(SystemDSLParser.T__30)
                self.state = 157
                self.match(SystemDSLParser.T__1)
                self.state = 158
                self.match(SystemDSLParser.ID)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(SystemDSLParser.T__15)
                self.state = 160
                self.match(SystemDSLParser.T__1)
                self.state = 161
                self.cardinality()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.match(SystemDSLParser.T__31)
                self.state = 163
                self.match(SystemDSLParser.T__1)
                self.state = 164
                self.match(SystemDSLParser.ID)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.match(SystemDSLParser.T__16)
                self.state = 166
                self.match(SystemDSLParser.T__1)
                self.state = 167
                self.match(SystemDSLParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CardinalityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemDSLParser.RULE_cardinality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCardinality" ):
                listener.enterCardinality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCardinality" ):
                listener.exitCardinality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCardinality" ):
                return visitor.visitCardinality(self)
            else:
                return visitor.visitChildren(self)




    def cardinality(self):

        localctx = SystemDSLParser.CardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cardinality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





