from readme_utils import build_lc_line, file_to_int, get_entry_from_file, build_cf_line
import os, click

# Command Line Interface for geneating the table in the readme file
# Read the files in the LeetCode folder and parses the comment on top
# Example use (use `--help` for more options): 
# python3 -u "/home/bogdan/PythonWork/readme_utils/cli.py" backfill-lc -s leetcode -o local/test.txt

@click.group()
def cli():
    pass


@cli.command()
@click.option("--number", "-n")
@click.option("--title", "-t")
@click.option("--url", "-u")
@click.option("--difficulty", "-d")
@click.option("--time_complexity", "-tc")
@click.option("--space_complexity", "-sc")
@click.option("--notes")
def table_entry_lc(
    number: str,
    title: str,
    url: str,
    difficulty: str,
    time_complexity: str,
    space_complexity: str,
    notes: str = "",
):
    """Create a markdown table entry from params"""
    markdown_line = build_lc_line(
        number, title, url, difficulty, time_complexity, space_complexity, notes
    )
    click.echo(markdown_line)


@cli.command()
@click.option("--outputfile", "-o")
@click.option(
    "--site",
    "-s",
    required=True,
    type=click.Choice(["leetcode", "codeforces"], case_sensitive=False),
)
def backfill_lc(outputfile: str, site: str):
    """Look in the Leetcode folder,
    generate table entries for files there:
    If they have expected lines
    """
    site_folders = {
        "leetcode": ("Leetcode", file_to_int, build_lc_line),
        "codeforces": ("CodeForces", file_to_int, build_cf_line),
    }

    problems_folder, ordering_func, line_str_func = site_folders.get(site)

    entries = []
    all_py_solutions = [x for x in os.listdir(problems_folder) if x.endswith(".py")]

    all_py_solutions_sorted = sorted(all_py_solutions, key=ordering_func)

    for file in all_py_solutions_sorted:
        print(f"File: {file:15}", end=" Processing result: ")
        with open(os.path.join(problems_folder, file), "r") as f:
            maybe_entry = get_entry_from_file(f, line_str_func)
            if maybe_entry:
                entries.append(maybe_entry)

    print(f"Out of {len(list(all_py_solutions))} got descriptions for {len(entries)}")

    if outputfile:
        with open(outputfile, "w+") as of:
            of.write("\n".join(entries))
            click.echo(f"Results written in {outputfile}")
    else:
        for entry in entries:
            print(entry)


if __name__ == "__main__":
    cli()
