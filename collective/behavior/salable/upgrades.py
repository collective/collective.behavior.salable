from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-collective.behavior.salable:default'


def update_catalog(context, logger=None):
    """Update catalog"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting catalog.')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog', run_dependencies=False, purge_old=False)
