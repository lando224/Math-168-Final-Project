#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:27:40 2020

@author: sarinaawatramani
"""

import networkx as nx
import matplotlib as mp
import pandas as pd


vc=pd.read_csv("../../../Downloads/GitHub/168/vc_investments.csv", header=0) 
#read vc investments into dataframe

people= pd.read_csv("../../../Downloads/GitHub/168/people_investments.csv")
#read people investments into dataframe

company= pd.read_csv("../../../Downloads/GitHub/168/company_investments.csv")
#read company investments into dataframe 

vc_edges= pd.DataFrame([vc.funding_id, vc.startup_id]).transpose()
vc_edges['combined']=vc_edges.values.tolist()
#extracts investments from vc investments dataframe 

edge_list_vc= vc_edges['combined'].tolist()
#creates list of node pairs

G_vc=nx.DiGraph()
G_vc.add_edges_from(edge_list_vc)
#creates graph from node pairs of vc investments

people_edges=pd.DataFrame([people.funding_id, people.startup_id]).transpose()
people_edges['combined']=people_edges.values.tolist()
#extracts investments from people investments to dataframe

edge_list_people=people_edges['combined'].tolist()
#creates list of node pairs


G_people=nx.DiGraph()
G_people.add_edges_from(edge_list_people)
#creates graph from node pair of people investments

company_edges=pd.DataFrame([company.funding_id, company.startup_id]).transpose()
company_edges['combined']=company_edges.values.tolist()
#extracts investments from company investments to dataframe

edge_list_company=company_edges['combined'].tolist()
#creates list of node pairs

G_companies=nx.DiGraph()
G_companies.add_edges_from(edge_list_company)
#creates graph from node pairs of company investments 

#definition of function to use for sort based on degree
def takeSecond(elem):
    return elem[1]

vc_out_deg=list(G_vc.out_degree()) #out degrees of the nodes of the vc network  
vc_out_deg.sort(key=takeSecond) #sorts list of degrees
fund_most_investments=vc_out_deg[-1] #fund which invests in the largest number of companies

vc_in_deg=list(G_vc.in_degree())#in degrees of the nodes of the vc network 
vc_in_deg.sort(key=takeSecond)
startup_mostvcs=vc_in_deg[-1]#startup with the largest number of VCs investing in it 

people_out_deg=list(G_people.out_degree())#out degrees of the nodes in the people investments network 
people_out_deg.sort(key=takeSecond)
person_most_investments=people_out_deg[-1] #person with the most investments

people_in_deg=list(G_people.in_degree())#in degrees of companies in the people investments network 
people_in_deg.sort(key=takeSecond)
startup_mostpeople=people_in_deg[-1] #startup with the most investments from single investors

companies_out_deg=list(G_companies.out_degree())#out degrees of company investment network 
companies_out_deg.sort(key=takeSecond)
company_most_investments=companies_out_deg[-1] #company which invests the most in other companies

companies_in_deg=list(G_companies.in_degree()) #in degrees of company investment network 
companies_in_deg.sort(key=takeSecond)
startup_most_companies=companies_in_deg[-1] #startup with the most other companies investng in it 
