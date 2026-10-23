# airgapped_mesh.py
import json
import base64
import numpy as np

class IsosOneAirGappedMesh:
    def __init__(self):
        self.clamp_288 = 2.88
        self.dither_432 = 0.432

    def encrypt_and_stage_packet(self, manual_user_text):
        raw_bytes = manual_user_text.encode('utf-8')
        encoded_payload = base64.b64encode(raw_bytes).decode('utf-8')
        
        signature_vector = [len(manual_user_text) * 0.432, self.clamp_288, self.dither_432]
        
        secure_packet = {
            "restricted_payload": encoded_payload,
            "boundary_signature": signature_vector,
            "security_lock": "AIR_GAPPED_USER_MANUAL_ONLY"
        }
        return json.dumps(secure_packet)

    def verify_and_decode_packet(self, incoming_packet_json):
        packet = json.loads(incoming_packet_json)
        sig = packet["boundary_signature"]
        
        if sig[0] > self.clamp_288 * 100:
            raise SecurityException("Packet rejects processing: External boundary clamp violation.")
            
        decoded_bytes = base64.b64decode(packet["restricted_payload"])
        return decoded_bytes.decode('utf-8')

class SecurityException(Exception):
    pass

if __name__ == "__main__":
    mesh_node = IsosOneAirGappedMesh()
    packet_stream = mesh_node.encrypt_and_stage_packet("Sovereign Information Vector Clear")
    print("[TEST V3] Staged Air-Gapped Transmission String:\\n", packet_stream)
    
    decrypted = mesh_node.verify_and_decode_packet(packet_stream)
    print("[TEST V3] Verified Extracted Output:", decrypted)
