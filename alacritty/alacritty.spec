%define githash 3e867a056018c507d79396cb5c5b4b8309c609c2
%define releasenum 45

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:          alacritty
Version:       0.8.0
Release:       1.%{releasenum}.git.%{shorthash}%{?dist}
Summary:       A cross-platform, GPU enhanced terminal emulator
License:       ASL 2.0
URL:           https://github.com/alacritty/alacritty
VCS:           https://github.com/alacritty/alacritty.git
Source:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: rust >= 1.43.0
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libxcb-devel
BuildRequires: desktop-file-utils
BuildRequires: ncurses

%description
Alacritty is a terminal emulator with a strong focus on simplicity and
performance. With such a strong focus on performance, included features are
carefully considered and you can always expect Alacritty to be blazingly fast.
By making sane choices for defaults, Alacritty requires no additional setup.
However, it does allow configuration of many aspects of the terminal.

%prep
%setup -q -n alacritty-%{githash}

%build
cargo build --release

%install
install -p -D -m755 target/release/alacritty         %{buildroot}%{_bindir}/alacritty
install -p -D -m644 extra/linux/Alacritty.desktop    %{buildroot}%{_datadir}/applications/Alacritty.desktop
install -p -D -m644 extra/logo/alacritty-term.svg    %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
install -p -D -m644 alacritty.yml                    %{buildroot}%{_datadir}/alacritty/alacritty.yml
tic     -xe alacritty-direct \
                    extra/alacritty.info       -o    %{buildroot}%{_datadir}/terminfo
install -p -D -m644 extra/completions/alacritty.bash %{buildroot}%{_datadir}/bash-completion/completions/alacritty
install -p -D -m644 extra/completions/_alacritty     %{buildroot}%{_datadir}/zsh/site-functions/_alacritty
install -p -D -m644 extra/completions/alacritty.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/alacritty.fish
install -p -D -m644 extra/alacritty.man              %{buildroot}%{_mandir}/man1/alacritty.1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Alacritty.desktop

%files
%{_bindir}/alacritty
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_datadir}/alacritty/alacritty.yml
%{_datadir}/terminfo/a/alacritty-direct
%{_datadir}/bash-completion/completions/alacritty
%{_datadir}/zsh/site-functions/_alacritty
%{_datadir}/fish/vendor_completions.d/alacritty.fish
%{_mandir}/man1/alacritty.1*

