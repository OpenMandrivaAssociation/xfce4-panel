%define url_ver %(echo %{version} | cut -c 1-3)
%define major 3
%define libname	%mklibname xfce4panel %{major}
%define develname %mklibname xfce4panel -d

Summary:	A Xfce panel
Name:		xfce4-panel
Version:	4.8.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel >= 4.7.2
BuildRequires:	gtk+2-devel
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	libwnck-devel
BuildRequires:	xfconf-devel >= 4.7.2
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	gtk-doc
BuildRequires:	garcon-devel >= 0.1.4
Requires:	desktop-common-data
Requires:	mandriva-xfce-config-common
Obsoletes:	xfce-panel
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
Obsoletes:	%{mklibname xfce4panel 1 -d} < 4.6.3-2

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--enable-gtk-doc \
	--enable-gio-unix

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS NEWS
%dir %{_sysconfdir}/xdg/xfce4/panel
%dir %{_libdir}/xfce4/panel
%dir %{_libdir}/xfce4/panel/plugins
%dir %{_datadir}/xfce4/panel
%dir %{_datadir}/xfce4/panel/plugins
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/migrate
%{_libdir}/xfce4/panel/wrapper
%{_datadir}/gtk-doc/html/libxfce4panel-1.0

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfce4panel-1.0/libxfce4panel/*.h
