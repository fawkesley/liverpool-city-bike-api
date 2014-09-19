#!/usr/bin/env python

from __future__ import unicode_literals

import gzip
import logging
import os
import sys

from six import BytesIO

import boto

__all__ = ['upload_locations_json']

AWS_KEY_NAME = 'v1/locations.json'


def main():
    logging.basicConfig(level=logging.DEBUG)
    with open(sys.argv[1], 'r') as f:
        json_string = f.read()
        upload_locations_json(json_string)


def upload_locations_json(json_string):
    gzipped_json = gzip_compress(json_string)
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']

    conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(AWS_BUCKET_NAME)
    cors = boto.s3.cors.CORSConfiguration()
    cors.add_rule('GET', '*', allowed_header="*")
    assert bucket.set_cors(cors), 'Failed to set CORS headers'

    k = bucket.new_key(AWS_KEY_NAME)

    k.content_type = 'application/json'

    k.set_contents_from_string(
        gzipped_json,
        headers={'Content-Encoding': 'gzip'},
        replace=True,
        policy='public-read')


def gzip_compress(string):
    out = BytesIO()
    with gzip.GzipFile(fileobj=out, mode='w') as f:
        f.write(string)
    return out.getvalue()


if __name__ == '__main__':
    main()
