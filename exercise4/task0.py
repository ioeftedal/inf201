"""
This program creates a folder pattern
- Project name
    - data/data.txt
    - ouput
in the current directory
"""

from pathlib import Path


def create_setup(project_name: str) -> None:
    # Get the curent path
    current_dir = Path.cwd()
    print(f"Current working directory is {current_dir}.")

    # Create the project directory
    project_dir = current_dir / project_name
    if not project_dir.exists():
        project_dir.mkdir()
    else:
        print("Directory already exists. Aborting")
        return

    # Create the data directory
    data_dir = project_dir / "data"
    if not data_dir.exists():
        data_dir.mkdir()

        # Create data
        data_name = data_dir / "data.txt"
        data_name.touch()
    else:
        print("Directory already exists. Aborting")
        return

    # Create the output folder
    output_dir = project_dir / "ouput"
    if not output_dir.exists():
        output_dir.mkdir()
    else:
        print("Directory already exists. Aborting")


project_name = "test"
create_setup(project_name)


dir_data = Path(project_name) / "data"
if dir_data.exists():
    print(
        f"Data directory created successfully. Absolute path is: {dir_data.resolve()}"
    )


dir_data = Path(project_name) / "ouput"
if dir_data.exists():
    print(
        f"Output directory created successfully. Absolute path is: {dir_data.resolve()}"
    )
