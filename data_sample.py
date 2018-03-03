import plotly
plotly.tools.set_credentials_file(username='Prashant5harma', api_key='MUQcfFBqFJ8HVoTULUaS')
import plotly.plotly as py
import plotly.figure_factory as ff

df = [
    dict(Task='Project Planning', Start='2018-01-13', Finish='2018-01-14 ', Resource='Both'),
    dict(Task='Find Research Paper', Start='2018-01-14 ', Finish='2018-01-21 ', Resource='Beta'),
    dict(Task='Find Relevant Projects', Start='2018-01-14 ', Finish='2018-01-17 ', Resource='Alpha'),
    dict(Task='Evaluate Research Paper', Start='2018-01-17 ', Finish='2018-01-24', Resource='Beta'),
    dict(Task='Generate Hypotheses', Start='2018-01-23 ', Finish='2018-02-03 ', Resource='Beta'),
    dict(Task='Finalize Project', Start='2018-0117 ', Finish='2018-01-17 ', Resource='Alpha'),
    dict(Task='Setup Git Versioning(Environment Setup)', Start='2018-01-17 ', Finish='2018-01-24 ', Resource='Alpha'),
    dict(Task='Setup IDE(Eclipse Neon)', Start='2018-01-17', Finish='2018-01-24 ', Resource='Alpha'),
    dict(Task='Setup Plugins/Add ons for calculating metrics', Start='2018-01-17', Finish='2018-01-24  ', Resource='Alpha'),
    dict(Task='Documentation 1', Start='2018-01-24 ', Finish='2018-02-10 ', Resource='Beta'),

    dict(Task='Finalizing Research Paper as related work', Start='2018-02-10 ', Finish='2018-02-11 ', Resource='Both'),
    dict(Task='Summarizing Research Paper', Start='2018-02-11', Finish='2018-02-16 ', Resource='Both'),
    dict(Task='Compare Research Paper with our Study', Start='2018-02-11', Finish='2018-02-16 ', Resource='Both'),
    dict(Task='Documentation 2', Start='2018-02-16 ', Finish='2018-02-17 ', Resource='Beta'),

    dict(Task='Define Internal Metrics', Start='2018-02-17', Finish='2018-02-22 ', Resource='Beta'),
    dict(Task='Internal metrics Implementation', Start='2018-02-22', Finish='2018-02-26', Resource='Both'),
    dict(Task='Metrics Evalutaion', Start='2018-02-26 ', Finish='2018-02-28', Resource='Alpha'),
    dict(Task='Define External Metrics', Start='2018-02-28', Finish='2018-03-04', Resource='Beta'),
    dict(Task='Quantify External attributes', Start='2018-03-04 ', Finish='2018-03-07', Resource='Both'),
    dict(Task='Internal metrics Implementation', Start='2018-03-07', Finish='2018-03-11 ', Resource='Alpha'),
    dict(Task='Documentation 3', Start='2018-03-11', Finish='2018-03-18 ', Resource='Beta'),

    dict(Task='Perform statistical test', Start='2018-03-18  ', Finish='2018-03-20', Resource='Alpha'),
    dict(Task='Compute Pearson coefficient', Start='2018-03-20', Finish='2018-03-23', Resource='Alpha'),
    dict(Task='Perform Linear regression', Start='2018-03-23 ', Finish='2018-03-25 ', Resource='Both'),
    dict(Task='Univariate Linear Regression', Start='2018-03-23 ', Finish='2018-03-25 ', Resource='Both'),
    dict(Task='Logistic regression', Start='2018-03-25', Finish='2018-03-27', Resource='Both'),
    dict(Task='Documentation 4', Start='2018-03-25', Finish='2018-03-31 ', Resource='Beta'),

    dict(Task='Final Documentation', Start='2018-03-31 ', Finish='2018-04-10', Resource='Both')

]

colors = dict(Alpha = 'rgb(46, 137, 205)',
              Beta = 'rgb(114, 44, 121)',
              Both = 'rgb(198, 47, 105)')

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
py.plot(fig, filename='gantt-hours-minutes', world_readable=True)