"""pact test for user service client"""

import logging
import os

from django.test import LiveServerTestCase
from pact import Verifier


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# PACT_UPLOAD_URL = (
#     "http://127.0.0.1/pacts/provider/UserService/consumer"
#     "/User_ServiceClient/version"
# )


# PACT_BROKER_URL = "http://localhost"
# PACT_BROKER_USERNAME = "pactbroker"
# PACT_BROKER_PASSWORD = "pactbroker"

# PACT_MOCK_HOST = 'localhost'
# PACT_MOCK_PORT = 18000
# PACT_URL = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)

# PACT_DIR = os.path.dirname(os.path.realpath(__file__))
PACT_DIR = os.path.dirname("lms/pacts/")
PACT_FILE = "fake-contract.json"


# @pytest.fixture
# def default_opts():
#     return {
#         # 'broker_username': PACT_BROKER_USERNAME,
#         # 'broker_password': PACT_BROKER_PASSWORD,
#         # 'broker_url': PACT_BROKER_URL,
#         'publish_version': '3',
#         'publish_verification_results': False
#     }

class MyLiveServerTest(LiveServerTestCase):
    """ Sample Live Server """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.verifier = Verifier(provider='lms-course-blocks',
                    provider_base_url=cls.live_server_url,
                    )


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_verify_pact(self):
        print("\n========LIVE SERVER URL==========")
        print(self.live_server_url)
        print("=================================\n")

        output, logs = self.verifier.verify_pacts(
                    os.path.join(PACT_DIR, PACT_FILE),
                    provider_states_setup_url= f"{self.live_server_url}/pact/provider_states/",
                )

        print(logs)
        assert output == 0
