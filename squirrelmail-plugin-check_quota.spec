# TODO:
# - check dir
# - separate locales
%define		_plugin	check_quota
%define		mversion	1.2.7
Summary:	Check Quota plugin for SquirrelMail
Summary(pl.UTF-8):	Wtyczka do sprawdzania limitów dyskowych
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	b9b6c50445dc68d29c6af6b9c11e3481
URL:		http://www.squirrelmail.org/plugin_view.php?id=237
Requires:	squirrelmail >= 1.4.6-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_webapps	/etc/webapps
%define		_sysconfdir	%{_webapps}/squirrelmail

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

%description -l pl.UTF-8
Wtyczka łączy funkcjonalność dwóch innych wtyczek - Quota Usage i Disk
Quota.

Można pobrać z serwera IMAP aktualne użycie przestrzeni dyskowej przy
użyciu rozszerzenia IMAP4 QUOTA. Wyświetla limity oparte o rozmiar
i/lub liczbę wiadomości zgodnie z tym, co podał serwer IMAP. Ta
funkcja pochodzi z wtyczki Quota Usage.

Można także pobrać aktualne użycie przestrzeni dyskowej z uniksowego
polecenia quota. Wyświelta limity oparte o rozmiar i/lub liczbę plików
zgodnie z tym co podało polecenie quota. Ta funkcja pochodzi z wtyczki
Disk Quota.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
cp -r images swf locale $RPM_BUILD_ROOT%{_plugindir}
mv config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/check_quota_config.php
ln -s %{_sysconfdir}/check_quota_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README FAQ TRANSLATING OLDCHANGELOG
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_quota_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
%{_plugindir}/swf
%{_plugindir}/locale
%{_plugindir}/images
