## Grammars
"""
A programming langugae has infinite set of programs. This means that python has infinite number of python programs.

Becasue the programming language has inifinite set of programs. You cannnot
list out all the programs.

Therefore, we list a set of rules in building programs. 

This list of rules is called context-free grammar. 

Grammars are usally used to specific the concrete syntax of a programming language.

In this note, we are writing the rules in a variant of Backus-Naur form

L(Int) -> Language that consists of integers and arihmetic operations
"""

## First rule 
"""
An instance of a Constant class is an expression.

        exp ::= Constant(int)

Each rule has the LHS and RHS. If the AST node matches the RHS, then you can
categorize the node as LHS.
"""

# Second rule
"""
    exp ::= Call(Name("get_number"), [])
"""

# Third rule
"""
    exp ::= UnaryOp(USub, exp)
"""

## Fourth rule and Fiveth rule
"""
    exp ::= BinOp(exp, Add(), exp)
    exp ::= BinOp(exp, Sub(), exp)
"""

## Application of rules 
"""
Using First rule and Second rule, we can represent
    -8

    exp ::= UnaryOp(USub, Constant(8))
"""