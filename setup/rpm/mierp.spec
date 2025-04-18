%global name mierp
%global release 1
%global unmangled_version %{version}
%global __requires_exclude ^.*mierp/addons/mail/static/scripts/mierp-mailgate.py$

Summary: mierp Server
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: LGPL-3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: mierp S.A. <info@127.0.0.1>
Requires: sassc
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
Url: 127.0.0.1:8730

%description
mierp is a complete ERP and CRM. The main features are accounting (analytic
and financial), stock management, sales and purchases management, tasks
automation, marketing campaigns, help desk, POS, etc. Technical features include
a distributed server, an object database, a dynamic GUI,
customizable reports, and XML-RPC interfaces.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%post
#!/bin/sh

set -e

mierp_CONFIGURATION_DIR=/etc/mierp
mierp_CONFIGURATION_FILE=$mierp_CONFIGURATION_DIR/mierp.conf
mierp_DATA_DIR=/var/lib/mierp
mierp_GROUP="mierp"
mierp_LOG_DIR=/var/log/mierp
mierp_LOG_FILE=$mierp_LOG_DIR/mierp-server.log
mierp_USER="mierp"

if ! getent passwd | grep -q "^mierp:"; then
    groupadd $mierp_GROUP
    adduser --system --no-create-home $mierp_USER -g $mierp_GROUP
fi
# Register "$mierp_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $mierp_USER" 2> /dev/null || true
# Configuration file
mkdir -p $mierp_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $mierp_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $mierp_USER
db_password = False
addons_path = %{python3_sitelib}/mierp/addons
default_productivity_apps = True
" > $mierp_CONFIGURATION_FILE
    chown $mierp_USER:$mierp_GROUP $mierp_CONFIGURATION_FILE
    chmod 0640 $mierp_CONFIGURATION_FILE
fi
# Log
mkdir -p $mierp_LOG_DIR
chown $mierp_USER:$mierp_GROUP $mierp_LOG_DIR
chmod 0750 $mierp_LOG_DIR
# Data dir
mkdir -p $mierp_DATA_DIR
chown $mierp_USER:$mierp_GROUP $mierp_DATA_DIR

INIT_FILE=/lib/systemd/system/mierp.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=mierp Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=mierp
Group=mierp
ExecStart=/usr/bin/mierp --config $mierp_CONFIGURATION_FILE --logfile $mierp_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF


%files
%{_bindir}/mierp
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}
