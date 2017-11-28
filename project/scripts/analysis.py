# Import all necessary dependencies to run the Hedring Effect analysis
import pandas as pd
import numpy as np
import pickle
import math
import matplotlib.pylab as plt
import scipy.stats as st

# Global variables
# Color definition
light_green = (152, 223, 138)
strong_green = (44, 160, 44)
light_red =  (255, 152, 150)
orange = (255, 187, 120)
strong_red = (214, 39, 40)

# Here we declared all the applied functions. 
# This represent functions that are applied on each row of a dataFrame through the pd.DataFrame.apply function
# to compute various significant data (these functions are mostly applied on the matching DataFrame representing
#  a pair of matching data with the asin_1 and asin_2 cols)
def return_first_review_overall(x, review_books_df):
    """
        return for the current row of the books dataFrame the rate of the first review

        @params:
        - x: the current row (with indices representing the asin of the book)
        - review_books_df: the dataframe containing the review of all books
    """
    asin = x.name
    return review_books_df.query('asin == @asin').sort_values(by=['unixReviewTime']).iloc[0].overall

def categorize_pair(x, return_category_func, books_df):
    """
        return for the current row of the matching dataFrame a pair of letter corresponding to the group of the pair (HH,HL,LL...)

        @params:
        - x the current row (with asin_1 and asin_2 value of pair asin matched)
        - return_category_func a helper function that return a letter category from a rating
        - books_df: the dataframe containing all books informations
    """
    asin_1 = x['asin_1']
    asin_2 = x['asin_2']
    book_1_first_overall = books_df.query('asin == @asin_1').first_review_overall
    book_2_first_overall = books_df.query('asin == @asin_2').first_review_overall
    return return_category_func(book_1_first_overall) + return_category_func(book_2_first_overall)

def find_highest_diff(asin_2, books_df):
    """
        return for the current asin_2 of the matching dataFrame a boolean that is True only if asin_2 represent 
        a book with the lowest possible rating: 1

        @params:
        - asin_2 the current row asin_2 of the matching dataFrame
        - books_df: the dataframe containing all books informations
    """
    val = books_df.query('asin == @asin_2').first_review_overall 
    val = int(val.values[0])
    if val == 1:
        return True
    else:
        return False

def find_n_reviews(x, n, review_books_df):
    """
        return for the current row of the matching dataFrame a list of dictionary containing n first rating attributed to each book

        @params:
        - x the current row (with asin_1 and asin_2 value of pair asin matched)
        - n: number of ratings to take after the first one
        - review_books_df: the dataframe containing the review of all books
    """
    asin_1 = x['asin_1']
    asin_2 = x['asin_2']

    overall_reviews_1 = review_books_df.query('asin == @asin_1').sort_values(
    'unixReviewTime').iloc[0:(n+1)].overall.tolist()
    overall_reviews_2 = review_books_df.query('asin == @asin_2').sort_values(
    'unixReviewTime').iloc[0:(n+1)].overall.tolist()

    dic_1 = {'asin': asin_1}
    for i, val in enumerate(overall_reviews_1):
        dic_1[str(i)+"-th-review"] = val

    dic_2 = {'asin': asin_2}
    for i, val in enumerate(overall_reviews_2):
        dic_2[str(i)+"-th-review"] = val
    
    return [dic_1, dic_2]

def mean_more_n_reviews(x, n, review_books_df):
    """
        return for the current row of the matching dataFrame a list of dictionary containing the mean of all the review from the nth

        @params:
        - x the current row (with asin_1 and asin_2 value of pair asin matched)
        - n: n-th review to start take the average from
        - review_books_df: the dataframe containing the review of all books
    """
    asin_1 = x['asin_1']
    asin_2 = x['asin_2']
    
    dic_1 = {}
    dic_2 = {}
    
    if (len(review_books_df.query('asin == @asin_1')) > n and len(review_books_df.query('asin == @asin_2')) > 20):
        overall_reviews_1 = review_books_df.query('asin == @asin_1').sort_values(
        'unixReviewTime').iloc[n:].overall.tolist()
        overall_reviews_2 = review_books_df.query('asin == @asin_2').sort_values(
        'unixReviewTime').iloc[n:].overall.tolist()

        dic_1 = {'asin': asin_1, 'mean': np.mean(overall_reviews_1)}
        dic_2 = {'asin': asin_2, 'mean': np.mean(overall_reviews_2)}
        
    
    return [dic_1, dic_2]

# Define some utility function used throughout our analysis
def return_category_from_value_HL(val):
    """
        return the letter H or L from a rating value in this particular case return H when val is in between 4 and 5 and L otherwise

        @params:
        - val: the value of the rating.
    """
    val = int(val.values[0])
    if val >= 4:
        return 'H'
    else:
        return 'L'

