# TODO:
# - check dir
# - separate locales
%define		_plugin	check_quota
%define		mversion	1.2.7
Summary:	Check Quota plugin for SquirrelMail
Summary(pl):	Wtyczka do sprawdzania limitów dyskowych
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.4
Release:	%{mversion}.0.1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	b9b6c50445dc68d29c6af6b9c11e3481
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_datadir}/squirrelmail/plugins/%{_plugin}

%description
This plugin includes the functionality of two plugins, which are Quota
Usage plugin and Disk Quota plugin.

It can retrieve the current quota usage from the IMAP server using the
IMAP4 QUOTA extension. It displays size-based quotas and/or
message-count quotas, as given by the IMAP server. This function comes
from Quota Usage plugin.

Also it can retrieve the current quota usage from UNIX quota command
for UNIX-quota based systems. It displays size-based quotas and/or
file-count quotas, as retreived from the quota command. This function
comes from Disk Quota plugin.

%description -l pl
Wtyczka ³±czy funkcjonalno¶æ dwóch innych wtyczek - Quota Usage i Disk
Quota.

Mo¿na pobraæ z serwera IMAP aktualne u¿ycie przestrzeni dyskowej przy
u¿yciu rozszerzenia IMAP4 QUOTA. Wy¶wietla limity oparte o rozmiar
i/lub liczbê wiadomo¶ci zgodnie z tym, co poda³ serwer IMAP. Ta
funkcja pochodzi z wtyczki Quota Usage.

Mo¿na tak¿e pobraæ aktualne u¿ycie przestrzeni dyskowej z uniksowego
polecenia quota. Wy¶wielta limity oparte o rozmiar i/lub liczbê plików
zgodnie z tym co poda³o polecenie quota. Ta funkcja pochodzi z wtyczki
Disk Quota.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
cp -r images swf locale $RPM_BUILD_ROOT%{_plugindir}
install config.php.sample $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README FAQ TRANSLATING OLDCHANGELOG
%config(noreplace) %verify(not md5 mtime size) %{_plugindir}/config.php
%dir %{_plugindir}
%{_plugindir}/*.php
%{_plugindir}/swf
%{_plugindir}/locale
%{_plugindir}/images
