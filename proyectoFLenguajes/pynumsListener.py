# Generated from pynums.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pynumsParser import pynumsParser
else:
    from pynumsParser import pynumsParser

# This class defines a complete listener for a parse tree produced by pynumsParser.
class pynumsListener(ParseTreeListener):

    # Enter a parse tree produced by pynumsParser#prog.
    def enterProg(self, ctx:pynumsParser.ProgContext):
        pass

    # Exit a parse tree produced by pynumsParser#prog.
    def exitProg(self, ctx:pynumsParser.ProgContext):
        pass


    # Enter a parse tree produced by pynumsParser#printExpr.
    def enterPrintExpr(self, ctx:pynumsParser.PrintExprContext):
        pass

    # Exit a parse tree produced by pynumsParser#printExpr.
    def exitPrintExpr(self, ctx:pynumsParser.PrintExprContext):
        pass


    # Enter a parse tree produced by pynumsParser#assign.
    def enterAssign(self, ctx:pynumsParser.AssignContext):
        pass

    # Exit a parse tree produced by pynumsParser#assign.
    def exitAssign(self, ctx:pynumsParser.AssignContext):
        pass


    # Enter a parse tree produced by pynumsParser#blank.
    def enterBlank(self, ctx:pynumsParser.BlankContext):
        pass

    # Exit a parse tree produced by pynumsParser#blank.
    def exitBlank(self, ctx:pynumsParser.BlankContext):
        pass


    # Enter a parse tree produced by pynumsParser#ifStatement.
    def enterIfStatement(self, ctx:pynumsParser.IfStatementContext):
        pass

    # Exit a parse tree produced by pynumsParser#ifStatement.
    def exitIfStatement(self, ctx:pynumsParser.IfStatementContext):
        pass


    # Enter a parse tree produced by pynumsParser#forStatement.
    def enterForStatement(self, ctx:pynumsParser.ForStatementContext):
        pass

    # Exit a parse tree produced by pynumsParser#forStatement.
    def exitForStatement(self, ctx:pynumsParser.ForStatementContext):
        pass


    # Enter a parse tree produced by pynumsParser#whileStatement.
    def enterWhileStatement(self, ctx:pynumsParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by pynumsParser#whileStatement.
    def exitWhileStatement(self, ctx:pynumsParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by pynumsParser#printStatement.
    def enterPrintStatement(self, ctx:pynumsParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by pynumsParser#printStatement.
    def exitPrintStatement(self, ctx:pynumsParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by pynumsParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:pynumsParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by pynumsParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:pynumsParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by pynumsParser#functionCall.
    def enterFunctionCall(self, ctx:pynumsParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by pynumsParser#functionCall.
    def exitFunctionCall(self, ctx:pynumsParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by pynumsParser#returnStatement.
    def enterReturnStatement(self, ctx:pynumsParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by pynumsParser#returnStatement.
    def exitReturnStatement(self, ctx:pynumsParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by pynumsParser#fileOperation.
    def enterFileOperation(self, ctx:pynumsParser.FileOperationContext):
        pass

    # Exit a parse tree produced by pynumsParser#fileOperation.
    def exitFileOperation(self, ctx:pynumsParser.FileOperationContext):
        pass


    # Enter a parse tree produced by pynumsParser#fileCSV.
    def enterFileCSV(self, ctx:pynumsParser.FileCSVContext):
        pass

    # Exit a parse tree produced by pynumsParser#fileCSV.
    def exitFileCSV(self, ctx:pynumsParser.FileCSVContext):
        pass


    # Enter a parse tree produced by pynumsParser#grafica.
    def enterGrafica(self, ctx:pynumsParser.GraficaContext):
        pass

    # Exit a parse tree produced by pynumsParser#grafica.
    def exitGrafica(self, ctx:pynumsParser.GraficaContext):
        pass


    # Enter a parse tree produced by pynumsParser#modificarArray.
    def enterModificarArray(self, ctx:pynumsParser.ModificarArrayContext):
        pass

    # Exit a parse tree produced by pynumsParser#modificarArray.
    def exitModificarArray(self, ctx:pynumsParser.ModificarArrayContext):
        pass


    # Enter a parse tree produced by pynumsParser#append.
    def enterAppend(self, ctx:pynumsParser.AppendContext):
        pass

    # Exit a parse tree produced by pynumsParser#append.
    def exitAppend(self, ctx:pynumsParser.AppendContext):
        pass


    # Enter a parse tree produced by pynumsParser#remove.
    def enterRemove(self, ctx:pynumsParser.RemoveContext):
        pass

    # Exit a parse tree produced by pynumsParser#remove.
    def exitRemove(self, ctx:pynumsParser.RemoveContext):
        pass


    # Enter a parse tree produced by pynumsParser#if_statement.
    def enterIf_statement(self, ctx:pynumsParser.If_statementContext):
        pass

    # Exit a parse tree produced by pynumsParser#if_statement.
    def exitIf_statement(self, ctx:pynumsParser.If_statementContext):
        pass


    # Enter a parse tree produced by pynumsParser#readCSV.
    def enterReadCSV(self, ctx:pynumsParser.ReadCSVContext):
        pass

    # Exit a parse tree produced by pynumsParser#readCSV.
    def exitReadCSV(self, ctx:pynumsParser.ReadCSVContext):
        pass


    # Enter a parse tree produced by pynumsParser#writeCSV.
    def enterWriteCSV(self, ctx:pynumsParser.WriteCSVContext):
        pass

    # Exit a parse tree produced by pynumsParser#writeCSV.
    def exitWriteCSV(self, ctx:pynumsParser.WriteCSVContext):
        pass


    # Enter a parse tree produced by pynumsParser#graficar.
    def enterGraficar(self, ctx:pynumsParser.GraficarContext):
        pass

    # Exit a parse tree produced by pynumsParser#graficar.
    def exitGraficar(self, ctx:pynumsParser.GraficarContext):
        pass


    # Enter a parse tree produced by pynumsParser#read1csv.
    def enterRead1csv(self, ctx:pynumsParser.Read1csvContext):
        pass

    # Exit a parse tree produced by pynumsParser#read1csv.
    def exitRead1csv(self, ctx:pynumsParser.Read1csvContext):
        pass


    # Enter a parse tree produced by pynumsParser#elif_statement.
    def enterElif_statement(self, ctx:pynumsParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by pynumsParser#elif_statement.
    def exitElif_statement(self, ctx:pynumsParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by pynumsParser#else_statement.
    def enterElse_statement(self, ctx:pynumsParser.Else_statementContext):
        pass

    # Exit a parse tree produced by pynumsParser#else_statement.
    def exitElse_statement(self, ctx:pynumsParser.Else_statementContext):
        pass


    # Enter a parse tree produced by pynumsParser#for_statement.
    def enterFor_statement(self, ctx:pynumsParser.For_statementContext):
        pass

    # Exit a parse tree produced by pynumsParser#for_statement.
    def exitFor_statement(self, ctx:pynumsParser.For_statementContext):
        pass


    # Enter a parse tree produced by pynumsParser#range_expr.
    def enterRange_expr(self, ctx:pynumsParser.Range_exprContext):
        pass

    # Exit a parse tree produced by pynumsParser#range_expr.
    def exitRange_expr(self, ctx:pynumsParser.Range_exprContext):
        pass


    # Enter a parse tree produced by pynumsParser#while_statement.
    def enterWhile_statement(self, ctx:pynumsParser.While_statementContext):
        pass

    # Exit a parse tree produced by pynumsParser#while_statement.
    def exitWhile_statement(self, ctx:pynumsParser.While_statementContext):
        pass


    # Enter a parse tree produced by pynumsParser#print_statement.
    def enterPrint_statement(self, ctx:pynumsParser.Print_statementContext):
        pass

    # Exit a parse tree produced by pynumsParser#print_statement.
    def exitPrint_statement(self, ctx:pynumsParser.Print_statementContext):
        pass


    # Enter a parse tree produced by pynumsParser#func_def.
    def enterFunc_def(self, ctx:pynumsParser.Func_defContext):
        pass

    # Exit a parse tree produced by pynumsParser#func_def.
    def exitFunc_def(self, ctx:pynumsParser.Func_defContext):
        pass


    # Enter a parse tree produced by pynumsParser#return_stat.
    def enterReturn_stat(self, ctx:pynumsParser.Return_statContext):
        pass

    # Exit a parse tree produced by pynumsParser#return_stat.
    def exitReturn_stat(self, ctx:pynumsParser.Return_statContext):
        pass


    # Enter a parse tree produced by pynumsParser#params.
    def enterParams(self, ctx:pynumsParser.ParamsContext):
        pass

    # Exit a parse tree produced by pynumsParser#params.
    def exitParams(self, ctx:pynumsParser.ParamsContext):
        pass


    # Enter a parse tree produced by pynumsParser#fileRead.
    def enterFileRead(self, ctx:pynumsParser.FileReadContext):
        pass

    # Exit a parse tree produced by pynumsParser#fileRead.
    def exitFileRead(self, ctx:pynumsParser.FileReadContext):
        pass


    # Enter a parse tree produced by pynumsParser#fileWrite.
    def enterFileWrite(self, ctx:pynumsParser.FileWriteContext):
        pass

    # Exit a parse tree produced by pynumsParser#fileWrite.
    def exitFileWrite(self, ctx:pynumsParser.FileWriteContext):
        pass


    # Enter a parse tree produced by pynumsParser#fileAppend.
    def enterFileAppend(self, ctx:pynumsParser.FileAppendContext):
        pass

    # Exit a parse tree produced by pynumsParser#fileAppend.
    def exitFileAppend(self, ctx:pynumsParser.FileAppendContext):
        pass


    # Enter a parse tree produced by pynumsParser#read.
    def enterRead(self, ctx:pynumsParser.ReadContext):
        pass

    # Exit a parse tree produced by pynumsParser#read.
    def exitRead(self, ctx:pynumsParser.ReadContext):
        pass


    # Enter a parse tree produced by pynumsParser#args.
    def enterArgs(self, ctx:pynumsParser.ArgsContext):
        pass

    # Exit a parse tree produced by pynumsParser#args.
    def exitArgs(self, ctx:pynumsParser.ArgsContext):
        pass


    # Enter a parse tree produced by pynumsParser#splitt.
    def enterSplitt(self, ctx:pynumsParser.SplittContext):
        pass

    # Exit a parse tree produced by pynumsParser#splitt.
    def exitSplitt(self, ctx:pynumsParser.SplittContext):
        pass


    # Enter a parse tree produced by pynumsParser#parens.
    def enterParens(self, ctx:pynumsParser.ParensContext):
        pass

    # Exit a parse tree produced by pynumsParser#parens.
    def exitParens(self, ctx:pynumsParser.ParensContext):
        pass


    # Enter a parse tree produced by pynumsParser#comparison.
    def enterComparison(self, ctx:pynumsParser.ComparisonContext):
        pass

    # Exit a parse tree produced by pynumsParser#comparison.
    def exitComparison(self, ctx:pynumsParser.ComparisonContext):
        pass


    # Enter a parse tree produced by pynumsParser#bool.
    def enterBool(self, ctx:pynumsParser.BoolContext):
        pass

    # Exit a parse tree produced by pynumsParser#bool.
    def exitBool(self, ctx:pynumsParser.BoolContext):
        pass


    # Enter a parse tree produced by pynumsParser#Exponent.
    def enterExponent(self, ctx:pynumsParser.ExponentContext):
        pass

    # Exit a parse tree produced by pynumsParser#Exponent.
    def exitExponent(self, ctx:pynumsParser.ExponentContext):
        pass


    # Enter a parse tree produced by pynumsParser#AddSub.
    def enterAddSub(self, ctx:pynumsParser.AddSubContext):
        pass

    # Exit a parse tree produced by pynumsParser#AddSub.
    def exitAddSub(self, ctx:pynumsParser.AddSubContext):
        pass


    # Enter a parse tree produced by pynumsParser#readdcsv.
    def enterReaddcsv(self, ctx:pynumsParser.ReaddcsvContext):
        pass

    # Exit a parse tree produced by pynumsParser#readdcsv.
    def exitReaddcsv(self, ctx:pynumsParser.ReaddcsvContext):
        pass


    # Enter a parse tree produced by pynumsParser#trig.
    def enterTrig(self, ctx:pynumsParser.TrigContext):
        pass

    # Exit a parse tree produced by pynumsParser#trig.
    def exitTrig(self, ctx:pynumsParser.TrigContext):
        pass


    # Enter a parse tree produced by pynumsParser#unary.
    def enterUnary(self, ctx:pynumsParser.UnaryContext):
        pass

    # Exit a parse tree produced by pynumsParser#unary.
    def exitUnary(self, ctx:pynumsParser.UnaryContext):
        pass


    # Enter a parse tree produced by pynumsParser#float.
    def enterFloat(self, ctx:pynumsParser.FloatContext):
        pass

    # Exit a parse tree produced by pynumsParser#float.
    def exitFloat(self, ctx:pynumsParser.FloatContext):
        pass


    # Enter a parse tree produced by pynumsParser#list.
    def enterList(self, ctx:pynumsParser.ListContext):
        pass

    # Exit a parse tree produced by pynumsParser#list.
    def exitList(self, ctx:pynumsParser.ListContext):
        pass


    # Enter a parse tree produced by pynumsParser#matrix.
    def enterMatrix(self, ctx:pynumsParser.MatrixContext):
        pass

    # Exit a parse tree produced by pynumsParser#matrix.
    def exitMatrix(self, ctx:pynumsParser.MatrixContext):
        pass


    # Enter a parse tree produced by pynumsParser#func_call.
    def enterFunc_call(self, ctx:pynumsParser.Func_callContext):
        pass

    # Exit a parse tree produced by pynumsParser#func_call.
    def exitFunc_call(self, ctx:pynumsParser.Func_callContext):
        pass


    # Enter a parse tree produced by pynumsParser#int.
    def enterInt(self, ctx:pynumsParser.IntContext):
        pass

    # Exit a parse tree produced by pynumsParser#int.
    def exitInt(self, ctx:pynumsParser.IntContext):
        pass


    # Enter a parse tree produced by pynumsParser#str.
    def enterStr(self, ctx:pynumsParser.StrContext):
        pass

    # Exit a parse tree produced by pynumsParser#str.
    def exitStr(self, ctx:pynumsParser.StrContext):
        pass


    # Enter a parse tree produced by pynumsParser#MulDivMod.
    def enterMulDivMod(self, ctx:pynumsParser.MulDivModContext):
        pass

    # Exit a parse tree produced by pynumsParser#MulDivMod.
    def exitMulDivMod(self, ctx:pynumsParser.MulDivModContext):
        pass


    # Enter a parse tree produced by pynumsParser#sqrt.
    def enterSqrt(self, ctx:pynumsParser.SqrtContext):
        pass

    # Exit a parse tree produced by pynumsParser#sqrt.
    def exitSqrt(self, ctx:pynumsParser.SqrtContext):
        pass


    # Enter a parse tree produced by pynumsParser#id.
    def enterId(self, ctx:pynumsParser.IdContext):
        pass

    # Exit a parse tree produced by pynumsParser#id.
    def exitId(self, ctx:pynumsParser.IdContext):
        pass


    # Enter a parse tree produced by pynumsParser#readd.
    def enterReadd(self, ctx:pynumsParser.ReaddContext):
        pass

    # Exit a parse tree produced by pynumsParser#readd.
    def exitReadd(self, ctx:pynumsParser.ReaddContext):
        pass


    # Enter a parse tree produced by pynumsParser#split.
    def enterSplit(self, ctx:pynumsParser.SplitContext):
        pass

    # Exit a parse tree produced by pynumsParser#split.
    def exitSplit(self, ctx:pynumsParser.SplitContext):
        pass


    # Enter a parse tree produced by pynumsParser#func_call1.
    def enterFunc_call1(self, ctx:pynumsParser.Func_call1Context):
        pass

    # Exit a parse tree produced by pynumsParser#func_call1.
    def exitFunc_call1(self, ctx:pynumsParser.Func_call1Context):
        pass


    # Enter a parse tree produced by pynumsParser#list_expr.
    def enterList_expr(self, ctx:pynumsParser.List_exprContext):
        pass

    # Exit a parse tree produced by pynumsParser#list_expr.
    def exitList_expr(self, ctx:pynumsParser.List_exprContext):
        pass


    # Enter a parse tree produced by pynumsParser#matrix_expr.
    def enterMatrix_expr(self, ctx:pynumsParser.Matrix_exprContext):
        pass

    # Exit a parse tree produced by pynumsParser#matrix_expr.
    def exitMatrix_expr(self, ctx:pynumsParser.Matrix_exprContext):
        pass



del pynumsParser