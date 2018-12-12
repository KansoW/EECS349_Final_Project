#!/bin/env python
import pandas as pd

def generateArff(dataframe, attributes_list, mode):
    '''
    input:
        dataframe (pandas) of a csv file
        a list of attributes
    output:
        arff file for weka
    '''
    # dataframe of selected attributes
    if mode=="all":
        sel_df = dataframe
    elif mode=="select":
        sel_df = dataframe.loc[:, attributes_list]
    elif mode=="delete":
        sel_df = dataframe.drop(columns=attributes_list)

    attr_list = extractAttr(sel_df)
    print(sel_df.head(4))

    with open('output.arff', 'w') as f:
        f.write("@relation training\n")
        f.write("\n")
        for i in range(len(attr_list)):
            temp_str = "@attribute "
            temp_str += attr_list[i]
            temp_str += "\n"
            f.write(temp_str)

        f.write("\n")
        f.write("@data\n")
        for player_idx in range(len(sel_df)):
            attr_str = ""
            for i in range(len(attr_list)):
                tmp = attr_list[i].split(' ')[0].strip("'")
                attr_str += str(sel_df.loc[player_idx, tmp])
                attr_str += ','
            attr_str = attr_str[:-1]
            attr_str += '\n'
            f.write(attr_str)

def extractAttr(dataframe):
    '''
    input: selected dataframe
    output: e.g. ["'attr1' numeric", "'attr2' string"]
    '''
    attr_list = []
    onerow = dataframe.iloc[0, :]
    print(onerow)
    for i in range(1, len(onerow)):
        tmp = onerow[i] # attribute
        if type(tmp) is str:
            attr_set = set(dataframe.iloc[:, i])
            temp_str = "'{}' ".format(dataframe.columns.values.tolist()[i])
            temp_str += '{'
            for value in attr_set:
                temp_str += value
                temp_str += ', '
            temp_str = temp_str[:-2]
            temp_str += '}'
            attr_list.append(temp_str)
        else:
            attr_list.append("'{}' {}".format(dataframe.columns.values.tolist()[i], 'numeric'))

    print(attr_list)
    return attr_list


if __name__ == "__main__":
    ## put "Player" on the first
    sel_attr = ["Player", "Status", "Pos", "X1", "g"]
    sel_attr = ["X1", "X2"]
    del_attr = ["Status", "g", "mp", "TOV", "TOV%", "OWS", "DWS", "WS", "WS/48", "fg3a_heave", "fg3_heave"]

    nba_df = pd.read_csv("nbaStats_modified.csv")
    # print(nba_df.head(5))
    generateArff(nba_df, del_attr, mode="delete")
