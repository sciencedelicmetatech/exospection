from services.authority import AuthorityService
from services.causal import CausalService
from services.norm import NormService

if __name__ == "__main__":
    print("=" * 50)
    print("EXOSPECTION: External Anchor Services")
    print("=" * 50)

    # 1. Authority Test
    print("\n--- 1. Authority Service (Revocation) ---")
    auth = AuthorityService()
    auth.revoke("record_99")
    
    res1 = auth.check_approval("record_99")
    print(f"Record 99 Approved? {res1['approved']} (Signature: {res1['signature'][:8]}...)")
    
    res2 = auth.check_approval("record_100")
    print(f"Record 100 Approved? {res2['approved']} (Signature: {res2['signature'][:8]}...)")

    # 2. Causal Test
    print("\n--- 2. Causal Service (Provenance) ---")
    causal = CausalService()
    causal.register_trace("record_100", "user_prompt_A", ["agent_alpha", "agent_beta"])
    
    res3 = causal.get_trace("record_100")
    print(f"Record 100 Trace: {res3['trace']['agent_chain']} (Signature: {res3['signature'][:8]}...)")
    
    res4 = causal.get_trace("record_101")
    print(f"Record 101 Trace Error: {res4['error']}")

    # 3. Norm Test
    print("\n--- 3. Norm Service (Context Policy) ---")
    norm = NormService()
    
    res5 = norm.check_policy("medical_record_1", "doctor")
    print(f"Medical Record for Doctor: {res5['decision']} (Signature: {res5['signature'][:8]}...)")
    
    res6 = norm.check_policy("medical_record_1", "marketing")
    print(f"Medical Record for Marketing: {res6['decision']} (Signature: {res6['signature'][:8]}...)")