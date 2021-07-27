"""pact test for user service client"""

import logging
import os

from paver.easy import task

from pact import Verifier
import pytest

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# PACT_UPLOAD_URL = (
#     "http://127.0.0.1/pacts/provider/UserService/consumer"
#     "/User_ServiceClient/version"
# )
PACT_FILE = "temp.json"
# PACT_BROKER_URL = "http://localhost"
# PACT_BROKER_USERNAME = "pactbroker"
# PACT_BROKER_PASSWORD = "pactbroker"

PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 18000
PACT_URL = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)
PACT_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def default_opts():
    return {
        # 'broker_username': PACT_BROKER_USERNAME,
        # 'broker_password': PACT_BROKER_PASSWORD,
        # 'broker_url': PACT_BROKER_URL,
        'publish_version': '3',
        'publish_verification_results': False
    }

@task
def verify_pact():
    verifier = Verifier(provider='LMS',
                        provider_base_url=PACT_URL)

    # output, logs = verifier.verify_with_broker(**default_opts,
    #                                            verbose=True,
    #                                            provider_states_setup_url="{}/_pact/provider_states".format(PACT_URL)                                               )

    output, logs = verifier.verify_pacts(
                os.path.join(PACT_DIR, PACT_FILE)
                # provider_states_setup_url=settings.PROVIDER_STATES_URL,
            )
    assert (output == 0)