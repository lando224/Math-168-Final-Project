#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:27:40 2020

@author: sarinaawatramani
"""

import networkx as nx
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd


vc=pd.read_csv("../../../Downloads/GitHub/168/vc_investments.csv", header=0) 
#read vc investments into dataframe

people= pd.read_csv("../../../Downloads/GitHub/168/people_investments.csv")
#read people investments into dataframe

company= pd.read_csv("../../../Downloads/GitHub/168/company_investments.csv")
#read company investments into dataframe 

d1 = pd.Series(vc.startup_name.values,index=vc.startup_id).to_dict()
d2= pd.Series(vc.funding_name.values,index=vc.funding_id).to_dict()

d3= {**d1, **d2} #dictionary of names for nodes in vc network 

#removes duplicate funds
result_vc = {}

for key,value in d3.items():
    if value not in result_vc.values():
        result_vc[key] = value

#print(result_vc)

vc_edges= pd.DataFrame([vc.funding_id, vc.startup_id]).transpose()
#vc_edges['weight']=1 #adds column for weight when adding weighted edges
vc_edges['combined']=vc_edges.values.tolist()

#extracts investments from vc investments dataframe 

edge_list_vc= vc_edges['combined'].tolist()
#creates list of node pairs

G_vc=nx.DiGraph()
G_vc.add_edges_from(edge_list_vc)
G_vc=nx.relabel_nodes(G_vc, result_vc)
#creates graph from node pairs of vc investments

people['full_name']=people['funding_first_name']+ people['funding_last_name']

dp1 = pd.Series(people.startup_name.values,index=people.startup_id).to_dict()
dp2= pd.Series(people.full_name.values,index=people.funding_id).to_dict()

dp3= {**dp1, **dp2} #dictionary of names for nodes in vc network 

#removes duplicate people
result_p = {}

for key,value in dp3.items():
    if value not in result_p.values():
        result_p[key] = value

people_edges=pd.DataFrame([people.funding_id, people.startup_id]).transpose()
#people_edges['weight']=1 #adds column for weight when adding weighted edges
people_edges['combined']=people_edges.values.tolist()
#extracts investments from people investments to dataframe

edge_list_people=people_edges['combined'].tolist()
#creates list of node pairs


G_people=nx.DiGraph()
G_people.add_edges_from(edge_list_people)
G_people=nx.relabel_nodes(G_people, result_p)
#creates graph from node pair of people investments

dc1 = pd.Series(company.startup_name.values,index=company.startup_id).to_dict()
dc2= pd.Series(company.funding_name.values,index=company.funding_id).to_dict()

dc3= {**dc1, **dc2} #dictionary of names for nodes in vc network 

#removes duplicate people
result_c = {}

for key,value in dc3.items():
    if value not in result_c.values():
        result_c[key] = value

company_edges=pd.DataFrame([company.funding_id, company.startup_id]).transpose()
company_edges['combined']=company_edges.values.tolist()
#extracts investments from company investments to dataframe

edge_list_company=company_edges['combined'].tolist()
#creates list of node pairs

G_companies=nx.DiGraph()
G_companies.add_edges_from(edge_list_company)
G_companies=nx.relabel_nodes(G_companies, result_c)
#creates graph from node pairs of company investments 

#definition of function to use for sort based on degree
def takeSecond(elem):
    return elem[1]

vc_out_deg=list(G_vc.out_degree()) #out degrees of the nodes of the vc network  
vc_out_deg.sort(key=takeSecond) #sorts list of degrees
fund_most_investments=vc_out_deg[-1] #fund which invests in the largest number of companies
#print(vc_out_deg)
print("Fund which has made the largest number of investments:", fund_most_investments)

vc_in_deg=list(G_vc.in_degree())#in degrees of the nodes of the vc network 
vc_in_deg.sort(key=takeSecond)
startup_mostvcs=vc_in_deg[-1]#startup with the largest number of VCs investing in it 
#print(vc_in_deg)

print("Startup with the most vcs invested in it:", startup_mostvcs)

people_out_deg=list(G_people.out_degree())#out degrees of the nodes in the people investments network 
people_out_deg.sort(key=takeSecond)
person_most_investments=people_out_deg[-1] #person with the most investments
#print(people_out_deg)
print("The person who has made the largest number of investments:", person_most_investments)

people_in_deg=list(G_people.in_degree())#in degrees of companies in the people investments network 
people_in_deg.sort(key=takeSecond)
startup_mostpeople=people_in_deg[-1] #startup with the most investments from single investors
print(people_in_deg)
print("The startup which has had the largest number of single investors:", startup_mostpeople)

companies_out_deg=list(G_companies.out_degree())#out degrees of company investment network 
companies_out_deg.sort(key=takeSecond)
company_most_investments=companies_out_deg[-1] #company which invests the most in other companies
#print(companies_out_deg)
print("The company which has made the largest number of investments in other companies:", company_most_investments)

companies_in_deg=list(G_companies.in_degree()) #in degrees of company investment network 
companies_in_deg.sort(key=takeSecond)
startup_most_companies=companies_in_deg[-1] #startup with the most other companies investng in it 
#print(companies_in_deg)
print("The startup which has received the largest number of investments from other companies:", startup_most_companies)


