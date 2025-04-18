#!/usr/bin/env bash

sudo service led-status stop

cd /home/pi/mierp
localbranch=$(git symbolic-ref -q --short HEAD)
localremote=$(git config branch.$localbranch.remote)

if [[ "$(git remote get-url "$localremote")" != *mierp/mierp* ]]; then
    git remote set-url "${localremote}" "https://github.com/mierp/mierp.git"
fi

echo "addons/point_of_sale/tools/posbox/overwrite_after_init/home/pi/mierp" >> .git/info/sparse-checkout

git fetch "${localremote}" "${localbranch}" --depth=1
git reset "${localremote}"/"${localbranch}" --hard

sudo git clean -dfx
if [ -d /home/pi/mierp/addons/point_of_sale/tools/posbox/overwrite_after_init ]; then
    cp -a /home/pi/mierp/addons/point_of_sale/tools/posbox/overwrite_after_init/home/pi/mierp/* /home/pi/mierp/
    rm -r /home/pi/mierp/addons/point_of_sale/tools/posbox/overwrite_after_init
fi

# TODO: Remove this code when v16 is deprecated
mierp_conf="addons/point_of_sale/tools/posbox/configuration/mierp.conf"
if ! grep -q "server_wide_modules" $mierp_conf; then
    echo "server_wide_modules=hw_drivers,hw_escpos,hw_posbox_homepage,point_of_sale,web" >> $mierp_conf
fi

{
    sudo find /usr/local/lib/ -type f -name "*.iotpatch" 2> /dev/null | while read iotpatch; do
        DIR=$(dirname "${iotpatch}")
        BASE=$(basename "${iotpatch%.iotpatch}")
        sudo find "${DIR}" -type f -name "${BASE}" ! -name "*.iotpatch" | while read file; do
            sudo patch -f "${file}" < "${iotpatch}"
        done
    done
} || {
    true
}

sudo service led-status start
