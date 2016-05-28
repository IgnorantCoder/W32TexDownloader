# -*- coding: utf-8 -*-

import json
import urllib.request
import os
import argparse

def jsonToFileNames(path) :
    arr = []
    with open(path) as f:
        arr = json.load(f)
    return arr

def fileNamesToUris(baseuri, fileNames) :
    return [baseuri + fileName for fileName in fileNames]

def download(uri, dir) :
    fileName = uri.rsplit('/', 1)[1].split('?')[0]
    path = os.path.join(dir, fileName)
    urllib.request.urlretrieve(uri, path)

def createDir(dir) :
    if not os.path.exists(dir) :
        os.makedirs(dir)
    return dir

def main():
    #---------------------------------------------------------------------------
    #   option parser
    #---------------------------------------------------------------------------
    parser = argparse.ArgumentParser(description = 'This script downloads w32tex files.')
    parser.add_argument('-b', '--baseuri', dest = 'baseuri', required = True, help='''target uri's base string.''')
    parser.add_argument('-j', '--json'   , dest = 'json'   , required = True, help='''target file name.'''        )
    parser.add_argument('-t', '--target' , dest = 'target' , required = True, help='''files download to this.'''  )
    args = parser.parse_args()
    
    fileNames = jsonToFileNames(args.json)
    uris = fileNamesToUris(args.baseuri, fileNames)
    targetDir = createDir(args.target)
    for uri in uris :
        print('download... ' + uri)
        download(uri, targetDir)

if __name__ == "__main__":
    main()