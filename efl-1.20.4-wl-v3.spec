%define        major 	        1
%define        libname          %mklibname %name %major
%define        libnamedev       %mklibname %name -d

%define        themedir         %{_datadir}/elementary/themes
%define        mageiatheme      %{name}-theme-mageia

%define        obsversion       1.18.2
%define        obsrelease       1

Summary:       Enlightenment Foundation Libraries
Name:          efl
Version:       1.20.4
Release:       %mkrel 1
License:       LGPLv2+
Group:         Graphical desktop/Enlightenment
Source:        http://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.xz

#contribution from Roy W. Reese (licensed to GPLv3)
Source1:       E21-Mageia6-GPLv3.edj.bz2

##Patch2:        efl-1.15.2-ldflags.patch
URL:           https://www.enlightenment.org/about-efl

BuildRequires: doxygen
BuildRequires: gettext-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(glesv2)
BuildRequires: giflib-devel
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xprintutil)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(bullet)
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: bzip2
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(sdl2)
BuildRequires:	lib64wayland-egl1-devel lib64wayland-devel 
##BuildRequires:	libwayland-cursor-devel libwayland-server-devel
BuildRequires: wayland-protocols-devel
BuildRequires: wayland-tools
BuildRequires: x11-server-xwayland
BuildRequires: lib64drm-devel 
BuildRequires: lib64input-devel	
BuildRequires: lib64gbm1-devel


Requires(post):      update-alternatives
Requires(postun):    update-alternatives
Requires(posttrans): update-alternatives

Obsoletes: eet        < %{obsversion}-%{obsrelease}
Obsoletes: evas       < %{obsversion}-%{obsrelease}
Obsoletes: ecore      < %{obsversion}-%{obsrelease}
Obsoletes: embryo     < %{obsversion}-%{obsrelease}
Obsoletes: edje       < %{obsversion}-%{obsrelease}
Obsoletes: efreet     < %{obsversion}-%{obsrelease}
Obsoletes: e_dbus     < %{obsversion}-%{obsrelease}
Obsoletes: eeze       < %{obsversion}-%{obsrelease}
Obsoletes: expedite   < %{obsversion}-%{obsrelease}
Obsoletes: ethumb     < %{obsversion}-%{obsrelease}
Obsoletes: edbus      < %{obsversion}-%{obsrelease}
Obsoletes: elementary < %{obsversion}-%{obsrelease}
Obsoletes: elementary-icon-theme   < %{obsversion}-%{obsrelease}
Obsoletes: evas_generic_loaders    < %{obsversion}-%{obsrelease}
Obsoletes: emotion_generic_players < %{obsversion}-%{obsrelease}



%description
The Enlightenment Foundation Libraries (EFL) are a set of graphics
libraries that grew out of the development of Enlightenment. The
libraries are meant to be portable and optimized to be functional even
on mobile devices such as smart phones and tablets. They provide both
a semi-traditional toolkit set in Elementary as well as the object
canvas (Evas) and powerful abstracted objects (Edje) that you can
combine, mix and match, even layer on top of each other with alpha
channels and events in-tact. The library supports 3D transformations
for all objects and more.


%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Obsoletes: %{_lib}eina1    < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}eet1     < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}evas1    < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}ecore1   < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}embryo1  < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}edje1    < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}efreet1  < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}e_dbus1  < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}eeze1    < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}eio1     < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}emotion1 < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}ethumb1  < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}edbus2   < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}elementary1 < %{obsversion}-%{obsrelease}

%description -n %libname
Libraries for %{name}.

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires:  %libname = %{version}-%{release}
Provides:  lib%{name}-devel = %{version}-%{release}
Provides:  %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}eina-devel   < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}eet-devel    < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}evas-devel   < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}ecore-devel  < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}embryo-devel < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}edje-devel   < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}efreet-devel < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}e_dbus-devel < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}eeze-devel   < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}eio-devel    < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}emotion-devel< %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}ethumb-devel < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}edbus-devel  < %{obsversion}-%{obsrelease}
Obsoletes: %{_lib}elementary-devel < %{obsversion}-%{obsrelease}

%description -n %libnamedev
%{name} development headers and libraries.




%package -n %{mageiatheme}
Summary:   Mageia Enlightenment theme
Group:     Graphical desktop/Enlightenment
Requires:  efl >= 0.18.4
Obsoletes: e17-themes-mageia <= 0.4
BuildArch: noarch

%description -n %{mageiatheme}
%{summary}.






%prep
%setup -q
##%autopatch -p1

%build
autoreconf -fi
automake --add-missing

%configure2_5x 	--enable-xinput22 \
		--enable-multisense \
		--enable-systemd \
		--disable-silent-rules \
		--enable-image-loader-webp \
		--enable-harfbuzz \
		--disable-tslib \
		--enable-fb \
		--disable-neon \
		--enable-wayland \
                --enable-wayland-egl \
                --enable-wl-desktop-shell \
                --enable-wl-drm \
		--enable-wl-text-input \
		--enable-xwayland --enable-wl-x11 \
                --enable-elput \
	         --enable-drm \
	         --enable-gl-drm \
	         --enable-libinput \
	         --enable-drm-hw-accel \
	         --enable-egl --with-opengl=es 
		
		
		
