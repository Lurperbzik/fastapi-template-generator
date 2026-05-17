grammar SystemDSL;

// ─── Regla raíz ───────────────────────────────────────────────
model
    : systemDecl
      enumsBlock
      entitiesBlock
      relationsBlock
      rulesBlock
      EOF
    ;

// ─── Cabecera ─────────────────────────────────────────────────
systemDecl
    : 'system' ':' ID
      'version' ':' STRING
    ;

// ─── Enums ────────────────────────────────────────────────────
enumsBlock
    : 'enums' '{' enumDecl* '}'
    ;

enumDecl
    : 'enum' ID '{' valuesDecl '}'
    ;

valuesDecl
    : 'values' ':' '[' ID (',' ID)* ']'
    ;

// ─── Entidades ────────────────────────────────────────────────
entitiesBlock
    : 'entities' '{' entityDecl* '}'
    ;

entityDecl
    : 'entity' ID '{' fieldsBlock '}'
    ;

fieldsBlock
    : 'fields' '{' fieldDecl* '}'
    ;

fieldDecl
    : 'field' ID '{' fieldProp+ '}'
    ;

fieldProp
    : 'type'     ':' typeExpr
    | 'required' ':' BOOL
    | 'unique'   ':' BOOL
    | 'default'  ':' defaultValue
    | 'min'      ':' NUMBER
    | 'max'      ':' NUMBER
    ;

typeExpr
    : 'String'
    | 'Integer'
    | 'Float'
    | 'Boolean'
    | 'DateTime'
    | ID
    ;

defaultValue
    : ID
    | STRING
    | NUMBER
    | BOOL
    | 'now()'
    ;

// ─── Relaciones ───────────────────────────────────────────────
relationsBlock
    : 'relations' '{' relationDecl* '}'
    ;

relationDecl
    : 'relation' '{' relationProp+ '}'
    ;

relationProp
    : 'from'     ':' ID
    | 'to'       ':' ID
    | 'type'     ':' cardinality
    | 'role'     ':' ID
    | 'required' ':' BOOL
    ;

cardinality
    : 'one-to-one'
    | 'one-to-many'
    | 'many-to-one'
    | 'many-to-many'
    ;

// ─── Reglas de negocio ────────────────────────────────────────
rulesBlock
    : 'rules' '{' ruleDecl* '}'
    ;

ruleDecl
    : 'rule' '{' ruleProp+ '}'
    ;

ruleProp
    : 'entity' ':' ID
    | 'rule'   ':' STRING
    ;

// ─── TOKENS ───────────────────────────────────────────────────
BOOL   : 'true' | 'false' ;
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' (~["\r\n])* '"' ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;