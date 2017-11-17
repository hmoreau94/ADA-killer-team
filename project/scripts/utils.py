import sys

sys.path.append('scripts/')
from data_import import *
from similarities import *
from amazon_api_interaction import *

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