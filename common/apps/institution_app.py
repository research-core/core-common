from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from common.models import Institution

class InstitutionAdminApp(ModelAdminWidget):
    

    UID   = 'common-Institution-app'.lower()
    MODEL = Institution
    
    TITLE = 'Institutions'

    #list of filters fields
    #LIST_FILTER    = ['membership','academiccareer','id','name','short_name']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['membership','academiccareer','id','name','short_name']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['membership','academiccareer','id','name','short_name']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['membership','academiccareer','id','name','short_name']
    
    #read only fields
    #READ_ONLY      = ['membership','academiccareer','id','name','short_name']
    
    #EDITFORM_CLASS = InstitutionModelFormWidget    #edit form class
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
    
    
    