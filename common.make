copr-build: $(PROJECT).spec
	cp release copr-build
	copr-cli build sway-extras-git $(PROJECT).spec

$(PROJECT).spec: commithash
	echo "%define githash $$(cat commithash)" > $(PROJECT).spec
	echo "%define releasenum $$(cat release)" >> $(PROJECT).spec
	cat $(PROJECT).tmpl.spec >> $(PROJECT).spec

commithash:
	bash ../update_commithash.sh $(REPO_URL) HEAD

release:
	rel=`cat release`; echo "$$rel+1" | bc > release

.PHONY: commithash release