def return_category_from_value_HML(val):
    """
        return the letter H, L or M from a rating value

        @params:
        - val: the value of the rating.
    """
    val = int(val.values[0])
    if val == 5:
        return 'H'
    elif val == 4:
        return 'M'
    else:
        return 'L'

def rgb_to_matplot_lib(rgb):
    """
        convert a rgb tuple into a matplotlib readable color tuple

        @params:
        - rgb: a simple rgb tuple
    """
    r, g, b = rgb
    return (r / 255., g / 255., b / 255.)

def compute_stats_on_reviews_df(df):
    """
        return a list of dictionarries containing the mean and the interval of confidence at 95% of each column of the specified df except asin col
        
        @params:
        - df: a df with each books of a certain category as row and a specified number of reviews following the first review as columns
    """
    stats = []
    for col in df.columns:
        if col != 'asin':
            mean = np.mean(df[col])
            if np.std(df[col]) != 0:
                b = st.t.interval(0.95, len(df[col])-1, loc=mean, scale=st.sem(df[col]))
            else:
                b = (np.nan, np.nan)
            stats.append({'mean': mean, 'interval95': (b[1] - b[0])/2})
    return stats

def error_from_interval(interval):
    """
        return the error value from an interval (value needed for errorplot)
        
        @params:
        - interval: tuple representing the interval we are interested to plot
    """
    return (interval[1] - interval[0]) / 2

# visualisation functions
def plot_example_rat_and_cumrat_subplots(data_1, data_2):
    """
        plot the example subplot of the ratings by rating index and cumulative rating by rating index with colors and size prefixed

        @params:
        - data_1: a dataFrame with the overall rating for each review of the first book
        - data_2: a dataFrame with the overall rating for each review of the second book
    """
    color_1 = rgb_to_matplot_lib(light_green)
    color_2 = rgb_to_matplot_lib(light_red)

    # create the fig. and axes.
    f, (ax1, ax2) = plt.subplots(1, 2)
    f.set_size_inches(16,7)

    # plot small dash lines to follow the grading   
    for y in range(1, 6):    
        ax1.plot(range(0, 45), [y] * len(range(0, 45)), "--", lw=0.5, color="black", alpha=0.3)
        ax2.plot(range(0, 45), [y] * len(range(0, 45)), "--", lw=0.5, color="black", alpha=0.3)

    # plot data for the first book
    indices_1 = data_1.reset_index().index.tolist()
    overall_1 = data_1.overall.tolist()

    ax1.plot(indices_1, overall_1, color=color_1)

    cum_avg = np.divide(np.cumsum(overall_1),np.add(indices_1, [1] * len(indices_1)))
    ax2.plot(indices_1, cum_avg, color=color_1, label="Book 1")

    # plot data for the second book
    indices_2 = data_2.reset_index().index.tolist()
    overall_2 = data_2.overall.tolist()

    ax1.plot(indices_2, overall_2, color=color_2)

    cum_avg = np.divide(np.cumsum(overall_2),np.add(indices_2, [1] * len(indices_2)))
    ax2.plot(indices_2, cum_avg, color=color_2, label="Book 2")

    # remove some plot frameline
    ax1.spines["top"].set_visible(False)       
    ax1.spines["right"].set_visible(False)
    ax2.spines["top"].set_visible(False)       
    ax2.spines["right"].set_visible(False)

    # axis 
    ax1.set_ylabel('Rating', fontsize = 14)
    ax2.set_ylabel('Rating', fontsize = 14)
    ax1.set_xlabel('Rating Index', fontsize = 14)
    ax2.set_xlabel('Rating Index', fontsize = 14)
    ax1.tick_params(axis='both', labelsize=14)
    ax2.tick_params(axis='both', labelsize=14)

    # set titles
    ax1.set_title('Ratings', fontsize = 14)
    ax2.set_title('Cumulative Average Ratings', fontsize = 14)

    # limit the axis to what's necessary
    ax1.set_ylim(1.0, 5.1)
    ax2.set_ylim(1.0, 5.1)
    ax1.set_xlim(0, 45)
    ax2.set_xlim(0, 45)

    # change ticks on y axis
    ax1.set_yticks(range(1,6))
    ax2.set_yticks(range(1,6))

    # add a legend
    ax2.legend(loc="lower right", fontsize=12)

    plt.show()

