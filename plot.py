import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator

ea_path = r'C:\META RL\first order MAML\runs\FOMAML\events.out.tfevents.1754432670.Kio.2780.0'

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
    
val_steps, val_values = get_data('VALIDATION Loss')


create_plot(val_steps, val_values, 'VALIDATION Loss')
