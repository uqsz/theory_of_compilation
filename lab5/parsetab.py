
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftASSIGNADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleftMORELESSMOREOREQLESSOREQEQUALSNOTEQUALSleftPLUSMINUSDOTADDDOTSUBleftTIMESDIVIDEDOTMULDOTDIVleftTRANSPOSEADDASSIGN ASSIGN BREAK COLON COMMA CONTINUE DIVASSIGN DIVIDE DOTADD DOTDIV DOTMUL DOTSUB ELSE EQUALS EYE FLOAT FOR ID IF INT LCURLY LESS LESSOREQ LPAREN LSQUAR MINUS MORE MOREOREQ MULASSIGN NOTEQUALS ONES PLUS PRINT RCURLY RETURN RPAREN RSQUAR SEMICOLON STRING SUBASSIGN TIMES TRANSPOSE WHILE ZEROSexpression : expression instruction\n                  | instructioninstruction : LCURLY expression RCURLY\n                  | line SEMICOLON\n                  | for_state \n                  | ifelse_state \n                  | while_state  line : assign\n            | PRINT print_state\n            | BREAK\n            | CONTINUE\n            | RETURN print_state\n            | RETURN  print_state : printable COMMA print_state \n                    | printable  printable : operation\n                | STRING  assign : object ASSIGN operation \n            | object ADDASSIGN operation \n            | object SUBASSIGN operation \n            | object MULASSIGN operation \n            | object DIVASSIGN operation  operation : LPAREN operation RPAREN\n                | operation PLUS operation\n                | operation MINUS operation \n                | operation TIMES operation \n                | operation DIVIDE operation \n                | operation DOTADD operation \n                | operation DOTSUB operation \n                | operation DOTMUL operation \n                | operation DOTDIV operation\n                | MINUS operation \n                | operation TRANSPOSE\n                | EYE LPAREN operation RPAREN\n                | ZEROS LPAREN operation RPAREN\n                | ONES LPAREN operation RPAREN\n                | object\n                | number\n                | matrix bool : LPAREN bool RPAREN \n            | operation MORE operation \n            | operation LESS operation \n            | operation MOREOREQ operation \n            | operation LESSOREQ operation \n            | operation EQUALS operation\n            | operation NOTEQUALS operation  object : ID vector\n            | ID  ifelse_state : IF LPAREN bool RPAREN instruction\n                    | IF LPAREN bool RPAREN instruction ELSE instruction while_state : WHILE LPAREN bool RPAREN instruction for_state : FOR ID ASSIGN forable COLON forable instruction  forable : object \n                | INT  matrix : LSQUAR row RSQUAR row : row COMMA vector \n                | vector  vector : LSQUAR elem RSQUAR  elem : elem COMMA number \n                | number number : INT \n            | FLOAT'
    
