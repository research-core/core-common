from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from common.models import Currency

class CurrencyAdminApp(ModelAdminWidget):
    

    UID   = 'common-Currency-app'.lower()
    MODEL = Currency
    
    TITLE = 'Currencies'

    #list of filters fields
    #LIST_FILTER    = ['project','order','currency_id','currency_name','currency_symbol']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['project','order','currency_id','currency_name','currency_symbol']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['project','order','currency_id','currency_name','currency_symbol']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['project','order','currency_id','currency_name','currency_symbol']
    
    #read only fields
    #READ_ONLY      = ['project','order','currency_id','currency_name','currency_symbol']
    
    #EDITFORM_CLASS = CurrencyModelFormWidget    #edit form class
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
    
    
    