from contextlib import contextmanager
from argparse import ArgumentParser
from starter_weppy import app


@contextmanager
def run_in_dev():
    from starter_weppy.dev_utils import remove_test_users
    try:
        yield
    finally:
        remove_test_users()


if __name__ == "__main__":
    arg_parser = ArgumentParser(description="StarterWeppy running utility.")
    arg_parser.add_argument('-d', '--dev', help="Setup add dev users and enable verbose logging",
                            action='store_true')
    args = arg_parser.parse_args()
    if args.dev:
        from starter_weppy.dev_utils import setup_test_users
        setup_test_users()
        with run_in_dev():
            app.run()
    else:
        app.run(host="0.0.0.0", debug=False)
