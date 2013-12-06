Summary:	PolicyKit integration for the GNOME desktop
Name:		polkit-gnome
Version:	0.105
Release:	8
License:	LGPLv2+
URL:		http://www.freedesktop.org/wiki/Software/PolicyKit
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/polkit-gnome/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.2
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(polkit-agent-1) >= 0.97
BuildRequires:	pkgconfig(polkit-gobject-1) >= 0.97
Provides:		polkit-agent

Obsoletes:	%{_lib}polkit-gtk1_0 < 0.104
Obsoletes:	%{_lib}polkit-gtk1-devel < 0.104
Obsoletes:	%{_lib}polkitgtk-gir1.0 < 0.104
Obsoletes:	polkit-gnome-docs < 0.104

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%find_lang polkit-gnome-1

%files -f polkit-gnome-1.lang
%doc AUTHORS README
%{_libexecdir}/polkit-gnome-authentication-agent-1

