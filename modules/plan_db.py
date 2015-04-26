#!/usr/bin/env python
# coding: utf8
from gluon import *

from applications.Core.modules.item_db import ItemDb
from applications.Core.modules.item_db import ItemItemsDb
from applications.Core.modules.item_db import ItemDataDb
from applications.Core.modules.item_db import ItemItemDb

class PlanDb(ItemDb):
    _name = 'Plan'

class PlanItemsDb(ItemItemsDb):
    _name = 'PlanItems'

class PlanDataDb(ItemDataDb):
    _name = 'PlanData'

class PlanItemDb(ItemItemDb):
    _name = 'Plan'
    _child_name = 'Item'

class PlanPlanDb(ItemItemDb):
    _name = 'Plan'
    _child_name = 'Plan'
