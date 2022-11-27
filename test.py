# %%
import kernel

# %%
task = kernel.exec([(('Measure', 0), 'Q0'), (('Measure', 1), 'Q1')], signal = 'count')
task.join()
task.result()['count'][0]

# %%
task.result()#['meta']['system']

# %%
kernel.get('gate').keys()

# %%
kernel.scheduler.list_tasks()

# %% 
task=kernel.scheduler.get_task_by_id(12777085118898036539)