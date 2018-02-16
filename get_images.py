import requests
import argparse
import os

FLAGS=None

def main():
    headers={'X-Requested-With': 'XMLHttpRequest'}
    url='https://cors-anywhere.herokuapp.com/https://www.google.com.ua/search?source=lnms&sa=X&gbv=1&tbm=isch&q='+FLAGS.keyword
    h=requests.get(url,headers=headers)
    xml_file=open('results.html', 'w+')
    xml_file.write(h.text)
    xml_file.close()
    lines=h.text.split()
    images_url=[]
    for line in lines:
        if line[0:13]=='src="https://':
            images_url.append(line.split('=',1)[1].replace('"',''))
    url_file=open('image_url.txt','w+')
    url_file.writelines(images_url)
    url_file.close()
    i=0
    for url in images_url:
        img_data=requests.get(url).content
        if not os.path.exists('downloaded_images'):
            os.makedirs('downloaded_images')
        if not os.path.exists(os.path.join('downloaded_images',FLAGS.keyword)):
            os.makedirs(os.path.join('downloaded_images',FLAGS.keyword))
        with open(os.path.join(os.getcwd(),'downloaded_images',FLAGS.keyword,FLAGS.keyword+str(i+1)+'.jpg'),'wb') as handler:
            handler.write(img_data)
        i+=1
        if i==20:
            break

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '--keyword',
        type=str,
        default='',
        help='keyword for image searching'
    )
    FLAGS, unparsed= parser.parse_known_args() # keyword is not parsed!!!
    main()