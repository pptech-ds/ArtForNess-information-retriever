# -*- coding: utf-8 -*-
from modules.bm25 import bm25_scoring

artistes_csv = 'data/artforness_data_artistes.csv'
oeuvres_csv = 'data/artforness_data_oeuvres.csv'

#test1 
query1 = "je recherche un art sur le parapluie"
test1_df = bm25_scoring(oeuvres_csv, query1)
print("dataframe:   {}".format(test1_df))
print("Titre:       {}".format(test1_df.iloc[0]['Titre']))
print("Descriptif:  {}".format(test1_df.iloc[0]['Descriptif']))
print("Description: {}".format(test1_df.iloc[0]['Description']))
print("Prix:        {}".format(test1_df.iloc[0]['Prix']))
print("Categorie:   {}".format(test1_df.iloc[0]['Categorie']))
print("Etiquette:   {}".format(test1_df.iloc[0]['Etiquette']))
print("Lien:        {}".format(test1_df.iloc[0]['Lien']))
print("score:       {}".format(test1_df.iloc[0]['score']))

#test1
query2 = "je recherche une Sérigraphie"
test2_df = bm25_scoring(oeuvres_csv, query2)
print("dataframe:   {}".format(test2_df))
print("Titre:       {}".format(test2_df.iloc[0]['Titre']))
print("Descriptif:  {}".format(test2_df.iloc[0]['Descriptif']))
print("Description: {}".format(test2_df.iloc[0]['Description']))
print("Prix:        {}".format(test2_df.iloc[0]['Prix']))
print("Categorie:   {}".format(test2_df.iloc[0]['Categorie']))
print("Etiquette:   {}".format(test2_df.iloc[0]['Etiquette']))
print("Lien:        {}".format(test2_df.iloc[0]['Lien']))
print("score:       {}".format(test2_df.iloc[0]['score']))
