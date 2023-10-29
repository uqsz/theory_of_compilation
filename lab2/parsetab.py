
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftASSIGNADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleftMORELESSMOREOREQLESSOREQEQUALSleftPLUSMINUSTIMESDIVIDEDOTADDDOTSUBDOTMULDOTDIVleftTRANSPOSEADDASSIGN ASSIGN BREAK COLON COMMA CONTINUE DIVASSIGN DIVIDE DOTADD DOTDIV DOTMUL DOTSUB ELSE EQUALS EYE FLOAT FOR ID IF INT LCURLY LESS LESSOREQ LPAREN LSQUAR MINUS MORE MOREOREQ MULASSIGN ONES PLUS PRINT RCURLY RETURN RPAREN RSQUAR SEMICOLON STRING SUBASSIGN TIMES TRANSPOSE WHILE ZEROSexpression : LPAREN expression RPAREN\n                  | LCURLY expression RCURLY\n                  | ID\n                  | INT \n                  | FLOAT\n                  | STRING \n                  | BREAK\n                  | CONTINUE\n                  | RETURN\n                  | expression SEMICOLON expression SEMICOLON\n                  | expression SEMICOLONexpression  : expression PLUS expression \n                    | expression MINUS expression\n                    | expression TIMES expression\n                    | expression DIVIDE expressionexpression  : expression DOTADD expression \n                    | expression DOTSUB expression\n                    | expression DOTMUL expression\n                    | expression DOTDIV expressionexpression  : expression ASSIGN expression \n                    | expression ADDASSIGN expression\n                    | expression SUBASSIGN expression\n                    | expression MULASSIGN expression\n                    | expression DIVASSIGN expressionexpression  : expression MORE expression \n                    | expression LESS expression\n                    | expression MOREOREQ expression\n                    | expression LESSOREQ expression\n                    | expression EQUALS expressionexpression  : MINUS expressionexpression  : expression TRANSPOSEexpression  : ZEROS LPAREN expression RPAREN SEMICOLON\n                    | EYE LPAREN expression RPAREN SEMICOLON\n                    | ONES LPAREN expression RPAREN SEMICOLONexpression : IF LPAREN expression RPAREN expression\n                    | IF LPAREN expression RPAREN expression ELSE expression\n    expression : WHILE LPAREN expression RPAREN expression\n    expression : FOR ID EQUALS expression COLON expression LCURLY expression expression\n    expression : LSQUAR expression RSQUAR\n                    | LSQUAR expression COMMA expression RSQUAR\n    expression : PRINT expression'
    
