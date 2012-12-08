Summary:	PolicyKit integration for the GNOME desktop
Name:		polkit-gnome
Version:	0.105
Release:	%mkrel 2
License:	LGPLv2+
URL:		http://www.freedesktop.org/wiki/Software/PolicyKit
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/polkit-gnome/0.105/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.2
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(polkit-agent-1) >= 0.97
BuildRequires:	pkgconfig(polkit-gobject-1) >= 0.97
Buildrequires:	intltool >= 0.35.0
Provides:	polkit-agent

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
make

%install
%makeinstall_std

%find_lang polkit-gnome-1

%files -f polkit-gnome-1.lang
%doc COPYING AUTHORS README
%{_libexecdir}/polkit-gnome-authentication-agent-1


%changelog

* Mon Sep 24 2012 ovitters <ovitters> 0.105-2.mga3
+ Revision: 297186
- get rid of the manually installed autostart file; we do not ship GNOME 2.32 anymore and this is prevents GNOME from starting up

* Fri Oct 28 2011 wally <wally> 0.105-1.mga2
+ Revision: 159248
- new version 0.105

* Mon Oct 17 2011 wally <wally> 0.104-1.mga2
+ Revision: 155969
- drop polkit-gtk
- new version 0.104
- use xz source from gnome
- clean .spec

  + fwang <fwang>
    - new version 0.102
    - splitout gir typelib

* Mon May 02 2011 ahmad <ahmad> 0.101-2.mga1
+ Revision: 94173
- install the autostart .desktop file manually, since upstream doesn't ship it
  any more and decided that it's the job of each DE to start
  polkit-gnome-authentication-agent-1, this doesn't seem to apply to
  gnome-session in GNOME 2.32

* Fri Apr 15 2011 dams <dams> 0.101-1.mga1
+ Revision: 85563
- update to 0.101

* Sat Jan 15 2011 blino <blino> 0.99-1.mga1
+ Revision: 19421
- imported package polkit-gnome


* Mon Sep 20 2010 Götz Waschk <waschk@mandriva.org> 0.99-1mdv2011.0
+ Revision: 579972
- update to new version 0.99

* Fri Aug 13 2010 Götz Waschk <waschk@mandriva.org> 0.97-1mdv2011.0
+ Revision: 569360
- update to new version 0.97

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 0.96-3mdv2011.0
+ Revision: 563865
- rebuild for new gobject-introspection

* Wed Apr 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.96-2mdv2010.1
+ Revision: 540133
- Ensure agent is started in all environments but KDE (instead of only GNOME)

* Mon Jan 18 2010 Frederic Crozat <fcrozat@mandriva.com> 0.96-1mdv2010.1
+ Revision: 493098
- Release 0.96

* Mon Nov 30 2009 Götz Waschk <waschk@mandriva.org> 0.95-1mdv2010.1
+ Revision: 471720
- new version
- bump polkit dep
- add introspection support
- disable parallel make

* Tue Aug 18 2009 Frederic Crozat <fcrozat@mandriva.com> 0.94-2mdv2010.0
+ Revision: 417612
- Provides polkit-agent virtual package

* Thu Aug 13 2009 Frederic Crozat <fcrozat@mandriva.com> 0.94-1mdv2010.0
+ Revision: 415994
- Release 0.94
- create lib/devel/doc subpackages

* Fri Jul 24 2009 Götz Waschk <waschk@mandriva.org> 0.93-1mdv2010.0
+ Revision: 399380
- new version
- update file list
- bump polkit dep

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 0.92-1mdv2010.0
+ Revision: 395928
- import polkit-gnome


* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 0.92-1mdv2010.0
- adapt for Mandriva

* Tue Jun  9 2009 Matthias Clasen <mclasen@redhat.com> - 0.9.2-3
- Fix BuildRequires

* Tue Jun 09 2009 David Zeuthen <davidz@redhat.com> - 0.92-2
- Change license to LGPLv2+
- Remove Requires: gnome-session

* Mon Jun 08 2009 David Zeuthen <davidz@redhat.com> - 0.92-1
- Update to 0.92 release

* Wed May 27 2009 David Zeuthen <davidz@redhat.com> - 0.92-0.git20090527
- Update to 0.92 snapshot

* Mon Feb  9 2009 David Zeuthen <davidz@redhat.com> - 0.91-1
- Initial spec file.
