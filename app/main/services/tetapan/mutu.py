from ...models.mysql.mutu import MutuModal

import pandas as pd

mutu_modal = MutuModal()

class MutuServices():
    def GetSenaraiMutu(self):
        mutu = mutu_modal.GetSenaraiMutu()
        tag = pd.DataFrame(mutu)
        get_tag = tag.groupby('tag')['mutu'].count().to_dict()
        item_in_tag = []
        for ind, g in enumerate(get_tag):
            ii = {}
            ii['tag'] = g
            in_tag = tag[tag['tag']==g].loc[:,['kod_mutu','mutu']]
            in_tag.reset_index(inplace=True)
            in_tag.to_dict()
            in_tag_item = []
            for i in range(len(in_tag['mutu'])):
                item = {
                    "kod_mutu": str(in_tag['kod_mutu'][i]),
                    "nama_mutu": in_tag['mutu'][i]
                }
                in_tag_item.append(item)
            ii['items'] = in_tag_item
            item_in_tag.append(ii)
        return item_in_tag
