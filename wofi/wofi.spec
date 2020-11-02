%define githash 19333fd3b265
%define releasenum 8

Name:		wofi
Version:	1.1.2
# Release:	1%{?dist}
Release:    0.%{releasenum}.hg.%{githash}%{?dist}
Summary:	A window switcher, application launcher and dmenu replacement for wayland

License:	GPLv3
URL:		https://hg.sr.ht/~scoopta/wofi

Source: %{url}/archive/%{githash}.tar.gz

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(wayland-client)

%description
Wofi is like "rofi" a window switcher, application launcher and dmenu
replacement but for wlroots-based wayland compositors.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -n %{name}-%{githash}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/wofi.1*
%{_mandir}/man5/wofi.5*
%{_mandir}/man7/wofi-keys.7*
%{_mandir}/man7/wofi.7*

%files devel
%{_includedir}/wofi-1/*.h
%{_libdir}/pkgconfig/wofi.pc
%{_mandir}/man3/wofi-api.3*
%{_mandir}/man3/wofi-config.3*
%{_mandir}/man3/wofi-map.3*
%{_mandir}/man3/wofi-utils.3*
%{_mandir}/man3/wofi.3*
%{_mandir}/man3/wofi-widget-builder.3*

%changelog
* Mon Mar  9 2020 Christian Kellner <ckellner@redhat.com> - 1.1.1-1
- New upstream release 1.1.1, includes header and pkg config file

* Wed Mar  4 2020 Christian Kellner <ckellner@redhat.com> - 1.1-1
- New upstream release 1.1, which includes man pages

* Mon Jan 27 2020 Christian Kellner <ckellner@redhat.com> - 1.0-1
- Initial package of v1.0



