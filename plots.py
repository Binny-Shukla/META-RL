import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator

ea_path = r"C:\META RL\RL²\PPO\runs\ppo_meta_rl\events.out.tfevents.1753994762.Kio.9948.0"

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
    
policy_steps, policy_values = get_data('Policy loss')
value_steps, value_values = get_data('Value loss')

create_plot(policy_steps, policy_values, 'Policy Loss')
create_plot(value_steps, value_values, 'Value Loss')
