Summary:	Tools for the iTVC15/16 and CX23415/16 driver
Name:		ivtv-utils
Version:	1.4.1
Release:	%mkrel 1
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
