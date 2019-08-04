from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from common.models import Country

class CountryAdminApp(ModelAdminWidget):
    

    UID   = 'common-Country-app'.lower()
    MODEL = Country
    
    TITLE = 'Countries'

    #list of filters fields
    #LIST_FILTER    = ['privateinfo','supplier','country_id','country_name','country_code']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['privateinfo','supplier','country_id','country_name','country_code']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['privateinfo','supplier','country_id','country_name','country_code']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['privateinfo','supplier','country_id','country_name','country_code']
    
    #read only fields
    #READ_ONLY      = ['privateinfo','supplier','country_id','country_name','country_code']
    
    #EDITFORM_CLASS = CountryModelFormWidget    #edit form class
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
    
    
    