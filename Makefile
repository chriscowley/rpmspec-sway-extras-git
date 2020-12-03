PKGS=alacritty kanshi wlroots sway waybar wdisplays wofi
JOBS?=32

all: 
	@$(MAKE) -j$(JOBS) pkgs

.PHONY: all pkgs $(PKGS)

pkgs: $(PKGS)

$(PKGS):
	$(MAKE) -C $@

sway: wlroots
	$(MAKE) -C $@
