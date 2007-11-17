%define major 1
%define libname	%mklibname xfce4panel %{major}
%define develname %mklibname xfce4panel -d

Summary:	Panel for Xfce
Name:		xfce4-panel
Version:	4.4.1
Release:	%mkrel 10
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-4.4.1-fix-segfault-with-2nd-panel.patch
Requires:	desktop-common-data
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	libxml2-devel >= 2.4.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%description -n %{libname}
Panel library for the Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	gtk-doc
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname xfce4panel 1 -d

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q
%patch0 -p1 -b .panel

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded devel files
rm -f %{buildroot}%{_libdir}/xfce4/panel-plugins/*.a
cp %{buildroot}%{_libdir}/pkgconfig/libxfce4panel-1.0.pc %{buildroot}%{_libdir}/pkgconfig/xfce4-panel-1.0.pc

%find_lang %{name}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%doc %{_datadir}/xfce4/doc/C/
%dir %{_sysconfdir}/X11/xdg/xfce4/panel
%exclude %{_sysconfdir}/X11/xdg/xfce4/panel/*
%{_bindir}/*
%{_libdir}/xfce4/panel-plugins/*.so
%{_libdir}/xfce4/mcs-plugins/*.so
%{_datadir}/applications/xfce4-panel-manager.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/panel-plugins/*
%dir %{_datadir}/gtk-doc/html/libxfce4panel
%{_datadir}/gtk-doc/html/libxfce4panel/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc HACKING README.Plugins
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/xfce4/panel-plugins/*.la
%{_libdir}/xfce4/mcs-plugins/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfce4panel/*
