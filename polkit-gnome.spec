Summary: PolicyKit integration for the GNOME desktop
Name: polkit-gnome
Version: 0.92
Release: %mkrel 1
License: LGPLv2+
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Group: System/Libraries
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel
BuildRequires: polkit-1-devel >= 0.92
BuildRequires: intltool

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f polkit-gnome-1.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_datadir}/gnome/autostart/*
%{_libexecdir}/polkit-gnome-authentication-agent-1

