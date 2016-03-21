from contextlib import contextmanager
from argparse import ArgumentParser
from my_weppy_app import app


@contextmanager
def run_in_dev():
    from my_weppy_app.dev_utils import setup_dev_users, remove_dev_users
    setup_dev_users()
    try:
        yield
    finally:
        remove_dev_users()


if __name__ == "__main__":
    arg_parser = ArgumentParser(description="MyWeppyApp running utility.")
    arg_parser.add_argument('-d', '--dev', help="Setup add dev users and enable verbose logging",
                            action='store_true')
    args = arg_parser.parse_args()
    if args.dev:
        with run_in_dev():
            app.run()
    else:
        app.run(debug=False)
