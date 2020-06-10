
copr-build: waybar.spec
	cp release copr-build
	copr-cli build sway-extras-git waybar.spec

waybar.spec: commithash
	echo "%define githash $$(cat commithash)" > waybar.spec
	echo "%define releasenum $$(cat release)" >> waybar.spec
	cat waybar.tmpl.spec >> waybar.spec

commithash:
	bash ../update_commithash.sh https://github.com/Alexays/waybar.git

release:
	rel=`cat release`; echo "$$rel+1" | bc > release

.PHONY: commithash release
