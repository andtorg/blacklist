#!/usr/bin/python

import shutil
import os, errno
import sys

SITES_TO_IGNORE = {
	'facebook': {'search_string': 'facebook', 'site_address':'www.facebook.com'}
	,'twitter':  {'search_string': 'twitter', 'site_address':'twitter.com'}
	,'g+':  {'search_string': 'plus', 'site_address':'plus.google.com'}
	,'gmail':  {'search_string': 'mail.google', 'site_address':'mail.google.com'}
	,'flickr':  {'search_string': 'flickr', 'site_address':'www.flickr.com'}
	,'flickr_2':  {'search_string': 'flickr', 'site_address':'flickr.com'}
	,'repubblica':  {'search_string': 'repubblica', 'site_address':'repubblica.it'}
	,'repubblica_2':  {'search_string': 'repubblica', 'site_address':'www.repubblica.it'}
}

ACCEPTED_ARGUMENTS = {
	'act': 'activate the blacklist filter',
	'deact': 'deactivate the blacklist filter'
}

# to be changed
host_file = '/etc/hosts'
backup_host_file = '/etc/hosts.bak'

file_lines = []

command = sys.argv[1]

def edit_file_host(command, source_file=host_file, backup_file=backup_host_file):
	_check_valid_argument(command)
	_remove_file_if_exists(backup_file)
	_make_backup_copy(source_file, backup_file)
	if command == "act":
		_enable_host_filter(source_file)
		print "blacklist activated"
	else:
		_disable_host_filter(source_file)
		print "blacklist deactivated"

def _check_valid_argument(arg):
	if arg not in ACCEPTED_ARGUMENTS:
		_allowed_args = ACCEPTED_ARGUMENTS.keys()
		raise IndexError ('{} is not a valid argument. Allowed values are: {}'.format(arg, _allowed_args))

def _enable_host_filter(file_path):
	global file_lines
	file_lines = _get_file_lines(file_path)  

	f = open(file_path, 'w')
	f.writelines(file_lines)

	noisy_sites_lines = _append_noisy_sites(SITES_TO_IGNORE)
	f.writelines(noisy_sites_lines)
	f.close()

def _append_noisy_sites(sites_dict):
	ignoring_site_list = []
	ignoring_site_string = '127.0.0.1' 

	for k in sites_dict:
		ignoring_site_list.append('{} {}\n'.format(ignoring_site_string, sites_dict[k]['site_address']))
	return ignoring_site_list

def _disable_host_filter(file_path):
	global file_lines
	file_lines = _get_file_lines(file_path)
	cleaned_file_lines = _remove_noisy_sites(file_lines, SITES_TO_IGNORE)

	f = open(file_path, 'w')
	f.writelines(cleaned_file_lines)
	f.close()	

def _remove_noisy_sites(lines, sites_dict):
	searchable_sites = [x['search_string'] for x in SITES_TO_IGNORE.values()]
	allowed_file_lines = [x for x in lines if not any(y in x for y in searchable_sites)]

	return allowed_file_lines

def _get_file_lines(file_path):
	f = open(file_path, 'r+')
	lines = f.readlines()
	f.close()
	return lines	
	
def _remove_file_if_exists(file):
	try:
		os.remove(file)
	except OSError, e:
		if e.errno != errno.ENOENT:
			raise

def _make_backup_copy(source_file, backup_file):
	shutil.copy2(source_file,backup_file)

if __name__ == '__main__':
	edit_file_host(command)
