from pynumsParser import pynumsParser
from pynumsVisitor import pynumsVisitor
import math
import numpy as np
import csv
import matplotlib.pyplot as plt

class MyVisitor(pynumsVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.return_value = None

    def visitProg(self, ctx:pynumsParser.ProgContext):
        for stat in ctx.stat():
            self.visit(stat)

    def visitPrintExpr(self, ctx:pynumsParser.PrintExprContext):
        value = self.visit(ctx.expr())
        return value

    def visitAssign(self, ctx:pynumsParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value

    def visitBlank(self, ctx:pynumsParser.BlankContext):
        pass

    def visitMulDivMod(self, ctx:pynumsParser.MulDivModContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
            if ctx.op.type == pynumsParser.MUL:
                return np.dot(left, right)
            elif ctx.op.type == pynumsParser.DIV:
                return np.divide(left, right)
            elif ctx.op.type == pynumsParser.MOD:
                return np.remainder(left, right)
        else:
            if ctx.op.type == pynumsParser.MUL:
                return left * right
            elif ctx.op.type == pynumsParser.DIV:
                return left / right
            elif ctx.op.type == pynumsParser.MOD:
                return left % right
        
    def visitExponent(self, ctx:pynumsParser.ExponentContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitAddSub(self, ctx:pynumsParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
            if ctx.op.type == pynumsParser.ADD:
                return np.add(left, right)
            elif ctx.op.type == pynumsParser.SUB:
                return np.subtract(left, right)
        else:
            if ctx.op.type == pynumsParser.ADD:
                return left + right
            elif ctx.op.type == pynumsParser.SUB:
                return left - right

    def visitId(self, ctx:pynumsParser.IdContext):
        var_name = ctx.ID().getText()
       
        if var_name in self.variables:
            return (self.variables[var_name])
        else:
            raise NameError(f'La variable {var_name} no esta definida')
    
    def visitSqrt(self, ctx:pynumsParser.SqrtContext):
        value = self.visit(ctx.expr())
        if value < 0:
            raise ValueError("No se puede hallar la raiz cuadrada de de un numero negativo ")
        return math.sqrt(value)
    
    def visitTrig(self, ctx:pynumsParser.TrigContext):
        value = self.visit(ctx.expr())
        a = ctx.TRIG().getText()
        if a == "sin":
            return math.sin(math.radians(value))
        elif a == "cos":
            return math.cos(math.radians(value))
        elif a == "tan":
            return math.tan(math.radians(value))
    
    def visitComparison(self, ctx:pynumsParser.ComparisonContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.COMP().getText() == "<":
            return left < right
        elif ctx.COMP().getText() == ">":
            return left > right
        elif ctx.COMP().getText() == "==":
            return left == right
        elif ctx.COMP().getText() == "<=":
            return left <= right
        elif ctx.COMP().getText() == ">=":
            return left >= right

    def visitIf_statement(self, ctx:pynumsParser.If_statementContext):
        condition = self.visit(ctx.expr())
        if condition:
            for stat in ctx.stat():
                self.visit(stat)
        else:
            elif_executed = False
            for elif_ctx in ctx.elif_statement():
                elif_condition = self.visit(elif_ctx.expr())
                if elif_condition:
                    for stat in elif_ctx.stat():
                        self.visit(stat)
                    elif_executed = True
                    break
            if not elif_executed and ctx.else_statement():
                for stat in ctx.else_statement().stat():
                    self.visit(stat)

    def visitElif_statement(self, ctx:pynumsParser.Elif_statementContext):
        condition = self.visit(ctx.expr())
        if condition:
            for stat in ctx.stat():
                self.visit(stat)

    def visitElse_statement(self, ctx:pynumsParser.Else_statementContext):
        for stat in ctx.stat():
            self.visit(stat)

    def visitUnary(self, ctx:pynumsParser.UnaryContext):
        value = self.visit(ctx.expr())
        if ctx.sign.type == pynumsParser.SUB:
            return -value
        else:
            return value
        
    def visitFor_statement(self, ctx:pynumsParser.For_statementContext):
        var_name = ctx.ID().getText()
        start = int(self.visit(ctx.range_expr().expr(0)))
        end = int(self.visit(ctx.range_expr().expr(1)))
        for i in range(start, end + 1):
            self.variables[var_name] = i
            for stat in ctx.stat():
                self.visit(stat)
            del self.variables[var_name]

    def visitWhile_statement(self, ctx:pynumsParser.While_statementContext):
        condition = self.visit(ctx.expr())
        while condition:
            for stat in ctx.stat():
                self.visit(stat)
            condition = self.visit(ctx.expr())

    def visitPrint_statement(self, ctx:pynumsParser.Print_statementContext):
        value = self.visit(ctx.expr())
        print(value)

    
        
        
    
    def visitList_expr(self, ctx:pynumsParser.List_exprContext):
        return np.array([self.visit(expr) for expr in ctx.expr()])

    def visitMatrix_expr(self, ctx:pynumsParser.Matrix_exprContext):
        return np.array([self.visit(list_expr) for list_expr in ctx.list_expr()])


    def visitFunc_def(self, ctx:pynumsParser.FunctionDefinitionContext):
        func_name = ctx.ID().getText()
        func_params = ctx.params().ID() if ctx.params() else []
        func_body = ctx.stat()
        self.functions[func_name] = (func_params, func_body)

    def visitFunc_call1(self, ctx:pynumsParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        if func_name not in self.functions:
            raise NameError(f'La funcion {func_name} no esta definida')
        
        func_params, func_body = self.functions[func_name]
        old_vars = self.variables.copy()
        if ctx.args() :
            if len(func_params) != len(ctx.args().expr()):
                raise ValueError(f'La funcion {func_name} esperaba {len(func_params)} argumentos, pero {len(ctx.args().expr())} recibidos')

            local_vars = {}

            for param, arg_expr in zip(func_params, ctx.args().expr()):
                local_vars[param.getText()] = self.visit(arg_expr)


            self.variables.update(local_vars)

        result = None
        for stat in func_body:
            result = self.visit(stat)
            if self.return_value is not None:
                result = self.return_value
                self.return_value = None
                break

        self.variables = old_vars

        return result
        

    def visitInt(self, ctx:pynumsParser.IntContext):
        return int(ctx.INT().getText())

    def visitFloat(self, ctx:pynumsParser.IntContext):
        return float(ctx.FLOAT().getText())

    def visitReturn_stat(self, ctx:pynumsParser.ReturnStatementContext):
        self.return_value = self.visit(ctx.expr())
        return self.return_value
    
    def visitParens(self, ctx:pynumsParser.ParensContext):
        return self.visit(ctx.expr())
    
    def visitRead(self, ctx:pynumsParser.FileReadContext):
        file_path = ctx.STR().getText().strip('"')
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    def visitFileWrite(self, ctx:pynumsParser.FileWriteContext):
        file_path = ctx.STR().getText().strip('"')
        content = self.visit(ctx.expr())
        with open(file_path, 'w') as file:
            file.write(str(content))

    def visitFileAppend(self, ctx:pynumsParser.FileAppendContext):
        file_path = ctx.STR().getText().strip('"')
        content = self.visit(ctx.expr())
        with open(file_path, 'a') as file:
            file.write(str(content))

    def visitStr(self, ctx:pynumsParser.StrContext):
        return ctx.STR().getText().strip('"')
    
    def visitRead1csv(self, ctx:pynumsParser.Read1csvContext):
        file_name = ctx.STR().getText().strip('"')
        data = []
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append([float(x) if x.replace('.', '', 1).isdigit() else x for x in row])
        return np.array(data)

    def visitWriteCSV(self, ctx:pynumsParser.WriteCSVContext):
        file_name = ctx.STR().getText().strip('"')
        data = self.visit(ctx.expr())
        if isinstance(data, np.ndarray):
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
        else:
            raise ValueError("Los datos por escribir deben de ser un arreglo numpy (lista)")
        
    def visitGraficar(self, ctx):
        title = ctx.STR().getText().strip('"')
        x_data = self.visit(ctx.expr(0))
        y_data = self.visit(ctx.expr(1))
        
        if ctx.expr(2):
            plot_type = self.visit(ctx.expr(2))
        else:
            plot_type = "linea"
        
        plt.figure()
        plt.title(title)
        
        if plot_type == "puntos":
            plt.scatter(x_data, y_data)
        else:
            plt.plot(x_data, y_data)
        
        filename = title.replace(" ", "_") + ".png"
        plt.savefig(filename)
        print(f"Grafica guardada como {filename}")
        

    def visitAppend(self, ctx):
        array_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if array_name in self.variables:
            array = self.variables[array_name]
            if isinstance(array, np.ndarray):
                self.variables[array_name] = np.append(array, value)
            else:
                raise ValueError(f"{array_name} no es un arreglo numpy")
        else:
            raise ValueError(f"{array_name} no se encontro en la memoria")
        return self.variables[array_name]


    def visitRemove(self, ctx):
        array_name = ctx.ID().getText()
        index = self.visit(ctx.expr())
        if array_name in self.variables:
            array = self.variables[array_name]
            if isinstance(array, np.ndarray):
                if 0 <= index < len(array):
                    self.variables[array_name] = np.delete(array, index)
                else:
                    raise IndexError("Indice fuera de los limites")
            else:
                raise ValueError(f"{array_name} no es un arreglo numpy")
        else:
            raise ValueError(f"{array_name} no se encontro en la memoria")
        return self.variables[array_name]
        

    def visitSplit(self, ctx):
        delimiter = self.visit(ctx.expr())
        textName = ctx.ID().getText()

        text = self.variables[textName]

        if isinstance(text, str) and isinstance(delimiter, str):
            return text.split(delimiter)
        else:
            raise ValueError("La funcion de separar requiere argumentos de tipo String")