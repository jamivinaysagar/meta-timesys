#!/usr/bin/env python

import json
import pprint
import os
import sys

# need to add our lib folder to import path
bindir = os.path.dirname(os.path.abspath(__file__))
topdir = os.path.dirname(bindir)
sys.path.insert(1, os.path.join(topdir, 'lib'))

import llapi


def print_usage():
    apidoc = '%s/docs/wiki/engineering/LinuxLink_Key_File' % llapi.LINUXLINK_SERVER
    print('This script sends a json manifest file for an image to LinuxLink '
          'to check the CVE status of the recipes.\n\n'
          'It requires a LinuxLink API keyfile, and an active LinuxLink '
          'subscription. See this document for keyfile information:\n'
          '%s\n\n'
          'Usage: %s <manifestfile>'
          % (apidoc, sys.argv[0]))


def read_manifest(manifest_file):
    with open(manifest_file, 'rb') as f:
        manifest = ''.join(line.rstrip() for line in f)
    return manifest


def print_cves(result):
    for cve in result:
        print('\nPackage: %s' % cve['package'])
        print('CVE ID:  %s' % cve['cve_id'])
        print('CVSS:    %s' % cve['cvss'])
        print('Status:  %s' % cve['status'])
        print('Summary: %s' % cve['summary'])


if __name__ == '__main__':
    resource = '/api/cves/reports/yocto/'
    home_dir = os.path.expanduser('~')
    key_file = os.getenv('KEY_FILE', '%s/timesys/linuxlink_key' % home_dir)

    try:
        manifest_file = sys.argv[1]
    except IndexError:
        print_usage()
        sys.exit(1)

    try:
        email, key = llapi.read_keyfile(key_file)
    except Exception as e:
        print('Error: %s\n' % e)
        print_usage()
        sys.exit(1)

    manifest = read_manifest(manifest_file)
    print('Requesting image analysis from LinuxLink ...')
    result = llapi.api_post(email, key, resource, {'manifest': manifest})
    result = result.get('cves', [])
    print_cves(result)