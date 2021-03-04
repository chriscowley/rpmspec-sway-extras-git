srpm:
	@echo "Preparing SRPM in $(PWD) for $(spec) to $(outdir)"
	spectool -g "$(spec)"
	rpkg srpm --outdir "$(outdir)" --spec "$(spec)"

.PHONY: srpm
