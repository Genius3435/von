from .. import model, view
import logging
import pyperclip
import sys

parser = view.Parser(prog="link", description="Pastes the URL to clipboard")
parser.add_argument("key", help="The key of the problem to open")


def main(self: object, argv: list[str]):
    opts = parser.process(argv)
    entry = model.getEntryByKey(opts.key)
    if entry is None:
        logging.error(opts.key + " not found")
    else:
        url = entry.url
        if url is None:
            print("No URL is provided for this problem")
            sys.exit(1)
        print(url)
        pyperclip.copy(url)
