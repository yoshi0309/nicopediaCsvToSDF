#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def main(options, args):
    import csv
    import json
    import re
    if options.file != None and options.out !=None:
        print('start reading csv %s' % options.file)
        reader = csv.reader(open(options.file, 'rb'),delimiter=',',quotechar='"',escapechar='\\',lineterminator='\n')
        writer = open(options.out, 'w')
        csv.field_size_limit(1000000000)
        writer.write('[')
        for row in reader:
            body = row[1]
            
            # get title
            p = re.compile(r"<[^>]*?>")
            i = body.index('\n')
            title = body[:i]
            title = p.sub("", title)
            
            body = body.replace('\r','')
            body = body.replace('\n','')
            body = body.replace('\\','')
            body = body.replace('&nbsp;',' ')
            
            # remove html tags from body.
            body = p.sub(" ", body)
            
            json_data = {'type':'add','id':row[0],'fields':{'title':title,'body':body}}
            json.dump(json_data,writer,ensure_ascii=False)
            writer.write(',')
        writer.write(']')

if __name__ == '__main__': 
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-f', '--file', dest='file', help='csv file path.')
    parser.add_option('-o', '--out', dest='out', help='output file path.')
    options, args = parser.parse_args(sys.argv[1:])
    sys.exit(main(options, args))
