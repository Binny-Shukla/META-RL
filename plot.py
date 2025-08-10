import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator

ea_path = r'C:\META RL\R2D2\runs\R2D2\events.out.tfevents.1754864298.Kio.5476.0'

ea = event_accumulator.EventAccumulator(ea_path)
ea.Reload()

def get_data(tag):

    events = ea.Scalars(tag)
    steps = [e.step for e in events]
    values = [e.value for e in events]

    return steps, values

def create_plot(steps, values, tag):
    plt.figure(figsize=(8, 5))
    plt.plot(steps, values, label= tag, color="royalblue")
    plt.xlabel("Step")
    plt.ylabel('Loss')
    plt.title(f'{tag} over time')
    plt.grid(True)
    plt.legend()
    plt.show()
    
val_steps, val_values = get_data('Value loss')
age_steps, age_values = get_data('Agent loss')
policy_steps, policy_values = get_data('Policy loss')


create_plot(val_steps, val_values, 'Value loss')
create_plot(policy_steps, policy_values, 'Policy loss')
create_plot(age_steps, age_values, 'Agent loss')
