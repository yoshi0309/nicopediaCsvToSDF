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
            # json_data = {'id':row[0],'body':row[1],'mdate':row[2]}
            body = row[1]
            body = body.replace('\r','')
            body = body.replace('\n','')
            body = body.replace('\\','')
            body = body.replace('&nbsp;',' ')
            
            # remove html tags from body.
            p = re.compile(r"<[^>]*?>")
            body = p.sub(" ", body)
            
            json_data = {'type':'add','id':row[0],'fields':{'body':body,'mdate':row[2]}}
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
