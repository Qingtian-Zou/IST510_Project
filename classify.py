import os
import shutil
import argparse
import sys

import label_image

FLAGS=None


def main():
    values=[]
    if(FLAGS.image_dir):
        image_files=os.listdir(FLAGS.image_dir)
        classify_one(FLAGS.image_dir.split('/')[-1],image_files,values)
        shutil.copy2(os.path.join('downloaded_images',FLAGS.image_dir.split('/')[-1],image_files[values.index(max(values))]),os.path.join('downloaded_images',image_files[values.index(max(values))]))
    else:
        labels=os.listdir('downloaded_images')
        if labels==[]:
            print('No images to classify! Quiting...')
            exit
        else:
            j=0
            for i in range(len(labels)):
                if '.' in labels[i]:
                    j+=1
                    continue
                values.append([])
                image_files=os.listdir(os.path.join('downloaded_images',labels[i]))
                classify_one(labels[i],image_files,values[i-j])
                shutil.copy2(os.path.join('downloaded_images',labels[i],image_files[values[i-j].index(max(values[i-j]))]),os.path.join('downloaded_images',image_files[values[i-j].index(max(values[i-j]))]))
                sys.stdout.write('Done: '+str(i-j+1)+'/256')
                sys.stdout.flush()
                sys.stdout.write('\b' * len('Done: '+str(i-j+1)+'/256'))

def classify_one(label,image_files,value):
    for ii in range(len(image_files)):
        value.append(label_image.main(label,os.path.join('downloaded_images',label,image_files[ii]),FLAGS.graph))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument(
        "--graph",
        type=str,
        help="Path to the graph"
    )
    parser.add_argument(
        "--image_dir",
        type=str,
        default='',
        help='Path to the images to classify. If not given, evaluation mode is activated, where all will be classified.'
    )
    FLAGS, unparsed= parser.parse_known_args()
    main()