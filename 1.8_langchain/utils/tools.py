# my tools are going to go in here
from langchain_core.tools import tool

@tool
def get_module_deadline(module_name:str)->str:
    """ Look up the submission deadline for named bootcamp module
    
    Args:
    module_name: the module name eg 'ANN', 'CNN', 'LLM'
    
    """
    deadline={
    "ANN":"2026-09-16",
    "CNN":"2026-09-17",
    "LLM":"2028-09-23"
    }    

    return deadline.get(module_name, "No deadline found for that module")

@tool
def count_students_in_module(module_name:str)->str:
    """look up how many students are enrolled in a named bootcamp module"""
    counts={"ANN":24, "CNN":21, "LLM":34}
    return str(counts.get(module_name, 0))


@tool
def check_prerequisite(
    module_name: str,
    completed_module: str
) -> str:
    """
    Check whether a student has completed the prerequisite
    required for a bootcamp module.

    Args:
        module_name: The module the student wants to take.
        completed_module: The module the student has already completed.
    """

    prerequisites = {
        "CNN": "ANN",
        "LLM": "CNN"
    }

    required = prerequisites.get(module_name.upper())

    if required is None:
        return f"No prerequisite information found for {module_name}."

    if completed_module.upper() == required:
        return (
            f"Yes. {module_name} requires {required}, "
            f"and you have completed {completed_module}."
        )

    return (
        f"No. {module_name} requires {required}, "
        f"but you completed {completed_module}."
    )


@tool
def get_room_schedule(room: str) -> str:
    """
    Look up the sessions scheduled in a specific classroom.

    Args:
        room: The classroom name, e.g. 'A101' or 'B202'.
    """

    schedules = {
        "A101": (
            "Monday 10:00 - ANN; "
            "Wednesday 14:00 - CNN"
        ),
        "B202": (
            "Tuesday 09:00 - LLM; "
            "Thursday 13:00 - Python"
        )
    }

    return schedules.get(
        room.upper(),
        f"No schedule found for room {room}."
    )


