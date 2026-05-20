import os
from inspect_ai import Task, task
from inspect_ai.scorer import includes
from inspect_cyber import create_agentic_eval_dataset, verify_solutions

SANDBOX_DIR = os.environ["SANDBOX_DIR"]


@task
def solution():
    return Task(
        name="Privilege Escalation, v0 Challenge Solutions",
        dataset=(
            create_agentic_eval_dataset(SANDBOX_DIR).filter_by_metadata_field(
                "variant_name", "solution"
            )
        ),
        solver=verify_solutions(),
        scorer=includes(),
    )