_lr_action_items = {'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[2,2,2,-3,-4,-5,-6,-7,-8,-9,2,43,44,45,46,47,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-31,-30,2,2,2,2,2,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,2,-39,2,2,2,2,-32,-33,-34,-35,-37,2,-40,2,-36,2,2,-38,2,-13,]),'LCURLY':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,],[3,3,3,-3,-4,-5,-6,-7,-8,-9,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-31,-30,3,3,3,3,3,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,3,-39,3,3,3,3,-32,-33,-34,-35,-37,3,-40,3,98,-36,3,3,-38,3,-13,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[4,4,4,-3,-4,-5,-6,-7,-8,-9,4,48,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-31,-30,4,4,4,4,4,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,4,-39,4,4,4,4,-32,-33,-34,-35,-37,4,-40,4,-36,4,4,-38,4,-13,]),'INT':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[5,5,5,-3,-4,-5,-6,-7,-8,-9,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-31,-30,5,5,5,5,5,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,5,-39,5,5,5,5,-32,-33,-34,-35,-37,5,-40,5,-36,5,5,-38,5,-13,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[6,6,6,-3,-4,-5,-6,-7,-8,-9,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-31,-30,6,6,6,6,6,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,6,-39,6,6,6,6,-32,-33,-34,-35,-37,6,-40,6,-36,6,6,-38,6,-13,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[7,7,7,-3,-4,-5,-6,-7,-8,-9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-31,-30,7,7,7,7,7,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,7,-39,7,7,7,7,-32,-33,-34,-35,-37,7,-40,7,-36,7,7,-38,7,-13,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[8,8,8,-3,-4,-5,-6,-7,-8,-9,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-31,-30,8,8,8,8,8,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,8,-39,8,8,8,8,-32,-33,-34,-35,-37,8,-40,8,-36,8,8,-38,8,-13,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[9,9,9,-3,-4,-5,-6,-7,-8,-9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-31,-30,9,9,9,9,9,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,9,-39,9,9,9,9,-32,-33,-34,-35,-37,9,-40,9,-36,9,9,-38,9,-13,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[10,10,10,-3,-4,-5,-6,-7,-8,-9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-31,-30,10,10,10,10,10,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,10,-39,10,10,10,10,-32,-33,-34,-35,-37,10,-40,10,-36,10,10,-38,10,-13,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,],[11,22,11,11,-3,-4,-5,-6,-7,-8,-9,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-31,22,22,-30,11,11,11,11,11,22,22,22,-12,-13,-14,-15,-16,-17,-18,-19,22,22,22,22,22,22,22,22,22,22,-1,-2,22,22,22,22,22,11,-39,11,11,11,11,22,22,-32,-33,-34,22,22,11,-40,11,22,22,11,101,22,11,-13,]),'ZEROS':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[12,12,12,-3,-4,-5,-6,-7,-8,-9,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-31,-30,12,12,12,12,12,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,12,-39,12,12,12,12,-32,-33,-34,-35,-37,12,-40,12,-36,12,12,-38,12,-13,]),'EYE':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[13,13,13,-3,-4,-5,-6,-7,-8,-9,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-31,-30,13,13,13,13,13,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,13,-39,13,13,13,13,-32,-33,-34,-35,-37,13,-40,13,-36,13,13,-38,13,-13,]),'ONES':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[14,14,14,-3,-4,-5,-6,-7,-8,-9,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-31,-30,14,14,14,14,14,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,14,-39,14,14,14,14,-32,-33,-34,-35,-37,14,-40,14,-36,14,14,-38,14,-13,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[15,15,15,-3,-4,-5,-6,-7,-8,-9,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-31,-30,15,15,15,15,15,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,15,-39,15,15,15,15,-32,-33,-34,-35,-37,15,-40,15,-36,15,15,-38,15,-13,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[16,16,16,-3,-4,-5,-6,-7,-8,-9,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-31,-30,16,16,16,16,16,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,16,-39,16,16,16,16,-32,-33,-34,-35,-37,16,-40,16,-36,16,16,-38,16,-13,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[17,17,17,-3,-4,-5,-6,-7,-8,-9,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-31,-30,17,17,17,17,17,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,17,-39,17,17,17,17,-32,-33,-34,-35,-37,17,-40,17,-36,17,17,-38,17,-13,]),'LSQUAR':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[18,18,18,-3,-4,-5,-6,-7,-8,-9,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-31,-30,18,18,18,18,18,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,18,-39,18,18,18,18,-32,-33,-34,-35,-37,18,-40,18,-36,18,18,-38,18,-13,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,77,78,79,80,84,85,88,89,90,91,92,93,94,95,97,98,99,100,101,102,],[19,19,19,-3,-4,-5,-6,-7,-8,-9,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-31,-30,19,19,19,19,19,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,19,-39,19,19,19,19,-32,-33,-34,-35,-37,19,-40,19,-36,19,19,-38,19,-13,]),'$end':([1,4,5,6,7,8,9,10,20,39,42,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,80,88,89,90,91,92,94,97,100,102,],[0,-3,-4,-5,-6,-7,-8,-9,-11,-31,-30,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,-39,-10,-32,-33,-34,-35,-37,-40,-36,-38,-30,]),'SEMICOLON':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,81,82,83,86,87,88,89,90,91,92,94,96,97,99,100,102,],[20,-3,-4,-5,-6,-7,-8,-9,-11,-31,20,20,-30,20,20,80,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,20,20,20,20,20,-39,-10,88,89,90,20,20,-32,-33,-34,20,20,-40,20,20,20,20,-13,]),'PLUS':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[21,-3,-4,-5,-6,-7,-8,-9,-11,-31,21,21,-30,21,21,21,-12,-13,-14,-15,-16,-17,-18,-19,21,21,21,21,21,21,21,21,21,21,-1,-2,21,21,21,21,21,-39,-10,21,21,-32,-33,-34,21,21,-40,21,21,21,21,-13,]),'TIMES':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[23,-3,-4,-5,-6,-7,-8,-9,-11,-31,23,23,-30,23,23,23,-12,-13,-14,-15,-16,-17,-18,-19,23,23,23,23,23,23,23,23,23,23,-1,-2,23,23,23,23,23,-39,-10,23,23,-32,-33,-34,23,23,-40,23,23,23,23,-13,]),'DIVIDE':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[24,-3,-4,-5,-6,-7,-8,-9,-11,-31,24,24,-30,24,24,24,-12,-13,-14,-15,-16,-17,-18,-19,24,24,24,24,24,24,24,24,24,24,-1,-2,24,24,24,24,24,-39,-10,24,24,-32,-33,-34,24,24,-40,24,24,24,24,-13,]),'DOTADD':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[25,-3,-4,-5,-6,-7,-8,-9,-11,-31,25,25,-30,25,25,25,-12,-13,-14,-15,-16,-17,-18,-19,25,25,25,25,25,25,25,25,25,25,-1,-2,25,25,25,25,25,-39,-10,25,25,-32,-33,-34,25,25,-40,25,25,25,25,-13,]),'DOTSUB':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[26,-3,-4,-5,-6,-7,-8,-9,-11,-31,26,26,-30,26,26,26,-12,-13,-14,-15,-16,-17,-18,-19,26,26,26,26,26,26,26,26,26,26,-1,-2,26,26,26,26,26,-39,-10,26,26,-32,-33,-34,26,26,-40,26,26,26,26,-13,]),'DOTMUL':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[27,-3,-4,-5,-6,-7,-8,-9,-11,-31,27,27,-30,27,27,27,-12,-13,-14,-15,-16,-17,-18,-19,27,27,27,27,27,27,27,27,27,27,-1,-2,27,27,27,27,27,-39,-10,27,27,-32,-33,-34,27,27,-40,27,27,27,27,-13,]),'DOTDIV':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[28,-3,-4,-5,-6,-7,-8,-9,-11,-31,28,28,-30,28,28,28,-12,-13,-14,-15,-16,-17,-18,-19,28,28,28,28,28,28,28,28,28,28,-1,-2,28,28,28,28,28,-39,-10,28,28,-32,-33,-34,28,28,-40,28,28,28,28,-13,]),'ASSIGN':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[29,-3,-4,-5,-6,-7,-8,-9,-11,-31,29,29,-30,29,29,29,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,29,29,29,29,29,-39,-10,29,29,-32,-33,-34,29,29,-40,29,29,29,29,-13,]),'ADDASSIGN':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[30,-3,-4,-5,-6,-7,-8,-9,-11,-31,30,30,-30,30,30,30,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,30,30,30,30,30,-39,-10,30,30,-32,-33,-34,30,30,-40,30,30,30,30,-13,]),'SUBASSIGN':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[31,-3,-4,-5,-6,-7,-8,-9,-11,-31,31,31,-30,31,31,31,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,31,31,31,31,31,-39,-10,31,31,-32,-33,-34,31,31,-40,31,31,31,31,-13,]),'MULASSIGN':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[32,-3,-4,-5,-6,-7,-8,-9,-11,-31,32,32,-30,32,32,32,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,32,32,32,32,32,-39,-10,32,32,-32,-33,-34,32,32,-40,32,32,32,32,-13,]),'DIVASSIGN':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[33,-3,-4,-5,-6,-7,-8,-9,-11,-31,33,33,-30,33,33,33,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,33,33,33,33,33,-39,-10,33,33,-32,-33,-34,33,33,-40,33,33,33,33,-13,]),'MORE':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[34,-3,-4,-5,-6,-7,-8,-9,-11,-31,34,34,-30,34,34,34,-12,-13,-14,-15,-16,-17,-18,-19,34,34,34,34,34,-25,-26,-27,-28,-29,-1,-2,34,34,34,34,34,-39,-10,34,34,-32,-33,-34,34,34,-40,34,34,34,34,-13,]),'LESS':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[35,-3,-4,-5,-6,-7,-8,-9,-11,-31,35,35,-30,35,35,35,-12,-13,-14,-15,-16,-17,-18,-19,35,35,35,35,35,-25,-26,-27,-28,-29,-1,-2,35,35,35,35,35,-39,-10,35,35,-32,-33,-34,35,35,-40,35,35,35,35,-13,]),'MOREOREQ':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[36,-3,-4,-5,-6,-7,-8,-9,-11,-31,36,36,-30,36,36,36,-12,-13,-14,-15,-16,-17,-18,-19,36,36,36,36,36,-25,-26,-27,-28,-29,-1,-2,36,36,36,36,36,-39,-10,36,36,-32,-33,-34,36,36,-40,36,36,36,36,-13,]),'LESSOREQ':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[37,-3,-4,-5,-6,-7,-8,-9,-11,-31,37,37,-30,37,37,37,-12,-13,-14,-15,-16,-17,-18,-19,37,37,37,37,37,-25,-26,-27,-28,-29,-1,-2,37,37,37,37,37,-39,-10,37,37,-32,-33,-34,37,37,-40,37,37,37,37,-13,]),'EQUALS':([1,4,5,6,7,8,9,10,20,39,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[38,-3,-4,-5,-6,-7,-8,-9,-11,-31,38,38,-30,77,38,38,38,-12,-13,-14,-15,-16,-17,-18,-19,38,38,38,38,38,-25,-26,-27,-28,-29,-1,-2,38,38,38,38,38,-39,-10,38,38,-32,-33,-34,38,38,-40,38,38,38,38,-13,]),'TRANSPOSE':([1,4,5,6,7,8,9,10,20,39,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,86,87,88,89,90,91,92,94,96,97,99,100,102,],[39,-3,-4,-5,-6,-7,-8,-9,-11,-31,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-1,-2,39,39,39,39,39,-39,-10,39,39,-32,-33,-34,39,39,-40,39,39,39,39,39,]),'RPAREN':([4,5,6,7,8,9,10,20,39,40,42,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,88,89,90,91,92,94,97,100,102,],[-3,-4,-5,-6,-7,-8,-9,-11,-31,70,-30,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,81,82,83,84,85,-39,-10,-32,-33,-34,-35,-37,-40,-36,-38,-30,]),'RCURLY':([4,5,6,7,8,9,10,20,39,41,42,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,80,88,89,90,91,92,94,97,100,102,],[-3,-4,-5,-6,-7,-8,-9,-11,-31,71,-30,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,-39,-10,-32,-33,-34,-35,-37,-40,-36,-38,-30,]),'RSQUAR':([4,5,6,7,8,9,10,20,39,42,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,80,87,88,89,90,91,92,94,97,100,102,],[-3,-4,-5,-6,-7,-8,-9,-11,-31,-30,78,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,-39,-10,94,-32,-33,-34,-35,-37,-40,-36,-38,-30,]),'COMMA':([4,5,6,7,8,9,10,20,39,42,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,80,88,89,90,91,92,94,97,100,102,],[-3,-4,-5,-6,-7,-8,-9,-11,-31,-30,79,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,-39,-10,-32,-33,-34,-35,-37,-40,-36,-38,-30,]),'COLON':([4,5,6,7,8,9,10,20,39,42,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,80,86,88,89,90,91,92,94,97,100,102,],[-3,-4,-5,-6,-7,-8,-9,-11,-31,-30,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,-39,-10,93,-32,-33,-34,-35,-37,-40,-36,-38,-30,]),'ELSE':([4,5,6,7,8,9,10,20,39,42,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,80,88,89,90,91,92,94,97,100,102,],[-3,-4,-5,-6,-7,-8,-9,-11,-31,-30,-41,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-1,-2,-39,-10,-32,-33,-34,95,-37,-40,-36,-38,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,44,45,46,47,77,79,80,84,85,93,95,98,99,101,],[1,40,41,42,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,72,73,74,75,76,86,87,51,91,92,96,97,99,100,102,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','Mparser.py',28),
  ('expression -> LCURLY expression RCURLY','expression',3,'p_expression','Mparser.py',29),
  ('expression -> ID','expression',1,'p_expression','Mparser.py',30),
  ('expression -> INT','expression',1,'p_expression','Mparser.py',31),
  ('expression -> FLOAT','expression',1,'p_expression','Mparser.py',32),
  ('expression -> STRING','expression',1,'p_expression','Mparser.py',33),
  ('expression -> BREAK','expression',1,'p_expression','Mparser.py',34),
  ('expression -> CONTINUE','expression',1,'p_expression','Mparser.py',35),
  ('expression -> RETURN','expression',1,'p_expression','Mparser.py',36),
  ('expression -> expression SEMICOLON expression SEMICOLON','expression',4,'p_expression','Mparser.py',37),
  ('expression -> expression SEMICOLON','expression',2,'p_expression','Mparser.py',38),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','Mparser.py',41),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','Mparser.py',42),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','Mparser.py',43),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','Mparser.py',44),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_binop_dot','Mparser.py',48),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_binop_dot','Mparser.py',49),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_binop_dot','Mparser.py',50),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression_binop_dot','Mparser.py',51),
  ('expression -> expression ASSIGN expression','expression',3,'p_expression_assign','Mparser.py',55),
  ('expression -> expression ADDASSIGN expression','expression',3,'p_expression_assign','Mparser.py',56),
  ('expression -> expression SUBASSIGN expression','expression',3,'p_expression_assign','Mparser.py',57),
  ('expression -> expression MULASSIGN expression','expression',3,'p_expression_assign','Mparser.py',58),
  ('expression -> expression DIVASSIGN expression','expression',3,'p_expression_assign','Mparser.py',59),
  ('expression -> expression MORE expression','expression',3,'p_expression_relative','Mparser.py',63),
  ('expression -> expression LESS expression','expression',3,'p_expression_relative','Mparser.py',64),
  ('expression -> expression MOREOREQ expression','expression',3,'p_expression_relative','Mparser.py',65),
  ('expression -> expression LESSOREQ expression','expression',3,'p_expression_relative','Mparser.py',66),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_relative','Mparser.py',67),
  ('expression -> MINUS expression','expression',2,'p_expression_neg','Mparser.py',70),
  ('expression -> expression TRANSPOSE','expression',2,'p_expression_trans','Mparser.py',73),
  ('expression -> ZEROS LPAREN expression RPAREN SEMICOLON','expression',5,'p_expression_specials','Mparser.py',76),
  ('expression -> EYE LPAREN expression RPAREN SEMICOLON','expression',5,'p_expression_specials','Mparser.py',77),
  ('expression -> ONES LPAREN expression RPAREN SEMICOLON','expression',5,'p_expression_specials','Mparser.py',78),
  ('expression -> IF LPAREN expression RPAREN expression','expression',5,'p_expression_if','Mparser.py',81),
  ('expression -> IF LPAREN expression RPAREN expression ELSE expression','expression',7,'p_expression_if','Mparser.py',82),
  ('expression -> WHILE LPAREN expression RPAREN expression','expression',5,'p_expression_while','Mparser.py',86),
  ('expression -> FOR ID EQUALS expression COLON expression LCURLY expression expression','expression',9,'p_expression_for','Mparser.py',90),
  ('expression -> LSQUAR expression RSQUAR','expression',3,'p_expression_read','Mparser.py',94),
  ('expression -> LSQUAR expression COMMA expression RSQUAR','expression',5,'p_expression_read','Mparser.py',95),
  ('expression -> PRINT expression','expression',2,'p_expression_print','Mparser.py',102),
]
