Summary:	Tools for the iTVC15/16 and CX23415/16 driver
Name:		ivtv-utils
Version:	1.4.1
Release:	3
License:	GPLv2
Group:		System/Kernel and hardware
Source0:	http://dl.ivtvdriver.org/ivtv/archive/1.4.x/%{name}-%{version}.tar.gz
Patch0:		ivtv-1.4.0-fix-string-format.patch
URL:		http://ivtvdriver.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Suggests:	ivtv-firmware
Conflicts:	v4l-utils <= 0.7.91-3mdv2010.1
Obsoletes:	ivtv < 1.2.0
Provides:	ivtv = %{version}-%{release}

%description
The primary goal of the IvyTV Project is to create a kernel driver for
the iTVC15 family of MPEG codecs. The iTVC15 family includes the
iTVC15 (CX24315) and iTVC16 (CX24316). These chips are commonly found
on Hauppauge's WinTV PVR-250 and PVR-350 TV capture cards.

The driver has made it into the kernel so this package only contains
some userland tools for ivtv.

%prep
%setup -q
%patch0 -p0
perl -pi -e's@CFLAGS = -D_GNU_SOURCE .*@CFLAGS = -D_GNU_SOURCE -D__user= %{optflags}@' utils/Makefile

%build
make -C utils

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/ivtv/
make -C utils DESTDIR=%{buildroot} BINDIR=%{_bindir} install

