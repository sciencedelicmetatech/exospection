import hashlib
import hmac
import os
import json
import time

class CausalService:
    def __init__(self):
        self.secret = os.urandom(32)
        self.traces = {}

    def register_trace(self, record_id: str, input_source: str, agent_chain: list):
        """The writer calls this at write time to register provenance."""
        trace_data = {
            "input_source": input_source,
            "agent_chain": agent_chain,
            "timestamp": time.time()
        }
        self.traces[record_id] = trace_data

    def _sign(self, payload: str) -> str:
        return hmac.new(self.secret, payload.encode(), hashlib.sha256).hexdigest()

    def get_trace(self, record_id: str) -> dict:
        """The caller asks: Where did this record come from?"""
        if record_id not in self.traces:
            return {"record_id": record_id, "trace": None, "error": "No trace found"}
        
        trace_data = self.traces[record_id]
        payload = f"{record_id}|{json.dumps(trace_data, sort_keys=True)}"
        signature = self._sign(payload)
        
        return {
            "record_id": record_id,
            "trace": trace_data,
            "signature": signature,
            "error": None
        }