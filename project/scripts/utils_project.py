import sys

from scripts.similarities import *
from scripts.amazon_api_interaction import *
from scripts.analysis import *
from scripts.data_import import *

def print_details(asins,metadata_df,interesting_cols=['title', 'authors', 'publisher', 'imUrl']):
    """returns the title and authors of all the candidate duplicates of a given asin in similars

    @params:
    - asins : an iterable of asin for which we which to print the details
    - metadata_df : a dataframe containing the information relative to the different ASINs (with authors)
    """
    metadata_df = metadata_df.reset_index().set_index('asin')
    for col in interesting_cols:
        for asin in asins:
            print('Book {} - {}: {}'.format(asin,col, metadata_df.loc[asin][col]))
        print()


def display_images(asins, metadata_df):
    """Display the images of the candidate duplicates of a given asin in get_candidate

    @params:
    - asins : an iterable of asin for which we which to print the details
    - metadata_df : a dataframe containing the information relative to the different ASINs (with authors)
    """
    url_list = []
    metadata_df = metadata_df.reset_index().set_index('asin')
    for asin in asins:
        url = metadata_df.loc[asin]['imUrl']
        url_list.append(url)
    for link in url_list:
        display(Image(url=link,width=250, height=500))

def human_readible_time(time_s,n_msec):
    ''' Convert seconds to 'D days, HH:MM:SS.FFF' 
    
    @params:
    - time_s : the time to print in seconds
    - n_msec : the number of msec we want to display
    '''
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