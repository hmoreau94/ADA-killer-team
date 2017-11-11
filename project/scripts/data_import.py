import pandas as pd
import numpy as np
import re

def get_paths(category_index,DATA_FOLDER,META_FOLDER,REVIEWS_FOLDER,CATEGORIES):
    """
    Returns the path to the meta and review file for a given category

    params:
    - category_index : the index of the category in the CATEGORIES list
    - DATA_FOLDER : path of the folder to the data
    - META_FOLDER : the name of the folder containing the metadata
    - REVIEWS_FOLDER : the name of the folder containing the reviews
    - CATEGORIES : the list of all categories of data files we have
    """
    meta_path = META_FOLDER + "meta_" + CATEGORIES[category_index] + ".json"
    review_path = REVIEWS_FOLDER + "reviews_" + CATEGORIES[category_index] + ".json"
    return meta_path,review_path

def get_raw_dataframe(path,max_count):
    """
    Used to explore the data without any prior processing of the json, 
    it will simply aggregate the rows of the JSON to form a dataframe
    """
    with open(path) as f:
        count = 0
        # Initialize the dict with empty lists
        df_list= []
        for chunk in f:
            if(count > 0 and count >= max_count): break
            d = eval(chunk)
            df_list.append(d)
            count += 1

        df = pd.DataFrame(df_list)
        return df

def clean_category_name(cat):
    cleaned = str(cat).replace("&amp;","")
    cleaned = re.sub(' +','_',cleaned)
    return cleaned

def handle_format(column_name,line,row):
    """
    Given a line of the JSON it will extract the value of the column column_name 
    into the correct format and will yield a NaN if the value isn't in the line
    
    params:
    - column_name : the column for which we wish to have the attribute
    - line : dictionnary extracted from the JSON line
    - row : the dictionnary to which we wish to save the value
    """
    valid_cols = ['title', 'unixReviewTime', 'asin', 'description', 'related', 'imUrl', 
                 'overall', 'reviewText', 'reviewTime', 'helpful', 'price', 'salesRank', 
                 'categories', 'summary', 'reviewerID', 'reviewerName','brand']
    
    # Handle arguments
    if(column_name not in valid_cols):
        raise NameError("{} not a valid column_name".format(column_name))
    if(not line.get(column_name)):
        # Cannot find the column in this line
        if(column_name != 'salesRank'):
            row[column_name] = np.nan
        return row
    else:
        value = line.get(column_name,np.nan)    

        if(column_name == 'salesRank'):
            for cat, rank in value.items():
                # give the rank for each category
                row['salesRank_'+clean_category_name(cat)]=rank
        elif(column_name == 'categories'):
            # categories are given as list of list
            row[column_name] = value[0]
        elif(column_name == "helpful"):
            # categories are given as list of list
            row[column_name] = 0 if value[1] == 0 else value[0]/np.float64(value[1])
        elif(column_name == "reviewTime"):
            # convert to readable format
            day,month,year = value.replace(",","").split()
            row[column_name] = "{}/{}/{}".format(day,month,year)
        else:
            row[column_name] = value
        return row

def import_interesting_cols(path,isMeta,interesting_cols=[],max_count=-1,dropna=False):
    """
    Will import from the loose JSON located at path the columns of interest and format then correctly
    Returns a Datafram
    
    @params:
    - path : the location of the JSON 
    - isMeta : a Boolean that explains if the file encapsulates metadata or reviews
    - interesting_cols : the columns that we want to obtain, by default it will get all the columns
    - max_count : the maximum amount of rows we wish to extract
    - dropna : if we wish to drop rows where at least one column in NaN
    """
    # Handling arguments
    if(isMeta):
        all_cols = ['asin','title','brand','salesRank','description','categories','imUrl','price','related']
    else:
        all_cols = ["asin","helpful","overall","reviewText","reviewTime","reviewerID","reviewerName",
                    "summary","unixReviewTime"]
    
    if(len(interesting_cols) == 0):
        interesting_cols = all_cols

    with open(path) as f:
        count = 0
        df_list= []
        for chunk in f:
            if(count > 0 and count >= max_count): break
            d = eval(chunk)
            row = {}
            for c in interesting_cols:
                row = handle_format(c,d,row)
            df_list.append(row)
            count += 1
        
        df = pd.DataFrame(df_list)

        ranks = [c for c in df.columns if c.startswith('salesRank')]
        numerical_cols = ranks + ['price']
        for c in numerical_cols:
            if(c in interesting_cols):
                df[c] = pd.to_numeric(df[c],errors='coerce')
        if("unixReviewTime" in interesting_cols):
            # Convert unix dates into proper date time
            df["unixReviewTime"] = pd.to_datetime(df["unixReviewTime"],unit='s')
        
        # we drop the rows that contains at least one NAN    
        if(dropna):
            df = df.dropna(how='any')

        return df