%make_build

%install
%make_install

find %buildroot -name '*.la' -delete

%find_lang %name


#supporting change of default theme
%__mv %{buildroot}%{themedir}/default.edj %{buildroot}%{themedir}/E-default.edj
%__install -D -m644 %{SOURCE1} %{buildroot}%{themedir}/E-mageia.edj.bz2
bunzip2 -fv %{buildroot}%{themedir}/E-mageia.edj.bz2



%post
#if the file has been edited by hand before, it is a regular file
#and not a symlink. So we first rename it before calling
#update-alternatives to create the symlink.
if [ -f %{themedir}/default.edj -a ! -h %{themedir}/default.edj ]; then
    %__mv %{themedir}/default.edj %{themedir}/default.rpmold
fi
update-alternatives --install  %{themedir}/default.edj enlightenment-default-theme.edj \
                    %{themedir}/E-default.edj 10

%postun
#uninstall only
if [ $1 -eq 0 ]; then
   update-alternatives --remove enlightenment-default-theme.edj %{themedir}/E-default.edj
fi


%posttrans
#Releases before 1.18.4-3 had default.edj as a file packaged in, so our symlink
#will be removed if one upgrade from those.
if ! [ -h %{themedir}/default.edj ]; then
   update-alternatives --install %{themedir}/default.edj enlightenment-default-theme.edj \
                    %{themedir}/E-default.edj 10
fi


%post -n %{mageiatheme}
if [ -f %{themedir}/default.edj -a ! -h %{themedir}/default.edj ]; then
    %__mv %{themedir}/default.edj %{themedir}/default.rpmold
fi
update-alternatives --install  %{themedir}/default.edj enlightenment-default-theme.edj \
                    %{themedir}/E-mageia.edj 11


%postun -n %{mageiatheme}
if [ $1 -eq 0 ]; then
   update-alternatives --remove enlightenment-default-theme.edj %{themedir}/E-mageia.edj
fi



