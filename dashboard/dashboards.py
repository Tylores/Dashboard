###
# Import modules
###
# datetime
import datetime

# django
from django.db.models import Count, Sum
from django.utils import timezone
from django.utils.timesince import timesince

# controlcenter
from controlcenter import Dashboard, widgets, app_settings
from controlcenter.widgets.core import WidgetMeta

# collections
from collections import defaultdict

# models
from der.models import Resource

###
# Define Classes
###
class ListWidgetEWH(widgets.ItemList):
    # Displays all ewh
    title = 'EWH'
    model = Resource
    queryset = (model.objects
                     .filter(type='ewh')
                     .order_by('energy'))
    # This is the magic
    list_display = [app_settings.SHARP, 'pk', 'energy']

    # If list_display_links is not defined, first column to be linked
    list_display_links = ['pk']

    # Makes list sortable
    sortable = True

    # Shows last 20
    limit_to = None
	
	# widget dimensions
    height = 400
#==========
# END CLASS
#==========

class ListWidgetBESS(widgets.ItemList):
    # Displays all bess
    title = 'BESS'
    model = Resource
    queryset = (model.objects
                     .filter(type='bess')
                     .order_by('energy'))
    # This is the magic
    list_display = [app_settings.SHARP, 'pk', 'energy']

    # If list_display_links is not defined, first column to be linked
    list_display_links = ['pk']

    # Makes list sortable
    sortable = True

    # Shows last 20
    limit_to = None
	
	# widget dimensions
    height = 400
#==========
# END CLASS
#==========

class TotalsBarChart(widgets.SingleBarChart):
    # Displays the total energy for each resource type
    title = 'Total Energy'
    model = Resource
	
	# widget dimensions
    height = 400
	
    class Chartist:
        options = {
            # Displays only integer values on y-axis
            'onlyInteger': True,
            # Visual tuning
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 24,
            }
        }

    def legend(self):
        # Duplicates series in legend, because Chartist.js
        # doesn't display values on bars
        return self.series

    def values(self):
        # Returns pairs of restaurant names and order count.
        queryset = self.get_queryset()
        return (queryset.values_list('type')
                        .annotate(total=Sum('energy'))
                        .order_by('-total')[:self.limit_to])
#==========
# END CLASS
#==========

class LineChartEWH(widgets.SingleLineChart):
    # label and series
    values_list = ('pk', 'energy')
    model = Resource
	
    # Data source
    queryset = (model.objects
                     .filter(type='ewh')
                     .order_by('-pk'))
	
	# widget dimensions
    height = 400
    width = widgets.LARGER
    title = 'EWH Energy vs ID'
#==========
# END CLASS
#==========

class LineChartBESS(widgets.SingleLineChart):
    # label and series
    values_list = ('pk', 'energy')
    model = Resource
	
    # Data source
    queryset = (model.objects
                     .filter(type='bess')
                     .order_by('-pk'))
	
	# widget dimensions
    height = 800
    width = widgets.LARGER
    title = 'BESS Energy vs ID'
#==========
# END CLASS
#==========

###
# This is where django-controlcenter creates the modular dashboards
###
class DisplayDashboard(Dashboard):
	# This is the display dashboard
	widgets = [
		# Creates a nice selectable widget
		widgets.Group([
			ListWidgetEWH,
			ListWidgetBESS,
			]),
		TotalsBarChart,
		widgets.Group([
			LineChartEWH,
			LineChartBESS,
			]),
	]
	pass
#==========
# END CLASS
#==========
	
class ControlDashboard(Dashboard):
	# This is the controls dashboard
	# TODO: create inputs for controls and the models to interface
    pass
#==========
# END CLASS
#==========