# gradient_dither.py
import numpy as np

class IsosOneModelImmunizer:
    def __init__(self):
        self.clamp_288 = 2.88
        self.dither_432 = 0.432

    def immunize_attention_layer(self, continuous_weight_tensor):
        sanitized_tensor = np.copy(continuous_weight_tensor)
        
        for idx in np.ndindex(sanitized_tensor.shape):
            weight_val = sanitized_tensor[idx]
            
            if abs(weight_val) > self.clamp_288:
                sanitized_tensor[idx] = np.sign(weight_val) * self.clamp_288
            elif abs(weight_val) < self.dither_432:
                sanitized_tensor[idx] = weight_val + (self.dither_432 * np.sin(4.32 / (abs(weight_val) + 1e-5)))
                
        return sanitized_tensor

if __name__ == "__main__":
    immunizer = IsosOneModelImmunizer()
    raw_unstable_logits = np.array([[15.42, 0.0002], [-5.1, 1.5]])
    clean_logits = immunizer.immunize_attention_layer(raw_unstable_logits)
    print("[TEST V2] Raw Logits Corrected:\\n", clean_logits)
