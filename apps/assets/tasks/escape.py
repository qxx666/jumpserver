# -*- coding: utf-8 -*-
#
from celery import shared_task

from common.utils import get_object_or_none, get_logger
from orgs.utils import tmp_to_org, tmp_to_root_org
from assets.models import (
    EscapeRoutePlan,
    EscapeRoutePlanTask
)

logger = get_logger(__file__)


@shared_task
def execute_escape_route_plan(pid, trigger):
    with tmp_to_root_org():
        plan = get_object_or_none(EscapeRoutePlan, pk=pid)
    if not plan:
        logger.error("No app escape route plan found: {}".format(pid))
        return
    with tmp_to_org(plan.org):
        plan.execute(trigger)


@shared_task
def start_escape_route_plan_task(tid):
    with tmp_to_root_org():
        task = get_object_or_none(EscapeRoutePlanTask, pk=tid)
    if not task:
        logger.error("No app escape route plan task found: {}".format(tid))
        return
    with tmp_to_org(task.org):
        task.start()
