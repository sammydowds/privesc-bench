import os

from inspect_ai import Task, eval_set, task
from inspect_ai.scorer import includes
from inspect_cyber import create_agentic_eval_dataset
from agent import privesc_agent

SANDBOX_DIR = os.environ["SANDBOX_DIR"]


@task
def task():
    return Task(
        name="Privilege Escalation, v0 Challenge Evaluations",
        dataset=(
            create_agentic_eval_dataset(SANDBOX_DIR).filter_by_metadata_field(
                "variant_name", ["easy", "moderate", "hard"]
            )
        ),
        solver=privesc_agent(),
        scorer=includes(),
    )
