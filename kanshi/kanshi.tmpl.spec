%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:           kanshi
Version:        1.1.1
Release:        0.%{releasenum}.git.%{shorthash}%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors
# MIT for main package, Boost for bundled clara.hpp
License:        MIT and Boost
URL:            https://github.com/emersion/kanshi/
Source0:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47.0
BuildRequires:  scdoc

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)


%description
%{summary}.

%prep
%autosetup -n kanshi-%{githash}

%build
%meson
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*

%changelog
* Sat Jun 06 2020 - contact@f0rki.at
- Initial Import from git master

