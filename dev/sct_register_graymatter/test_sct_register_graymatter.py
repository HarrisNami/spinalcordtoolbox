#!/usr/bin/env python
#########################################################################################
#
# Test function sct_segment_graymatter
#
# ---------------------------------------------------------------------------------------
# Copyright (c) 2014 Polytechnique Montreal <www.neuro.polymtl.ca>
# Author: Sara Dupont
# modified: 2015/08/31
#
# About the license: see the file LICENSE.TXT
#########################################################################################

import commands
import sys
# append path that contains scripts, to be able to load modules
status, path_sct = commands.getstatusoutput('echo $SCT_DIR')
sys.path.append(path_sct + '/scripts')
from msct_image import Image
from numpy import any


def test(data_path):
    output = ''
    status = 0
    # parameters
    folder_data = ['mt/', 't2/']
    file_data = ['mt0.nii.gz', 'mt0_seg.nii.gz', 't2.nii.gz', 't2_seg.nii.gz', 'warp_template2anat.nii.gz']

    # define command
    cmd = 'sct_register_graymatter -i ' + data_path + folder_data[0] + file_data[0] \
          + ' -iseg ' + data_path + folder_data[0] + file_data[1] \
          + ' -anat ' + data_path + folder_data[1] + file_data[2] \
          + ' -anat-seg ' + data_path + folder_data[1] + file_data[3] \
          + ' -warp ' + data_path + folder_data[1] + file_data[4] \
          + ' -v 1 -r 0'

    output += '\n====================================================================================================\n'+cmd+'\n====================================================================================================\n\n'  # copy command
    # run command
    s, o = commands.getstatusoutput(cmd)
    status += s
    output += o

    return status, output

if __name__ == "__main__":
    # call main function
    status, output = test(path_sct+'/testing/sct_testing_data/data/')
    print output