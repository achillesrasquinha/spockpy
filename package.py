# Inspired by npm's package.json file
name              = 'spockpy'
version           = '0.1.0'
release           = '0.1.0'
description       = 'A Python library for hand gestures as an input interface.'
long_description  = ['README.md']
keywords          = ['hand', 'gesture', 'input', '']
authors           = [
    { 'name': 'Achilles Rasquinha', 'email': 'achillesrasquinha@gmail.com' },
    { 'name': 'Ameya Shenoy', 'email': 'shenoy.ameya@gmail.com' }
]
maintainers       = [
    { 'name': 'Achilles Rasquinha', 'email': 'achillesrasquinha@gmail.com' },
    { 'name': 'Ameya Shenoy', 'email': 'shenoy.ameya@gmail.com' }
]
license           = 'Apache 2.0'
modules           = [
    'spockpy',
    'spockpy.config',
    'spockpy.app'
]
test_modules      = [
	'spockpy.test'
]
homepage          = 'https://achillesrasquinha.github.io/spockpy'
github_username   = 'achillesrasquinha'
github_repository = 'spockpy'
github_url        = '{baseurl}/{username}/{repository}'.format(
    baseurl    = 'https://github.com',
    username   = github_username,
    repository = github_repository
)