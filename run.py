#run.py
import subprocess


def dict2args(d):
    out = ''
    for k, v in d.items():
        if v is not None:
            out += f' --{k} {v}'
    return out


def run(d):
    print(d)
    for s in range(3):
        print(f'seed {s}')
        d['seed'] = s
        response = subprocess.call('python main.py' + dict2args(d), shell=True)


if __name__ == "__main__":

    # repeated prisoners dilemma
    run({'env_name': 'repeated_prisoners_dilemma', 'global_epochs': 500, 'n_episodes_per_update': 5, 'batch_size': 5})





