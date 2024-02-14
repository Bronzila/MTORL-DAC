import argparse

from src.utils.generate_plots import (
    plot_optimization_trace,
    plot_actions,
    plot_multiple_optim_trace,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate plots based on run data"
    )
    parser.add_argument(
        "--data_dir",
        help="Path to the directory including the run information and run data",
    )
    parser.add_argument(
        "--agent_path",
        help="Relative path of the RL agents data based on data_dir.",
    )
    parser.add_argument(
        "--optim_trace",
        help="Generate plots for optimization trace",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    parser.add_argument(
        "--optim_multiple",
        help="Comparison plot for optimization trace of multiple runs",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    parser.add_argument(
        "--action",
        help="Generate plots for teacher-agent action comparison",
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--trajectory",
        help="Generate plots for optimization trajectory (function values)",
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--show",
        default=False,
        help="Either show or save the selected plots. Default is save.",
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--num_runs",
        help="Path to the directory including the run information and run data",
        type=int,
        default=1,
    )
    args = parser.parse_args()

    if args.optim_trace:
        plot_optimization_trace(
            args.data_dir, args.agent_path, args.show, args.num_runs
        )
    if args.optim_multiple:
        plot_multiple_optim_trace(
            args.data_dir, args.agent_path, args.show, args.num_runs
        )
    if args.action:
        plot_actions(args.data_dir, args.agent_path, args.show)
