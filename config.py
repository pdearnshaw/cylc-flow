#!/usr/bin/python

# User-editable controller configuration file

# This file gets listed automatically in the latex
# documentation, so keep line lengths reasonable.

import logging

# dummy mode settings
dummy_mode = True
dummy_clock_rate = 60      
dummy_clock_offset = 10 

# logging 
logging_dir = 'LOGFILES' 
#logging_level = logging.INFO
logging_level = logging.DEBUG

state_dump_file = 'STATE'

# pyro nameserver group must be unique per controller
# instance so that different programs don't interfere.
pyro_ns_group = ':ecoconnect'   

# start and (optional) stop reference times
start_time = "2008102018"
stop_time = "2008102218"

# list the tasks to run
operational_tasks = [ 
        'downloader',
        'nwp_global',
        'global_prep',
        'globalwave',
        'nzlam:finished',
        'nzlam_post',
        'nzwave',
        'ricom',
        'nztide',
        'streamflow',
        'topnet',
        'topnet_vis',
        'topnet_products',
        'mos' 
        ]

topnet_test_tasks = [ 
        'oper2test_topnet',
        'streamflow',
        'topnet',
        'topnet_vis',
        'topnet_products'
        ]

#task_list = operational_tasks
task_list = topnet_test_tasks

# list tasks to dummy out in non-dummy-mode
# (currently needs to be defined as an empty list if not needed)
dummy_out = []
#dummy_out = [ 'topnet' ]
