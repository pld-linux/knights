Name:		knights
Summary:	A KDE based chess enviroment.
Summary(pl):	¦rodowisko gry w szachy dla KDE.
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sourceforge/knights/%{name}-%{version}.tar.gz
# Source0-md5:  b04574568b9bc3982b934328ee63fb74
Source1:	http://dl.sourceforge.net/sourceforge/knights/knights-themepack-0.5.9.tar.gz
# Source1-md5:  ece32b73d43e16b997423c219dcda21d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Url:		http://www.knights-chess.com
Requires:	libpng
Requires:	audiofile
BuildRequires:	libpng-devel
BuildRequires:	kdelibs-devel
BuildRequires:	arts-devel
BuildRequires:	libjpeg-devel
BuildRequires:	audiofile-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	qt-devel >= 3.0.2

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Knights aims to be the ultimate chess resource on your computer.
Written for the K Desktop Environment, it's designed to be both
friendly to new chess players and functional for Grand Masters. Some
of Knights' key features include: single, multi, and internet play;
customizable board and pieces; audio cues; move previews; and much
much more...

%package themes
Summary:	Knights themepack.
Summary(pl):	Zestaw tematów do knights.
Group:		Themes
Requires:	%{name}

%description themes 
Additional themes for the Knights chess enviroment.

%description themes -l pl
Dodakowe tematy do ¶rodowiska gry w szachy knights.

%prep
%setup -q

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install 

install -d $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes/
%{__tar} xfz %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes/
mv $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes/{knights-themepack/*.tar.gz,}
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes/knights-themepack/
mv $RPM_BUILD_ROOT%{_desktopdir}/{Games/Board/,}knights.desktop
echo "Categories=Qt;KDE;Game;BoardGame" >> $RPM_BUILD_ROOT%{_desktopdir}/knights.desktop

%find_lang knights --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f knights.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README INSTALL
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/apps/%{name}/[!t]*
%{_desktopdir}/knights.desktop
%{_datadir}/mimelnk/application/pgn.desktop  
%dir %{_datadir}/apps/knights/themes
%{_datadir}/apps/knights/themes/KBDefault.tar.gz  
%{_datadir}/apps/knights/themes/KCDefault.tar.gz
%{_datadir}/apps/knights/themes/KSDefault.tar.gz
%{_pixmapsdir}/*

%files themes
%defattr(644,root,root,755)
%{_datadir}/apps/%{name}/themes/*
%exclude %{_datadir}/apps/knights/themes/KBDefault.tar.gz
%exclude %{_datadir}/apps/knights/themes/KCDefault.tar.gz
%exclude %{_datadir}/apps/knights/themes/KSDefault.tar.gz
