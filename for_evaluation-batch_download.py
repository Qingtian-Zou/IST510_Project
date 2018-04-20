import os
import argparse
import sys

import get_images

FLAGS=None

def main():
    classes=os.listdir('256_ObjectCategories')
    for i in range(len(classes)):
        classes[i]=classes[i].split('.')[1].replace('-101','')
    i=0
    for kw in classes:
        get_images.download_image(kw)
        i+=1
        sys.stdout.write('Done: '+str(i)+'/256')
        sys.stdout.flush()
        sys.stdout.write('\b' * len('Done: '+str(i)+'/256'))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    FLAGS, unparsed=parser.parse_known_args()
    main()
