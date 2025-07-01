import argparse
import json
import os
import pathlib

import markdown
import jinja2
from markupsafe import Markup
import yaml

DATA_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
JINJA2_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(str(DATA_DIR)))
JINJA2_ENV.filters.update(
    {
        "as_json": lambda val: Markup(json.dumps(val)),
        "comma_list": lambda vals: ", ".join(vals),
        "date_range": lambda s: (
            s["startDate"]
            if s["startDate"] == s["endDate"]
            else f'{s["startDate"]}–{s["endDate"]}'
        ),
        "md": lambda s: Markup(markdown.markdown(s)),
    }
)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--file", type=pathlib.Path)
    p.add_argument("-o", "--output", type=pathlib.Path)

    args = p.parse_args()

    args.output.write_text(
        JINJA2_ENV.get_template("markdown_template.md").render(
            **yaml.safe_load(args.file.read_text()),
        )
    )


if __name__ == "__main__":
    main()
