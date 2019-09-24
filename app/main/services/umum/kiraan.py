class UmumKiraanServices():

    def KiraModalEmasStok(self, payloads):
        modal_penuh = payloads['stk_emas'] + payloads['stk_permata'] + payloads['stk_upah']
        modal_segram = modal_penuh/payloads['stk_weight']
        return {
            "penuh"     : modal_penuh,
            "segram"    : modal_segram
        }