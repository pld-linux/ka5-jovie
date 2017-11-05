%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		jovie
Summary:	Jovie
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c8e0c135855eeffc368fb5b91702ab3b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	speech-dispatcher-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jovie -- KDE Text-to-Speech -- is a subsystem within the KDE desktop
for conversion of text to audible speech. Jovie is currently under
development and aims to become the standard subsystem for all KDE
applications to provide speech output.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jovie
%attr(755,root,root) %{_libdir}/kde4/jovie_stringreplacerplugin.so
%attr(755,root,root) %{_libdir}/kde4/jovie_talkerchooserplugin.so
%attr(755,root,root) %{_libdir}/kde4/jovie_xmltransformerplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kttsd.so
%attr(755,root,root) %{_libdir}/libkttsd.so
%attr(755,root,root) %ghost %{_libdir}/libkttsd.so.4
%attr(755,root,root) %{_libdir}/libkttsd.so.*.*.*
%{_desktopdir}/kde4/org.kde.jovie.desktop
%{_datadir}/apps/jovie
%{_iconsdir}/hicolor/16x16/actions/female.png
%{_iconsdir}/hicolor/16x16/actions/male.png
%{_iconsdir}/hicolor/16x16/actions/nospeak.png
%{_iconsdir}/hicolor/16x16/actions/speak.png
%{_iconsdir}/hicolor/22x22/actions/nospeak.png
%{_iconsdir}/hicolor/22x22/actions/speak.png
%{_iconsdir}/hicolor/32x32/actions/nospeak.png
%{_iconsdir}/hicolor/32x32/actions/speak.png
%{_iconsdir}/hicolor/48x48/actions/nospeak.png
%{_iconsdir}/hicolor/48x48/actions/speak.png
%{_datadir}/kde4/services/jovie.desktop
%{_datadir}/kde4/services/jovie_stringreplacerplugin.desktop
%{_datadir}/kde4/services/jovie_talkerchooserplugin.desktop
%{_datadir}/kde4/services/jovie_xmltransformerplugin.desktop
%{_datadir}/kde4/services/kcmkttsd.desktop
%{_datadir}/kde4/services/kttsd.desktop
%{_datadir}/kde4/servicetypes/jovie_filterplugin.desktop
%{_datadir}/metainfo/org.kde.jovie.appdata.xml
