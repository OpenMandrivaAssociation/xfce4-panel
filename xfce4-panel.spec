%define url_ver %(echo %{version} | cut -c 1-3)
%define major 4
%define libname	%mklibname xfce4panel %{major}
%define develname %mklibname xfce4panel -d

Summary:	A Xfce panel
Name:		xfce4-panel
Version:	4.10.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	gtk+2-devel
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	libwnck-devel
BuildRequires:	xfconf-devel >= 4.10.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	gtk-doc
BuildRequires:	garcon-devel >= 0.1.11
Requires:	desktop-common-data
#Requires:	mandriva-xfce-config-common
Obsoletes:	xfce-panel

%description
The Xfce 4 Panel supports multiple panels, with many options
for their position, appearance, transparency and behavior.
There are many items available by default to full fit a panel,
like application launchers with detachable menus, a graphical pager,
a tasklist, a clock, a system tray, a show/hide desktop switcher,
and even more. It offers an easy way to add items using a dialog,
and to move items accross different panels.

%package -n %{libname}
Summary:	Panel library for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Obsoletes:	%{mklibname xfce4panel 1}
Obsoletes:	%{mklibname xfce4panel 2}
Obsoletes:	%{mklibname xfce4panel 3}

%description -n %{libname}
Panel library for the Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname xfce4panel 1 -d} < 4.6.3-2

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--enable-gtk-doc \
	--enable-gio-unix \
	--disable-static

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
#rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/*

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README AUTHORS NEWS
%dir %{_libdir}/xfce4/panel
%dir %{_libdir}/xfce4/panel/plugins
%dir %{_datadir}/xfce4/panel
%dir %{_datadir}/xfce4/panel/plugins
%{_sysconfdir}/xdg/xfce4/panel/*.xml
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/migrate
%{_libdir}/xfce4/panel/wrapper
%{_datadir}/gtk-doc/html/libxfce4panel-1.0

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfce4panel-1.0/libxfce4panel/*.h


%changelog
* Tue May 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794656
- update to new version 4.10.0

* Mon Apr 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-2
+ Revision: 791385
- obsolete old library

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-1
+ Revision: 791133
- bump major
- update to new version 4.9.2

* Tue Apr 03 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-1
+ Revision: 789083
- do not require gtk-doc
- update to new version 4.9.1
- spec file clean

* Mon Feb 27 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.6-3
+ Revision: 780954
- fix files listed more tha once
- rebuild

* Fri Jan 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.6-2
+ Revision: 757978
- drop la files
- fix find_lang syntax

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.6-1
+ Revision: 700932
- update to new version 4.8.6

* Mon Jun 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.5-1
+ Revision: 687570
- update to new version 4.8.5

* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.3-2
+ Revision: 660712
- obsolete old library major

* Sat Apr 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.3-1
+ Revision: 652037
- update to new version 4.8.3

* Sun Feb 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-1
+ Revision: 640578
- update to new version 4.8.2

* Wed Feb 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 635381
- update to new version 4.8.1

* Sun Jan 23 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 632432
- update to new version 4.8.0

* Fri Jan 07 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.7-1mdv2011.0
+ Revision: 629571
- update to new version 4.7.7
- fix file list

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.6-1mdv2011.0
+ Revision: 616407
- update to new version 4.7.6

* Sat Dec 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 609367
- update to new version 4.7.5

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 593817
- update to new version 4.7.4
- drop some conditions in spec file for mdv older than 200900

* Fri Sep 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 579302
- update to new version 4.7.3
- tune up buildrequires
- fix file list

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.4-1mdv2011.0
+ Revision: 553870
- update to new version 4.6.4

* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-2mdv2010.1
+ Revision: 512430
- fix obsoletes in devel subpackages

* Wed Dec 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.3-1mdv2010.1
+ Revision: 484149
- update to new version 4.6.3
- drop patch 0, fixed upstream (xfce bz #6110)

* Sun Dec 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-3mdv2010.1
+ Revision: 482718
- reeanble gtk-doc

* Wed Dec 23 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-2mdv2010.1
+ Revision: 481842
- apply patch 0 only for mdv >= 2010.0
- disable gtk-docs for now

  + Christophe Fergeau <cfergeau@mandriva.com>
    - make sure panels don't show window decorations

* Sun Oct 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2010.0
+ Revision: 458148
- update to new version 4.6.2
- adapt to new urls
- drop patch 0 and 1 because they were merged in by upstream

* Thu Jun 25 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-3mdv2010.0
+ Revision: 389207
- Patch1: fix command args for session restart

* Thu Jun 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.0
+ Revision: 385028
- Patch0: open Terminal with exo-open

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368576
- update to new version 4.6.1

* Sun Apr 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-4mdv2009.1
+ Revision: 364183
- Patch1: migrate launcher category icons
- Patch2: don't crash when quit button is pressed
- Patch3: properly set the systray orientation property

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-3mdv2009.1
+ Revision: 360503
- Patch0: fix build with -Wl,--as-needed

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349226
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345704
- New upstream release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333946
- update to new version 4.5.99.1

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329515
- update to new version 4.5.93
- add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-3mdv2009.1
+ Revision: 303523
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Thu Nov 13 2008 Oden Eriksson <oeriksson@mandriva.com> 4.5.91-3mdv2009.1
+ Revision: 302650
- rebuild

* Tue Nov 11 2008 Oden Eriksson <oeriksson@mandriva.com> 4.5.91-2mdv2009.1
+ Revision: 302229
- rebuilt against new libxcb

* Thu Oct 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294486
- Xfce4.6 beta1 is landing on cooker
- patch 1 and 2 were merged upstream
- fix file list
- tune up buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-4mdv2009.0
+ Revision: 208978
- Patch0: fix drag and drop files over panels
- Patch1: fix dialogs on multiscreen

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2009.0
+ Revision: 205611
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Mon Mar 31 2008 Antoine Ginies <aginies@mandriva.com> 4.4.2-3mdv2008.1
+ Revision: 191245
- add mandriva-xfce-config-common to fix bug 39496

* Thu Jan 17 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 154147
- do not package big changelog
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109979
- New release 4.4.2

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - obsolete old release
    - new license policy
    - use upstream tarball name as a real name
    - use upstream name

* Sat Sep 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-9mdv2008.0
+ Revision: 92276
- provide patch 0 which fixes upstream Xfce bug #3496

* Fri Sep 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-8mdv2008.0
+ Revision: 91879
- exclude config files, which are now in mandriva-xfce-config package

* Fri Sep 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-7mdv2008.0
+ Revision: 81884
- drop patch 0, because we rely on mandriva-xfce-config packages
  remove unneeded provides and obsoletes

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-6mdv2008.0
+ Revision: 44272
- fix file list
- don't own configuration files
- new devel library policy
- correct obsoletes/provides
- move Sources 1,2,3,4,5 to the xfce-config package
- update description

* Thu May 31 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-5mdv2008.0
+ Revision: 33090
- Fix errors
- Fix Mandriva Theme

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 32517
- spec file clean
- add %%post and %%postun for main package
  move icon caching macros from lib to main package

* Fri May 25 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 31097
- Remove french desktop
- Bump release
- Add mandriva default theme

* Wed Apr 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 14793
- New release 4.4.1

