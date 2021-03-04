
srpm: install-deps
	@echo "Preparing SRPM in $(PWD) for $(spec) to $(outdir)"
	spectool -g "$(spec)"
	rpkg srpm --outdir "$(outdir)" --spec "$(spec)"

install-deps:
	dnf -y install rpkg rpmdevtools

.PHONY: srpm
