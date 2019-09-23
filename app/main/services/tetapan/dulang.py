from ...models.mysql.dulang import DulangModel

import pandas as pd

dulang = DulangModel()

class DulangServices():
    def GetSenaraiDulang(self):
        data = dulang.GetSenaraiDulang()
        tag = pd.DataFrame(data)
        get_tag = tag.groupby('tag')['nama_dulang'].count().to_dict()
        item_in_tag = []
        for ind, g in enumerate(get_tag):
            ii = {}
            ii['tag'] = g
            in_tag = tag[tag['tag']==g].loc[:,['kod_dulang','nama_dulang']]
            in_tag.reset_index(inplace=True)
            in_tag.to_dict()
            in_tag_item = []
            for i in range(len(in_tag['kod_dulang'])):
                if i in in_tag['kod_dulang']:
                    item = {
                        "kod_dulang": in_tag['kod_dulang'][i],
                        "nama_dulang": in_tag['nama_dulang'][i]
                    }
                in_tag_item.append(item)
            ii['items'] = in_tag_item
            item_in_tag.append(ii)
        return item_in_tag