# perform analysis process for all directories

import sys
import glob
import os
import subprocess

args = sys.argv

if len(args) < 2:
    print("usage: %s [dir]"%(args[0]))
    sys.exit(1)

# first, obtain list of files

for path,dirs,names in os.walk(args[1]):
    for name in names:
        if name.endswith('.mp4'):
            fname_out = os.path.join('./processed',os.path.splitext(name)[0]) + '.avi'

            # perform openface
            if os.path.exists(fname_out) is not True:
                str = "./FeatureExtraction -f %s"%(os.path.join(path,name))
                print("Performing openface")
                print(str)
                os.system(str)
            else:
                print('%s exists. skip this file.'%(fname_out))

print("finished")

