Summary:	PolicyKit integration for the GNOME desktop
Name:		polkit-gnome
Version:	0.105
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.freedesktop.org/wiki/Software/PolicyKit
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Source1:	polkit-gnome-authentication-agent-1.desktop.in

BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(gobject-introspection-1.0)
Provides:	polkit-agent
Obsoletes:	%{_lib}polkit-gtk1_0 < 0.105
Obsoletes:	%{_lib}polkit-gtk1-devel < 0.105
Obsoletes:	polkit-gnome-docs < 0.105

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%prep
%setup -q

%build
%configure2_5x \
	--enable-gtk-doc \
	--disable-static

%make

%install
%makeinstall_std
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
sed -i 's,@FULL_LIBEXECDIR@,%{_libdir},' %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop

%find_lang %{name}-1

%files -f %{name}-1.lang
%doc COPYING AUTHORS README
%config(noreplace) %{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
%{_libexecdir}/polkit-gnome-authentication-agent-1

