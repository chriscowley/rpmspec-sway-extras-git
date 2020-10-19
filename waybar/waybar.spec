%define githash f151d435a872777376796b48d6997b78afede474
%define releasenum 19

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:           waybar
Version:        0.9.3
Release:        0.%{releasenum}.git.%{shorthash}%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors
# MIT for main package, Boost for bundled clara.hpp
License:        MIT and Boost
URL:            https://github.com/Alexays/Waybar
Source0:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz
Conflicts:      waybar

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47.0
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(date)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt) >= 5.3.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.3.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)

Recommends:     fontawesome-fonts

%description
%{summary}.

%prep
%autosetup -n Waybar-%{githash}

%build
MESON_OPTIONS=(
    -Dsndio=disabled
)
%{meson} "${MESON_OPTIONS[@]}"
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
%{_mandir}/man5/%{name}*
# FIXME: exclude user service until a proper way to start it has been decided
# see rhbz#1798811 for more context
%exclude %{_userunitdir}/%{name}.service

%changelog
* Sat Apr 11 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Mon Feb 10 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.1-1
- Update to 0.9.1
- Remove upstreamed patch
- Add BuildRequires: pkgconfig(date)

* Sat Feb 08 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.0-1
- Initial import (#1798811)
