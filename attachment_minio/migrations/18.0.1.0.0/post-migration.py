# Copyright 2020 Hibou Corp.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info('Migrating attachment_minio to version 18.0.1.0.0')
    # Migration logic if needed
    pass