install -p utils/*.pl %{buildroot}%{_datadir}/ivtv/
ln -s ivtv-radio %{buildroot}%{_bindir}/radio-ivtv

rm -f %{buildroot}%{_includedir}/linux/ivtv.h %{buildroot}%{_includedir}/linux/ivtvfb.h

# already provided by v4l-utils with a more uptodate copy
rm -f %{buildroot}%{_bindir}/v4l2-ctl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/*
%{_datadir}/ivtv


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdv2011.0
+ Revision: 612427
- the mass rebuild of 2010.1 packages

* Sun Apr 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 536077
- new upstream release 1.4.1

* Sat Mar 27 2010 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.4.0-2mdv2010.1
+ Revision: 527885
- Do not provide v4l2-ctl, v4l-utils already provides a more uptodate
  copy (#58419).

* Sun Mar 21 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.4.0-1mdv2010.1
+ Revision: 526206
- import ivtv-utils


* Tue Feb 03 2009 Jarod Wilson <jarod@redhat.com> - 1.3.0-8
- Fix up for current rawhide

* Tue Dec 02 2008 Jarod Wilson <jarod@redhat.com> - 1.3.0-7
- Update to 1.3.0.

* Wed Aug 27 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.0-6
- Rename to ivtv-utils (in anticipation for ivtv-utils 1.3.0.
- Use rename to get rid of the epoch.

* Fri Jun 18 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:1.2.0-4
- Update to 1.2.0.

* Wed Dec 26 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:1.0.3-3
- Remove the dependencies on old perl helper modules.
- Changed summary and description to reflect removal of driver code.

* Wed Oct 24 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:1.0.3-2
- Update to 1.0.3.
- Remove pseudo-firmware file (mpeg initialisation sequence).
- Remove devel subpackage.
- Use %%{optflags}.
- Move parl scripts to %%{_datadir}.
- Add dependency to firmware package.

* Sun Aug 26 2007 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.2.

* Thu Jul 26 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:1.0.1-1
- Update to 1.0.1.
- Prepare package for Fedora.

* Sun Jul 22 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.10.5-130
- Update to 0.10.5.

* Fri Jun  1 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.10.3-129
- Update to 0.10.3.

* Sat May 19 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.10.2-128
- Update to 0.10.2.

* Fri Mar  2 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.10.1-126
- Update to 0.10.1.

* Sun Feb 18 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.10.0-125
- Update to 0.10.0 final.

* Mon Feb  5 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.10.0-124_rc1
- Update to 0.10.0rc1.

* Sun Jan  7 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.1-123
- Update to 0.9.1.

* Sun Dec 10 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.8.2-123
- Update to 0.8.2.

* Mon Nov 20 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.8.1-122
- Update to 0.8.1.

* Mon Sep 25 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.8.0-119
- Update to 0.8.0.

* Tue Jul  4 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.7.0.

* Sun Jul  2 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to latest svn.

* Mon Jun 26 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to latest svn.

* Sun May 28 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to latest svn.

* Sat Apr  8 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to latest svn.

* Thu Mar 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to ivtv trunk.
- Build against video4linux-devel.

* Sat Mar 25 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.6.1.

* Fri Mar 24 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.6.0.

* Wed Mar 15 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.6 branch.

* Tue Mar  7 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Stop renaming supporting ivtv modules with -ivtv suffix.
- Remove any alias foo foo-ivtv lines.

* Fri Feb 17 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.4.3.

* Thu Jan 19 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.4.2.

* Mon Dec 19 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.4.1.

* Sun Oct  9 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.4.0.

* Tue Sep 13 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.8.

* Fri Sep  2 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.7k.

* Mon Aug 15 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.7d.

* Sat Jul  2 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.6w.

* Sat Jun 18 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.6o.

* Sat May 28 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.5l.

* Wed May 25 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- update to 0.3.5g.

* Wed May 18 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.4w.

* Sat May 14 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.4p.

* Thu May 12 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.4m.

* Tue May 10 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.4j.

* Fri May  6 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.4b.

* Tue May  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.4a.

* Tue May  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.3z.

* Wed Apr 27 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.3p.

* Wed Apr 27 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.3o.

* Mon Apr 25 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.3k.

* Fri Apr 22 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.3g.

* Thu Apr 21 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.3f.

* Fri Apr  1 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2q.

* Sun Mar 27 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2p.

* Sat Mar 26 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2o.

* Fri Mar 25 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2m.

* Tue Mar 22 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2k.

* Tue Mar 22 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2j.

* Wed Mar 16 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2i.

* Mon Mar  7 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2h.

* Thu Feb 24 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2e.

* Mon Feb  7 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2d.

* Tue Jan 25 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2c.

* Thu Jan  6 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2b.

* Wed Dec 29 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.2a.

* Mon Dec  6 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.1z.

* Sat Nov 27 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.1w.

* Tue Nov  2 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.1f.

* Mon Oct 18 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.3.0j.
- build the ivtvdev_drv.o X driver.

* Tue Oct 12 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.2.0-rc1a.
- Update to 0.3.0c.

* Mon Oct 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck115d.

* Sun Oct 10 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck114v.
- Update to 0.1.10-pre2-ck114y.

* Fri Oct  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck114m.

* Sun Sep 26 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Downgrade to 100z.
- Apply sys_* removal patch (Jarod Wilson <jcw@wilsonet.com>).
- Apply new tuners patch (Michael T. Dean <mtdean@thirdcontact.com>).
- Don't package msp3400.

* Thu Sep  9 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck108k.

* Sun Sep  5 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck108.

* Sat Sep  4 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck107u.

* Fri Sep  3 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck107o.

* Sat Aug 28 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck106e.

* Wed Aug 18 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck104f.

* Thu Jul 29 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck100m.

* Fri Jul 16 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck99z.

* Sun Jul 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck99t.

* Thu Jul  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck99e.

* Thu Jul  1 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck97v.

* Fri Jun 25 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck96i.

* Mon Jun 21 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck94r.

* Sat Jun 19 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2-ck94e.

* Sun May 30 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2_ck77b.

* Sat May 15 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.10-pre2_ck66b.

* Mon Mar 29 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Add m179 patch (Chris Pinkham <cpinkham@bc2va.org>).
- Rename radio to radio-ivtv to avoid conflict with xawtv
  (Aaron Levinson <alevinsn@aracnet.com>).

* Wed Jan 14 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.1.9.

* Wed Dec 31 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Updated to 0.1.7.

* Mon Dec 29 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Updated to official release 0.1.6.

* Mon Dec 15 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Updated to Robert Kulagowski's patched version containing
  o Jens Axboe's 1125A patches
  o Chris Pinkham's M179 patch
  o Anduin's close_stream patch

* Wed Oct 22 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Removed firmware due to unknown licensing.
- Removed ivtv-fb.o due to unresolved depmod issues.
- Added patch for building on gcc < 3.

* Mon Oct  6 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to decoder_alpha 20031004.
- Remove i2c patch (applied upstream). Only -DNEW_I2C patch remains.
- Added missing include to videodev2.h

* Tue Sep 30 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to decoder_alpha 20030929.

* Wed Aug 20 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update rom image (reported by "Shad L. Lords").

* Tue Aug 19 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 20030813.

* Thu Jul 17 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 20030717.

* Thu Jul  7 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 20030707.

* Sun Jun 22 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 20030622.

* Mon Jun 16 2003 Axel Thimm <Axel.Thimm@ATrpms.net> 
- Initial build.
