PKGS=alacritty kanshi wlroots sway waybar wdisplays wofi
JOBS?=32

all: 
	@$(MAKE) -j$(JOBS) pkgs

update:
	$(MAKE) -j$(JOBS) pkgs
	git commit -am 'version bump'
	git push

.PHONY: all update pkgs $(PKGS)

pkgs: $(PKGS)

$(PKGS):
	$(MAKE) -C $@

sway: wlroots
	$(MAKE) -C $@
