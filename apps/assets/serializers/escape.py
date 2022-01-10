# -*- coding: utf-8 -*-
#
from django.utils.translation import ugettext as _
from rest_framework import serializers

from orgs.mixins.serializers import BulkOrgResourceModelSerializer
from ops.mixin import PeriodTaskSerializerMixin
from common.utils import get_logger

from ..models import (
    EscapeRoutePlan,
    EscapeRoutePlanExecution,
    EscapeRoutePlanTask,
)

logger = get_logger(__file__)

__all__ = [
    'EscapeRoutePlanSerializer', 'EscapeRoutePlanExecutionSerializer',
    'EscapeRoutePlanExecutionTaskSerializer'
]


class EscapeRoutePlanSerializer(PeriodTaskSerializerMixin, BulkOrgResourceModelSerializer):
    class Meta:
        model = EscapeRoutePlan
        fields = [
            'id', 'name', 'is_periodic', 'interval', 'crontab', 'date_created',
            'date_updated', 'created_by', 'periodic_display', 'comment',
            'recipients'
        ]
        extra_kwargs = {
            'name': {'required': True},
            'periodic_display': {'label': _('Periodic perform')},
            'recipients': {'label': _('Recipient'), 'help_text': _(
                'Currently only mail sending is supported'
            )}
        }


class EscapeRoutePlanExecutionSerializer(serializers.ModelSerializer):
    trigger_display = serializers.ReadOnlyField(
        source='get_trigger_display', label=_('Trigger mode')
    )

    class Meta:
        model = EscapeRoutePlanExecution
        fields = '__all__'
        read_only_fields = (
            'plan_snapshot', 'date_start', 'timedelta', 'date_created'
        )

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.extend(['recipients', ])
        return fields


class EscapeRoutePlanExecutionTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscapeRoutePlanTask
        fields = '__all__'
