import math
class rechnungen:

    def klammern(rechnung):
        if "(" in rechnung and ")":
            start = rechnung.index("(")
            end = rechnung.rindex(")")
            inner_rechnung = rechnung[start+1:end]
            result = rechnungen.klammern(inner_rechnung)
            rechnung = rechnung[:start] + str(result) + rechnung[end+1:]
            return rechnungen.klammern(rechnung)
        else:
            return rechnungen.berechne(rechnung)

    def fakultaet (rechnung, zahlen, operatoren):
        for i in rechnung:
                if rechnung[rechnung.index(i)-2] == "-":
                    return "Mathematischer Fehler"
        for i, op in enumerate(operatoren):
                if op == "!":
                        if i == "0":
                            zahlen[i]=1
                            del operatoren[i]
                        else:
                            zahlen[i]=math.factorial(int(zahlen[i]))
                            del operatoren[i]

    def prozent (zahlen, operatoren):
        for i, op in enumerate(operatoren):
                if op == "%":
                    zahlen[i]=zahlen[i]/100
                    del operatoren[i]

    def potenz (zahlen, operatoren):
        for i, op in enumerate(operatoren):
                if op == "%":
                    zahlen[i]=zahlen[i]/100
                    del operatoren[i]

    def dividierenundmultiplizieren (zahlen, operatoren):
        for i, op in enumerate(operatoren):
                if op == "*":
                    zahlen[i] = zahlen[i] * zahlen[i+1]
                    del zahlen[i+1]
                    del operatoren[i]
                    break
                elif op == "/":
                    if zahlen[i+1] == 0:
                        return "Mathematischer Fehler"
                    zahlen[i] = zahlen[i] / zahlen[i+1]
                    del zahlen[i+1]
                    del operatoren[i]
                    break
            
    def plusminus (zahlen, operatoren):
        op = operatoren.pop(0)
        zahl = zahlen.pop(0)
        if op == "+":
            zahlen[0] += zahl
        elif op == "-":
            zahlen[0] -= zahl
            if zahlen[0]==0:
                zahlen[0]=zahlen[0]*1
            else:
                zahlen[0]=zahlen[0]*-1
        return zahlen[0]
    