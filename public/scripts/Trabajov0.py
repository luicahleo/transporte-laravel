# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:22:27 2021

@author: jgmir
"""

from ortools.linear_solver import pywraplp
from IOfunctionsExcel import *

name='Trabajov0.xlsx'  
excel_doc=openpyxl.load_workbook(name,data_only=True)
sheet=excel_doc['Sheet1']
a=Read_Excel_to_List(sheet, 'B8', 'B11')
b=Read_Excel_to_List(sheet, 'D8', 'D12')
Fabricas=Read_Excel_to_List(sheet, 'A8', 'A11')
Almacenes=Read_Excel_to_List(sheet, 'C8', 'C12')
c=Read_Excel_to_NesteDic(sheet, 'A1', 'F5') #rutas prohibidas se rellenan con una x
#a=[8,7,6,2] #producción
#b=[10,4,5,4] #demanda
#c=[[3,1,4,5],[2,3,2,1],[1,4,5,3],[3,5,4,1]] #costes
print(c)
#Fabricas=[j for j in range(1,len(a)+1)]
#Almacenes=[j for j in range(1,len(b)+1)]

def ejemplo():
    solver=pywraplp.Solver.CreateSolver('GLOP')
    
    x={}
    rfab={}
    ralm={}
    for i in Fabricas:
        x[i]={}
        for j in Almacenes:
            if c[i][j]!='x':
                x[i][j]=solver.NumVar(0,solver.infinity(),'X%d;%d'%(i,j))
    print('Número de variables=',solver.NumVariables())
    
    for i in Fabricas:
        rfab[i]=solver.Add(sum(x[i][j] for j in Almacenes if c[i][j]!='x')==a[i-1], 'RF%d'%(i))
    
    for j in Almacenes:
        ralm[j]=solver.Add(sum(x[i][j] for i in Fabricas if c[i][j]!='x')==b[j-1], 'RA%d'%(j))

    print('Número de restricciones=',solver.NumConstraints())
    
    solver.Minimize(solver.Sum(c[i][j]*x[i][j] for i in Fabricas for j in Almacenes if c[i][j]!='x')) #c[i-1][j-1] para listas internas
    
    status=solver.Solve()

    if status==pywraplp.Solver.OPTIMAL:
        for i in Fabricas:
            for j in Almacenes:
                if c[i][j]!='x':
                    print('X%d;%d = %d' % (i,j,x[i][j].solution_value()))
        for i in Fabricas:
            for j in Almacenes:
                if c[i][j]!='x':
                    print('CR%d;%d = %d' % (i,j,x[i][j].ReducedCost()))
        for i in Fabricas:
            print('u%d=%d'%(i,rfab[i].dual_value()))
        for j in Almacenes:
            print('v%d=%d'%(j,ralm[j].dual_value()))
        print('Funcion objetivo =',solver.Objective().Value())
    
    else:
        print('El problema es inadmisible')
    
    Solu={}
    for i in Almacenes:
        Solu[i]={j:0.0 for j in Almacenes}
    for i in Fabricas:
        for j in Almacenes:
            if c[i][j]!='x':
                Solu[i][j]=x[i][j].solution_value()
            else:
                Solu[i][j]=c[i][j]
    Write_NesteDic_to_Excel(excel_doc, name, sheet, Solu, 'F7', 'K11')
        
ejemplo()