import sys

from data_import import *
from similarities import *
from amazon_api_interaction import *


def print_details(asin,similars,book_only_candidates):
    """returns the title and authors of all the candidate duplicates of a given asin in similars

    @params:
    - asin : the ASIN of the book for which we want to compare titles
    - similars : a dictionnary that attributes ASIN to a list of ASIN corresponding to candidate similars 
    - book_only_candidates : a dataframe containing the information relative to the different ASINs (with authors)
    """
    key_entry = book_only_candidates.loc[asin]
    print("{}\n\t{}".format(key_entry['title'],key_entry['authors']))
    for sim in similars[asin]:
        entry = book_only_candidates.loc[sim]
        title = entry['title']
        authors = entry['authors']
        print("{}\n\t{}".format(title,authors))
    print("--------------------------------------------------------------")


def get_titles(asin,get_candidate,book_desc_titles):
    """returns the titles of all the candidate duplicates of a given asin in get_candidate

    @params:
    - asin : the ASIN of the book for which we want to compare titles
    - get_candidate : a dictionnary that attributes ASIN to a list of ASIN corresponding to candidate similars 
    - book_desc_titles : a dataframe containing the information relative to the different ASINs
    """
    title_desc_list = []
    title_desc_list.append(book_desc_titles.loc[asin]['title'])
    for sim in get_candidate[asin]:
        entry = book_desc_titles.loc[sim]
        title = entry['title']
        title_desc_list.append(title)
    return title_desc_list

def get_desc(asin,get_candidate, book_desc_titles):
    """returns the description of all the candidate duplicates of a given asin in get_candidate

     @params:
    - asin : the ASIN of the book for which we want to compare description
    - get_candidate : a dictionnary that attributes ASIN to a list of ASIN corresponding to candidate similars 
    - book_desc_titles : a dataframe containing the information relative to the different ASINs
    """
    title_desc_list = []
    title_desc_list.append(book_desc_titles.loc[asin]['description'])
    for sim in get_candidate[asin]:
        entry = book_desc_titles.loc[sim]
        desc = entry['description']
        title_desc_list.append(desc)
    return title_desc_list

def display_images(asin,get_candidate, book_desc_titles):
    """Display the images of the candidate duplicates of a given asin in get_candidate

     @params:
    - asin : the ASIN of the book for which we want to compare images
    - get_candidate : a dictionnary that attributes ASIN to a list of ASIN corresponding to candidate similars 
    - book_desc_titles : a dataframe containing the information relative to the different ASINs
    """
    url_list = []
    url_list.append(book_desc_titles.loc[asin]['imUrl'])
    for sim in get_candidate[asin]:
        entry = book_desc_titles.loc[sim]
        url = entry['imUrl']
        url_list.append(url)
    for link in url_list:
        display(Image(url=link))

def print_time(time_s,n_msec):
    ''' Convert seconds to 'D days, HH:MM:SS.FFF' '''
    m, s = divmod(time_s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if n_msec > 0:
        pattern = '%%02d:%%02d:%%0%d.%df' % (n_msec+3, n_msec)
    else:
        pattern = r'%02d:%02d:%02d'
    if d == 0:
        return pattern % (h, m, s)
    return ('%d days, ' + pattern) % (d, h, m, s)


def progress(count, total, suffix=''):
    """ Shows the progress of a given action 
    
    @params:
    - count : the current count of done operations
    - total : the total number of operation to do
    - suffix : a message printed after the progress bar
    """
    
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s (%s/%s) %s\r' % (bar, percents, '%', count,total,suffix))
    sys.stdout.flush()