%files -f %name.lang
%{_bindir}/*
%{_datadir}/dbus-1
%{_datadir}/ecore
%{_datadir}/ecore_imf
%{_datadir}/ecore_x
%{_datadir}/edje
%{_datadir}/eeze
%{_datadir}/efreet
%{_datadir}/elua
%{_datadir}/embryo
%{_datadir}/emotion
%{_datadir}/eo
%{_datadir}/ethumb
%{_datadir}/ethumb_client
%{_datadir}/evas
%{_datadir}/gdb/auto-load/usr/%_lib/*
%{_datadir}/mime/packages/edje.xml
%{_datadir}/eolian
%dir %{_datadir}/elementary
%{_datadir}/elementary/config
%{_datadir}/elementary/edje_externals
%{_datadir}/elementary/images
%{_datadir}/elementary/objects
%{_datadir}/elementary/test*
%dir %{_datadir}/elementary/themes
%{_datadir}/elementary/themes/E-default.edj
%{_datadir}/applications
%{_iconsdir}/Enlightenment-X
%{_iconsdir}/elementary.png
%{_libdir}/ecore*
%{_libdir}/edje
%{_libdir}/eeze
%{_libdir}/efreet
%{_libdir}/emotion
%{_libdir}/ethumb
%{_libdir}/ethumb_client
%{_libdir}/evas
%{_libdir}/elementary
%{_userunitdir}/*.service

%files -n %libname
%doc AUTHORS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %libnamedev
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/cmake/*

%files -n %{mageiatheme}
%{themedir}/E-mageia.edj

%changelog
* Fri Sep 29 2017 onlyhuman <onlyhuman> 120.4-1.mga6
+built with wl support (hopefully) :)
- Upgrade to version 1.20.4

* Sun Jun 04 2017 eatdirt <eatdirt> 1.19.1-2.mga6
+ Revision: 1106693
- Update Mageia theme, fix description

* Wed May 24 2017 eatdirt <eatdirt> 1.19.1-1.mga6
+ Revision: 1104473
- Upgrade to version 1.19.1

* Tue May 02 2017 eatdirt <eatdirt> 1.19.0-1.mga6
+ Revision: 1098618
- Upgrade to version 1.19.0

* Mon Apr 10 2017 eatdirt <eatdirt> 1.18.4-3.mga6
+ Revision: 1096265
- Add a default mageia theme

* Sat Feb 25 2017 wally <wally> 1.18.4-2.mga6
+ Revision: 1087818
- rebuild for new bullet

* Fri Jan 20 2017 eatdirt <eatdirt> 1.18.4-1.mga6
+ Revision: 1082505
- Upgrade to version 1.18.4

* Wed Dec 28 2016 neoclust <neoclust> 1.18.2-3.mga6
+ Revision: 1078430
- Rebuild for new libraw

* Tue Nov 29 2016 eatdirt <eatdirt> 1.18.2-2.mga6
+ Revision: 1070941
- Fix typo in obsoleting elementary-devel

* Mon Nov 28 2016 eatdirt <eatdirt> 1.18.2-1.mga6
+ Revision: 1070569
- Upgrading efl to 1.18.2

* Thu Nov 17 2016 daviddavid <daviddavid> 1.17.0-6.mga6
+ Revision: 1067956
- add missing BR on pkgconfig(udev)
- finally disable neon on all arches

* Thu Oct 27 2016 akien <akien> 1.17.0-5.mga6
+ Revision: 1063774
- Rebuild for bullet 2.85.1

* Wed Jun 08 2016 tv <tv> 1.17.0-4.mga6
+ Revision: 1020781
- adjust BRs for latest systemd

* Sun May 08 2016 daviddavid <daviddavid> 1.17.0-3.mga6
+ Revision: 1010537
- obsoletes also lib(64)edbus2 and lib(64)edbus-devel

* Fri May 06 2016 pterjan <pterjan> 1.17.0-2.mga6
+ Revision: 1009664
- Force disable neon on arches we don't want it

* Sun Apr 17 2016 trem <trem> 1.17.0-1.mga6
+ Revision: 1003299
- efl: bump to version 1.17.0

* Wed Mar 02 2016 umeabot <umeabot> 1.16.1-5.mga6
+ Revision: 983364
- Rebuild for openssl

* Sun Feb 14 2016 umeabot <umeabot> 1.16.1-4.mga6
+ Revision: 959983
- Mageia 6 Mass Rebuild

* Thu Jan 07 2016 luigiwalser <luigiwalser> 1.16.1-3.mga6
+ Revision: 920391
- rebuild for giflib

* Sat Jan 02 2016 luigiwalser <luigiwalser> 1.16.1-2.mga6
+ Revision: 918198
- rebuild for libwebp

* Thu Dec 31 2015 trem <trem> 1.16.1-1.mga6
+ Revision: 917144
- efl: bump to version 1.16.1

* Sat Dec 05 2015 trem <trem> 1.16.0-1.mga6
+ Revision: 908408
- efl: bump version to 1.16.0

* Wed Oct 07 2015 fwang <fwang> 1.15.2-3.mga6
+ Revision: 886694
- set module flag

* Wed Oct 07 2015 fwang <fwang> 1.15.2-2.mga6
+ Revision: 886690
- br gettext
- correct populate ldflags

* Wed Oct 07 2015 fwang <fwang> 1.15.2-1.mga6
+ Revision: 886681
- 1.15.2

* Sat Sep 05 2015 trem <trem> 1.15.1-1.mga6
+ Revision: 873140
- efl: add patch efl-0001-eio-add-a-dependancy-on-efl.patch
- efl: bump version to 1.15.1

* Sun Aug 09 2015 trem <trem> 1.15.0-1.mga6
+ Revision: 862314
- efl: bump version to 1.15.0

* Sat Jul 04 2015 trem <trem> 1.14.2-1.mga6
+ Revision: 850614
- efl: bump version to 1.14.2
- bump version to 1.11.2

  + fwang <fwang>
    - 1.14.1

  + umeabot <umeabot>
    - Second Mageia 5 Mass Rebuild
    - Mageia 5 Mass Rebuild

* Thu Sep 04 2014 trem <trem> 1.11.1-1.mga5
+ Revision: 672131
- bump version to 1.11.1

* Thu Sep 04 2014 colin <colin> 1.10.2-2.mga5
+ Revision: 671892
- Rebuild for new systemd

* Sat Jul 19 2014 trem <trem> 1.10.2-1.mga5
+ Revision: 653965
- bump version to 1.10.2

* Mon Jul 14 2014 trem <trem> 1.10.1-2.mga5
+ Revision: 651834
- increase release to force rebuild
- use _userunitdir intead of %%{_libdir}/systemd/user/
- bump to 1.10.1

* Sat May 17 2014 trem <trem> 1.9.4-1.mga5
+ Revision: 623147
- bump version to 1.9.4

* Fri May 09 2014 trem <trem> 1.9.3-2.mga5
+ Revision: 621510
- add obsolete on edbus

* Sun Apr 20 2014 trem <trem> 1.9.3-1.mga5
+ Revision: 617126
- efl: bump version to 1.9.3

* Sat Apr 05 2014 trem <trem> 1.9.2-1.mga5
+ Revision: 611853
- bump version to 1.9.2

* Thu Mar 13 2014 trem <trem> 1.9.1-1.mga5
+ Revision: 603241
- bump version to 1.9.1

* Sat Mar 08 2014 trem <trem> 1.9.0-1.mga5
+ Revision: 601334
- bump version to 1.9.0

* Tue Feb 25 2014 trem <trem> 1.8.5-2.mga5
+ Revision: 597117
- fix obsoletes (use %%{_lib}, ...)
- remove "rm -fr %%buildroot" in %%install

* Sun Feb 23 2014 trem <trem> 1.8.5-1.mga5
+ Revision: 595978
- fix path for gdb auto-load file (replase lib by %%_lib)
- fix buildrequires (replace devel(libgif) by giflib-devel)
- imported package efl

