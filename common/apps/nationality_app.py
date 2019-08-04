from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from common.models import Nationality

class NationalityAdminApp(ModelAdminWidget):
    

    UID   = 'common-Nationality-app'.lower()
    MODEL = Nationality
    
    TITLE = 'Nationalities'

    #list of filters fields
    #LIST_FILTER    = ['grant','nationality_id','nationality_name']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['grant','nationality_id','nationality_name']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['grant','nationality_id','nationality_name']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['grant','nationality_id','nationality_name']
    
    #read only fields
    #READ_ONLY      = ['grant','nationality_id','nationality_name']
    
    #EDITFORM_CLASS = NationalityModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>CityAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dollar'
    ########################################################
    
    
    