#===================================================================================================
# pytest_addoption
#===================================================================================================
def pytest_addoption(parser):
    '''
    Adds a new "--jenkins-available" option to pytest's command line. If not given, tests that
    require a live Jenkins instance will be skipped.
    '''
    parser.addoption(
        "--url",
        help="Specify URL where Jenkins that will be used on tests is running. Default is http://localhost:8080",
    )

    parser.addoption(
        "--user",
        help="Username that should be user to authenticate on Jenkins (if necessary).",
    )

    parser.addoption(
        "--pass",
        help="Password that should be user to authenticate on Jenkins (if necessary).",
    )
