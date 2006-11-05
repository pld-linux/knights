Summary:	A KDE based chess environment
Summary(pl):	¦rodowisko do gry w szachy dla KDE
Name:		knights
Version:	0.6
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/knights/%{name}-%{version}.tar.gz
# Source0-md5:	b04574568b9bc3982b934328ee63fb74
Source1:	http://dl.sourceforge.net/knights/knights-themepack-0.5.9.tar.gz
# Source1-md5:	ece32b73d43e16b997423c219dcda21d
Patch0:		%{name}-desktop.patch
URL:		http://www.knights-chess.com/
BuildRequires:	arts-devel
BuildRequires:	automake
BuildRequires:	audiofile-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt-devel >= 3.0.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knights aims to be the ultimate chess resource on your computer.
Written for the K Desktop Environment, it's designed to be both
friendly to new chess players and functional for Grand Masters. Some
of Knights' key features include: single, multi, and Internet play;
customizable board and pieces; audio cues; move previews; and much
much more...

%description -l pl
Knights d±¿y do tego, by byæ najlepszym programem szachowym na twoim
komputerze. Napisany zosta³ dla KDE, jest zaprojektowany w sposób
przyjazny dla nowych graczy, jak te¿ funkcjonalny dla Wielkich
Mistrzów. Cechy Knights to: mo¿liwo¶æ gry jednego, i wielu graczy, jak
te¿ gry przez Internet; mo¿liwo¶æ wybory stylu szachownicy i figur;
podpowiedzi d¼wiêkowe; podgl±d ruchów i wiele, wiele innych...

%package themes
Summary:	Knights themepack
Summary(pl):	Zestaw motywów do knights
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description themes
Additional themes for the Knights chess enviroment.

%description themes -l pl
Dodatkowe motywy do ¶rodowiska gry w szachy knights.

%prep
%setup -q
%patch0 -p1

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
cp -f /usr/share/automake/config.sub admin/config.sub
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes
%{__tar} xfz %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes
mv $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes/{knights-themepack/*.tar.gz,}
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/knights/themes/knights-themepack
mv $RPM_BUILD_ROOT%{_desktopdir}/{Games/Board/,}knights.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}*
%dir %{_datadir}/apps/knights
%{_datadir}/apps/knights/[!t]*
%{_desktopdir}/knights.desktop
%{_datadir}/mimelnk/application/pgn.desktop
%dir %{_datadir}/apps/knights/themes
%{_datadir}/apps/knights/themes/KBDefault.tar.gz
%{_datadir}/apps/knights/themes/KCDefault.tar.gz
%{_datadir}/apps/knights/themes/KSDefault.tar.gz
%{_iconsdir}/*/*/*/*.png

%files themes
%defattr(644,root,root,755)
%{_datadir}/apps/%{name}/themes/*
%exclude %{_datadir}/apps/knights/themes/KBDefault.tar.gz
%exclude %{_datadir}/apps/knights/themes/KCDefault.tar.gz
%exclude %{_datadir}/apps/knights/themes/KSDefault.tar.gz
