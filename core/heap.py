from nodes import *
import math

class Heap:
    def __init__(self, tree):
        self.tree = tree
        self.html = ""

    def getValue(self, node):

        if(isinstance(node, NumberNode)):
            if(node.value == "&"):
                return " "

            else:
                return node.value

        elif(isinstance(node, AdditionNode)):
            return "+"

        elif(isinstance(node, SubtractionNode)):
            return "-"

        elif(isinstance(node, MultiplyNode)):
            return "*"

        elif(isinstance(node, DivideNode)):
            return "/"

        else:
            return ""


    def createHeap(self):
        treeList = self.traverseTree(self.tree)

        n = len(treeList)
        h = int(math.ceil(math.log2(n+1)))
        mi = int(math.pow(2, h-1)-1)
        mf = mi * 2
        w = mf + 1
        matrix = []

        for i in range (0,h):
            row = []
            for j in range (0, w):
                row.append("&nbsp;")

            matrix.append(row)

        #Primera Fila
        matrix[0][int(math.floor(w/2))] = self.getValue(treeList[0])

        #filas intermedias
        positionCounter = 1
        for i in range(1, h-1):

            for count in range ( int((math.pow(2,h-1-i))-1) , int(len(matrix[i]) - 1),  int(math.pow(2,h-i))):
                matrix[i][count] = self.getValue(treeList[positionCounter])
                positionCounter += 1

        #Ultima fila
        for count in range( 0 , w, 2):
            if(positionCounter >= len(treeList)):
                break

            else:
                matrix[h-1][count] = str(self.getValue(treeList[positionCounter]))
                positionCounter += 1
        
        self.printHeap(matrix)

        return self.html


    def traverseTree(self, root):

        if( isinstance(root, NumberNode) ):
            return [root]

        else:

            left, right = [], []

            if(root.node_a != None):
                left = self.traverseTree(root.node_a)

            if(root.node_b != None):
                right = self.traverseTree(root.node_b)

            diference = 0

            if(len(left) > len(right)):
                diference = len(left) - len(right)

                for i in range (0, diference):
                    right.append(NumberNode("&"))

            elif(len(right) > len(left)):
                diference = len(right) - len(left)

                for i in range (0, diference):
                    left.append(NumberNode("&"))

            return [root] + left + right

    def printHeap(self, matrix = []):
        self.html = "<table border ='1'>"

        for i in range (0, len(matrix)) :
            self.html += "<tr>";
                
            for j in range ( 0, len(matrix[i])):
                if((len(matrix[i]) == 2) and (j == 1)):
                    self.html += '<td colspan = "2"> %s </td>'%(matrix[i][j]);

                else:
                    self.html += '<td> %s </td>'%(matrix[i][j]);

            self.html += "</tr>";
