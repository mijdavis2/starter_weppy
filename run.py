from contextlib import contextmanager
from argparse import ArgumentParser
from <%= app_name %> import app


@contextmanager
def run_in_dev():
    from <%= app_name %>.dev_utils import remove_test_users
    try:
        yield
    finally:
        remove_test_users()


if __name__ == "__main__":
    arg_parser = ArgumentParser(description="<%= app_title %> running utility.")
    arg_parser.add_argument('-d', '--dev', help="Setup add dev users and enable verbose logging",
                            action='store_true')
    args = arg_parser.parse_args()
    if args.dev:
        from <%= app_name %>.dev_utils import setup_test_users
        setup_test_users()
        with run_in_dev():
            app.run()
    else:
        app.run(host="0.0.0.0", debug=False)
