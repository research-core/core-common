from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from common.models import Citizenship

class CitizenshipAdminApp(ModelAdminWidget):
    

    UID   = 'common-Citizenship-app'.lower()
    MODEL = Citizenship
    
    TITLE = 'Citizenships'

    #list of filters fields
    #LIST_FILTER    = ['privateinfo','citizenship_id','citizenship_name']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['privateinfo','citizenship_id','citizenship_name']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['privateinfo','citizenship_id','citizenship_name']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['privateinfo','citizenship_id','citizenship_name']
    
    #read only fields
    #READ_ONLY      = ['privateinfo','citizenship_id','citizenship_name']
    
    #EDITFORM_CLASS = CitizenshipModelFormWidget    #edit form class
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
    
    
    