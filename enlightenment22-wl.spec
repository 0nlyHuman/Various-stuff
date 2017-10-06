%define efl_version 1.20.4

Summary:        Enlightenment DR 22 window manager
Name:           enlightenment
Version:        0.22.0_beta
Release:        %mkrel 1
License:        BSD
Group:          Graphical desktop/Enlightenment
URL:            http://www.enlightenment.org/
Source:         http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.gz
Patch0:         e17_sysactions.conf.patch
Patch1:         fix-enlightenment_filemanager.desktop.patch
##Patch2:         fix-emixer.desktop.patch

BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(efl) >= %{efl_version}
BuildRequires:  pkgconfig(ecore) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-con) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-evas) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-file) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-input) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-input-evas) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-ipc) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-x) >= %{efl_version}
BuildRequires:  pkgconfig(edje) >= %{efl_version}
BuildRequires:  pkgconfig(eet) >= %{efl_version}
BuildRequires:  pkgconfig(eeze) >= %{efl_version}
BuildRequires:  pkgconfig(efreet) >= %{efl_version}
BuildRequires:  pkgconfig(efreet-mime) >= %{efl_version}
BuildRequires:  pkgconfig(efreet-trash) >= %{efl_version}
BuildRequires:  pkgconfig(eina) >= %{efl_version}
BuildRequires:  pkgconfig(eio) >= %{efl_version}
BuildRequires:  pkgconfig(evas) >= %{efl_version}
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  gettext-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  multiarch-utils
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  doxygen
BuildRequires:  efl

Requires:       terminology
Requires:       acpitool
Requires:       desktop-common-data

# mixer module have been merged into main from e_modules
Conflicts:      e_modules < 1:0.0.1-1.r81625.3
# default theme has been renamed and replaced by theme from e17-themes-mageia
Conflicts:      e17-themes-mageia < 0:0.4-4

# e was renamed to enlightenment
Obsoletes:      e < 0.21.3-2
Provides:       e = %{version}-%{release}

Recommends:     efl-theme-mageia

%description
Enlightenment is a next generation window manager for UNIX operating systems.
Based on the Enlightenment Foundation Libraries (EFL), Enlightenment is much more
than just another window manager - it's an ambitious and innovative project that
aims to drive the development of graphical applications industry-wide for several
years to come.

%package devel
Summary:        Enlightenment library headers and development libraries
Group:          System/Libraries

# e was renamed to enlightenment
Obsoletes:      e-devel < 0.21.3-2
Provides:       e-devel = %{version}-%{release}

%description devel
Enlightenment development headers and development libraries.

%prep
%setup -q
%autopatch -p1
autoreconf -ivf
%build
%configure2_5x \
	--enable-files \
	--disable-static \
	--disable-device-hal \
	--disable-mount-hal \
	--enable-device-udev \
	--enable-wayland-clients \
	--enable-wayland-egl \
	--enable-wayland \
	--enable-xwayland 
%make_build

%install
%make_install

find %buildroot -name '*.la' -delete

#fake e-config
touch %buildroot/%{_bindir}/enlightenment-config
%multiarch_binaries %buildroot/%{_bindir}/enlightenment-config
%find_lang enlightenment




%triggerpostun -- e < 0.18.8-7
if [ -e %{_datadir}/xsessions/23E18.desktop ]; then
    rm -rf %{_datadir}/xsessions/23E18.desktop
fi
if [ -e %{_sysconfdir}/X11/dm/Sessions/23E18.desktop ]; then
    rm -rf %{_sysconfdir}/X11/dm/Sessions/23E18.desktop
fi

%posttrans
if [ "$1" -eq 1 ]; then
    if [ -e %{_datadir}/xsessions/23E22.desktop ]; then
        rm -rf %{_datadir}/xsessions/23E22.desktop
    fi
    if [ -e %{_sysconfdir}/X11/dm/Sessions/23E22.desktop ]; then
	rm -rf %{_sysconfdir}/X11/dm/Sessions/23E22.desktop
    fi
