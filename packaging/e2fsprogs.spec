Name:           e2fsprogs
BuildRequires:  autoconf
BuildRequires:  libblkid-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config
Version:        1.42.11
Release:        0
Summary:        Utilities for the Second Extended File System
License:        GPL-2.0
Group:          System/Filesystems
Url:            http://e2fsprogs.sourceforge.net
Requires:       libcom_err >= %{version}
Requires:       libext2fs >= %{version}
Source:         http://downloads.sourceforge.net/project/e2fsprogs/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.xz
Source1:        baselibs.conf
Source2:        e2fsck.conf
Source1001: 	e2fsprogs.manifest

%description
Utilities needed to create and maintain ext2 and ext3 file systems
under Linux. Included in this package are: chattr, lsattr, mke2fs,
mklost+found, tune2fs, e2fsck, resize2fs, and badblocks.

%package devel
Summary:        Dummy development package
License:        LGPL-2.0
Group:          Base/Development
Requires:       libblkid-devel
Requires:       libext2fs-devel = %version
Requires:       libuuid-devel

%description devel
Dummy development package for backwards compatibility.

%package -n libext2fs
Summary:        Ext2fs library
License:        LGPL-2.0
Group:          Base/File Systems

%description -n libext2fs
The basic Ext2fs shared library.

%package -n libext2fs-devel
Summary:        Development files for libext2fs
License:        LGPL-2.0
Group:          Base/Development
Requires:       libcom_err-devel
Requires:       libext2fs = %version

%description -n libext2fs-devel
Development files for libext2fs.

%package -n libcom_err
Summary:        E2fsprogs error reporting library
License:        MIT
Group:          Base/File Systems

%description -n libcom_err
com_err is an error message display library.

%package -n libcom_err-devel
Summary:        Development files for libcom_err
License:        MIT
Group:          Base/Development
Requires:       glibc-devel
Requires:       libcom_err = %version

%description -n libcom_err-devel
Development files for the com_err error message display library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
%configure \
  --disable-evms \
  --with-root-prefix=''   \
  --enable-elf-shlibs \
  --disable-libblkid \
  --disable-libuuid \
  --disable-uuidd \
  --disable-nls \
  --disable-fsck \
  CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} V=1

%install
make install install-libs DESTDIR=$RPM_BUILD_ROOT ELF_INSTALL_DIR=/%{_libdir}
find "%buildroot/%_libdir" -type f -name "*.a" \
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
       -print -delete
# Let boot continue even if system clock is wrong
install -p -m 644 %{SOURCE2} %{buildroot}/etc/e2fsck.conf


rm $RPM_BUILD_ROOT%{_libdir}/e2initrd_helper
rm -f $RPM_BUILD_ROOT/%{_sbindir}/mkfs.ext4dev
rm -f $RPM_BUILD_ROOT/%{_sbindir}/fsck.ext4dev
rm -f $RPM_BUILD_ROOT/usr/share/man/man8/mkfs.ext4dev.8*
rm -f $RPM_BUILD_ROOT/usr/share/man/man8/fsck.ext4dev.8*

mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
install -p -m 644 README %{buildroot}/%{_defaultdocdir}/%{name}/README
install -p -m 644 RELEASE-NOTES %{buildroot}/%{_defaultdocdir}/%{name}/RELEASE-NOTES

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libext2fs -p /sbin/ldconfig

%postun -n libext2fs -p /sbin/ldconfig

%post -n libcom_err -p /sbin/ldconfig

%postun -n libcom_err -p /sbin/ldconfig

%docs_package
%doc %{_defaultdocdir}/%{name}/RELEASE-NOTES
%doc %{_defaultdocdir}/%{name}/README

%files devel
%manifest %{name}.manifest
%doc README

%files 
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%config /etc/e2fsck.conf
%config /etc/mke2fs.conf
%{_sbindir}/badblocks
%{_sbindir}/debugfs
%{_sbindir}/dumpe2fs
%{_sbindir}/e2undo
%{_sbindir}/e2fsck
%{_sbindir}/e2label
%{_sbindir}/fsck.ext2
%{_sbindir}/fsck.ext3
%{_sbindir}/fsck.ext4
%{_sbindir}/mke2fs
%{_sbindir}/mkfs.ext2
%{_sbindir}/mkfs.ext3
%{_sbindir}/mkfs.ext4
%{_sbindir}/resize2fs
%{_sbindir}/tune2fs
%{_sbindir}/e2image
%{_sbindir}/logsave 
%{_bindir}/chattr
%{_bindir}/lsattr
%{_sbindir}/mklost+found
%{_sbindir}/filefrag
%{_sbindir}/e2freefrag
%{_sbindir}/e4defrag

%files -n libext2fs
%manifest %{name}.manifest
%defattr(-, root, root)
%{_libdir}/libext2fs.so.*
%{_libdir}/libe2p.so.*

%files -n libext2fs-devel
%manifest %{name}.manifest
%defattr(-, root, root)
%{_libdir}/libext2fs.so
%{_libdir}/libe2p.so
/usr/include/ext2fs
/usr/include/e2p
%_libdir/pkgconfig/e2p.pc
%_libdir/pkgconfig/ext2fs.pc

%files -n libcom_err
%manifest %{name}.manifest
%defattr(-, root, root)
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*

%files -n libcom_err-devel
%manifest %{name}.manifest
%defattr(-, root, root)
%_bindir/compile_et
%_bindir/mk_cmds
%{_libdir}/libcom_err.so
%{_libdir}/libss.so
%_libdir/pkgconfig/com_err.pc
%_libdir/pkgconfig/ss.pc
%_includedir/com_err.h
%_includedir/et
%_includedir/ss
%_datadir/et
%_datadir/ss

%changelog