_lr_action_items = {'LCURLY':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[3,3,-2,3,-5,-6,-7,-48,-1,3,-4,-47,-3,-53,-54,-58,3,3,-49,-51,3,3,-52,-50,]),'PRINT':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[9,9,-2,9,-5,-6,-7,-48,-1,9,-4,-47,-3,-53,-54,-58,9,9,-49,-51,9,9,-52,-50,]),'BREAK':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[10,10,-2,10,-5,-6,-7,-48,-1,10,-4,-47,-3,-53,-54,-58,10,10,-49,-51,10,10,-52,-50,]),'CONTINUE':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[11,11,-2,11,-5,-6,-7,-48,-1,11,-4,-47,-3,-53,-54,-58,11,11,-49,-51,11,11,-52,-50,]),'RETURN':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[12,12,-2,12,-5,-6,-7,-48,-1,12,-4,-47,-3,-53,-54,-58,12,12,-49,-51,12,12,-52,-50,]),'FOR':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[13,13,-2,13,-5,-6,-7,-48,-1,13,-4,-47,-3,-53,-54,-58,13,13,-49,-51,13,13,-52,-50,]),'IF':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[15,15,-2,15,-5,-6,-7,-48,-1,15,-4,-47,-3,-53,-54,-58,15,15,-49,-51,15,15,-52,-50,]),'WHILE':([0,1,2,3,5,6,7,14,18,19,20,38,47,93,94,95,99,106,114,121,122,123,124,125,],[16,16,-2,16,-5,-6,-7,-48,-1,16,-4,-47,-3,-53,-54,-58,16,16,-49,-51,16,16,-52,-50,]),'ID':([0,1,2,3,5,6,7,9,12,13,14,18,19,20,25,26,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,62,65,68,93,94,95,99,100,101,102,103,104,105,106,111,114,121,122,123,124,125,],[14,14,-2,14,-5,-6,-7,14,14,37,-48,-1,14,-4,14,14,-47,14,14,14,14,14,14,14,-3,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-53,-54,-58,14,14,14,14,14,14,14,14,14,-49,-51,14,14,-52,-50,]),'$end':([1,2,5,6,7,18,20,47,114,121,124,125,],[0,-2,-5,-6,-7,-1,-4,-3,-49,-51,-52,-50,]),'RCURLY':([2,5,6,7,18,19,20,47,114,121,124,125,],[-2,-5,-6,-7,-1,47,-4,-3,-49,-51,-52,-50,]),'SEMICOLON':([4,8,10,11,12,14,21,22,23,24,30,31,32,33,34,36,38,57,59,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,95,107,108,109,],[20,-8,-10,-11,-13,-48,-9,-15,-16,-17,-37,-38,-39,-61,-62,-12,-47,-33,-32,-18,-19,-20,-21,-22,-14,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,-34,-35,-36,]),'ELSE':([5,6,7,20,47,114,121,124,125,],[-5,-6,-7,-4,-3,123,-51,-52,-50,]),'STRING':([9,12,48,],[24,24,24,]),'LPAREN':([9,12,15,16,25,26,27,28,29,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,100,101,102,103,104,105,],[25,25,40,41,25,25,60,61,62,68,68,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,68,25,25,25,25,25,25,]),'MINUS':([9,12,14,23,25,26,30,31,32,33,34,38,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,68,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,100,101,102,103,104,105,107,108,109,115,116,117,118,119,120,],[26,26,-48,50,26,26,-37,-38,-39,-61,-62,-47,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-33,50,-32,26,26,26,26,50,50,50,50,50,50,-24,-25,-26,-27,-28,-29,-30,-31,-23,50,50,50,-55,-58,50,26,26,26,26,26,26,-34,-35,-36,50,50,50,50,50,50,]),'EYE':([9,12,25,26,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,100,101,102,103,104,105,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'ZEROS':([9,12,25,26,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,100,101,102,103,104,105,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'ONES':([9,12,25,26,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,100,101,102,103,104,105,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'INT':([9,12,25,26,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,65,68,96,100,101,102,103,104,105,111,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,94,33,33,33,33,33,33,33,33,94,]),'FLOAT':([9,12,25,26,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,96,100,101,102,103,104,105,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'LSQUAR':([9,12,14,25,26,35,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,91,100,101,102,103,104,105,],[35,35,39,35,35,39,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,39,35,35,35,35,35,35,]),'ASSIGN':([14,17,37,38,95,],[-48,42,65,-47,-58,]),'ADDASSIGN':([14,17,38,95,],[-48,43,-47,-58,]),'SUBASSIGN':([14,17,38,95,],[-48,44,-47,-58,]),'MULASSIGN':([14,17,38,95,],[-48,45,-47,-58,]),'DIVASSIGN':([14,17,38,95,],[-48,46,-47,-58,]),'PLUS':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,49,-37,-38,-39,-61,-62,-47,-33,49,-32,49,49,49,49,49,49,-24,-25,-26,-27,-28,-29,-30,-31,-23,49,49,49,-55,-58,49,-34,-35,-36,49,49,49,49,49,49,]),'TIMES':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,51,-37,-38,-39,-61,-62,-47,-33,51,51,51,51,51,51,51,51,51,51,-26,-27,51,51,-30,-31,-23,51,51,51,-55,-58,51,-34,-35,-36,51,51,51,51,51,51,]),'DIVIDE':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,52,-37,-38,-39,-61,-62,-47,-33,52,52,52,52,52,52,52,52,52,52,-26,-27,52,52,-30,-31,-23,52,52,52,-55,-58,52,-34,-35,-36,52,52,52,52,52,52,]),'DOTADD':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,53,-37,-38,-39,-61,-62,-47,-33,53,-32,53,53,53,53,53,53,-24,-25,-26,-27,-28,-29,-30,-31,-23,53,53,53,-55,-58,53,-34,-35,-36,53,53,53,53,53,53,]),'DOTSUB':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,54,-37,-38,-39,-61,-62,-47,-33,54,-32,54,54,54,54,54,54,-24,-25,-26,-27,-28,-29,-30,-31,-23,54,54,54,-55,-58,54,-34,-35,-36,54,54,54,54,54,54,]),'DOTMUL':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,55,-37,-38,-39,-61,-62,-47,-33,55,55,55,55,55,55,55,55,55,55,-26,-27,55,55,-30,-31,-23,55,55,55,-55,-58,55,-34,-35,-36,55,55,55,55,55,55,]),'DOTDIV':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,56,-37,-38,-39,-61,-62,-47,-33,56,56,56,56,56,56,56,56,56,56,-26,-27,56,56,-30,-31,-23,56,56,56,-55,-58,56,-34,-35,-36,56,56,56,56,56,56,]),'TRANSPOSE':([14,23,30,31,32,33,34,38,57,58,59,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,98,107,108,109,115,116,117,118,119,120,],[-48,57,-37,-38,-39,-61,-62,-47,-33,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-23,57,57,57,-55,-58,57,-34,-35,-36,57,57,57,57,57,57,]),'COMMA':([14,22,23,24,30,31,32,33,34,38,57,59,63,64,66,67,78,79,80,81,82,83,84,85,86,90,95,107,108,109,110,112,],[-48,48,-16,-17,-37,-38,-39,-61,-62,-47,-33,-32,91,-57,96,-60,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,-34,-35,-36,-56,-59,]),'RPAREN':([14,30,31,32,33,34,38,57,58,59,69,71,78,79,80,81,82,83,84,85,86,87,88,89,90,95,97,98,107,108,109,113,115,116,117,118,119,120,],[-48,-37,-38,-39,-61,-62,-47,-33,86,-32,99,106,-24,-25,-26,-27,-28,-29,-30,-31,-23,107,108,109,-55,-58,113,86,-34,-35,-36,-40,-41,-42,-43,-44,-45,-46,]),'MORE':([14,30,31,32,33,34,38,57,59,70,78,79,80,81,82,83,84,85,86,90,95,98,107,108,109,],[-48,-37,-38,-39,-61,-62,-47,-33,-32,100,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,100,-34,-35,-36,]),'LESS':([14,30,31,32,33,34,38,57,59,70,78,79,80,81,82,83,84,85,86,90,95,98,107,108,109,],[-48,-37,-38,-39,-61,-62,-47,-33,-32,101,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,101,-34,-35,-36,]),'MOREOREQ':([14,30,31,32,33,34,38,57,59,70,78,79,80,81,82,83,84,85,86,90,95,98,107,108,109,],[-48,-37,-38,-39,-61,-62,-47,-33,-32,102,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,102,-34,-35,-36,]),'LESSOREQ':([14,30,31,32,33,34,38,57,59,70,78,79,80,81,82,83,84,85,86,90,95,98,107,108,109,],[-48,-37,-38,-39,-61,-62,-47,-33,-32,103,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,103,-34,-35,-36,]),'EQUALS':([14,30,31,32,33,34,38,57,59,70,78,79,80,81,82,83,84,85,86,90,95,98,107,108,109,],[-48,-37,-38,-39,-61,-62,-47,-33,-32,104,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,104,-34,-35,-36,]),'NOTEQUALS':([14,30,31,32,33,34,38,57,59,70,78,79,80,81,82,83,84,85,86,90,95,98,107,108,109,],[-48,-37,-38,-39,-61,-62,-47,-33,-32,105,-24,-25,-26,-27,-28,-29,-30,-31,-23,-55,-58,105,-34,-35,-36,]),'COLON':([14,38,92,93,94,95,],[-48,-47,111,-53,-54,-58,]),'RSQUAR':([33,34,63,64,66,67,95,110,112,],[-61,-62,90,-57,95,-60,-58,-56,-59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,],[1,19,]),'instruction':([0,1,3,19,99,106,122,123,],[2,18,2,18,114,121,124,125,]),'line':([0,1,3,19,99,106,122,123,],[4,4,4,4,4,4,4,4,]),'for_state':([0,1,3,19,99,106,122,123,],[5,5,5,5,5,5,5,5,]),'ifelse_state':([0,1,3,19,99,106,122,123,],[6,6,6,6,6,6,6,6,]),'while_state':([0,1,3,19,99,106,122,123,],[7,7,7,7,7,7,7,7,]),'assign':([0,1,3,19,99,106,122,123,],[8,8,8,8,8,8,8,8,]),'object':([0,1,3,9,12,19,25,26,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,65,68,99,100,101,102,103,104,105,106,111,122,123,],[17,17,17,30,30,17,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,93,30,17,30,30,30,30,30,30,17,93,17,17,]),'print_state':([9,12,48,],[21,36,77,]),'printable':([9,12,48,],[22,22,22,]),'operation':([9,12,25,26,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,100,101,102,103,104,105,],[23,23,58,59,70,70,72,73,74,75,76,23,78,79,80,81,82,83,84,85,87,88,89,98,115,116,117,118,119,120,]),'number':([9,12,25,26,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,96,100,101,102,103,104,105,],[31,31,31,31,67,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,112,31,31,31,31,31,31,]),'matrix':([9,12,25,26,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,100,101,102,103,104,105,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'vector':([14,35,91,],[38,64,110,]),'row':([35,],[63,]),'elem':([39,],[66,]),'bool':([40,41,68,],[69,71,97,]),'forable':([65,111,],[92,122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression instruction','expression',2,'p_expression','Mparser.py',26),
  ('expression -> instruction','expression',1,'p_expression','Mparser.py',27),
  ('instruction -> LCURLY expression RCURLY','instruction',3,'p_instruction','Mparser.py',36),
  ('instruction -> line SEMICOLON','instruction',2,'p_instruction','Mparser.py',37),
  ('instruction -> for_state','instruction',1,'p_instruction','Mparser.py',38),
  ('instruction -> ifelse_state','instruction',1,'p_instruction','Mparser.py',39),
  ('instruction -> while_state','instruction',1,'p_instruction','Mparser.py',40),
  ('line -> assign','line',1,'p_line','Mparser.py',48),
  ('line -> PRINT print_state','line',2,'p_line','Mparser.py',49),
  ('line -> BREAK','line',1,'p_line','Mparser.py',50),
  ('line -> CONTINUE','line',1,'p_line','Mparser.py',51),
  ('line -> RETURN print_state','line',2,'p_line','Mparser.py',52),
  ('line -> RETURN','line',1,'p_line','Mparser.py',53),
  ('print_state -> printable COMMA print_state','print_state',3,'p_print_state','Mparser.py',65),
  ('print_state -> printable','print_state',1,'p_print_state','Mparser.py',66),
  ('printable -> operation','printable',1,'p_printable','Mparser.py',74),
  ('printable -> STRING','printable',1,'p_printable','Mparser.py',75),
  ('assign -> object ASSIGN operation','assign',3,'p_assign','Mparser.py',83),
  ('assign -> object ADDASSIGN operation','assign',3,'p_assign','Mparser.py',84),
  ('assign -> object SUBASSIGN operation','assign',3,'p_assign','Mparser.py',85),
  ('assign -> object MULASSIGN operation','assign',3,'p_assign','Mparser.py',86),
  ('assign -> object DIVASSIGN operation','assign',3,'p_assign','Mparser.py',87),
  ('operation -> LPAREN operation RPAREN','operation',3,'p_operation','Mparser.py',93),
  ('operation -> operation PLUS operation','operation',3,'p_operation','Mparser.py',94),
  ('operation -> operation MINUS operation','operation',3,'p_operation','Mparser.py',95),
  ('operation -> operation TIMES operation','operation',3,'p_operation','Mparser.py',96),
  ('operation -> operation DIVIDE operation','operation',3,'p_operation','Mparser.py',97),
  ('operation -> operation DOTADD operation','operation',3,'p_operation','Mparser.py',98),
  ('operation -> operation DOTSUB operation','operation',3,'p_operation','Mparser.py',99),
  ('operation -> operation DOTMUL operation','operation',3,'p_operation','Mparser.py',100),
  ('operation -> operation DOTDIV operation','operation',3,'p_operation','Mparser.py',101),
  ('operation -> MINUS operation','operation',2,'p_operation','Mparser.py',102),
  ('operation -> operation TRANSPOSE','operation',2,'p_operation','Mparser.py',103),
  ('operation -> EYE LPAREN operation RPAREN','operation',4,'p_operation','Mparser.py',104),
  ('operation -> ZEROS LPAREN operation RPAREN','operation',4,'p_operation','Mparser.py',105),
  ('operation -> ONES LPAREN operation RPAREN','operation',4,'p_operation','Mparser.py',106),
  ('operation -> object','operation',1,'p_operation','Mparser.py',107),
  ('operation -> number','operation',1,'p_operation','Mparser.py',108),
  ('operation -> matrix','operation',1,'p_operation','Mparser.py',109),
  ('bool -> LPAREN bool RPAREN','bool',3,'p_bool','Mparser.py',129),
  ('bool -> operation MORE operation','bool',3,'p_bool','Mparser.py',130),
  ('bool -> operation LESS operation','bool',3,'p_bool','Mparser.py',131),
  ('bool -> operation MOREOREQ operation','bool',3,'p_bool','Mparser.py',132),
  ('bool -> operation LESSOREQ operation','bool',3,'p_bool','Mparser.py',133),
  ('bool -> operation EQUALS operation','bool',3,'p_bool','Mparser.py',134),
  ('bool -> operation NOTEQUALS operation','bool',3,'p_bool','Mparser.py',135),
  ('object -> ID vector','object',2,'p_object','Mparser.py',144),
  ('object -> ID','object',1,'p_object','Mparser.py',145),
  ('ifelse_state -> IF LPAREN bool RPAREN instruction','ifelse_state',5,'p_ifelse_state','Mparser.py',154),
  ('ifelse_state -> IF LPAREN bool RPAREN instruction ELSE instruction','ifelse_state',7,'p_ifelse_state','Mparser.py',155),
  ('while_state -> WHILE LPAREN bool RPAREN instruction','while_state',5,'p_while_state','Mparser.py',163),
  ('for_state -> FOR ID ASSIGN forable COLON forable instruction','for_state',7,'p_for_state','Mparser.py',168),
  ('forable -> object','forable',1,'p_forable','Mparser.py',173),
  ('forable -> INT','forable',1,'p_forable','Mparser.py',174),
  ('matrix -> LSQUAR row RSQUAR','matrix',3,'p_matrix','Mparser.py',182),
  ('row -> row COMMA vector','row',3,'p_row','Mparser.py',187),
  ('row -> vector','row',1,'p_row','Mparser.py',188),
  ('vector -> LSQUAR elem RSQUAR','vector',3,'p_vector','Mparser.py',196),
  ('elem -> elem COMMA number','elem',3,'p_elem','Mparser.py',201),
  ('elem -> number','elem',1,'p_elem','Mparser.py',202),
  ('number -> INT','number',1,'p_number','Mparser.py',210),
  ('number -> FLOAT','number',1,'p_number','Mparser.py',211),
]
