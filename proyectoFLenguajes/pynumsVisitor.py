# Generated from pynums.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pynumsParser import pynumsParser
else:
    from pynumsParser import pynumsParser

# This class defines a complete generic visitor for a parse tree produced by pynumsParser.

class pynumsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pynumsParser#prog.
    def visitProg(self, ctx:pynumsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#printExpr.
    def visitPrintExpr(self, ctx:pynumsParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#assign.
    def visitAssign(self, ctx:pynumsParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#blank.
    def visitBlank(self, ctx:pynumsParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#ifStatement.
    def visitIfStatement(self, ctx:pynumsParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#forStatement.
    def visitForStatement(self, ctx:pynumsParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#whileStatement.
    def visitWhileStatement(self, ctx:pynumsParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#printStatement.
    def visitPrintStatement(self, ctx:pynumsParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:pynumsParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#functionCall.
    def visitFunctionCall(self, ctx:pynumsParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#returnStatement.
    def visitReturnStatement(self, ctx:pynumsParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#fileOperation.
    def visitFileOperation(self, ctx:pynumsParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#fileCSV.
    def visitFileCSV(self, ctx:pynumsParser.FileCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#grafica.
    def visitGrafica(self, ctx:pynumsParser.GraficaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#modificarArray.
    def visitModificarArray(self, ctx:pynumsParser.ModificarArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#append.
    def visitAppend(self, ctx:pynumsParser.AppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#remove.
    def visitRemove(self, ctx:pynumsParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#if_statement.
    def visitIf_statement(self, ctx:pynumsParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#readCSV.
    def visitReadCSV(self, ctx:pynumsParser.ReadCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#writeCSV.
    def visitWriteCSV(self, ctx:pynumsParser.WriteCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#graficar.
    def visitGraficar(self, ctx:pynumsParser.GraficarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#read1csv.
    def visitRead1csv(self, ctx:pynumsParser.Read1csvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#elif_statement.
    def visitElif_statement(self, ctx:pynumsParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#else_statement.
    def visitElse_statement(self, ctx:pynumsParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#for_statement.
    def visitFor_statement(self, ctx:pynumsParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#range_expr.
    def visitRange_expr(self, ctx:pynumsParser.Range_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#while_statement.
    def visitWhile_statement(self, ctx:pynumsParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#print_statement.
    def visitPrint_statement(self, ctx:pynumsParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#func_def.
    def visitFunc_def(self, ctx:pynumsParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#return_stat.
    def visitReturn_stat(self, ctx:pynumsParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#params.
    def visitParams(self, ctx:pynumsParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#fileRead.
    def visitFileRead(self, ctx:pynumsParser.FileReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#fileWrite.
    def visitFileWrite(self, ctx:pynumsParser.FileWriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#fileAppend.
    def visitFileAppend(self, ctx:pynumsParser.FileAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#read.
    def visitRead(self, ctx:pynumsParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#args.
    def visitArgs(self, ctx:pynumsParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#splitt.
    def visitSplitt(self, ctx:pynumsParser.SplittContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#parens.
    def visitParens(self, ctx:pynumsParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#comparison.
    def visitComparison(self, ctx:pynumsParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#bool.
    def visitBool(self, ctx:pynumsParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#Exponent.
    def visitExponent(self, ctx:pynumsParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#AddSub.
    def visitAddSub(self, ctx:pynumsParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#readdcsv.
    def visitReaddcsv(self, ctx:pynumsParser.ReaddcsvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#trig.
    def visitTrig(self, ctx:pynumsParser.TrigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#unary.
    def visitUnary(self, ctx:pynumsParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#float.
    def visitFloat(self, ctx:pynumsParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#list.
    def visitList(self, ctx:pynumsParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#matrix.
    def visitMatrix(self, ctx:pynumsParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#func_call.
    def visitFunc_call(self, ctx:pynumsParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#int.
    def visitInt(self, ctx:pynumsParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#str.
    def visitStr(self, ctx:pynumsParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#MulDivMod.
    def visitMulDivMod(self, ctx:pynumsParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#sqrt.
    def visitSqrt(self, ctx:pynumsParser.SqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#id.
    def visitId(self, ctx:pynumsParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#readd.
    def visitReadd(self, ctx:pynumsParser.ReaddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#split.
    def visitSplit(self, ctx:pynumsParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#func_call1.
    def visitFunc_call1(self, ctx:pynumsParser.Func_call1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#list_expr.
    def visitList_expr(self, ctx:pynumsParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pynumsParser#matrix_expr.
    def visitMatrix_expr(self, ctx:pynumsParser.Matrix_exprContext):
        return self.visitChildren(ctx)



del pynumsParser