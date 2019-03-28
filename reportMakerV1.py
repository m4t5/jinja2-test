'''
Demo outputting contents of a dataframe to a pdf via html

For test purposes, create 1000 random items in df and plot distribution

Also output percentile values

Templates
    Layout
        - header, footer. Consistent css etc
        - block 1
        - block 2
        - block 3
'''

import argparse
import jinja2
import pandas as pd
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description = "Make a report")
    parser.add_argument('--debug', '-d', action = 'store_true')
    return parser.parse_args()


def makeDf():
    df = pd.DataFrame()
    df['Rand No'] = np.random.random( size = 20)
    return df

def makeHtml(df):
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "block1.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render(df = df, aaa='998i')

def writeFile(filename, html):
    print('Writing file %s' % (filename))
    #print(html)
    outfile = open(filename , 'w')
    outfile.write(html)
    outfile.close()

def main():  
    df = makeDf()
    html = makeHtml(df)    
    writeFile('test.html', html)

args = get_args()
main()