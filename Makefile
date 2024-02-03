BASEDIR=$(CURDIR)
DOCDIR=$(BASEDIR)/docs
DISTDIR=$(BASEDIR)/dist


check:
	pre-commit run --show-diff-on-failure --color=always --all-files

update: pip-tools
	poetry up
	pre-commit autoupdate
