from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from common.models import City

class CityAdminApp(ModelAdminWidget):
    

    UID   = 'common-City-app'.lower()
    MODEL = City
    
    TITLE = 'Cities'

    #list of filters fields
    #LIST_FILTER    = ['privateinfo','city_id','city_name']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['privateinfo','city_id','city_name']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['privateinfo','city_id','city_name']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['privateinfo','city_id','city_name']
    
    #read only fields
    #READ_ONLY      = ['privateinfo','city_id','city_name']
    
    #EDITFORM_CLASS = CityModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dollar'
    ########################################################
    
    
    