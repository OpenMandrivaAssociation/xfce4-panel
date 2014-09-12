%define url_ver %(echo %{version} | cut -c 1-3)
%define major 4
%define api 1.0
%define libname	%mklibname xfce4panel- %{api} %{major}
%define develname %mklibname xfce4panel -d

Summary:	A Xfce panel
Name:		xfce4-panel
Version:	4.11.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(exo-1) >= 0.7.2
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(libxfconf-0) >= 4.10.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(garcon-1) >= 0.2.1
Requires:	desktop-common-data
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
Obsoletes:	%{mklibname xfce4panel 4} < 4.10.1

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
PLATFORM_LDFLAGS="-lm"

%configure2_5x \
	--enable-gtk-doc \
	--enable-gio-unix \
	--disable-static

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/*

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS
%dir %{_libdir}/xfce4/panel
%dir %{_libdir}/xfce4/panel/plugins
%dir %{_datadir}/xfce4/panel
%dir %{_datadir}/xfce4/panel/plugins
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/migrate
%{_libdir}/xfce4/panel/wrapper-%{api}
%{_datadir}/gtk-doc/html/libxfce4panel-%{api}

%files -n %{libname}
%{_libdir}/lib*%{api}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfce4panel-%{api}/libxfce4panel/*.h
