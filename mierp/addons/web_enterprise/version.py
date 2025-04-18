# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

import mierp

# ----------------------------------------------------------
# Monkey patch release to set the edition as 'enterprise'
# ----------------------------------------------------------
mierp.release.version_info = mierp.release.version_info[:5] + ('e',)
if '+e' not in mierp.release.version:     # not already patched by packaging
    mierp.release.version = '{0}+e{1}{2}'.format(*mierp.release.version.partition('-'))

mierp.service.common.RPC_VERSION_1.update(
    server_version=mierp.release.version,
    server_version_info=mierp.release.version_info)