def plot_stats_bar_plot(title, stats_1, color_1, label_1, stats_2, color_2, label_2):
    """
        plot the mean and the 95% confidence interval of the rating of 2 defined books category

        @params:
        - title: the title of the grap
        - stats_1: a list of dictionnary containing the mean and interval95 for the books in the first category
        - color_1: the color wanted for the first category
        - label_1: the label used in the legend for the first category
        - stats_2: a list of dictionnary containing the mean and interval95 for the books in the second category
        - color_2: the color wanted for the secondcategory
        - label_2: the label used in the legend for the second category
    """
    plt.figure(figsize=(12, 9))   
    
    # create the fig. and axes.
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)       
    ax.spines["right"].set_visible(False)

    color_1 = rgb_to_matplot_lib(color_1)
    color_2 = rgb_to_matplot_lib(color_2)
    
    plt.errorbar(range(0, len(stats_1)), [x['mean'] for x in stats_1],
                 [x['interval95'] for x in stats_1], color=color_1, capsize=5, label=label_1)
    plt.errorbar(range(0, len(stats_2)), [x['mean'] for x in stats_2],
                 [x['interval95'] for x in stats_2], color=color_2, capsize=5, label=label_2)
    
    # axis 
    ax.set_ylabel('Rating', fontsize = 14)
    ax.set_xlabel('Rating Index', fontsize = 14)
    ax.tick_params(axis='both', labelsize=14)
    
    # plot small dash lines to follow the grading   
    for y in range(1, 6):    
        ax.plot(range(0, 45), [y] * len(range(0, 45)), "--", lw=0.5, color="black", alpha=0.3)
    
    # add a legend
    ax.legend(loc="lower right", fontsize=14)
    
    # set titles
    ax.set_title(title, fontsize = 14)
    
    plt.ylim([1,5.1])
    plt.xlim([0,5.1])
    plt.show()

def plot_lastreviews_means_and_errors(H_in_HL_mean, H_in_HL_error, L_in_HL_mean, L_in_HL_error,
                                     H_in_HH_mean, H_in_HH_error, H_in_HM_mean, H_in_HM_error,
                                     M_in_HM_mean, M_in_HM_error):
    """
        plot the errorplot with each longterm ratings mean.

        @params:
        - H_in_HL_mean: the mean value for the specified category
        - H_in_HL_error: the error value for the specified category.
        - L_in_HL_mean: the mean value for the specified category
        - L_in_HL_error: the error value for the specified category.
        - H_in_HH_mean: the mean value for the specified category
        - H_in_HH_error: the error value for the specified category.
        - H_in_HM_mean: the mean value for the specified category
        - H_in_HM_error: the error value for the specified category.
        - M_in_HM_mean: the mean value for the specified category
        - M_in_HM_error: the error value for the specified category.
    """
    # plot the result in a nice plot
    plt.figure(figsize=(12, 9))   

    # create the fig. and axes.
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)       
    ax.spines["right"].set_visible(False)

    # define the color to use
    color_1 = rgb_to_matplot_lib(strong_green)
    color_2 = rgb_to_matplot_lib(light_green)
    color_3 = rgb_to_matplot_lib(strong_red)
    color_4 = rgb_to_matplot_lib(light_green)
    color_5 = rgb_to_matplot_lib(orange)



    # axis 
    ax.set_ylabel('Rating', fontsize = 14)
    ax.tick_params(axis='both', labelsize=14)

    # plot small dash lines to follow the grading   
    for y in np.arange(4.0, 4.6, 0.1):    
        ax.plot(range(0, 45), [y] * len(range(0, 45)), "--", lw=0.5, color="black", alpha=0.3)


    # set titles
    ax.set_title('20+ reviews average rating for each case in each group', fontsize = 14)

    plt.ylim([1,5.1])
    plt.xlim([0,5.1])

    plt.errorbar(1, H_in_HH_mean, H_in_HH_error, lineStyle= None, capsize=5, marker="^", color=color_1)
    plt.errorbar(2, H_in_HL_mean, H_in_HL_error, lineStyle= None, capsize=5, marker="^", color=color_2)
    plt.errorbar(3, L_in_HL_mean, L_in_HL_error, lineStyle= None, capsize=5, marker="^", color=color_3)
    plt.errorbar(4, H_in_HM_mean, H_in_HM_error, lineStyle= None, capsize=5, marker="^", color=color_4)
    plt.errorbar(5, M_in_HM_mean, M_in_HM_error, lineStyle= None, capsize=5, marker="^", color=color_5)

    plt.text(0.8, 4.01, "({:04.3f})".format(H_in_HH_mean), fontsize=14, color=color_1)
    plt.text(1.8, 4.01, "({:04.3f})".format(H_in_HL_mean), fontsize=14, color=color_2) 
    plt.text(2.8, 4.01, "({:04.3f})".format(L_in_HL_mean), fontsize=14, color=color_3) 
    plt.text(3.8, 4.01, "({:04.3f})".format(H_in_HM_mean), fontsize=14, color=color_4) 
    plt.text(4.8, 4.01, "({:04.3f})".format(M_in_HM_mean), fontsize=14, color=color_5) 


    # set ticks label
    ax.set_xticks(range(1,6))
    ax.set_xticklabels(('H in HH', 'H in HL', 'L in HL', 'H in HM', 'M in HM'))

    #set ticks color
    colors = [color_1, color_2, color_3, color_4, color_5]
    for xtick, color in zip(ax.get_xticklabels(), colors):
        xtick.set_color(color)

    plt.ylim([4,4.6])
    plt.xlim([0.5,5.5])
    plt.show()