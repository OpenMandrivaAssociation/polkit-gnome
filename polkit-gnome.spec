%define libmajor 0
%define api_version 1
%define libname %mklibname polkit-gtk %api_version %{libmajor}
%define libname_devel %mklibname -d polkit-gtk %api_version
%define polkit 0.95

Summary: PolicyKit integration for the GNOME desktop
Name: polkit-gnome
Version: 0.95
Release: %mkrel 1
License: LGPLv2+
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Group: System/Libraries
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel
BuildRequires: polkit-1-devel >= %polkit
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
Provides: polkit-agent

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%package -n %{libname}
Summary: Development files for polkit-gnome
Group: System/Libraries

%description -n %{libname}
Development files for polkit-gnome.

%package -n %{libname_devel}
Summary: Development files for polkit-gnome
Group: Development/C
Requires: %name = %{version}
Requires: %libname = %{version}
Suggests: %name-docs = %{version}
Provides: %name-devel = %{version}-%{release}
Provides: libpolkit-gtk-1-devel = %{version}-%{release}
Provides: libpolkit-gtk-devel = %{version}-%{release}

%description -n %{libname_devel}
Development files for polkit-gnome.

%package docs
Summary: Development documentation for polkit-gnome
Group: Development/C

%description docs
Development documentation for polkit-gnome.

%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc --disable-static
#gw parallel build broken in 0.95
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f polkit-gnome-1.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%config(noreplace) %_sysconfdir/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
%{_libexecdir}/polkit-gnome-authentication-agent-1

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so.%{libmajor}*
%_libdir/girepository-1.0/PolkitGtk-1.0.typelib

%files -n %{libname_devel}
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%_datadir/gir-1.0/PolkitGtk-1.0.gir

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/*

