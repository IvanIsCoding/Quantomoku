import os
from qiskit import IBMQ

ibm_q_api_key = os.getenv("IBM_Q")

IBMQ.save_account(ibm_q_api_key)
