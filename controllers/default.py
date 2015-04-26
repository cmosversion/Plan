# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    from applications.Core.modules.item_db import ItemDb

    item_db = ItemDb(db)
    plan_objects_db = item_db.get_item_object_dbs('plan')
    plan_component = get_component(request, response)
    template = plan_component.get_template()
    #plan_db = plan_objects_db['plan']
    plan_items = {}#plan_db.get_primary_items()

    response.view = 'plan/default_list.html'
    response.title = 'Plan (List)'

    return dict(data=plan_items)

def create():
    response.title = 'Plan (Create)'
    item_icons = ['icon-trash icon-white', 'icon-briefcase icon-white']
    items = {
        '1': dict (
            item='plan_title_1'
            , fields={
                '1':dict(
                    field='plan_title_1_title_field_item'
                    , value=''
                    , field_id=''
                )
            }
        )
        , '2':dict(
            item='plan_goals_2'
            , fields={
                '1':dict(field='plan_goals_2_goals_field_item')
            }
            , items={
                '1':dict(
                    fields={
                        '1':dict(
                            field='plan_goals_2_goals_goal_1_goal_field_item'
                            , value=''
                            , field_id=''
                        )
                    }
                    , items={
                        '1':dict(
                            fields={
                                '1':dict(
                                    field='plan_goals_2_goals_goal_1_goal_objectives_1_objectives_field_item'
                                    , value=''
                                    , field_id=''
                                )
                            }
                            , items={
                                '1': dict(
                                    data={
                                        '1':dict(
                                            field='plan_goals_2_goals_goal_1_goal_objectives_1_objectives_objective_1_objective_data_data'
                                            , field_id=''
                                            , value=''
                                        )
                                    }
                                )
                                , '2': dict(
                                    data={
                                        '1':dict(
                                            field='plan_goals_2_goals_goal_1_goal_objectives_1_objectives_objective_2_objective_data_data'
                                            , field_id=''
                                            , value=''
                                        )
                                    }
                                )
                            }
                        )
                   }
                )
            }
        )
    }

    default_plan_items = dict(
        field={
            'plan-field-item':'Plan'
        }
        , items={
            '1':dict(
                field={
                    'plan-title-1-title-field-item':''
                    , 'plan-title-1-title-field-item_label':'Title'
                }
            )
            , '2':dict(
                field={
                    'plan-goals-2-goals-field-item':'Goals'
                }
                , items={
                    '1': dict (
                        field={
                            'plan-goals-2-goals-goal-1-goal-field-item':''
                        }
                        , items={
                            '1':dict(
                                field={
                                    'plan-goals-2-goals-goal-1-goal-objectives-1-objectives-field-item':'Objectives'
                                }
                                , items={
                                    '1':dict(
                                        data={
                                            'plan-goals-2-goals-goal-1-goal-objectives-1-objective-objective-1-objective-data-1-data-field-item':''
                                        }
                                    )
                                    , '2':dict(
                                        data={
                                            'plan-goals-2-goals-goal-1-goal-objectives-1-objective-objective-2-objective-data-1-data-field-item':''
                                        }
                                    )
                                }
                            )
                        }
                    )
                }
            )
        }
    )

    default_plan_items =    [
        dict(
            label='Title'
            , value=''
            , item='title'
         )
        , dict(
            label='Goals'
            , item_id='goals_1'
            , value=''
            , icons=item_icons
            , items=[
                dict(
                    value=''
                    , item='goal'
                    , item_id='goal_1_0'
                    , items=[
                        dict(
                            label='Objectives'
                            , icons=item_icons
                            , item_id='objectives_1_0_0'
                            , items=[
                                dict(
                                    value=''
                                    , data=[dict(data='',icons=['icon-remove'])]
                                )
                                , dict(
                                    value=''
                                    , data=[dict(data='',icons=['icon-remove'])]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        , dict(
            label='Procedure'
            , icons=item_icons
            , item_id='procedure_2'
            , value=''
            , items=[
                dict(
                    value=''
                    , label='Openning'
                    , item_id='openning_2_0'
                    , icons=item_icons
                    , items=[
                        dict(
                            value=''
                            , data=[dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove'])]
                        )
                    ]
                )
                , dict(
                    value=''
                    , label='Determination'
                    , item_id='determination_2_1'
                    , icons=item_icons
                    , items=[
                        dict(
                            value=''
                            , data=[dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove'])]
                        )
                    ]
                )
                , dict(
                    value=''
                    , label='Closing'
                    , item_id='closing_2_3'
                    , icons=item_icons
                    , items=[
                        dict(
                            value=''
                            , data=[dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove'])]
                        )
                    ]
                )
            ]
        )
        , dict(
            label='Evaluation'
            , icons=item_icons
            , item_id='evaluation_3'
            , value=''
            , items=[
                dict(
                    value=''
                    , label='Preliminary'
                    , item_id='preliminary_3_0'
                    , icons=item_icons
                    , items=[
                        dict(
                            value=''
                            , data=[dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove'])]
                        )
                    ]
                )
                , dict(
                    value=''
                    , icons=item_icons
                    , item_id='final_3_1'
                    , label='Final'
                    , items=[
                        dict(
                            value=''
                            , data=[dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove']), dict(data='',icons=['icon-remove'])]
                        )
                    ]
                )
            ]
        )
    ]
    default_plan_items = {
    "item": {
        "item_id": "plan-field-item",
        "value": "Plan"
    },
    "items": {
        "1": {
            "item": {
                "item_id": "plan-title-1-title-field-item",
                "value": ""
            }
        },
        "2": {
            "item_id": {
                "item_id": "plan-goals-2-goals-field-item_id",
                "value": "123"
            },
            "item": {
                "item_id": "plan-goals-2-goals-field-item",
                "value": "Goals"
            },
            "items": {
                "1": {
                    "item": {
                        "item_id": "plan-goals-2-goals-goal-1-goal-field-item",
                        "value": ""
                    },
                    "items": {
                        "1": {
                            "item": {
                                "item_id": "plan-goals-2-goals-goal-1-goal-objectives-1-objectives-field-item",
                                "value": "Objectives"
                            },
                            "items": {
                                "1": {
                                    "data_data": {
                                        "item_id": "plan-goals-2-goals-goal-1-goal-objectives-1-objectives-objective-1-objective-data-1-data-field-data",
                                        "value": ""
                                    }
                                },
                                "2": {
                                    "data_data": {
                                        "item_id": "plan-goals-2-goals-goal-1-goal-objectives-1-objectives-objective-2-objective-data-1-data-field-data",
                                        "value": ""
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
    from applications.Core.modules.item_db import ItemUtil
    names = {
        'plan-field-item':'Plan'
        , 'plan-title-1-title-field-item':'(Title)'
        , 'plan-goals-2-goals-field-item':'Goals'
        , 'plan-goals-2-goals-goal-1-goal-field-item':'Goal'
        , 'plan-goals-2-goals-goal-1-goal-objectives-1-objectives-field-item':'Objectives'
        , 'plan-goals-2-goals-goal-1-goal-objectives-1-objectives-objective-1-objective-data-1-data-field-data':''
        , 'plan-goals-2-goals-goal-1-goal-objectives-1-objectives-objective-2-objective-data-1-data-field-data':''
        , 'plan-procedure-3-procedure-field-item':'Procedure'
        , 'plan-procedure-3-procedure-openning-1-openning-field-item':'Openning'
        , 'plan-procedure-3-procedure-openning-1-openning-content-1-content-field-item':''
        , 'plan-procedure-3-procedure-openning-1-openning-content-1-content-field-data':''
        , 'plan-procedure-3-procedure-openning-1-openning-content-1-content-field-value':''
        , 'plan-procedure-3-procedure-determination-2-determination-field-item':'Determination'
        , 'plan-procedure-3-procedure-determination-2-determination-content-1-content-field-item':''
        , 'plan-procedure-3-procedure-determination-2-determination-content-1-content-field-data':''
        , 'plan-procedure-3-procedure-determination-3-determination-field-item':'Closing'
        , 'plan-procedure-3-procedure-determination-3-determination-content-1-content-field-item':''
        , 'plan-procedure-3-procedure-determination-3-determination-content-1-content-field-data':''
        , 'plan-evaluation-4-evaluation-field-item':'Evaluation'
        , 'plan-evaluation-4-evaluation-preliminary-1-preliminary-field-item':'Preliminary'
        , 'plan-evaluation-4-evaluation-preliminary-1-preliminary-content-1-content-field-item':''
        , 'plan-evaluation-4-evaluation-preliminary-1-preliminary-content-1-content-field-data':''
        , 'plan-evaluation-4-evaluation-final-2-final-field-item':'Final'
        , 'plan-evaluation-4-evaluation-final-2-final-content-1-content-field-item':''
        , 'plan-evaluation-4-evaluation-final-2-final-content-1-content-field-data':''
    }


    item_type_ids = {
        'item':1,'plan':2,'goals':4,'goal':5,'objectives':6,'objective':7,'title':8, 'procedure':9, 'openning':10, 'content':11, 'determination':12
        , 'evaluation':13, 'preliminary':14, 'final':15
    }
    html_data = ItemUtil.form_data_to_item(names, item_type_ids)
    default_plan_items = ItemUtil.item_to_form_data(html_data)
    return process(default_plan_items, item_icons)

def update():
    response.title = 'Plan (Update)'

    return process()

def get_component(request, response):
    from plan_component import PlanComponent
    return PlanComponent(db, request, response)

def process(default_plan_items=None, item_icons=None):

    plan_component = get_component(request, response)
    template = plan_component.get_template()

    data = plan_component.get_data()
    control = plan_component.get_control()
    error = plan_component.get_errors()
    css_template = template.get('css')
    html_template = template.get('html')

    html_template = 'plan/default_test.html'

    response.view = html_template
    response.files.insert(4, css_template)
    view = dict(css=[css_template])
    db.define_table('test', Field('ddd', 'string'))

    data = dict(item=default_plan_items, item_icons=item_icons, form=SQLFORM(db.test))

    return dict(data=data, view=view)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