fi



%files -f enlightenment.lang
%license COPYING
%doc AUTHORS README doc/*
%config(noreplace) %_sysconfdir/enlightenment/sysactions.conf
%config(noreplace) %_sysconfdir/xdg/menus/e-applications.menu
%{_bindir}/enlightenment
%{_bindir}/enlightenment_*
%{_bindir}/emixer
%{_datadir}/enlightenment
%{_libdir}/enlightenment
%{_userunitdir}/enlightenment.service
%{_datadir}/applications/enlightenment_filemanager.desktop
%{_datadir}/applications/emixer.desktop
%{_datadir}/pixmaps/emixer.png
%{_datadir}/xsessions/enlightenment.desktop
%{_datadir}/applications/enlightenment_askpass.desktop
%{_datadir}/pixmaps/enlightenment-askpass.png
%{_datadir}/wayland-sessions/enlightenment.desktop

%files devel
%{_bindir}/enlightenment-config
%{_libdir}/pkgconfig/*.pc
%multiarch %{multiarch_bindir}/enlightenment-config
%{_includedir}/enlightenment


%changelog
* Fri Sep 29 2017 onlyhuman <onlyhuman> 0.22_beta-1.mga6
+ needs efl-1.20.4 disabled fix-emixer.desktop.patch
- both these have been built with wl support (hopefully) :)

* Tue May 30 2017 eatdirt <eatdirt> 0.21.8-1.mga6
+ Revision: 1105554
- Upgrade to version 0.21.8

* Thu May 25 2017 eatdirt <eatdirt> 0.21.7-4.mga6
+ Revision: 1104528
- Rebuild for new efl

* Tue May 02 2017 eatdirt <eatdirt> 0.21.7-3.mga6
+ Revision: 1098740
- Rebuild for new efl

* Mon Apr 10 2017 eatdirt <eatdirt> 0.21.7-2.mga6
+ Revision: 1096271
- Add recommends to mageia theme, cleaning spec

* Fri Mar 31 2017 eatdirt <eatdirt> 0.21.7-1.mga6
+ Revision: 1095514
- Upgrade to bug fix release 0.21.7

* Thu Mar 02 2017 eatdirt <eatdirt> 0.21.6-1.mga6
+ Revision: 1088490
- Upgrade to version 0.21.6

* Sat Feb 25 2017 wally <wally> 0.21.5-2.mga6
+ Revision: 1087820
- remove also old generated E18 xsessions .desktop file lefovers on mga5 to mga6 update
- remove generated xsessions .desktop file leftovers also from /etc/X11/dm/Sessions

* Fri Jan 20 2017 eatdirt <eatdirt> 0.21.5-1.mga6
+ Revision: 1082506
- Upgrade to version 0.21.5

* Wed Nov 30 2016 eatdirt <eatdirt> 0.21.4-1.mga6
+ Revision: 1071351
- Upgrade to 0.21.4

* Tue Nov 29 2016 eatdirt <eatdirt> 0.21.3-2.mga6
+ Revision: 1070915
- Upgrading to version 0.21.3

  + akien <akien>
    - Rename e to enlightenment (spec file changes)
    - Rename e to enlightenment (moved spec file)
    - Rename e to enlightenment for clarity

* Sun May 01 2016 wally <wally> 0.20.7-2.mga6
+ Revision: 1008420
- remove old xsessions file on pkg update

* Fri Apr 29 2016 trem <trem> 0.20.7-1.mga6
+ Revision: 1007639
- e: bump to version 0.20.7

* Tue Apr 26 2016 ngompa <ngompa> 0.20.6-3.mga6
+ Revision: 1006421
- Small fixups and removal of wmsession.d stuff

* Mon Apr 18 2016 trem <trem> 0.20.6-2.mga6
+ Revision: 1003461
- e: rebuild to use efl 1.17.0

* Sun Apr 17 2016 trem <trem> 0.20.6-1.mga6
+ Revision: 1003244
- e: bump to version 0.20.6

* Thu Dec 31 2015 trem <trem> 0.20.2-1.mga6
+ Revision: 917165
- e: bump version to 0.20.2

* Mon Dec 21 2015 trem <trem> 0.20.1-1.mga6
+ Revision: 912803
- e: bump version to 0.20.1

* Sun Dec 20 2015 trem <trem> 0.20.0-1.mga6
+ Revision: 912729
- e: fix desktop file (emixer and enlightenment_filemanager)
- e: add emixer and rename E18 to E20
- e: bump version to 0.20.0

* Sun Nov 15 2015 trem <trem> 0.19.13-1.mga6
+ Revision: 903461
- e: bump version to 0.19.13

* Wed Oct 07 2015 fwang <fwang> 0.19.12-1.mga6
+ Revision: 886680
- 0.19.12

* Sun Sep 13 2015 trem <trem> 0.19.10-1.mga6
+ Revision: 878909
- e: bump version to 0.19.10

* Sun Sep 06 2015 trem <trem> 0.19.9-1.mga6
+ Revision: 873369
- e: bump version to 0.19.9

* Mon Aug 10 2015 trem <trem> 0.19.8-1.mga6
+ Revision: 862346
- e: bump version to 0.19.8

* Sun Jul 26 2015 trem <trem> 0.19.7-1.mga6
+ Revision: 857979
- bump version to 0.19.7

* Sun Jul 05 2015 trem <trem> 0.19.5-1.mga6
+ Revision: 850863
- e: bump version to 0.19.5

* Wed Oct 15 2014 umeabot <umeabot> 0.18.8-6.mga5
+ Revision: 742385
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.18.8-5.mga5
+ Revision: 678902
- Mageia 5 Mass Rebuild

* Fri Sep 05 2014 trem <trem> 0.18.8-4.mga5
+ Revision: 672422
- bump release to force rebuild

* Sun Jul 20 2014 trem <trem> 0.18.8-3.mga5
+ Revision: 654739
- bump release to force rebuild

* Mon Jul 14 2014 trem <trem> 0.18.8-2.mga5
+ Revision: 651881
- increase release to force rebuild

* Sat May 17 2014 trem <trem> 0.18.8-1.mga5
+ Revision: 623225
- bump version to 0.18.8

* Sun Apr 20 2014 trem <trem> 0.18.7-1.mga5
+ Revision: 617163
- e: bump version to 0.18.7

* Sat Apr 05 2014 trem <trem> 0.18.6-1.mga5
+ Revision: 611973
- bump version to 0.18.6

* Sat Mar 08 2014 trem <trem> 0.18.5-1.mga5
+ Revision: 601382
- bump version to 0.18.5

* Sat Mar 01 2014 trem <trem> 0.18.4-3.mga5
+ Revision: 598199
- add elementary as requires

* Mon Feb 24 2014 trem <trem> 0.18.4-2.mga5
+ Revision: 596628
- add elementary as requires

* Sun Feb 23 2014 trem <trem> 0.18.4-1.mga5
+ Revision: 596026
- add buildrequires (efl)
- bump version to 0.18.4

* Thu Feb 13 2014 trem <trem> 0.17.6-1.mga5
+ Revision: 590854
- bump version to 0.17.6

* Sat Nov 23 2013 trem <trem> 0.17.5-2.mga4
+ Revision: 552471
- use pkgconfig for the buildrequire to avoid issue with epoch
- increase release
- update to version 0.17.5

  + umeabot <umeabot>
    - Mageia 4 Mass Rebuild

* Sun Sep 08 2013 trem <trem> 0.17.4-3.mga4
+ Revision: 476194
- fix logging (mga#11179)

* Sun Aug 04 2013 trem <trem> 0.17.4-2.mga4
+ Revision: 463361
- update version to 0.17.4 (fix changelog from previous commit)
- increase release to rebuild

* Wed Jun 19 2013 fwang <fwang> 0.17.3-1.mga4
+ Revision: 444964
- new version 0.17.3

* Tue May 07 2013 trem <trem> 0.17.1-3.mga3
+ Revision: 412584
- increase release to rebuild

* Sun Mar 31 2013 neoclust <neoclust> 0.17.1-2.mga3
+ Revision: 406899
- Fix upgrade by adding a conflict

* Sun Mar 10 2013 trem <trem> 0.17.1-1.mga3
+ Revision: 402041
- update to 0.17.1 (bugfix release)

  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Dec 23 2012 trem <trem> 0.17.0-3.mga3
+ Revision: 334122
- update theme (use default one)

* Sat Dec 22 2012 trem <trem> 0.17.0-2.mga3
+ Revision: 333977
- update to release 0.17.0
- update to release 0.17.0

* Fri Dec 21 2012 trem <trem> 0.17.0-1.omega.1.mga3
+ Revision: 333637
- update default theme to A-Mageia-3.edj

* Fri Dec 21 2012 trem <trem> 0.17.0-0.omega.1.mga3
+ Revision: 333628
- update to release 0.17.0-omega

* Sat Dec 15 2012 trem <trem> 0.17.0-0.lucky.1.mga3
+ Revision: 331085
- update to release 0.17.0-lucky

* Tue Dec 11 2012 trem <trem> 0.17.0-0.gamma.1.mga3
+ Revision: 329790
- update to release 0.17.0-gamma

* Sat Dec 08 2012 trem <trem> 0.17.0-0.beta.1.mga3
+ Revision: 328221
- update to release 0.17.0-beta

* Tue Dec 04 2012 trem <trem> 0.17.0-0.alpha8.1.mga3
+ Revision: 326517
- update to release 0.17.0-alpha8

* Fri Nov 30 2012 trem <trem> 0.17.0-0.alpha7.1.mga3
+ Revision: 323545
- update to release 0.17.0-alpha7

* Sat Nov 24 2012 trem <trem> 0.17.0-0.alpha5.1.mga3
+ Revision: 321521
- add xcb-keysyms as buildrequires
- update to release 0.17.0-alpha5

* Sat Sep 22 2012 trem <trem> 0.16.999.76819-1.mga3
+ Revision: 296657
- update to release 76819

* Wed Sep 12 2012 fwang <fwang> 0.16.999.76435-1.mga3
+ Revision: 292552
- update file list
- disable hal
- new version 0.16.999.76435

  + doktor5000 <doktor5000>
    - updated default A-Mageia2 theme (Agust)
      o fixes some glitches, f.ex. with E first-start wizard

* Wed May 02 2012 trem <trem> 0.16.999.68658-0.r69188.3.mga2
+ Revision: 234539
- update conflict to fix upgrade between mga1 and mga2 (#5721)

  + doktor5000 <doktor5000>
    - add default Mageia 2 theme as standard theme
    - rename default upstream theme to original-default.edj
    - drop unused Mageia background/profile

* Sun Mar 11 2012 trem <trem> 0.16.999.68658-0.r69188.1.mga2
+ Revision: 222696
- update to release 69188

* Sat Mar 10 2012 trem <trem> 0.16.999.68658-0.r69165.1.mga2
+ Revision: 222519
- use 68658 as version
- update to release 69165

* Sun Mar 04 2012 trem <trem> 0.16.999.68658-0.r68658.1.mga2
+ Revision: 218007
- update to release 68658

* Sat Mar 03 2012 trem <trem> 0.16.999.68649-0.r68649.1.mga2
+ Revision: 217557
- update to release 68649

* Sun Feb 26 2012 trem <trem> 0.16.999.68450-0.r68450.1.mga2
+ Revision: 215225
- update to release 68450

* Sat Feb 25 2012 trem <trem> 0.16.999.68434-0.r68434.1.mga2
+ Revision: 214436
- update to release 68434

* Fri Feb 24 2012 trem <trem> 0.16.999.68363-0.r68363.1.mga2
+ Revision: 213985
- update to release 68363

* Wed Feb 22 2012 trem <trem> 0.16.999.68228-0.r68228.1.mga2
+ Revision: 212088
- update to release 68228

* Sun Feb 19 2012 trem <trem> 0.16.999.68120-0.r68120.1.mga2
+ Revision: 210804
- update to release 68120

* Sat Feb 18 2012 trem <trem> 0.16.999.68102-0.r68102.1.mga2
+ Revision: 210252
- update to release 68102

* Sat Feb 11 2012 trem <trem> 0.16.999.67851-0.r67851.1.mga2
+ Revision: 207555
- update to release 67851

* Sat Feb 11 2012 trem <trem> 0.16.999.67846-0.r67846.1.mga2
+ Revision: 207268
- update to release 67846

* Fri Feb 10 2012 trem <trem> 0.16.999.67830-0.r67830.1.mga2
+ Revision: 206977
- update to release 67830

* Tue Feb 07 2012 trem <trem> 0.16.999.67715-0.r67715.1.mga2
+ Revision: 206012
- update to release 67715
- update to release 67703
- update to release 67702
- update to release 67698
- update to release 67688
- update to release 67680

* Sun Dec 04 2011 trem <trem> 0.16.999.65867-0.r65867.1.mga2
+ Revision: 176097
- update to release 65867

* Tue Nov 29 2011 trem <trem> 0.16.999.65688-0.r65688.1.mga2
+ Revision: 174243
- update to release 65688

* Sun Nov 27 2011 trem <trem> 0.16.999.65613-0.r65613.1.mga2
+ Revision: 172966
- update to release 65613

* Sun Nov 20 2011 trem <trem> 0.16.999.65428-0.r65428.1.mga2
+ Revision: 169729
- update to release 65428

* Thu Nov 17 2011 trem <trem> 0.16.999.65341-0.r65341.1.mga2
+ Revision: 168448
- update to release 65341

* Wed Nov 16 2011 trem <trem> 0.16.999.65269-0.r65269.1.mga2
+ Revision: 168203
- update to release 65269

* Sun Nov 13 2011 trem <trem> 0.16.999.65129-0.r65129.1.mga2
+ Revision: 167165
- update to release 65129

* Fri Nov 11 2011 trem <trem> 0.16.999.65056-0.r65056.1.mga2
+ Revision: 166587
- update to release 65056

* Sat Nov 05 2011 trem <trem> 0.16.999.64753-0.r64753.1.mga2
+ Revision: 163330
- update to release 64753

* Tue Nov 01 2011 trem <trem> 0.16.999.64603-0.r64603.1.mga2
+ Revision: 160816
- update to release 64603

* Mon Oct 31 2011 trem <trem> 0.16.999.64579-0.r64579.1.mga2
+ Revision: 160602
- update to release 64579

* Sun Oct 30 2011 trem <trem> 0.16.999.64519-0.r64519.1.mga2
+ Revision: 160065
- update to release 64519

* Sat Oct 29 2011 trem <trem> 0.16.999.64511-0.r64511.1.mga2
+ Revision: 159818
- update to r64511

* Fri Oct 28 2011 trem <trem> 0.16.999.64327-0.r64501.1.mga2
+ Revision: 159292
- update to r64501

* Wed Oct 26 2011 trem <trem> 0.16.999.64327-0.r64414.1.mga2
+ Revision: 158389
- update to r64414
- use release-version on e17 br package (instead of just version)

* Mon Oct 24 2011 trem <trem> 0.16.999.64327-0.r64328.1.mga2
+ Revision: 157791
- use svn release (instead of stable release)
- spec cleaning

* Wed Sep 21 2011 fwang <fwang> 0.16.999.55225-2.mga2
+ Revision: 146439
- drop .la files

* Tue Apr 19 2011 ennael <ennael> 0.16.999.55225-1.mga1
+ Revision: 88122
- add mageia background
- imported package e

