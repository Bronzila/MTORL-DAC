import argparse
import json
from pathlib import Path

import numpy as np


def generate_step_agent(agent_id):
    gamma = np.random.uniform(0.5, 0.99)
    step_size = np.random.randint(1, 10)
    agent = {
        "params": {
            "gamma": gamma,
            "step_size": step_size,
        },
        "type": "step_decay",
        "id": agent_id,
    }

    return agent

def generate_exponential_agent(agent_id):
    decay_rate = np.random.uniform(0.5, 0.99)
    decay_steps = np.random.randint(1, 10)
    agent = {
        "params": {
            "decay_rate": decay_rate,
            "decay_steps": decay_steps,
        },
        "type": "exponential_decay",
        "id": agent_id,
    }

    return agent

def save_agents(agent_configs, agent_type):
    save_path = Path(
        "configs",
        "agents",
        agent_type,
    )
    for config in agent_configs:
        agent_id = config["id"]
        file = save_path / f"{agent_id}.json"
        with file.open("w") as f:
            json.dump(config, f, indent=4)

def generate_random_agent_configs(n, agent_type):
    agent_configs = []

    for id in range(n):
        if agent_type == "step_decay":
            agent_configs.append(generate_step_agent(id + 1))
        elif agent_type == "exponential_decay":
            agent_configs.append(generate_exponential_agent(id + 1))

    save_agents(agent_configs, agent_type)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate agent configurations")
    parser.add_argument(
        "--generation_type",
        type=str,
        default="random",
    )
    parser.add_argument(
        "--agent_type", type=str, default="step_decay", choices=["step_decay", "exponential_decay"]
    )
    parser.add_argument(
        "--n",
        type=int,
        default=10,
        help="Number of agents to generate",
    )
    args = parser.parse_args()

    if args.generation_type == "random":
        generate_random_agent_configs(args.n, args.agent_type)